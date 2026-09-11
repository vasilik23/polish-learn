from django.test import TestCase

from polskiflow.learning.models import Question


class B2EconomyLawEditorialTests(TestCase):
    def test_explanations_teach_rules_or_cite_reading_evidence(self):
        questions = Question.objects.filter(
            lesson__topic_id__in=["b2-economy-consumption", "b2-law-civic"]
        )

        self.assertEqual(questions.count(), 44)
        for question in questions:
            with self.subTest(lesson=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 10)
                self.assertEqual(len(question.options), 3)
                self.assertIn(question.correct, range(len(question.options)))

        law_evidence = questions.get(lesson_id="b2law-reading-check", position=2)
        self.assertIn("elektronicznym potwierdzeniem", law_evidence.explanation)
        economy_rule = questions.get(lesson_id="b2economy-grammar", position=1)
        self.assertIn("wartość początkową i końcową", economy_rule.explanation)
