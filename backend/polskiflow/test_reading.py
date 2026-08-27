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
            glossary={
                "kota": {
                    "lemma": "kot",
                    "translation": "кот",
                    "part_of_speech": "существительное",
                },
                "lubi": {
                    "lemma": "lubić",
                    "translation": "любить",
                    "part_of_speech": "глагол",
                },
                "mleko": "молоко",
            },
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
        self.news_patch = patch(
            "polskiflow.reading_views.latest_official_news", return_value=[]
        )
        self.news_patch.start()
        self.addCleanup(self.news_patch.stop)

    def test_library_lists_active_texts(self):
        response = self.client.get("/reading/")

        self.assertContains(response, "Krótka historia")
        self.assertContains(response, "Тестовый рассказ")

    def test_reader_marks_only_glossary_words_as_interactive(self):
        response = self.client.get("/reading/test-story/")

        self.assertContains(response, 'data-word="kota"')
        self.assertContains(response, 'data-lemma="kot"')
        self.assertContains(response, 'data-translation="кот"')
        self.assertContains(response, 'data-part-of-speech="существительное"')
        self.assertContains(response, 'class="reader-word"', count=3)

    @patch("polskiflow.reading_views.save_personal_word", return_value=True)
    def test_glossary_word_can_be_saved(self, save_word):
        response = self.client.post(
            "/reading/test-story/save/",
            {"word": "KOTA", "translation": "кот", "context": "Ala ma kota."},
            headers={"HX-Request": "true"},
        )

        self.assertContains(response, "теперь в словаре")
        save_word.assert_called_once_with(
            "access",
            "00000000-0000-0000-0000-000000000123",
            "kot",
            "кот",
            "Ala ma kota.",
            "test-story",
        )

    @patch("polskiflow.reading_views.save_personal_word", return_value=True)
    def test_legacy_glossary_value_still_saves_surface_form(self, save_word):
        response = self.client.post(
            "/reading/test-story/save/",
            {"word": "mleko", "translation": "молоко", "context": "Kot lubi mleko."},
            headers={"HX-Request": "true"},
        )

        self.assertEqual(response.status_code, 200)
        save_word.assert_called_once_with(
            "access",
            "00000000-0000-0000-0000-000000000123",
            "mleko",
            "молоко",
            "Kot lubi mleko.",
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

    @patch("polskiflow.reading_views.load_personal_words")
    def test_practice_builds_quiz_from_personal_words(self, load_words):
        load_words.return_value = self._practice_words()

        response = self.client.get("/dictionary/practice/")

        self.assertContains(response, "Выбери перевод")
        self.assertContains(response, "dom")
        self.assertContains(response, "дом")
        self.assertContains(response, "молоко")

    @patch("polskiflow.reading_views.load_personal_words")
    def test_practice_requires_four_distinct_translations(self, load_words):
        load_words.return_value = self._practice_words()[:3]

        response = self.client.get("/dictionary/practice/")

        self.assertContains(response, "Нужно минимум 4 слова")
        self.assertContains(response, "Сейчас в словаре: 3")

    @patch("polskiflow.reading_views.load_personal_words")
    def test_practice_answer_shows_feedback(self, load_words):
        load_words.return_value = self._practice_words()

        response = self.client.post(
            "/dictionary/practice/step/",
            {"action": "answer", "index": 0, "score": 0, "choice": 0},
        )

        self.assertContains(response, "Верно!")
        self.assertContains(response, "Следующее слово")

    @patch("polskiflow.reading_views.save_lesson_completion", return_value=True)
    @patch("polskiflow.reading_views.load_personal_words")
    def test_practice_completion_is_saved(self, load_words, save_completion):
        load_words.return_value = self._practice_words()

        response = self.client.post(
            "/dictionary/practice/step/",
            {"action": "next", "index": 3, "score": 3, "selected": 3},
        )

        self.assertContains(response, "4 / 4")
        self.assertContains(response, "Результат добавлен")
        save_completion.assert_called_once_with(
            "access",
            "00000000-0000-0000-0000-000000000123",
            "dictionary-practice",
            4,
            4,
        )

    @staticmethod
    def _practice_words():
        return [
            {"word": "dom", "translation": "дом", "context": "To jest dom."},
            {"word": "mleko", "translation": "молоко", "context": "Lubię mleko."},
            {"word": "chleb", "translation": "хлеб", "context": "Jem chleb."},
            {"word": "okno", "translation": "окно", "context": "Otwieram okno."},
        ]
