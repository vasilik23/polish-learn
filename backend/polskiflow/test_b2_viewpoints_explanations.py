from django.test import TestCase

from polskiflow.learning.models import Question


class B2ViewpointsExplanationTests(TestCase):
    def test_weakest_explanations_are_expanded(self):
        expected_positions = {
            "b2view-grammar": {1, 3},
            "b2view-quiz": {0, 1, 5},
            "b2view-reading-check": {0, 1, 3, 4, 5},
        }
        for lesson_id, positions in expected_positions.items():
            questions = Question.objects.filter(
                lesson_id=lesson_id, position__in=positions
            )
            self.assertEqual(questions.count(), len(positions))
            for question in questions:
                self.assertGreaterEqual(len(question.explanation.split()), 10)
