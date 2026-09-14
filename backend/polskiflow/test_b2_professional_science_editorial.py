from django.test import TestCase

from polskiflow.learning.models import Question


class B2ProfessionalScienceEditorialTests(TestCase):
    lesson_ids = (
        "b2prof-grammar",
        "b2prof-quiz",
        "b2prof-reading-check",
        "b2tech-grammar",
        "b2tech-quiz",
        "b2tech-reading-check",
    )

    def test_all_questions_have_teaching_explanations(self):
        questions = Question.objects.filter(lesson_id__in=self.lesson_ids)

        self.assertEqual(questions.count(), 44)
        for question in questions:
            with self.subTest(lesson=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 10)

    def test_explanations_include_rule_and_reading_evidence(self):
        professional = Question.objects.get(lesson_id="b2prof-grammar", position=3)
        science = Question.objects.get(lesson_id="b2tech-reading-check", position=4)

        self.assertIn("przyimkiem „o”", professional.explanation)
        self.assertIn("niewielką próbkę", science.explanation)
