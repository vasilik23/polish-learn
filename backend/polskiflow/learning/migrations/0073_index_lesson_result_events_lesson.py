from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("learning", "0072_improve_c1_public_discussion_editorial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="lessonresultevent",
            index=models.Index(
                fields=["lesson_id"], name="result_events_lesson_idx"
            ),
        ),
    ]
