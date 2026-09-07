from django.test import TestCase

from polskiflow.learning.models import Question


class B1BiographyExplanationTests(TestCase):
    def test_weakest_explanations_are_expanded(self):
        expected_positions = {
            "bio-grammar": {1},
            "bio-quiz": {0, 3, 4, 6, 8, 9},
            "bio-reading-check": {0, 1, 4},
        }
        for lesson_id, positions in expected_positions.items():
            questions = Question.objects.filter(
                lesson_id=lesson_id, position__in=positions
            )
            self.assertEqual(questions.count(), len(positions))
            for question in questions:
                self.assertGreaterEqual(len(question.explanation.split()), 10)
