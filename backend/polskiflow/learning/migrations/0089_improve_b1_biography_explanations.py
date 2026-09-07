from django.db import migrations


EXPLANATIONS = {
    "bio-grammar": {
        1: "Forma ukończyła nazywa zakończoną czynność z wyraźnym rezultatem: Marta otrzymała certyfikat.",
    },
    "bio-quiz": {
        0: "Czasownik dorastać opisuje stopniowe dojrzewanie i przechodzenie od dzieciństwa do dorosłości.",
        3: "Wyrażenie osiągnął cel oznacza uzyskanie zamierzonego rezultatu po roku pracy nad projektem.",
        4: "Niedokonana forma jeździłem opisuje czynność wielokrotną, ponieważ podróże powtarzały się w przeszłości.",
        6: "Słowo początkowo wprowadza pierwszy etap historii i zapowiada późniejszą zmianę sytuacji.",
        8: "Markery najpierw, następnie, z czasem i w końcu porządkują kolejne etapy biografii.",
        9: "Forma ukończyłem wskazuje zakończony etap edukacji, a data precyzuje moment jego zamknięcia.",
    },
    "bio-reading-check": {
        0: "Joanna dorastała w Białymstoku; ta informacja pojawia się na początku jej biografii.",
        1: "Joanna studiowała architekturę w Warszawie, zanim zaczęła rozwijać własną drogę zawodową.",
        4: "Joanna postanowiła projektować przestrzenie publiczne, więc ukierunkowała pracę na potrzeby mieszkańców.",
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
    dependencies = [("learning", "0088_improve_b1_regions_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
