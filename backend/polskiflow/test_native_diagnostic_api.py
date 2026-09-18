import json
from unittest.mock import patch

from django.test import TestCase, override_settings

from polskiflow.auth import SupabaseUser
from polskiflow.domain.diagnostic import CHECK_TASKS


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class NativeDiagnosticApiTests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    def _auth(self):
        return patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser(id="owner-1", email="owner@example.com"),
        )

    def _payload(self):
        return {
            "self_ratings": {
                "reception": "3", "production": "2",
                "interaction": "3", "mediation": "2",
            },
            "answers": {task["key"]: task["answer"] for task in CHECK_TASKS},
        }

    def test_form_requires_bearer_and_hides_keys(self):
        self.client.cookies["polskiflow_access_token"] = "cookie-token"
        with self._auth():
            rejected = self.client.get("/api/v1/diagnostic/")
            response = self.client.get("/api/v1/diagnostic/", **self.authorization)
        self.assertEqual(rejected.status_code, 401)
        self.assertEqual(response.status_code, 200)
        data = response.json()["data"]
        self.assertEqual(len(data["self_assessment"]), 4)
        self.assertEqual(len(data["checked_tasks"]), 8)
        self.assertEqual(data["persistence"], "none")
        serialized = json.dumps(data, ensure_ascii=False)
        self.assertNotIn('"answer"', serialized)
        self.assertNotIn("correct_option_id", serialized)
        self.assertNotIn("explanation", serialized)
        self.assertIn("не экзамен", serialized)
        self.assertEqual(response["Cache-Control"], "private, no-store")

    def test_evaluation_returns_cautious_transparent_result_without_persistence(self):
        with self._auth(), patch(
            "polskiflow.api_views.consume_api_mutation", return_value=(True, 0)
        ):
            response = self.client.post(
                "/api/v1/diagnostic/evaluate/",
                data=json.dumps(self._payload()), content_type="application/json",
                **self.authorization,
            )
        self.assertEqual(response.status_code, 200)
        result = response.json()["data"]
        self.assertEqual(result["recommended_level"], "B1")
        self.assertEqual(result["self_assessment"]["level"], "B1")
        self.assertEqual(result["checked_sample"]["level"], "B2")
        self.assertEqual(result["checked_sample"]["correct"], 8)
        self.assertEqual(len(result["checked_sample"]["mode_scores"]), 4)
        self.assertEqual(len(result["checked_sample"]["feedback"]), 8)
        self.assertFalse(result["persisted"])
        self.assertIn("не экзамен", result["disclaimer"])

    def test_evaluation_rejects_incomplete_unknown_and_oversized_payloads(self):
        incomplete = self._payload()
        incomplete["answers"].pop("check_8")
        unknown = self._payload()
        unknown["extra"] = True
        with self._auth(), patch(
            "polskiflow.api_views.consume_api_mutation", return_value=(True, 0)
        ):
            for payload in (incomplete, unknown, []):
                with self.subTest(payload=payload):
                    response = self.client.post(
                        "/api/v1/diagnostic/evaluate/",
                        data=json.dumps(payload), content_type="application/json",
                        **self.authorization,
                    )
                    self.assertEqual(response.status_code, 400)
            oversized = self.client.post(
                "/api/v1/diagnostic/evaluate/",
                data=json.dumps({"padding": "x" * 5000}), content_type="application/json",
                **self.authorization,
            )
        self.assertEqual(oversized.status_code, 413)

    def test_evaluation_requires_bearer_json_post_and_rate_contract(self):
        with self._auth():
            no_bearer = self.client.post(
                "/api/v1/diagnostic/evaluate/",
                data=json.dumps(self._payload()), content_type="application/json",
            )
            wrong_type = self.client.post(
                "/api/v1/diagnostic/evaluate/", data="{}", content_type="text/plain",
                **self.authorization,
            )
            wrong_method = self.client.get(
                "/api/v1/diagnostic/evaluate/", **self.authorization
            )
        self.assertEqual(no_bearer.status_code, 401)
        self.assertEqual(wrong_type.status_code, 415)
        self.assertEqual(wrong_method.status_code, 405)

    def test_openapi_describes_bearer_only_non_persistent_contract(self):
        paths = self.client.get("/api/v1/openapi.json").json()["paths"]
        self.assertEqual(paths["/api/v1/diagnostic/"]["get"]["security"], [{"supabaseBearer": []}])
        operation = paths["/api/v1/diagnostic/evaluate/"]["post"]
        self.assertEqual(operation["security"], [{"supabaseBearer": []}])
        self.assertIn("429", operation["responses"])
