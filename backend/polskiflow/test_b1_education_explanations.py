from django.test import TestCase

from polskiflow.learning.models import Question


class B1EducationExplanationTests(TestCase):
    def test_weakest_explanations_are_expanded(self):
        expected_positions = {
            "b1edu-grammar": {0, 2},
            "b1edu-quiz": {2, 3, 4, 5, 6, 8},
            "b1edu-reading-check": {0, 5},
        }
        for lesson_id, positions in expected_positions.items():
            questions = Question.objects.filter(
                lesson_id=lesson_id, position__in=positions
            )
            self.assertEqual(questions.count(), len(positions))
            for question in questions:
                self.assertGreaterEqual(len(question.explanation.split()), 10)
