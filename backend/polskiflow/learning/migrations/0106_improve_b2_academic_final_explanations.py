from django.db import migrations


EXPLANATIONS = {
    "b2academic-grammar": {
        0: "Forma „wynika” łączy się z przyimkiem „z” i wprowadza wniosek oparty na danych.",
        1: "Czasownik „sugerują” sygnalizuje ostrożną zależność, ponieważ dane nie dowodzą związku przyczynowego.",
        2: "Spójnik „podczas gdy” zestawia dwa odmienne podejścia badawcze opisane w zdaniu.",
        3: "Po konstrukcji „nie pozwala” używamy bezokolicznika, dlatego poprawną formą jest „uogólnić”.",
        4: "Zaimek „oba” zgadza się z nijakim rzeczownikiem „źródła”, a zdanie poprawnie przeciwstawia metody.",
        5: "Wyrażenie „na podstawie” wymaga dopełniacza „tej próby” i wskazuje podstawę formułowanego wniosku.",
    },
    "b2academic-quiz": {
        0: "„Wiarygodne źródło” to po rosyjsku „надёжный источник”, czyli materiał zasługujący na zaufanie.",
        1: "„Przypis” oznacza rosyjską „сноску”, która wskazuje źródło informacji lub dodaje objaśnienie.",
        2: "„Teza” odpowiada rosyjskiemu słowu „тезис” i nazywa główne twierdzenie wymagające uzasadnienia.",
        3: "„Dowód” to po rosyjsku „доказательство”, czyli fakt lub argument potwierdzający dane twierdzenie.",
        4: "„Wniosek” oznacza rosyjski „вывод”, formułowany na podstawie wcześniej przedstawionych danych i argumentów.",
        5: "„Streszczenie” to rosyjskie „резюме”, czyli zwięzłe przedstawienie najważniejszych treści dłuższego tekstu.",
        6: "„Sparafrazować” znaczy „перефразировать”, a więc przekazać tę samą myśl własnymi słowami.",
        7: "„Cytować” odpowiada rosyjskiemu „цитировать” i oznacza dosłownie przytaczać cudze słowa ze źródłem.",
        8: "Zwrot „porównać wyniki” oznacza „сравнить результаты”, czyli wskazać podobieństwa i różnice rezultatów.",
        9: "„Zakres badania” to „охват исследования”, określający temat, granice i obszar przeprowadzonej analizy.",
    },
    "b2academic-reading-check": {
        0: "Oba opisane badania dotyczyły nauki słownictwa, choć sprawdzały odmienne metody uczenia się.",
        1: "Pierwsze badanie trwało tylko trzy tygodnie, dlatego jego ograniczeniem był krótki czas obserwacji.",
        2: "Drugie badanie sugerowało, że samodzielne tworzenie przykładów pomaga skuteczniej zapamiętywać nowe słowa.",
        3: "Natalia nie połączyła liczb, ponieważ badania wykorzystywały różne metody i odmienne próby.",
        4: "Natalia sparafrazowała tezy i podała przypisy, zachowując zasady rzetelnej pracy ze źródłami.",
        5: "Końcowy wniosek wskazywał korzyści metody, ale wyraźnie uwzględniał również ograniczenia badań.",
    },
    "b2final-grammar": {
        0: "Forma „zbadalibyśmy” wyraża niezrealizowaną możliwość zależną od warunku wprowadzonego przez „gdybyśmy”.",
        1: "Spójnik „niemniej” wprowadza istotne zastrzeżenie, które ogranicza wcześniejszą pozytywną ocenę wyniku.",
        2: "Czasownik „odwoływać się” wymaga przyimka „do” oraz rzeczownika w dopełniaczu: „do danych”.",
        3: "Spójnik „o ile” wprowadza warunek, a czasownik „spełnia” zgadza się z podmiotem „projekt”.",
        4: "Spójnik „chociaż” wyraża ustępstwo, a konstrukcja „nie można” bezosobowo wskazuje konieczność.",
        5: "Po „gdybyśmy” występuje forma przeszła, a „zebralibyśmy” wyraża skutek nierealnego warunku.",
    },
    "b2final-quiz": {
        0: "„Pytanie badawcze” oznacza „исследовательский вопрос” i precyzyjnie określa problem analizowany w projekcie.",
        1: "„Założenie” odpowiada rosyjskiej „предпосылке”, czyli twierdzeniu przyjętemu jako punkt wyjścia analizy.",
        2: "„Kryterium sukcesu” to „критерий успеха”, pozwalający zmierzyć, czy projekt osiągnął cel.",
        3: "„Harmonogram” oznacza „график”, czyli uporządkowany w czasie plan działań i terminów projektu.",
        4: "„Etap pośredni” to „промежуточный этап”, znajdujący się między rozpoczęciem a zakończeniem projektu.",
        5: "„Uzasadnienie” oznacza „обоснование”, czyli przedstawienie powodów i dowodów wspierających daną decyzję.",
        6: "„Kontrargument” to „контраргумент”, a więc argument skierowany przeciwko wcześniej przedstawionej tezie.",
        7: "„Zastrzeżenie” odpowiada rosyjskiej „оговорке” i wskazuje ograniczenie albo warunek przedstawionej opinii.",
        8: "Zwrot „wyciągnąć wniosek” znaczy „сделать вывод”, czyli sformułować rezultat na podstawie danych.",
        9: "„Ocenić rezultat” oznacza „оценить результат”, czyli porównać uzyskany wynik z przyjętymi kryteriami.",
    },
    "b2final-reading-check": {
        0: "Pytanie projektu dotyczyło poprawy warunków dzięki cichej godzinie bez ograniczania dostępu do biblioteki.",
        1: "Zespół przyjął mierzalne kryteria: mniej hałasu oraz brak wzrostu liczby skarg użytkowników.",
        2: "Harmonogram wydłużono po informacji zwrotnej, aby możliwe było porównanie wyników z różnych dni.",
        3: "Badanie objęło tylko jedną filię, więc jego wyniku nie można automatycznie uogólnić.",
        4: "Zespół przyznał, że problem jest możliwy, a następnie odpowiedział na niego konkretnymi danymi.",
        5: "Dobra obrona projektu wymagała uczciwego pokazania zarówno siły danych, jak i ich granic.",
    },
}


def improve_explanations(apps, schema_editor):
    Question = apps.get_model("learning", "Question")
    for lesson_id, explanations in EXPLANATIONS.items():
        for position, explanation in explanations.items():
            Question.objects.filter(lesson_id=lesson_id, position=position).update(
                explanation=explanation
            )


class Migration(migrations.Migration):
    dependencies = [("learning", "0105_improve_b2_economy_law_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
