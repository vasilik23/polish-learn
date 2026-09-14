from django.test import TestCase

from polskiflow.learning.models import Question


class B2PsychologyLiteratureEditorialTests(TestCase):
    lesson_ids = (
        "b2psych-grammar", "b2psych-quiz", "b2psych-reading-check",
        "b2lit-grammar", "b2lit-quiz", "b2lit-reading-check",
    )

    def test_all_questions_have_teaching_explanations(self):
        questions = Question.objects.filter(lesson_id__in=self.lesson_ids)
        self.assertEqual(questions.count(), 44)
        for question in questions:
            with self.subTest(lesson=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 10)

    def test_explanations_include_rule_and_reading_evidence(self):
        psychology = Question.objects.get(lesson_id="b2psych-grammar", position=2)
        literature = Question.objects.get(lesson_id="b2lit-reading-check", position=4)
        self.assertIn("bezokolicznik", psychology.explanation)
        self.assertIn("kto nadchodzi", literature.explanation)
