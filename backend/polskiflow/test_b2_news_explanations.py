from django.test import TestCase

from polskiflow.learning.models import Question


class B2NewsExplanationTests(TestCase):
    def test_short_explanations_are_expanded(self):
        expected_positions = {
            "b2news-grammar": {3, 5},
            "b2news-quiz": set(range(10)),
            "b2news-reading-check": set(range(6)),
        }
        for lesson_id, positions in expected_positions.items():
            questions = Question.objects.filter(
                lesson_id=lesson_id, position__in=positions
            )
            self.assertEqual(questions.count(), len(positions))
            for question in questions:
                self.assertGreaterEqual(len(question.explanation.split()), 10)
