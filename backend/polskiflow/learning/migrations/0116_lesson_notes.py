from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("learning", "0115_learner_mistakes")]
    operations = [
        migrations.CreateModel(
            name="LessonNote",
            fields=[
                ("user_id", models.UUIDField()),
                ("lesson_id", models.TextField()),
                ("body", models.TextField()),
                ("updated_at", models.DateTimeField()),
                ("pk", models.CompositePrimaryKey("user_id", "lesson_id", primary_key=True, serialize=False)),
            ],
            options={"db_table": "lesson_notes", "managed": False},
        )
    ]
