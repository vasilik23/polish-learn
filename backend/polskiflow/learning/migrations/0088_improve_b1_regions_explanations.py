from django.db import migrations


EXPLANATIONS = {
    "b1region-grammar": {
        0: "Przyimek „według” łączy się z dopełniaczem, dlatego poprawną formą jest „według przewodnika”.",
        2: "„Natomiast” podkreśla kontrast między płaską północą regionu a górskim krajobrazem południa.",
    },
    "b1region-quiz": {
        0: "Województwo jest największą jednostką podziału administracyjnego Polski i obejmuje wiele powiatów oraz gmin.",
        2: "Przyimek „według” wymaga dopełniacza, więc rzeczownik „kronika” przyjmuje formę „kroniki”.",
        3: "Konstrukcja „zarówno…, jak i…” łączy równorzędne elementy: w tym zdaniu góry oraz jeziora.",
        5: "„Natomiast” zestawia dwa odmienne obrazy: ruchliwe centrum oraz spokojne wsie.",
        8: "Wyrażenie „w przeciwieństwie do” ma stałe połączenie z przyimkiem „do” i dopełniaczem.",
    },
    "b1region-reading-check": {
        0: "Kasia zaplanowała wyjazd w Beskid Niski, ponieważ chciała poznać mniej oczywisty region Polski.",
        2: "Muzeum prezentowało lokalne dziedzictwo, czyli historię, tradycje i codzienne życie mieszkańców regionu.",
        3: "Kasia odwiedziła rodzinną pracownię, gdzie spotkała rzemieślników pielęgnujących lokalną tradycję.",
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
    dependencies = [("learning", "0087_improve_b1_society_explanations")]
    operations = [migrations.RunPython(improve_explanations, migrations.RunPython.noop)]
