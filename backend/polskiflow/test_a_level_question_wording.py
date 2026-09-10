from django.test import TestCase

from polskiflow.learning.models import Question


class ALevelQuestionWordingTests(TestCase):
    def test_editorial_fixes_keep_one_expected_answer(self):
        expected = {
            ("food-grammar", 2): "chleb",
            ("weather-grammar", 0): "trzeba",
            ("weather-grammar", 3): "może",
            ("city-grammar", 4): "Jak dojść do dworca?",
            ("city-quiz", 2): "Proszę skręcić w prawo.",
            ("city-quiz", 7): "Jak dojść do apteki?",
            ("countries-grammar", 4): "Pochodzę z Ukrainy.",
            ("daily-routine-grammar", 4): "Nigdy nie piję kawy wieczorem.",
            ("family-grammar", 3): "Ile lat ma twoja siostra?",
            ("family-quiz", 7): "Ile lat ma twój brat?",
            ("final-quiz", 0): "Mam na imię Lena.",
            ("final-quiz", 6): "Jak dojść do dworca?",
            ("food-quiz", 7): "Poproszę kawę bez cukru.",
            ("free-quiz", 6): "Co lubisz robić w weekend?",
            ("home-quiz", 6): "Gdzie jest klucz?",
            ("a2final-quiz", 5): "Powinieneś odpocząć i skontaktować się z lekarzem.",
            ("a2final-quiz", 8): "Czy może mi pani powiedzieć, gdzie mam podpisać?",
            ("office-grammar", 0): "Chciałbym złożyć wniosek.",
            ("office-grammar", 2): "dwunasty marca dwa tysiące dwudziestego szóstego roku",
            ("office-grammar", 3): "Proszę podpisać formularz tutaj.",
            ("housing-quiz", 3): "Zgłosić usterkę administracji.",
            ("med-quiz", 3): "Mam uczulenie na penicylinę.",
            ("med-quiz", 5): "Jeśli stan się pogorszy…",
        }
        for key, answer in expected.items():
            question = Question.objects.get(lesson_id=key[0], position=key[1])
            self.assertEqual(question.options[question.correct], answer, key)
            self.assertEqual(len(question.options), len(set(question.options)), key)

    def test_ambiguous_prompts_are_explicit(self):
        prompts = {
            ("food-grammar", 2): "Kupuję dziś ___.",
            ("weather-grammar", 0): "Lekarz podkreśla konieczność:",
            ("weather-grammar", 3): "Prognoza nie jest pewna:",
        }
        for key, fragment in prompts.items():
            question = Question.objects.get(lesson_id=key[0], position=key[1])
            self.assertIn(fragment, question.prompt)
