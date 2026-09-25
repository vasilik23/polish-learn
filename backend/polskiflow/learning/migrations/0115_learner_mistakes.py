from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("learning", "0114_lesson_bookmarks")]
    operations = [
        migrations.CreateModel(
            name="LearnerMistake",
            fields=[
                ("user_id", models.UUIDField()),
                ("lesson_id", models.TextField()),
                ("question_position", models.PositiveSmallIntegerField()),
                ("last_wrong_at", models.DateTimeField()),
                ("pk", models.CompositePrimaryKey("user_id", "lesson_id", "question_position", primary_key=True, serialize=False)),
            ],
            options={"db_table": "learner_mistakes", "managed": False},
        )
    ]
