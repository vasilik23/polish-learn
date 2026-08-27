import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("learning", "0015_a1_free_time_content")]

    operations = [
        migrations.AddField(
            model_name="personalword",
            name="ease_factor",
            field=models.FloatField(default=2.5),
        ),
        migrations.AddField(
            model_name="personalword",
            name="interval_days",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="personalword",
            name="last_reviewed_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="personalword",
            name="next_review_date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="personalword",
            name="repetitions",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddConstraint(
            model_name="personalword",
            constraint=models.CheckConstraint(
                condition=models.Q(("ease_factor__gte", 1.3)),
                name="personal_word_minimum_ease",
            ),
        ),
    ]
