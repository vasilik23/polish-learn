import json
from unittest.mock import patch

from django.test import TestCase, override_settings

from polskiflow.auth import SupabaseUser


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class NativeInteractionApiTests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    def _auth(self):
        return patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser(id="owner-1", email="owner@example.com"),
        )

    def test_library_requires_bearer_and_hides_feedback(self):
        self.client.cookies["polskiflow_access_token"] = "cookie-token"
        with self._auth():
            rejected = self.client.get("/api/v1/interaction/")
            response = self.client.get("/api/v1/interaction/", **self.authorization)
        self.assertEqual(rejected.status_code, 401)
        self.assertEqual(response.status_code, 200)
        data = response.json()["data"]
        self.assertEqual(data["scenario_count"], 10)
        self.assertEqual({item["kind"] for item in data["scenarios"]}, {"choice", "sequence", "free_production"})
        serialized = json.dumps(data, ensure_ascii=False)
        self.assertNotIn("correct_option_id", serialized)
        self.assertNotIn("correct_order", serialized)
        self.assertNotIn("explanation", serialized)
        self.assertIn('"submission": "local_only"', serialized)
        self.assertEqual(response["Cache-Control"], "private, no-store")

    def test_choice_and_sequence_feedback_are_revealed_after_submission(self):
        with self._auth(), patch(
            "polskiflow.api_views.consume_api_mutation", return_value=(True, 0)
        ):
            choice = self.client.post(
                "/api/v1/interaction/weekend-plan/answer/",
                data=json.dumps({"option_id": "b"}), content_type="application/json",
                **self.authorization,
            )
            sequence = self.client.post(
                "/api/v1/interaction/library-request/answer/",
                data=json.dumps({"block_ids": ["context", "question", "request"]}),
                content_type="application/json", **self.authorization,
            )
        self.assertTrue(choice.json()["data"]["correct"])
        self.assertEqual(choice.json()["data"]["correct_option_id"], "b")
        self.assertTrue(sequence.json()["data"]["correct"])
        self.assertEqual(sequence.json()["data"]["correct_order"], ["context", "question", "request"])

    def test_answer_validation_is_strict_and_bounded(self):
        cases = (
            ("weekend-plan", {"option_id": "b", "extra": True}, 400),
            ("weekend-plan", {"option_id": True}, 400),
            ("library-request", {"block_ids": ["context", "context", "request"]}, 400),
            ("schedule-compromise", {"option_id": "a"}, 400),
            ("missing", {"option_id": "a"}, 404),
        )
        with self._auth(), patch(
            "polskiflow.api_views.consume_api_mutation", return_value=(True, 0)
        ):
            for scenario_id, payload, status in cases:
                with self.subTest(scenario_id=scenario_id):
                    response = self.client.post(
                        f"/api/v1/interaction/{scenario_id}/answer/",
                        data=json.dumps(payload), content_type="application/json",
                        **self.authorization,
                    )
                    self.assertEqual(response.status_code, status)
            oversized = self.client.post(
                "/api/v1/interaction/weekend-plan/answer/",
                data=json.dumps({"option_id": "x" * 1100}), content_type="application/json",
                **self.authorization,
            )
        self.assertEqual(oversized.status_code, 413)

    def test_answer_requires_bearer_post_json_and_is_rate_limited(self):
        with self._auth():
            no_bearer = self.client.post(
                "/api/v1/interaction/weekend-plan/answer/",
                data=json.dumps({"option_id": "b"}), content_type="application/json",
            )
            wrong_method = self.client.get(
                "/api/v1/interaction/weekend-plan/answer/", **self.authorization
            )
            wrong_type = self.client.post(
                "/api/v1/interaction/weekend-plan/answer/",
                data="{}", content_type="text/plain", **self.authorization,
            )
        self.assertEqual(no_bearer.status_code, 401)
        self.assertEqual(wrong_method.status_code, 405)
        self.assertEqual(wrong_type.status_code, 415)

    def test_openapi_describes_bearer_only_contract(self):
        paths = self.client.get("/api/v1/openapi.json").json()["paths"]
        self.assertEqual(paths["/api/v1/interaction/"]["get"]["security"], [{"supabaseBearer": []}])
        operation = paths["/api/v1/interaction/{scenario_id}/answer/"]["post"]
        self.assertEqual(operation["security"], [{"supabaseBearer": []}])
        self.assertIn("429", operation["responses"])
