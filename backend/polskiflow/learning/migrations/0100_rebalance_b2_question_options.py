from django.db import migrations


OPTION_FIXES = {
    ("b2view-grammar", 4): [
        "Z jednej strony propozycja oszczędza czas, z drugiej strony ogranicza wybór.",
        "Z jednej strony propozycja oszczędza czas, z drugiej strony zwiększa wybór.",
        "Propozycja oszczędza czas, dlatego nie ogranicza wyboru.",
    ],
    ("b2news-grammar", 4): [
        "Według urzędu most zostanie otwarty w poniedziałek.",
        "Według urzędu most został otwarty w poniedziałek.",
        "Według urzędu most będzie zamknięty w poniedziałek.",
    ],
    ("b2prof-grammar", 4): [
        "W nawiązaniu do naszego spotkania przesyłam uzgodnione podsumowanie.",
        "W nawiązaniu do naszego spotkania przesłałem wstępne podsumowanie.",
        "Przed naszym spotkaniem przesyłam uzgodniony porządek obrad.",
    ],
    ("b2tech-grammar", 4): [
        "Algorytm to zbiór reguł, który jest wykorzystywany do przetwarzania danych.",
        "Algorytm to zbiór danych, który jest wykorzystywany do ustalania reguł.",
        "Algorytm to pojedyncza reguła, która nie służy do przetwarzania danych.",
    ],
    ("b2economy-grammar", 4): [
        "Popyt wzrósł o 8%, ale podaż prawie się nie zmieniła.",
        "Podaż wzrosła o 8%, ale popyt prawie się nie zmienił.",
        "Popyt wzrósł o 8%, dlatego podaż wyraźnie się zwiększyła.",
    ],
    ("b2law-grammar", 4): [
        "Proszę o ponowne rozpatrzenie sprawy na podstawie załączonych dokumentów.",
        "Proszę o pierwsze rozpatrzenie sprawy bez załączonych dokumentów.",
        "Proszę o ponowne odrzucenie sprawy na podstawie ustnego wyjaśnienia.",
    ],
    ("b2psych-grammar", 4): [
        "Prawdopodobnie wycofała się, ponieważ obawiała się kolejnego konfliktu.",
        "Z pewnością wycofała się, chociaż nie obawiała się kolejnego konfliktu.",
        "Prawdopodobnie zaangażowała się, ponieważ oczekiwała kolejnego konfliktu.",
    ],
    ("b2lit-grammar", 4): [
        "Ten obraz można odczytać jako symbol utraconej bliskości.",
        "Ten obraz należy odczytać dosłownie jako opis odzyskanej bliskości.",
        "Ten obraz można odczytać jako symbol przyszłego sukcesu.",
    ],
    ("b2discussion-grammar", 4): [
        "Jeśli dobrze rozumiem, proponuje pan zmienić porządek dyskusji.",
        "Jeśli dobrze rozumiem, proponuje pan zakończyć dyskusję.",
        "Ponieważ dobrze rozumiem, zmienił pan temat dyskusji.",
    ],
    ("b2intercultural-grammar", 4): [
        "W moim doświadczeniu lepiej doprecyzować normę, niż robić założenia.",
        "W moim doświadczeniu lepiej przyjąć założenie, niż pytać o normę.",
        "Bez względu na moje doświadczenie nie warto doprecyzowywać normy.",
    ],
    ("b2academic-grammar", 4): [
        "Oba źródła wskazują na korzyść, ale stosują różne metody.",
        "Oba źródła wskazują na zagrożenie i stosują tę samą metodę.",
        "Tylko jedno źródło wskazuje na korzyść, choć metody są podobne.",
    ],
    ("b2final-grammar", 4): [
        "Chociaż wynik potwierdził tezę, nie można ignorować ograniczenia próby.",
        "Ponieważ wynik podważył tezę, można pominąć ograniczenie próby.",
        "Wynik potwierdził tezę, dlatego ograniczenie próby nie ma znaczenia.",
    ],
}


def rebalance_options(apps, schema_editor):
    Question = apps.get_model("learning", "Question")
    for (lesson_id, position), options in OPTION_FIXES.items():
        Question.objects.filter(lesson_id=lesson_id, position=position).update(
            options=options, correct=0
        )

    questions = Question.objects.filter(
        lesson__topic__course_id="b2-advanced", is_active=True
    ).order_by("lesson_id", "position", "id")
    for index, question in enumerate(questions.iterator()):
        options = list(question.options)
        if len(options) < 2:
            continue
        target = index % len(options)
        answer = options.pop(question.correct)
        options.insert(target, answer)
        question.options = options
        question.correct = target
        question.save(update_fields=["options", "correct"])


class Migration(migrations.Migration):
    dependencies = [("learning", "0099_improve_b2_news_explanations")]
    operations = [migrations.RunPython(rebalance_options, migrations.RunPython.noop)]
