from django.db import migrations


EXPLANATIONS = {
    "b1media-grammar": {
        2: "W mowie zależnej treść relacji po czasowniku relacjonował wprowadzamy spójnikiem że.",
        3: "Słowo następnie porządkuje streszczenie, łącząc przedstawienie tematu z kolejną główną myślą.",
    },
    "b1media-quiz": {
        1: "Udostępniać wiadomość znaczy przekazywać ją dalej, czego nie warto robić bez sprawdzenia źródła.",
        2: "Czasownik twierdzić wprowadza zdecydowane stanowisko autora, a nie neutralny wynik analizy.",
        4: "Dobre streszczenie najpierw wskazuje temat tekstu, a następnie jasno podaje jego główną myśl.",
        5: "Po czasowniku zaprzeczył treść odrzucanego twierdzenia wprowadzamy w tym zdaniu spójnikiem że.",
        8: "Czasownik relacjonować oznacza przedstawiać przebieg wydarzenia w uporządkowanym porządku chronologicznym.",
    },
    "b1media-reading-check": {
        1: "Nagłówek wzbudził wątpliwości Marty, ponieważ nie zawierał autora ani daty opisywanej decyzji.",
        2: "Marta sprawdziła wiadomość, porównując wpis z oficjalną stroną oraz wiarygodnym lokalnym portalem.",
        3: "Biblioteka planowała jedynie krótki remont jednego piętra, a nie całkowite zamknięcie placówki.",
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
    dependencies = [("learning", "0091_improve_b1_education_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
