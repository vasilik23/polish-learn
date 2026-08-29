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
        ReadingText.objects.create(
            id="test-story-a2", title="Historia A2", description="Уровень A2",
            level="A2", paragraphs=["To jest A2."], glossary={}, position=1,
        )
        ReadingText.objects.create(
            id="test-story-fallback", title="Historia bez poziomu",
            description="Резервный уровень", level="", paragraphs=["Tekst."],
            glossary={}, position=2,
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
        self.news_mock = self.news_patch.start()
        self.addCleanup(self.news_patch.stop)

    def test_library_lists_active_texts(self):
        response = self.client.get("/reading/")

        self.assertContains(response, "Krótka historia")
        self.assertContains(response, "Historia bez poziomu")
        self.assertNotContains(response, "Historia A2")
        self.assertContains(response, "Тестовый рассказ")
        self.assertContains(response, "Политика")
        self.assertContains(response, "Спорт")
        self.assertContains(response, "Культура и медиа")
        self.assertContains(response, 'aria-label="Уровень учебных текстов"')
        self.assertContains(response, 'href="?level=A1#texts-title" aria-current="page"')

    def test_library_filters_texts_by_level_and_falls_back_to_a1(self):
        response = self.client.get("/reading/?level=A2")

        self.assertContains(response, "Historia A2")
        self.assertNotContains(response, "Krótka historia")
        self.assertContains(response, 'href="?level=A2#texts-title" aria-current="page"')

        response = self.client.get("/reading/?level=unknown")
        self.assertContains(response, "Krótka historia")
        self.assertContains(response, 'href="?level=A1#texts-title" aria-current="page"')

    def test_library_filters_news_by_allowlisted_category(self):
        response = self.client.get("/reading/?category=sport")

        self.assertEqual(response.status_code, 200)
        self.news_mock.assert_called_with(category="sport")
        self.assertContains(response, 'href="?level=A1&amp;category=sport#news-title" aria-current="page"')

        response = self.client.get("/reading/?level=A2&category=sport")
        self.assertContains(response, 'href="?level=A1&amp;category=sport#texts-title"')
        self.assertContains(response, 'href="?level=A2&amp;category=sport#news-title" aria-current="page"')

        self.client.get("/reading/?category=not-a-category")
        self.news_mock.assert_called_with(category=None)

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

    def test_a2_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/weekend-kasi-i-pawla/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Проверь понимание текста")
        self.assertContains(response, "5 вопросов · A2")
        self.assertContains(response, 'href="/lesson/weekend-reading-check/"')

        activity = self.client.get("/lesson/weekend-reading-check/")
        self.assertContains(activity, "Dokąd Kasia pojechała po pracy?")
        self.assertContains(activity, "Do Wrocławia")

    def test_travel_reader_links_to_its_comprehension_activity(self):
        response = self.client.get("/reading/plan-wyjazdu-do-gdanska/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/lesson/travel-reading-check/"')
        activity = self.client.get("/lesson/travel-reading-check/")
        self.assertContains(activity, "Kiedy Marta i Kuba wyjadą z Krakowa?")
        self.assertContains(activity, "W piątek wieczorem")

    def test_housing_reader_links_to_its_comprehension_activity(self):
        response = self.client.get("/reading/usterka-w-mieszkaniu/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/lesson/housing-reading-check/"')
        activity = self.client.get("/lesson/housing-reading-check/")
        self.assertContains(activity, "Jaki problem zauważyła Lena?")
        self.assertContains(activity, "Nie działało ogrzewanie")

    def test_work_reader_links_to_its_comprehension_activity(self):
        response = self.client.get("/reading/pierwszy-tydzien-mai/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/lesson/a2work-reading-check/"')
        activity = self.client.get("/lesson/a2work-reading-check/")
        self.assertContains(activity, "Gdzie zaczęła pracować Maja?")

    def test_returns_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/reklamacja-natalii/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/lesson/returns-reading-check/"')
        activity = self.client.get("/lesson/returns-reading-check/")
        self.assertContains(activity, "Dlaczego Natalia wróciła do sklepu?")

    def test_medical_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/adam-u-lekarza-i-w-aptece/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/lesson/med-reading-check/"')
        activity = self.client.get("/lesson/med-reading-check/")
        self.assertContains(activity, "Jak długo Adam miał objawy?")

    def test_relationships_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/szczera-rozmowa-marty-i-ani/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/lesson/rel-reading-check/"')
        self.assertContains(response, 'data-word="przyjaźnią"')
        activity = self.client.get("/lesson/rel-reading-check/")
        self.assertContains(activity, "Dlaczego Marta była rozczarowana?")

    def test_culture_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/wieczor-krotkich-filmow/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/lesson/culture-reading-check/"')
        self.assertContains(response, 'data-word="reżyserów"')
        activity = self.client.get("/lesson/culture-reading-check/")
        self.assertContains(activity, "Na jakie wydarzenie poszli Lena i Paweł?")

    def test_institutions_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/natalia-sklada-wniosek/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/lesson/office-reading-check/"')
        self.assertContains(response, 'data-word="ważności"')
        activity = self.client.get("/lesson/office-reading-check/")
        self.assertContains(activity, "Po co Natalia przyszła do urzędu?")

    def test_weather_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/weather-wycieczka-przed-burza/")
        self.assertContains(response, 'href="/lesson/weather-reading-check/"')
        self.assertContains(response, 'data-word="wzgórza"')
        activity = self.client.get("/lesson/weather-reading-check/")
        self.assertContains(activity, "Dokąd pojechali Lena i Kuba?")

    def test_poland_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/poland-maja-odkrywa-torun/")
        self.assertContains(response, 'href="/lesson/poland-reading-check/"')
        self.assertContains(response, 'data-word="przewodniczką"')
        activity = self.client.get("/lesson/poland-reading-check/")
        self.assertContains(activity, "Dokąd pojechała grupa Mai?")

    def test_final_a2_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/a2final-weekend-leny/")
        self.assertContains(response, 'href="/lesson/a2final-reading-check/"')
        self.assertContains(response, 'data-word="kłótni"')
        activity = self.client.get("/lesson/a2final-reading-check/")
        self.assertContains(activity, "Dlaczego Lena pojechała do Torunia?")

    def test_b1_biography_reader_links_to_comprehension_activity(self):
        response = self.client.get("/reading/bio-droga-joanny/")
        self.assertContains(response, 'href="/lesson/bio-reading-check/"')
        self.assertContains(response, 'data-word="dorastała"')
        activity = self.client.get("/lesson/bio-reading-check/")
        self.assertContains(activity, "Gdzie dorastała Joanna?")

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
        self.assertContains(response, "Насколько легко вспомнилось слово?")
        self.assertContains(response, "Трудно")

    @patch("polskiflow.reading_views.save_personal_word_review", return_value=True)
    @patch("polskiflow.reading_views.save_lesson_completion", return_value=True)
    @patch("polskiflow.reading_views.load_personal_words")
    def test_practice_completion_is_saved(
        self, load_words, save_completion, save_review
    ):
        load_words.return_value = self._practice_words()

        response = self.client.post(
            "/dictionary/practice/step/",
            {
                "action": "next",
                "index": 3,
                "score": 3,
                "selected": 3,
                "quality": "easy",
            },
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
        self.assertEqual(save_review.call_args.args[2], "word-4")
        self.assertEqual(save_review.call_args.args[3].repetitions, 1)
        self.assertEqual(save_review.call_args.args[3].ease_factor, 2.6)

    @patch("polskiflow.reading_views.save_personal_word_review", return_value=True)
    @patch("polskiflow.reading_views.load_personal_words")
    def test_wrong_answer_forces_again_schedule(self, load_words, save_review):
        load_words.return_value = self._practice_words()

        response = self.client.post(
            "/dictionary/practice/step/",
            {
                "action": "next",
                "index": 0,
                "score": 0,
                "selected": 1,
                "quality": "easy",
            },
        )

        self.assertEqual(response.status_code, 200)
        result = save_review.call_args.args[3]
        self.assertEqual(result.repetitions, 0)
        self.assertEqual(result.interval_days, 1)

    @patch("polskiflow.reading_views.load_personal_words")
    def test_practice_selects_only_due_words(self, load_words):
        words = self._practice_words()
        words[0]["next_review_date"] = "2999-01-01"
        load_words.return_value = words

        response = self.client.get("/dictionary/practice/")

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, ">dom<")
        self.assertContains(response, "Слово 1 из 3")

    @patch("polskiflow.reading_views.load_personal_words")
    def test_practice_reports_when_no_words_are_due(self, load_words):
        words = self._practice_words()
        for word in words:
            word["next_review_date"] = "2999-01-01"
        load_words.return_value = words

        response = self.client.get("/dictionary/practice/")

        self.assertContains(response, "На сегодня всё")

    @staticmethod
    def _practice_words():
        return [
            {"id": "word-1", "word": "dom", "translation": "дом", "context": "To jest dom."},
            {"id": "word-2", "word": "mleko", "translation": "молоко", "context": "Lubię mleko."},
            {"id": "word-3", "word": "chleb", "translation": "хлеб", "context": "Jem chleb."},
            {"id": "word-4", "word": "okno", "translation": "окно", "context": "Otwieram okno."},
        ]
