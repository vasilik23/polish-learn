from django.test import TestCase

from polskiflow.learning.models import Flashcard, Question


class C1PublicDiscussionEditorialTests(TestCase):
    def test_flashcards_use_terms_in_natural_public_discussion_contexts(self):
        cards = Flashcard.objects.filter(id__regex=r"^c18-").order_by("position")
        self.assertEqual(cards.count(), 15)

        for card in cards:
            with self.subTest(card_id=card.id):
                self.assertIn(card.polish.lower(), card.example.lower())
                self.assertNotIn("W tej wypowiedzi ważne", card.example)
                self.assertGreaterEqual(len(card.example.split()), 9)

    def test_all_explanations_teach_concepts_or_point_to_reading_evidence(self):
        questions = Question.objects.filter(lesson__topic_id="c1-public-discussion")
        self.assertEqual(questions.count(), 22)

        weak_templates = (
            "oznacza:",
            "Ответ прямо следует из текста.",
            "Первый вариант точно передаёт содержание абзаца.",
        )
        for question in questions:
            with self.subTest(lesson_id=question.lesson_id, position=question.position):
                self.assertGreaterEqual(len(question.explanation.split()), 12)
                for template in weak_templates:
                    self.assertNotIn(template, question.explanation)

        fair_argument = questions.get(lesson_id="c18-grammar", position=5)
        self.assertIn("najmocniejszą wersję", fair_argument.explanation)
        common_ground = questions.get(lesson_id="c18-reading-check", position=0)
        self.assertIn("miejsc parkingowych", common_ground.explanation)
