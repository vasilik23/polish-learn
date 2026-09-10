from collections import Counter

from django.test import TestCase

from polskiflow.learning.models import Question


class B2QuestionOptionTests(TestCase):
    def test_correct_answers_are_evenly_distributed(self):
        questions = Question.objects.filter(
            lesson__topic__course_id="b2-advanced", is_active=True
        )
        self.assertEqual(questions.count(), 264)
        self.assertEqual(
            Counter(questions.values_list("correct", flat=True)),
            {0: 88, 1: 88, 2: 88},
        )
        for lesson_id in questions.values_list("lesson_id", flat=True).distinct():
            indices = set(
                questions.filter(lesson_id=lesson_id).values_list(
                    "correct", flat=True
                )
            )
            self.assertEqual(indices, {0, 1, 2}, lesson_id)

    def test_grammar_distractor_fixes_preserve_expected_answers(self):
        expected = {
            "b2view-grammar": "Z jednej strony propozycja oszczędza czas, z drugiej strony ogranicza wybór.",
            "b2news-grammar": "Według urzędu most zostanie otwarty w poniedziałek.",
            "b2prof-grammar": "W nawiązaniu do naszego spotkania przesyłam uzgodnione podsumowanie.",
            "b2tech-grammar": "Algorytm to zbiór reguł, który jest wykorzystywany do przetwarzania danych.",
            "b2economy-grammar": "Popyt wzrósł o 8%, ale podaż prawie się nie zmieniła.",
            "b2law-grammar": "Proszę o ponowne rozpatrzenie sprawy na podstawie załączonych dokumentów.",
            "b2psych-grammar": "Prawdopodobnie wycofała się, ponieważ obawiała się kolejnego konfliktu.",
            "b2lit-grammar": "Ten obraz można odczytać jako symbol utraconej bliskości.",
            "b2discussion-grammar": "Jeśli dobrze rozumiem, proponuje pan zmienić porządek dyskusji.",
            "b2intercultural-grammar": "W moim doświadczeniu lepiej doprecyzować normę, niż robić założenia.",
            "b2academic-grammar": "Oba źródła wskazują na korzyść, ale stosują różne metody.",
            "b2final-grammar": "Chociaż wynik potwierdził tezę, nie można ignorować ograniczenia próby.",
        }
        for lesson_id, answer in expected.items():
            question = Question.objects.get(lesson_id=lesson_id, position=4)
            self.assertEqual(question.options[question.correct], answer)

        all_options = " ".join(
            option
            for lesson_id in expected
            for option in Question.objects.get(lesson_id=lesson_id, position=4).options
        )
        artificial_fragments = (
            "propozycja czas",
            "most otworzyć",
            "wysyłam podsumowaniem",
            "reguły, które wykorzystuje",
            "Podaż o popyt",
            "dla sprawa",
            "Wycofała prawdopodobny",
            "Obrazem można",
            "pan propozycja",
            "norma lepsza",
            "Obie źródła",
            "Wynik chociaż",
        )
        for artificial in artificial_fragments:
            self.assertNotIn(artificial, all_options)

    def test_sentence_building_distractors_are_natural_near_misses(self):
        expected = {
            "b2view-grammar": "Mimo że rozumiem to zastrzeżenie, nowe dane potwierdzają nasz wniosek.",
            "b2news-grammar": "Świadek przekazał, że pociąg zatrzymał się przed stacją.",
            "b2prof-grammar": "Ustalono, że wdrożenie zostanie przesunięte na przyszły miesiąc.",
            "b2tech-grammar": "Na podstawie wyników opracowano nowe rozwiązanie.",
            "b2economy-grammar": "Prawdopodobnie ten wariant będzie bardziej opłacalny w porównaniu z poprzednim.",
            "b2law-grammar": "W związku z brakiem odpowiedzi składam skargę na bezczynność organu.",
            "b2psych-grammar": "Z jego perspektywy mogła okazać więcej zrozumienia.",
            "b2lit-grammar": "Bohaterka powiedziała, że wróci, ale narrator poddaje jej słowa w wątpliwość.",
            "b2discussion-grammar": "Podsumowując, zgadzamy się co do celu, ale sposób pozostaje sporny.",
            "b2intercultural-grammar": "Jeśli dobrze rozumiem, milczenie nie oznaczało sprzeciwu.",
            "b2academic-grammar": "Na podstawie tej próby nie można sformułować ostatecznego wniosku.",
            "b2final-grammar": "Gdybyśmy powtórzyli projekt, wcześniej zebralibyśmy informację zwrotną.",
        }
        for lesson_id, answer in expected.items():
            question = Question.objects.get(lesson_id=lesson_id, position=5)
            self.assertEqual(question.options[question.correct], answer)
            self.assertEqual(len(question.options), 3)
            self.assertEqual(len(set(question.options)), 3)

        all_options = " ".join(
            option
            for lesson_id in expected
            for option in Question.objects.get(lesson_id=lesson_id, position=5).options
        )
        artificial_fragments = (
            "dane wnioskiem",
            "przed stacji",
            "przesunęło miesiącem",
            "opracować rozwiązanie",
            "wariant będzie opłacalność",
            "skargą do bezczynność",
            "zrozumieć mogła",
            "poddawać słowa",
            "mimo sposób spornego",
            "milczenie bez sprzeciwem",
            "wniosek kończy",
            "informacja zbiera",
        )
        for artificial in artificial_fragments:
            self.assertNotIn(artificial, all_options)
