from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.learning.models import Flashcard, Lesson, LessonFlashcard, Question
from polskiflow.progress_store import DashboardProgress


class LessonViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Lesson.objects.all().delete()
        Flashcard.objects.all().delete()
        lesson_data = [
            ("words", "Słówka dnia", "Новые слова"),
            ("grammar", "Gramatyka", "Грамматика"),
            ("review", "Powtórka", "Повторение"),
            ("quiz", "Quiz", "Мини-тест"),
        ]
        for position, (lesson_id, title, plan_title) in enumerate(lesson_data):
            Lesson.objects.create(
                id=lesson_id,
                kind=lesson_id,
                title=title,
                plan_title=plan_title,
                subtitle="5 заданий",
                description="Описание",
                position=position,
                theory_title="Rodzajnik i ród rzeczownika" if lesson_id == "grammar" else "",
                theory_sections=[["Род существительных", "Короткая теория"]] if lesson_id == "grammar" else [],
            )
        cards = [
            ("czesc", "cześć", "привет"),
            ("dziekuje", "dziękuję", "спасибо"),
            ("prosze", "proszę", "пожалуйста"),
            ("tak", "tak", "да"),
            ("nie", "nie", "нет"),
        ]
        for position, (card_id, polish, translation) in enumerate(cards):
            card = Flashcard.objects.create(id=card_id, polish=polish, translation=translation, position=position)
            LessonFlashcard.objects.create(
                lesson_id="words", flashcard=card, position=position
            )
        review_card = Flashcard.objects.create(
            id="jestem", polish="jestem", translation="я есть", position=5
        )
        LessonFlashcard.objects.create(
            lesson_id="review", flashcard=review_card, position=0
        )
        grammar_prompts = ["Слово «kawa»", "Слово «dom»", "Слово «miasto»"]
        for position, prompt in enumerate(grammar_prompts):
            Question.objects.create(lesson_id="grammar", prompt=prompt, options=["мужской", "женский", "средний"], correct=position % 3, explanation="Пояснение", position=position)
        quiz_prompts = ["Как переводится «cześć»?", "Что значит «dziękuję»?", "Выберите перевод", "Как будет «да»?", "Как будет «нет»?"]
        for position, prompt in enumerate(quiz_prompts):
            Question.objects.create(lesson_id="quiz", prompt=prompt, options=["нет", "привет", "спасибо"], correct=1, explanation="Cześć — неформальное «привет».", position=position)
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        self.auth_patch = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser("user-123", "learner@example.com"),
        )
        self.auth_patch.start()
        self.addCleanup(self.auth_patch.stop)

    def test_home_lists_all_lessons(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Słówka dnia")
        self.assertContains(response, "Gramatyka")
        self.assertContains(response, "Powtórka")
        self.assertContains(response, "Quiz")

    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_home_marks_today_progress(self, mocked_progress):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A2",
            streak_days=4,
            completed_lesson_ids=frozenset({"words", "grammar"}),
            available=True,
        )

        response = self.client.get("/")

        self.assertContains(response, "Cześć, Василий!")
        self.assertContains(response, "Уровень A2")
        self.assertContains(response, "4 дн. подряд")
        self.assertContains(response, "2 из 4")
        self.assertContains(response, 'class="task-complete"', count=2)

    def test_unknown_lesson_returns_404(self):
        self.assertEqual(self.client.get("/lesson/unknown/").status_code, 404)

    def test_flashcard_can_be_revealed_and_completed(self):
        revealed = self.client.post(
            "/lesson/words/step/", {"action": "reveal", "index": 0, "score": 0}
        )
        self.assertContains(revealed, "привет")

        response = None
        for index in range(5):
            response = self.client.post(
                "/lesson/words/step/",
                {"action": "know", "index": index, "score": index},
            )
        self.assertContains(response, "5 / 5")
        self.assertContains(response, "Урок завершён")

    def test_quiz_answer_shows_explanation_and_next_question(self):
        answered = self.client.post(
            "/lesson/quiz/step/",
            {"action": "answer", "index": 0, "score": 0, "choice": 1},
        )
        self.assertContains(answered, "Cześć — неформальное")
        next_question = self.client.post(
            "/lesson/quiz/step/",
            {"action": "next", "index": 0, "score": 0, "selected": 1},
        )
        self.assertContains(next_question, "Что значит")

    def test_grammar_theory_starts_exercises(self):
        page = self.client.get("/lesson/grammar/")
        self.assertContains(page, "Род существительных")
        exercise = self.client.post(
            "/lesson/grammar/step/", {"action": "start", "index": 0, "score": 0}
        )
        self.assertContains(exercise, "Слово «kawa»")

    def test_review_uses_only_its_linked_flashcards(self):
        page = self.client.get("/lesson/review/")

        self.assertContains(page, "jestem")
        self.assertContains(page, "Карточка 1 из 1")
        self.assertNotContains(page, "cześć")

    def test_invalid_lesson_state_is_rejected(self):
        response = self.client.post(
            "/lesson/quiz/step/",
            {"action": "answer", "index": 999, "score": 0, "choice": 0},
        )
        self.assertEqual(response.status_code, 400)
