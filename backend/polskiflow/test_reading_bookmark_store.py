import json
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase, override_settings

from polskiflow.reading_bookmark_store import load_reading_bookmarks, set_reading_bookmark


@override_settings(SUPABASE_URL="https://db.example", SUPABASE_ANON_KEY="anon", SUPABASE_AUTH_TIMEOUT=1)
class ReadingBookmarkStoreTests(SimpleTestCase):
    @patch("polskiflow.reading_bookmark_store.urlopen")
    def test_load_is_owner_scoped(self, mocked_open):
        response = MagicMock(status=200)
        response.__enter__.return_value = response
        response.read.return_value = json.dumps([{"reading_text_id": "story"}]).encode()
        mocked_open.return_value = response
        self.assertEqual(load_reading_bookmarks("token", "user-1"), {"story"})
        request = mocked_open.call_args.args[0]
        self.assertIn("user_id=eq.user-1", request.full_url)
        self.assertEqual(request.headers["Authorization"], "Bearer token")

    @patch("polskiflow.reading_bookmark_store.urlopen")
    def test_save_uses_authenticated_owner_payload(self, mocked_open):
        response = MagicMock(status=201)
        response.__enter__.return_value = response
        mocked_open.return_value = response
        self.assertTrue(set_reading_bookmark("token", "user-1", "story", True))
        request = mocked_open.call_args.args[0]
        self.assertEqual(json.loads(request.data), {"user_id": "user-1", "reading_text_id": "story"})
