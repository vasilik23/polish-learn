from django.db import migrations


READING_IDS = ("poranek-anny", "zakupy-na-targu")


def align_comprehension_topics(apps, schema_editor):
    ReadingText = apps.get_model("learning", "ReadingText")
    ReadingText.objects.filter(id__in=READING_IDS).update(topic_id="introductions")


class Migration(migrations.Migration):
    dependencies = [("learning", "0060_complete_c2_curriculum")]
    operations = [
        migrations.RunPython(
            align_comprehension_topics,
            migrations.RunPython.noop,
        )
    ]
