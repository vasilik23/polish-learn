import json
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase, override_settings

from polskiflow.progress_store import save_lesson_completion


class ProgressStoreTests(SimpleTestCase):
    def test_unconfigured_store_does_not_attempt_a_write(self):
        self.assertFalse(save_lesson_completion("token", "user", "quiz", 5, 4))

    @override_settings(
        SUPABASE_URL="https://project.supabase.co",
        SUPABASE_ANON_KEY="public-key",
        SUPABASE_AUTH_TIMEOUT=2,
    )
    @patch("polskiflow.progress_store.urlopen")
    def test_completion_is_upserted_with_user_token(self, mocked_urlopen):
        response = MagicMock(status=201)
        mocked_urlopen.return_value.__enter__.return_value = response

        saved = save_lesson_completion("access", "user-123", "quiz", 5, 4)

        self.assertTrue(saved)
        request = mocked_urlopen.call_args.args[0]
        self.assertEqual(request.headers["Authorization"], "Bearer access")
        self.assertEqual(json.loads(request.data)["cards_known"], 4)
        self.assertIn("on_conflict=user_id%2Clesson_id%2Cplan_date", request.full_url)
