from django.db import migrations


EXPLANATIONS = {
    "b2view-grammar": {
        1: "Marker niemniej jednak wprowadza kontrast: wysoki koszt nie wyklucza przyszłych oszczędności.",
        3: "Stałe wyrażenie odnieść się do wymaga przyimka do oraz rzeczownika w dopełniaczu.",
    },
    "b2view-quiz": {
        0: "Stanowisko w dyskusji oznacza jasno określoną opinię uczestnika wobec omawianej kwestii.",
        1: "Uzasadnienie wyjaśnia, dlaczego teza jest przekonująca, łącząc ją z argumentami lub danymi.",
        5: "Marker z drugiej strony wprowadza odmienną perspektywę, która kontrastuje z wcześniejszym argumentem.",
    },
    "b2view-reading-check": {
        0: "Debata dotyczyła ograniczenia ruchu samochodowego w centrum oraz skutków takiej zmiany.",
        1: "Lena poparła pilotaż warunkowo, domagając się zabezpieczeń i późniejszej oceny jego skutków.",
        3: "Kontrargument Leny opierał się na wynikach porównywalnego pilotażu przeprowadzonego w innym mieście.",
        4: "Uczestnicy uwzględnili wyjątki oraz ocenę skutków po pół roku działania rozwiązania.",
        5: "Tekst pokazuje, że rzeczowa debata może doprecyzować i ulepszyć początkową propozycję.",
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
    dependencies = [("learning", "0096_improve_b1_relationships_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
