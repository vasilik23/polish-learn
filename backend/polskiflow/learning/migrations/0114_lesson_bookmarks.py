import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("learning", "0113_reminder_preferences")]
    operations = [
        migrations.CreateModel(
            name="LessonBookmark",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("user_id", models.UUIDField()),
                ("lesson_id", models.CharField(max_length=32)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "lesson_bookmarks", "managed": False},
        )
    ]
