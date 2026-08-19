from unittest.mock import patch

from django.test import SimpleTestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser


class LessonViewsTests(SimpleTestCase):
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
        self.assertContains(response, "5 из 5")
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

    def test_invalid_lesson_state_is_rejected(self):
        response = self.client.post(
            "/lesson/quiz/step/",
            {"action": "answer", "index": 999, "score": 0, "choice": 0},
        )
        self.assertEqual(response.status_code, 400)
