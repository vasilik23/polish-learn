import json
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase, override_settings

from polskiflow.dictionary_store import load_personal_words, save_personal_word


class DictionaryStoreTests(SimpleTestCase):
    def test_unconfigured_store_stays_local(self):
        self.assertEqual(load_personal_words("token", "user"), [])
        self.assertFalse(
            save_personal_word("token", "user", "dom", "дом", "", "story")
        )

    @override_settings(
        SUPABASE_URL="https://project.supabase.co",
        SUPABASE_ANON_KEY="public-key",
        SUPABASE_AUTH_TIMEOUT=2,
    )
    @patch("polskiflow.dictionary_store.urlopen")
    def test_word_is_upserted_with_user_token(self, mocked_urlopen):
        mocked_urlopen.return_value.__enter__.return_value = MagicMock(status=201)

        saved = save_personal_word(
            "access", "user-123", "dom", "дом", "To jest dom.", "story"
        )

        self.assertTrue(saved)
        request = mocked_urlopen.call_args.args[0]
        self.assertEqual(request.headers["Authorization"], "Bearer access")
        self.assertEqual(json.loads(request.data)["user_id"], "user-123")
        self.assertIn("on_conflict=user_id%2Cword", request.full_url)

    @override_settings(
        SUPABASE_URL="https://project.supabase.co",
        SUPABASE_ANON_KEY="public-key",
        SUPABASE_AUTH_TIMEOUT=2,
    )
    @patch("polskiflow.dictionary_store.urlopen")
    def test_words_are_filtered_by_authenticated_user(self, mocked_urlopen):
        response = MagicMock()
        response.read.return_value = json.dumps(
            [{"id": "word-1", "word": "dom", "translation": "дом"}]
        ).encode()
        mocked_urlopen.return_value.__enter__.return_value = response

        words = load_personal_words("access", "user-123")

        self.assertEqual(words[0]["word"], "dom")
        request = mocked_urlopen.call_args.args[0]
        self.assertIn("user_id=eq.user-123", request.full_url)
        self.assertEqual(request.headers["Authorization"], "Bearer access")
