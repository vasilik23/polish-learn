import json
from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser


class ReminderPreferencesApiTests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer access"}

    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        auth = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser("user-123", "anna@example.com"),
        )
        auth.start()
        self.addCleanup(auth.stop)

    @patch("polskiflow.api_views.load_reminder_preferences")
    def test_get_returns_owner_preferences_and_honest_delivery_status(self, load):
        load.return_value = {
            "daily_reminder_enabled": True,
            "reminder_time": "08:30",
            "timezone": "Europe/Warsaw",
        }
        response = self.client.get("/api/v1/me/reminder-preferences/", **self.authorization)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Cache-Control"], "private, no-store")
        self.assertFalse(response.json()["data"]["delivery_active"])
        self.assertEqual(response.json()["data"]["preferences"]["reminder_time"], "08:30")

    @patch("polskiflow.api_views.save_reminder_preferences", return_value=True)
    @patch("polskiflow.api_views.load_reminder_preferences")
    @patch("polskiflow.api_views._mutation_rate_limit", return_value=None)
    def test_patch_can_enable_or_fully_disable_opt_in(self, _limit, load, save):
        load.return_value = {
            "daily_reminder_enabled": False,
            "reminder_time": "19:00",
            "timezone": "Europe/Warsaw",
        }
        for enabled in (True, False):
            response = self.client.patch(
                "/api/v1/me/reminder-preferences/",
                data=json.dumps({"daily_reminder_enabled": enabled, "reminder_time": "07:45"}),
                content_type="application/json",
                **self.authorization,
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["data"]["preferences"]["daily_reminder_enabled"], enabled)
        self.assertEqual(save.call_args_list[-1].args, ("access", "user-123", False, "07:45", "Europe/Warsaw"))

    @patch("polskiflow.api_views.save_reminder_preferences")
    @patch("polskiflow.api_views.load_reminder_preferences", return_value={"daily_reminder_enabled": False, "reminder_time": "19:00", "timezone": "Europe/Warsaw"})
    @patch("polskiflow.api_views._mutation_rate_limit", return_value=None)
    def test_patch_rejects_unknown_fields_types_and_invalid_time(self, _limit, _load, save):
        for payload in (
            {"timezone": "UTC"},
            {"daily_reminder_enabled": "yes"},
            {"reminder_time": "24:00"},
            {},
        ):
            with self.subTest(payload=payload):
                response = self.client.patch(
                    "/api/v1/me/reminder-preferences/",
                    data=json.dumps(payload), content_type="application/json", **self.authorization,
                )
                self.assertEqual(response.status_code, 400)
        save.assert_not_called()

    @patch("polskiflow.api_views.load_reminder_preferences", return_value=None)
    def test_upstream_failure_is_not_presented_as_defaults(self, _load):
        response = self.client.get("/api/v1/me/reminder-preferences/", **self.authorization)
        self.assertEqual(response.status_code, 503)

    def test_requires_explicit_bearer(self):
        self.assertEqual(self.client.get("/api/v1/me/reminder-preferences/").status_code, 401)

    def test_openapi_has_strict_patch_schema(self):
        document = self.client.get("/api/v1/openapi.json").json()
        operation = document["paths"]["/api/v1/me/reminder-preferences/"]["patch"]
        schema = document["components"]["schemas"]["ReminderPreferencesPatchRequest"]
        self.assertEqual(operation["security"], [{"supabaseBearer": []}])
        self.assertFalse(schema["additionalProperties"])
        self.assertIn("429", operation["responses"])
