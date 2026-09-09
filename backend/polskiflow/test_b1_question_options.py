from django.test import TestCase

from polskiflow.learning.models import Question


class B1QuestionOptionTests(TestCase):
    def test_correct_answers_use_multiple_positions_per_lesson(self):
        questions = Question.objects.filter(
            lesson__topic__course_id="b1-independent", is_active=True
        )
        self.assertEqual(questions.count(), 264)
        self.assertEqual(set(questions.values_list("correct", flat=True)), {0, 1, 2})
        for lesson_id in questions.values_list("lesson_id", flat=True).distinct():
            indices = set(
                questions.filter(lesson_id=lesson_id).values_list("correct", flat=True)
            )
            self.assertGreaterEqual(len(indices), 2, lesson_id)

    def test_corrected_distractors_preserve_expected_answers(self):
        expected = {
            ("bio-grammar", 0): "pracowała",
            ("b1health-grammar", 0): "odłożyć",
            ("b1health-quiz", 2): "radzić sobie ze stresem",
            ("b1media-grammar", 0): "twierdzi",
            ("b1media-quiz", 7): "streścić publikację",
            ("b1soc-quiz", 6): "korzyści",
            ("b1region-quiz", 6): "zachować tradycję",
            ("b1final-quiz", 2): "Z poważaniem",
            ("b1final-quiz", 6): "konkretny przykład",
        }
        for lookup, answer in expected.items():
            question = Question.objects.get(lesson_id=lookup[0], position=lookup[1])
            self.assertEqual(question.options[question.correct], answer)

        all_options = " ".join(
            option
            for options in Question.objects.filter(
                lesson__topic__course_id="b1-independent"
            ).values_list("options", flat=True)
            for option in options
        )
        for artificial in ("wadywać", "Do zobaczyska", "odkładać raz"):
            self.assertNotIn(artificial, all_options)
