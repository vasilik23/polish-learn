from django.test import TestCase

from polskiflow.learning.models import Question


class B1TravelExplanationTests(TestCase):
    def test_weakest_explanations_are_expanded(self):
        expected_positions = {
            "b1trip-grammar": {0, 2},
            "b1trip-quiz": {0, 1, 4, 9},
            "b1trip-reading-check": {0, 1, 3, 4},
        }
        for lesson_id, positions in expected_positions.items():
            questions = Question.objects.filter(
                lesson_id=lesson_id, position__in=positions
            )
            self.assertEqual(questions.count(), len(positions))
            for question in questions:
                self.assertGreaterEqual(len(question.explanation.split()), 10)
