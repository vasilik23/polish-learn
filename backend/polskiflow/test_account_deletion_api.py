import json
from unittest.mock import patch

from django.test import SimpleTestCase, override_settings

from polskiflow.auth import SupabaseAuthError, SupabaseUser


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class AccountDeletionApiTests(SimpleTestCase):
    headers = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    def setUp(self):
        auth = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser("owner-1", "owner@example.com"),
        )
        auth.start()
        self.addCleanup(auth.stop)

    @patch("polskiflow.api_views.consume_api_mutation", return_value=(True, 60))
    @patch("polskiflow.api_views.delete_account")
    def test_delete_is_bearer_only_and_owner_scoped(self, delete, _rate):
        missing = self.client.delete(
            "/api/v1/me/account/", data=json.dumps({"password": "CurrentPassword2026"}),
            content_type="application/json",
        )
        self.assertEqual(missing.status_code, 401)
        delete.assert_not_called()
        response = self.client.delete(
            "/api/v1/me/account/", data=json.dumps({"password": "CurrentPassword2026"}),
            content_type="application/json", **self.headers,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["data"]["deleted"])
        self.assertEqual(response["Cache-Control"], "private, no-store")
        delete.assert_called_once_with("owner-token", "owner-1", "CurrentPassword2026")

    @patch("polskiflow.api_views.consume_api_mutation", return_value=(True, 60))
    @patch("polskiflow.api_views.delete_account")
    def test_payload_is_strict_and_bounded(self, delete, _rate):
        for payload in ({}, {"password": ""}, {"password": "x", "user_id": "other"}):
            response = self.client.delete(
                "/api/v1/me/account/", data=json.dumps(payload),
                content_type="application/json", **self.headers,
            )
            self.assertEqual(response.status_code, 400)
        oversized = self.client.delete(
            "/api/v1/me/account/", data=json.dumps({"password": "x" * 2049}),
            content_type="application/json", **self.headers,
        )
        self.assertEqual(oversized.status_code, 413)
        delete.assert_not_called()

    @patch("polskiflow.api_views.consume_api_mutation", return_value=(True, 60))
    @patch("polskiflow.api_views.delete_account", side_effect=SupabaseAuthError("upstream secret", status_code=403))
    def test_worker_failure_is_neutral(self, _delete, _rate):
        response = self.client.delete(
            "/api/v1/me/account/", data=json.dumps({"password": "wrong"}),
            content_type="application/json", **self.headers,
        )
        self.assertEqual(response.status_code, 403)
        self.assertNotIn("upstream secret", response.content.decode())

    @patch("polskiflow.api_views.consume_api_mutation", return_value=(True, 60))
    @patch("polskiflow.api_views.delete_account", side_effect=SupabaseAuthError("upstream secret", status_code=503))
    def test_worker_outage_is_unavailable_not_bad_password(self, _delete, _rate):
        response = self.client.delete(
            "/api/v1/me/account/", data=json.dumps({"password": "valid"}),
            content_type="application/json", **self.headers,
        )
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json()["error"]["code"], "account_deletion_unavailable")

    def test_openapi_documents_destructive_contract(self):
        payload = self.client.get("/api/v1/openapi.json").json()
        operation = payload["paths"]["/api/v1/me/account/"]["delete"]
        self.assertEqual(operation["operationId"], "deleteLearnerAccount")
        self.assertEqual(operation["security"], [{"supabaseBearer": []}])
        self.assertFalse(payload["components"]["schemas"]["AccountDeletionRequest"]["additionalProperties"])
