from django.db import migrations


EXPLANATIONS = {
    "b1culture-grammar": {
        1: "Forma której wyraża przynależność: nagrodzony film należy do dorobku wspomnianej reżyserki.",
    },
    "b1culture-quiz": {
        0: "Ekranizacja to filmowa wersja utworu literackiego, która może zmieniać elementy oryginału.",
        1: "Fabuła oznacza uporządkowany ciąg wydarzeń przedstawionych w książce, filmie lub spektaklu.",
        2: "Zaimek której wyraża przynależność: przeczytana powieść jest dziełem wspomnianej autorki.",
        4: "Ocena przekonująca i naturalna opisuje wiarygodną grę aktora, a nie element fabuły.",
        5: "Scenografia obejmuje wizualną oprawę sceny, która pomaga budować nastrój przedstawienia.",
        8: "Zaimek w którym wskazuje miejsce wydarzenia: wystawa odbywa się w opisanym muzeum.",
    },
    "b1culture-reading-check": {
        2: "Ola pozytywnie oceniła przekonującą grę głównej aktorki, która wiarygodnie stworzyła postać.",
        3: "Film połączył kilka postaci i skrócił wybrane wątki, dlatego różnił się od powieści.",
        4: "Po seansie publiczność spotkała się z reżyserką i mogła porozmawiać o ekranizacji.",
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
    dependencies = [("learning", "0092_improve_b1_media_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
