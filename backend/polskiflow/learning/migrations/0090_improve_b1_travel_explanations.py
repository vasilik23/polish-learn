from django.db import migrations


EXPLANATIONS = {
    "b1trip-grammar": {
        0: "Czasownik dojechać podkreśla dotarcie do celu, tutaj do Krakowa przed określoną godziną.",
        2: "Zwrot przejechać przez opisuje ruch przez miejsce bez zatrzymywania się w nim.",
    },
    "b1trip-quiz": {
        0: "Przesiadka oznacza zmianę pociągu lub innego środka transportu podczas jednej podróży.",
        1: "Odwołany lot nie odbędzie się zgodnie z planem, dlatego trzeba znaleźć inne połączenie.",
        4: "Czasownik dojechać wskazuje na osiągnięcie celu podróży, a nie sam ruch.",
        9: "Stałe wyrażenie zrobić wrażenie oznacza wywołać u kogoś określoną reakcję lub ocenę.",
    },
    "b1trip-reading-check": {
        0: "Marta i Paweł jechali do Pragi, co tekst wskazuje jako cel ich podróży.",
        1: "Pierwszy problem pojawił się w Katowicach, gdzie podróżni dowiedzieli się o utrudnieniach.",
        3: "Pracownica znalazła połączenie przez inną miejscowość, dzięki czemu podróż mogła trwać dalej.",
        4: "Podczas przerwy podróżni zwiedzili okolicę, zamiast cały czas czekać na peronie.",
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
    dependencies = [("learning", "0089_improve_b1_biography_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
