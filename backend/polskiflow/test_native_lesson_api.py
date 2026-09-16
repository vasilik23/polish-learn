import json
from unittest.mock import patch

from django.test import TestCase, override_settings

from polskiflow.auth import SupabaseUser
from polskiflow.domain.native_lessons import build_native_lesson


GRAMMAR = {
    "title": "Szyk",
    "sections": [{"heading": "Reguła", "body": "Opis"}],
    "questions": [
        {"prompt": "Wybierz", "options": ["dobrze", "źle"], "correct": 0, "explanation": "Forma pasuje do kontekstu."},
        {"prompt": "Ułóż", "options": ["Dzisiaj uczę się języka polskiego", "Źle"], "correct": 0, "explanation": "To naturalny szyk zdania."},
    ],
}


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class NativeLessonApiTests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    def _auth(self):
        return patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser(id="owner-1", email="owner@example.com"))

    def test_get_requires_explicit_bearer(self):
        self.client.cookies["polskiflow_access_token"] = "cookie-token"
        with self._auth(), patch("polskiflow.api_views.build_native_lesson") as build:
            response = self.client.get("/api/v1/lessons/grammar-1/")
        self.assertEqual(response.status_code, 401)
        build.assert_not_called()

    @patch("polskiflow.domain.native_lessons.task", return_value={"id": "grammar-1", "kind": "grammar", "title": "Gramatyka"})
    @patch("polskiflow.domain.native_lessons.grammar", return_value=GRAMMAR)
    def test_get_hides_answers_and_explanations(self, _grammar, _task):
        with self._auth():
            response = self.client.get("/api/v1/lessons/grammar-1/", **self.authorization)
        self.assertEqual(response.status_code, 200)
        data = response.json()["data"]
        self.assertEqual(data["step_count"], 2)
        self.assertEqual(data["steps"][0]["type"], "choice")
        self.assertEqual(data["steps"][1]["type"], "sentence_builder")
        serialized = json.dumps(data, ensure_ascii=False)
        self.assertNotIn('"correct"', serialized)
        self.assertNotIn("explanation", serialized)
        self.assertNotIn("owner-1", serialized)

    @patch("polskiflow.domain.native_lessons.task", return_value={"id": "grammar-1", "kind": "grammar", "title": "Gramatyka"})
    @patch("polskiflow.domain.native_lessons.grammar", return_value=GRAMMAR)
    def test_answer_evaluates_choice_and_reveals_feedback_after_submission(self, _grammar, _task):
        with self._auth():
            response = self.client.post(
                "/api/v1/lessons/grammar-1/answer/",
                data=json.dumps({"position": 0, "selected_index": 1}),
                content_type="application/json", **self.authorization,
            )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["data"]["correct"])
        self.assertEqual(response.json()["data"]["correct_index"], 0)
        self.assertIn("kontekstu", response.json()["data"]["explanation"])

    @patch("polskiflow.domain.native_lessons.task", return_value={"id": "grammar-1", "kind": "grammar", "title": "Gramatyka"})
    @patch("polskiflow.domain.native_lessons.grammar", return_value=GRAMMAR)
    def test_sentence_builder_accepts_only_a_complete_token_permutation(self, _grammar, _task):
        lesson = build_native_lesson("grammar-1")
        tokens = lesson.steps[1]["tokens"]
        expected = GRAMMAR["questions"][1]["options"][0].split()
        order = [tokens.index(word) for word in expected]
        with self._auth():
            correct = self.client.post(
                "/api/v1/lessons/grammar-1/answer/", data=json.dumps({"position": 1, "token_order": order}),
                content_type="application/json", **self.authorization,
            )
            invalid = self.client.post(
                "/api/v1/lessons/grammar-1/answer/", data=json.dumps({"position": 1, "token_order": [0]}),
                content_type="application/json", **self.authorization,
            )
        self.assertTrue(correct.json()["data"]["correct"])
        self.assertEqual(invalid.status_code, 400)

    @patch("polskiflow.domain.native_lessons.task", return_value={"id": "words-1", "kind": "words", "title": "Słowa"})
    @patch("polskiflow.domain.native_lessons.flashcards", return_value=[{"polish": "dom", "translation": "дом", "example": "To jest dom."}])
    def test_flashcard_lesson_is_readable_but_self_assessed(self, _cards, _task):
        with self._auth():
            lesson = self.client.get("/api/v1/lessons/words-1/", **self.authorization)
            answer = self.client.post(
                "/api/v1/lessons/words-1/answer/", data=json.dumps({"position": 0, "selected_index": 0}),
                content_type="application/json", **self.authorization,
            )
        self.assertEqual(lesson.json()["data"]["steps"][0]["polish"], "dom")
        self.assertEqual(answer.status_code, 400)
        self.assertEqual(answer.json()["error"]["detail"], "self_assessed_lesson")

    def test_unknown_lesson_invalid_payload_and_content_type_are_explicit(self):
        with self._auth(), patch("polskiflow.api_views.build_native_lesson", return_value=None):
            missing = self.client.get("/api/v1/lessons/missing/", **self.authorization)
        with self._auth():
            wrong_type = self.client.post("/api/v1/lessons/missing/answer/", data="{}", content_type="text/plain", **self.authorization)
        self.assertEqual(missing.status_code, 404)
        self.assertEqual(wrong_type.status_code, 415)
