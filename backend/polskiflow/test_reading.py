from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.learning.models import ReadingText


class ReadingViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        ReadingText.objects.create(
            id="test-story",
            title="Krótka historia",
            description="Тестовый рассказ",
            level="A1",
            emoji="📖",
            paragraphs=["Ala ma kota. Kot lubi mleko."],
            glossary={"kota": "кота", "lubi": "любит", "mleko": "молоко"},
        )

    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        self.auth_patch = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser(
                "00000000-0000-0000-0000-000000000123", "reader@example.com"
            ),
        )
        self.auth_patch.start()
        self.addCleanup(self.auth_patch.stop)

    def test_library_lists_active_texts(self):
        response = self.client.get("/reading/")

        self.assertContains(response, "Krótka historia")
        self.assertContains(response, "Тестовый рассказ")

    def test_reader_marks_only_glossary_words_as_interactive(self):
        response = self.client.get("/reading/test-story/")

        self.assertContains(response, 'data-word="kota"')
        self.assertContains(response, 'data-translation="кота"')
        self.assertContains(response, 'class="reader-word"', count=3)

    @patch("polskiflow.reading_views.save_personal_word", return_value=True)
    def test_glossary_word_can_be_saved(self, save_word):
        response = self.client.post(
            "/reading/test-story/save/",
            {"word": "KOTA", "translation": "кота", "context": "Ala ma kota."},
            headers={"HX-Request": "true"},
        )

        self.assertContains(response, "теперь в словаре")
        save_word.assert_called_once_with(
            "access",
            "00000000-0000-0000-0000-000000000123",
            "kota",
            "кота",
            "Ala ma kota.",
            "test-story",
        )

    @patch("polskiflow.reading_views.save_personal_word")
    def test_unknown_translation_is_rejected(self, save_word):
        response = self.client.post(
            "/reading/test-story/save/",
            {"word": "kota", "translation": "подменённый перевод"},
        )

        self.assertEqual(response.status_code, 400)
        save_word.assert_not_called()

    @patch("polskiflow.reading_views.load_personal_words")
    def test_dictionary_lists_user_words(self, load_words):
        load_words.return_value = [
            {
                "id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
                "word": "mleko",
                "translation": "молоко",
                "context": "Kot lubi mleko.",
            }
        ]

        response = self.client.get("/dictionary/")

        self.assertContains(response, "mleko")
        self.assertContains(response, "молоко")

    def test_unknown_text_returns_404(self):
        self.assertEqual(self.client.get("/reading/no-story/").status_code, 404)
