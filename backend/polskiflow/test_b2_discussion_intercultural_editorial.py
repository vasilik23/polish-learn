from django.test import TestCase

from polskiflow.learning.models import Question


class B2DiscussionInterculturalEditorialTests(TestCase):
    lesson_ids = (
        "b2discussion-grammar",
        "b2discussion-quiz",
        "b2discussion-reading-check",
        "b2intercultural-grammar",
        "b2intercultural-quiz",
        "b2intercultural-reading-check",
    )

    def test_all_questions_have_teaching_explanations(self):
        questions = Question.objects.filter(lesson_id__in=self.lesson_ids)
        self.assertEqual(questions.count(), 44)
        for question in questions:
            with self.subTest(lesson=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 10)

    def test_explanations_teach_moderation_and_intercultural_evidence(self):
        discussion = Question.objects.get(lesson_id="b2discussion-grammar", position=2)
        intercultural = Question.objects.get(
            lesson_id="b2intercultural-reading-check", position=2
        )
        self.assertIn("dopełniaczem", discussion.explanation)
        self.assertIn("wieku, roli, branży", intercultural.explanation)
