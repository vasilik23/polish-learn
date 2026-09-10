from django.db import migrations


def resolve_ambiguity(apps, schema_editor):
    Question = apps.get_model("learning", "Question")
    Question.objects.filter(lesson_id="food-grammar", position=2).update(
        prompt="Widzę świeży ___ na półce.",
        options=["chleb", "chleba", "chlebem"],
        correct=0,
    )


class Migration(migrations.Migration):
    dependencies = [("learning", "0101_improve_a1_a2_question_wording")]
    operations = [migrations.RunPython(resolve_ambiguity, migrations.RunPython.noop)]
