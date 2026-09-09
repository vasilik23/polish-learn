from django.db import migrations


OPTION_FIXES = {
    ("bio-grammar", 0): ["pracowała", "pracuje", "będzie pracować"],
    ("b1health-grammar", 0): ["odłożyć", "odkładam", "odłożony"],
    ("b1health-quiz", 2): ["radzić sobie ze stresem", "radzić stresowi", "radzić o stresie"],
    ("b1media-grammar", 0): ["twierdzi", "wynika", "streszcza"],
    ("b1media-quiz", 7): ["streścić publikację", "skomentować publikację", "udostępnić publikację"],
    ("b1soc-quiz", 6): ["korzyści", "korzyść", "korzystni"],
    ("b1region-quiz", 6): ["zachować tradycję", "opisać krajobraz", "poznać gwarę"],
    ("b1final-quiz", 2): ["Z poważaniem", "Do zobaczenia", "Trzymaj się"],
    ("b1final-quiz", 6): ["konkretny przykład", "powitanie", "zmiana tematu"],
}


def rebalance_options(apps, schema_editor):
    Question = apps.get_model("learning", "Question")
    for (lesson_id, position), options in OPTION_FIXES.items():
        Question.objects.filter(lesson_id=lesson_id, position=position).update(
            options=options, correct=0
        )

    questions = Question.objects.filter(
        lesson__topic__course_id="b1-independent", is_active=True
    )
    for question in questions.iterator():
        options = list(question.options)
        if len(options) < 2:
            continue
        shift = 1 + (question.position + sum(map(ord, question.lesson_id))) % (
            len(options) - 1
        )
        rotated = [None] * len(options)
        for index, option in enumerate(options):
            rotated[(index + shift) % len(options)] = option
        question.options = rotated
        question.correct = (question.correct + shift) % len(options)
        question.save(update_fields=["options", "correct"])


class Migration(migrations.Migration):
    dependencies = [("learning", "0097_improve_b2_viewpoints_explanations")]
    operations = [migrations.RunPython(rebalance_options, migrations.RunPython.noop)]
