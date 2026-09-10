from django.db import migrations


EXPLANATIONS = {
    "b2news-grammar": {
        3: "Przymiotnik „przełomowa” wyraża ocenę autora, której nie da się sprawdzić jak faktu.",
        5: "Spójnik „że” wprowadza treść relacji świadka i wymaga zmiany mowy niezależnej na zależną.",
    },
    "b2news-quiz": {
        0: "Sprostowanie oficjalnie poprawia wcześniej opublikowaną informację, która okazała się nieprawdziwa lub nieścisła.",
        1: "Zwrot „jak podaje urząd” jednoznacznie przypisuje wiadomość konkretnemu, możliwemu do sprawdzenia źródłu.",
        2: "Określenie „katastrofalny” zawiera silną ocenę skutków, zamiast neutralnie opisywać sprawdzalny fakt.",
        3: "Czasownik „wynikać” łączy się z przyimkiem „z”, dlatego poprawna forma brzmi „wynika z komunikatu”.",
        4: "Partykuła „podobno” sygnalizuje, że informacja nie została potwierdzona i autor zachowuje wobec niej dystans.",
        5: "Czasownik „zaprzeczyć” wymaga celownika, dlatego ministerstwo zaprzecza właśnie „doniesieniom”, a nie „doniesienia”.",
        6: "Godzina rozpoczęcia konferencji jest konkretną daną, którą można niezależnie potwierdzić w harmonogramie.",
        7: "Spójnik „że” wprowadza mowę zależną, a „jutro” zmienia się na „następnego dnia”.",
        8: "Zestawienie niezależnych relacji ujawnia ich wspólne fakty oraz oddziela je od ocen i przypuszczeń.",
        9: "Nagłówek podaje mierzalny wynik bez emocjonalnych epitetów, dlatego pozostaje najbardziej bezstronny.",
    },
    "b2news-reading-check": {
        0: "Każda z trzech publikacji opisywała tę samą awarię systemu sprzedaży biletów.",
        1: "Operator potwierdził czas rozpoczęcia awarii oraz liczbę niedostępnych punktów sprzedaży.",
        2: "Operator nie wskazał przyczyny awarii, ponieważ miała zostać ustalona dopiero po analizie.",
        3: "Po aktualizacji redakcja zastąpiła sensacyjne określenia ostrożniejszym, bardziej neutralnym językiem.",
        4: "Porównanie źródeł potwierdziło samą awarię, lecz nie sensacyjne hipotezy dotyczące jej przyczyn.",
        5: "Grupa postanowiła wyraźnie oznaczać fakty, oceny i przypuszczenia, aby kontrolować stopień pewności.",
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
    dependencies = [("learning", "0098_rebalance_b1_question_options")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
