import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("learning", "0109_improve_b2_discussion_intercultural_explanations")]
    operations = [
        migrations.CreateModel(
            name="ReadingBookmark",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("user_id", models.UUIDField()),
                ("reading_text_id", models.CharField(max_length=80)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "reading_bookmarks", "managed": False},
        )
    ]
