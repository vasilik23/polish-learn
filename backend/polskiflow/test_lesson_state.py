from django.test import SimpleTestCase

from polskiflow.domain.lesson_state import (
    InvalidLessonState,
    load_lesson_state,
    sign_lesson_state,
)


class LessonStateTests(SimpleTestCase):
    def test_round_trip_preserves_bounded_state(self):
        token = sign_lesson_state("user-1", "quiz", "quiz", 3, 2)
        self.assertEqual(load_lesson_state(token, "user-1", "quiz", "quiz").index, 3)
        self.assertEqual(load_lesson_state(token, "user-1", "quiz", "quiz").score, 2)
        self.assertEqual(load_lesson_state(token, "user-1", "quiz", "quiz").phase, "ready")
        self.assertNotIn("user-1", token)

    def test_token_is_bound_to_owner_lesson_and_kind(self):
        token = sign_lesson_state("user-1", "quiz", "quiz", 1, 1)
        for owner, lesson, kind in (
            ("user-2", "quiz", "quiz"),
            ("user-1", "grammar", "quiz"),
            ("user-1", "quiz", "grammar"),
        ):
            with self.assertRaises(InvalidLessonState):
                load_lesson_state(token, owner, lesson, kind)

    def test_tampering_is_rejected(self):
        token = sign_lesson_state("user-1", "quiz", "quiz", 1, 1)
        with self.assertRaises(InvalidLessonState):
            load_lesson_state(token[:-1] + "x", "user-1", "quiz", "quiz")
