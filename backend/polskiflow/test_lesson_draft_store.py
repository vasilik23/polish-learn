import json
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase, override_settings

from polskiflow.lesson_draft_store import delete_lesson_draft, load_lesson_draft, save_lesson_draft


@override_settings(SUPABASE_URL="https://project.supabase.co", SUPABASE_ANON_KEY="public", SUPABASE_AUTH_TIMEOUT=2)
class LessonDraftStoreTests(SimpleTestCase):
    @patch("polskiflow.lesson_draft_store.urlopen")
    def test_load_is_owner_scoped(self, urlopen):
        response = MagicMock(); response.read.return_value = b'[{"lesson_kind":"quiz","step_index":2,"score":1}]'
        urlopen.return_value.__enter__.return_value = response
        self.assertEqual(load_lesson_draft("access", "user-1", "quiz")["step_index"], 2)
        request = urlopen.call_args.args[0]
        self.assertIn("user_id=eq.user-1", request.full_url)
        self.assertEqual(request.headers["Authorization"], "Bearer access")

    @patch("polskiflow.lesson_draft_store.urlopen")
    def test_save_upserts_only_supplied_owner(self, urlopen):
        urlopen.return_value.__enter__.return_value = MagicMock(status=201)
        self.assertTrue(save_lesson_draft("access", "user-1", "quiz", "quiz", 2, 1))
        request = urlopen.call_args.args[0]
        self.assertEqual(request.method, "POST")
        self.assertEqual(json.loads(request.data)["user_id"], "user-1")
        self.assertIn("on_conflict=user_id%2Clesson_id", request.full_url)

    @patch("polskiflow.lesson_draft_store.urlopen")
    def test_delete_is_owner_scoped(self, urlopen):
        urlopen.return_value.__enter__.return_value = MagicMock(status=204)
        self.assertTrue(delete_lesson_draft("access", "user-1", "quiz"))
        request = urlopen.call_args.args[0]
        self.assertEqual(request.method, "DELETE")
        self.assertIn("user_id=eq.user-1", request.full_url)
