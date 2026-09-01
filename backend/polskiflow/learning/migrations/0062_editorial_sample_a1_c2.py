from django.db import migrations


def deactivate_empty_legacy_topic(apps, schema_editor):
    Topic = apps.get_model("learning", "Topic")
    Topic.objects.filter(id="first-steps").update(is_active=False)


class Migration(migrations.Migration):
    dependencies = [("learning", "0061_fix_a1_reading_comprehension_topics")]
    operations = [
        migrations.RunPython(
            deactivate_empty_legacy_topic,
            migrations.RunPython.noop,
        )
    ]
