from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("learning", "0053_c1_topics_five_eight_content")]
    operations = [
        migrations.AddField(
            model_name="profile",
            name="daily_goal_lessons",
            field=models.PositiveSmallIntegerField(default=4),
        )
    ]
