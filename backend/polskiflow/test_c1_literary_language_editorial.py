from django.test import TestCase

from polskiflow.learning.models import Flashcard, Question


class C1LiteraryLanguageEditorialTests(TestCase):
    def test_flashcards_use_terms_in_natural_literary_analysis(self):
        cards = Flashcard.objects.filter(id__regex=r"^c17-").order_by("position")
        self.assertEqual(cards.count(), 15)

        for card in cards:
            with self.subTest(card_id=card.id):
                self.assertIn(card.polish.lower(), card.example.lower())
                self.assertNotIn("W tej wypowiedzi ważne", card.example)
                self.assertGreaterEqual(len(card.example.split()), 10)

    def test_explanations_teach_terms_and_identify_textual_evidence(self):
        questions = Question.objects.filter(lesson__topic_id="c1-literary-language")
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

        metaphor = questions.get(lesson_id="c17-grammar", position=2)
        self.assertIn("bez dosłownego «jak»", metaphor.explanation)
        evidence = questions.get(lesson_id="c17-reading-check", position=4)
        self.assertIn("ironię dramatyczną", evidence.explanation)
