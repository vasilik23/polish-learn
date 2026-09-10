from collections import Counter

from django.db import migrations


def rebalance_options(apps, schema_editor):
    Question = apps.get_model("learning", "Question")
    for level in ("A1", "A2"):
        questions = list(
            Question.objects.filter(
                lesson__topic__course__level=level, is_active=True
            ).order_by("lesson_id", "position", "id")
        )
        counts = Counter(question.correct for question in questions)
        expected_positions = {0, 1, 2}
        if (
            set(counts).issubset(expected_positions)
            and max((counts[position] for position in expected_positions), default=0)
            - min((counts[position] for position in expected_positions), default=0)
            <= 1
        ):
            continue

        for index, question in enumerate(questions):
            options = list(question.options)
            if len(options) < 2 or question.correct >= len(options):
                continue
            target = index % min(len(options), 3)
            answer = options.pop(question.correct)
            options.insert(target, answer)
            question.options = options
            question.correct = target
            question.save(update_fields=["options", "correct"])


class Migration(migrations.Migration):
    dependencies = [("learning", "0102_resolve_food_grammar_ambiguity")]
    operations = [migrations.RunPython(rebalance_options, migrations.RunPython.noop)]
