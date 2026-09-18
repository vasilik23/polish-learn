import json
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase, override_settings

from polskiflow.reminder_preference_store import (
    load_reminder_preferences,
    save_reminder_preferences,
)


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class ReminderPreferenceStoreTests(SimpleTestCase):
    @patch("polskiflow.reminder_preference_store.urlopen")
    def test_loads_only_owner_scoped_preferences(self, mocked_urlopen):
        response = MagicMock()
        response.__enter__.return_value = response
        response.read.return_value = json.dumps([{
            "daily_reminder_enabled": True,
            "reminder_time": "08:30:00",
            "timezone": "Europe/Warsaw",
        }]).encode()
        mocked_urlopen.return_value = response

        result = load_reminder_preferences("access", "user-123")

        self.assertTrue(result["daily_reminder_enabled"])
        request = mocked_urlopen.call_args.args[0]
        self.assertIn("user_id=eq.user-123", request.full_url)
        self.assertEqual(request.headers["Authorization"], "Bearer access")

    @patch("polskiflow.reminder_preference_store.urlopen")
    def test_missing_row_is_safely_opted_out(self, mocked_urlopen):
        response = MagicMock()
        response.__enter__.return_value = response
        response.read.return_value = b"[]"
        mocked_urlopen.return_value = response

        result = load_reminder_preferences("access", "user-123")

        self.assertFalse(result["daily_reminder_enabled"])

    @patch("polskiflow.reminder_preference_store.urlopen")
    def test_upsert_uses_user_token_and_owner_id(self, mocked_urlopen):
        response = MagicMock(status=201)
        response.__enter__.return_value = response
        mocked_urlopen.return_value = response

        self.assertTrue(save_reminder_preferences("access", "user-123", True, "08:30", "Europe/Warsaw"))

        request = mocked_urlopen.call_args.args[0]
        self.assertEqual(request.method, "POST")
        self.assertEqual(request.headers["Authorization"], "Bearer access")
        self.assertEqual(json.loads(request.data)["user_id"], "user-123")
