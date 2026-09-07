from django.test import TestCase

from polskiflow.learning.models import Question


class B1SocietyExplanationTests(TestCase):
    def test_weakest_explanations_are_expanded(self):
        expected_positions = {
            "b1soc-grammar": {0, 1, 2, 3, 4},
            "b1soc-quiz": {2, 3},
            "b1soc-reading-check": {2, 3, 4},
        }

        for lesson_id, positions in expected_positions.items():
            questions = Question.objects.filter(
                lesson_id=lesson_id, position__in=positions
            )
            self.assertEqual(questions.count(), len(positions))
            for question in questions:
                self.assertGreaterEqual(len(question.explanation.split()), 10)
