from django.test import TestCase

from polskiflow.learning.models import Question


class B1MediaExplanationTests(TestCase):
    def test_weakest_explanations_are_expanded(self):
        expected_positions = {
            "b1media-grammar": {2, 3},
            "b1media-quiz": {1, 2, 4, 5, 8},
            "b1media-reading-check": {1, 2, 3},
        }
        for lesson_id, positions in expected_positions.items():
            questions = Question.objects.filter(
                lesson_id=lesson_id, position__in=positions
            )
            self.assertEqual(questions.count(), len(positions))
            for question in questions:
                self.assertGreaterEqual(len(question.explanation.split()), 10)
