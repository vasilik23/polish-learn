from django.test import TestCase

from polskiflow.learning.models import Question


class B2AcademicFinalEditorialTests(TestCase):
    def test_all_explanations_are_substantive(self):
        for topic_id in ("b2-academic-skills", "b2-final-project"):
            questions = Question.objects.filter(lesson__topic_id=topic_id)
            self.assertEqual(questions.count(), 22)
            for question in questions:
                self.assertGreaterEqual(
                    len(question.explanation.split()),
                    10,
                    f"{question.lesson_id}:{question.position}",
                )

    def test_explanations_teach_evidence_and_form(self):
        academic = Question.objects.get(lesson_id="b2academic-grammar", position=1)
        final = Question.objects.get(lesson_id="b2final-reading-check", position=3)
        self.assertIn("nie dowodzą", academic.explanation)
        self.assertIn("nie można automatycznie uogólnić", final.explanation)
