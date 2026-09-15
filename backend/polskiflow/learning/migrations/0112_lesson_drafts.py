from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("learning", "0111_user_feedback")]
    operations = [
        migrations.CreateModel(
            name="LessonDraft",
            fields=[
                ("pk", models.CompositePrimaryKey("user_id", "lesson_id", blank=True, editable=False, primary_key=True, serialize=False)),
                ("user_id", models.UUIDField()),
                ("lesson_id", models.TextField()),
                ("lesson_kind", models.CharField(max_length=16)),
                ("step_index", models.PositiveSmallIntegerField(default=0)),
                ("score", models.PositiveSmallIntegerField(default=0)),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "lesson_drafts", "managed": False},
        ),
    ]
