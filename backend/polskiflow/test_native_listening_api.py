import json
from unittest.mock import patch

from django.test import TestCase, override_settings

from polskiflow.auth import SupabaseUser


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class NativeListeningApiTests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    def _auth(self):
        return patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser(id="owner-1", email="owner@example.com"),
        )

    def test_library_requires_explicit_bearer_and_hides_feedback(self):
        self.client.cookies["polskiflow_access_token"] = "cookie-token"
        with self._auth():
            rejected = self.client.get("/api/v1/listening/")
            response = self.client.get("/api/v1/listening/", **self.authorization)
        self.assertEqual(rejected.status_code, 401)
        self.assertEqual(response.status_code, 200)
        data = response.json()["data"]
        self.assertEqual(data["exercise_count"], 4)
        self.assertTrue(data["exercises"][0]["transcript"])
        self.assertTrue(data["exercises"][0]["fragments"])
        self.assertTrue(data["exercises"][0]["questions"])
        serialized = json.dumps(data, ensure_ascii=False)
        self.assertNotIn('"answer"', serialized)
        self.assertNotIn('"correct"', serialized)
        self.assertNotIn("explanation", serialized)
        self.assertEqual(response["Cache-Control"], "private, no-store")

    def test_answer_reveals_feedback_only_after_submission(self):
        payload = {"question_id": "dialogue_detail", "selected_index": 1}
        with self._auth(), patch(
            "polskiflow.api_views.consume_api_mutation", return_value=(True, 0)
        ):
            response = self.client.post(
                "/api/v1/listening/travel-dialogue/answer/",
                data=json.dumps(payload), content_type="application/json", **self.authorization,
            )
        self.assertEqual(response.status_code, 200)
        feedback = response.json()["data"]
        self.assertTrue(feedback["correct"])
        self.assertEqual(feedback["correct_index"], 1)
        self.assertIn("Spotkajmy", feedback["explanation"])

    def test_answer_has_strict_bounded_validation(self):
        cases = (
            ({"question_id": "dialogue_detail", "selected_index": True}, 400),
            ({"question_id": "dialogue_detail", "selected_index": 1, "extra": 1}, 400),
            ({"question_id": "x" * 81, "selected_index": 0}, 400),
        )
        with self._auth(), patch(
            "polskiflow.api_views.consume_api_mutation", return_value=(True, 0)
        ):
            for payload, status in cases:
                with self.subTest(payload=payload):
                    response = self.client.post(
                        "/api/v1/listening/travel-dialogue/answer/",
                        data=json.dumps(payload), content_type="application/json", **self.authorization,
                    )
                    self.assertEqual(response.status_code, status)
            oversized = self.client.post(
                "/api/v1/listening/travel-dialogue/answer/",
                data=json.dumps({"question_id": "dialogue_detail", "selected_index": 1, "padding": "x" * 600}),
                content_type="application/json", **self.authorization,
            )
            wrong_type = self.client.post(
                "/api/v1/listening/travel-dialogue/answer/",
                data="{}", content_type="text/plain", **self.authorization,
            )
            missing = self.client.post(
                "/api/v1/listening/missing/answer/",
                data=json.dumps({"question_id": "dialogue_detail", "selected_index": 1}),
                content_type="application/json", **self.authorization,
            )
        self.assertEqual(oversized.status_code, 413)
        self.assertEqual(wrong_type.status_code, 415)
        self.assertEqual(missing.status_code, 404)

    def test_answer_requires_bearer_and_post(self):
        self.client.cookies["polskiflow_access_token"] = "cookie-token"
        with self._auth():
            rejected = self.client.post(
                "/api/v1/listening/travel-dialogue/answer/",
                data=json.dumps({"question_id": "dialogue_detail", "selected_index": 1}),
                content_type="application/json",
            )
            method = self.client.get(
                "/api/v1/listening/travel-dialogue/answer/", **self.authorization
            )
        self.assertEqual(rejected.status_code, 401)
        self.assertEqual(method.status_code, 405)

    def test_openapi_describes_bearer_only_stateless_contract(self):
        paths = self.client.get("/api/v1/openapi.json").json()["paths"]
        self.assertEqual(
            paths["/api/v1/listening/"]["get"]["security"],
            [{"supabaseBearer": []}],
        )
        operation = paths["/api/v1/listening/{exercise_id}/answer/"]["post"]
        self.assertEqual(operation["security"], [{"supabaseBearer": []}])
        self.assertIn("429", operation["responses"])
