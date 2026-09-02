import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("learning", "0070_improve_c1_literary_language_editorial")]

    operations = [
        migrations.CreateModel(
            name="LessonResultEvent",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("user_id", models.UUIDField()),
                ("event_id", models.UUIDField()),
                ("payload_hash", models.CharField(max_length=64)),
                ("lesson_id", models.CharField(max_length=32)),
                ("plan_date", models.DateField()),
                ("completed_at", models.DateTimeField()),
                ("cards_total", models.PositiveIntegerField()),
                ("cards_known", models.PositiveIntegerField()),
                ("contract_version", models.CharField(max_length=16)),
                ("client_instance_id", models.CharField(blank=True, max_length=128, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "lesson_result_events", "managed": False},
        ),
    ]
