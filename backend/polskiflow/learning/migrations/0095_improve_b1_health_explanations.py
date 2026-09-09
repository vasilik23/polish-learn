from django.db import migrations


EXPLANATIONS = {
    "b1health-grammar": {
        0: "Jednorazowa rada z oczekiwanym skutkiem wymaga formy dokonanej odłożyć, czyli usunąć telefon.",
    },
    "b1health-quiz": {
        0: "Utrzymać nawyk oznacza regularnie kontynuować wybrane działanie mimo pojawiających się trudności.",
        1: "Czasownik wysypiać się oznacza spać wystarczająco długo, aby odzyskać energię i koncentrację.",
        4: "Dokonana forma wykonałem podkreśla, że cały zaplanowany zestaw ćwiczeń został zakończony.",
        6: "Jedna niewielka zmiana naraz jest bezpieczniejsza i łatwiejsza do trwałego utrzymania.",
    },
    "b1health-reading-check": {
        0: "Kuba chciał zmienić tryb życia, ponieważ często czuł zmęczenie i źle spał.",
        2: "Fizjoterapeutka zaleciła jeden mały nawyk oraz uważne obserwowanie reakcji własnego organizmu.",
        3: "Kuba zaczął od krótkiego spaceru po pracy, wybierając realistyczny i łagodny pierwszy krok.",
        4: "Po kilku tygodniach regularnych spacerów Kuba lepiej spał i miał więcej energii.",
        5: "Trwała zmiana powstaje stopniowo i wymaga obserwacji samopoczucia oraz odpowiedniej regeneracji.",
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
    dependencies = [("learning", "0094_improve_b1_work_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
