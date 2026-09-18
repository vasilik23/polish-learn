from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("learning", "0112_lesson_drafts")]
    operations = [
        migrations.CreateModel(
            name="ReminderPreference",
            fields=[
                ("user_id", models.UUIDField(primary_key=True, serialize=False)),
                ("daily_reminder_enabled", models.BooleanField(default=False)),
                ("reminder_time", models.TimeField(default="19:00")),
                ("timezone", models.CharField(default="Europe/Warsaw", max_length=64)),
                ("updated_at", models.DateTimeField()),
            ],
            options={"db_table": "reminder_preferences", "managed": False},
        ),
    ]
