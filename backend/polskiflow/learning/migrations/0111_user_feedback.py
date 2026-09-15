import uuid
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("learning", "0110_reading_bookmarks")]
    operations = [migrations.CreateModel(name="UserFeedback", fields=[
        ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
        ("user_id", models.UUIDField()), ("category", models.CharField(max_length=24)),
        ("message", models.TextField()), ("page_url", models.CharField(blank=True, max_length=300)),
        ("status", models.CharField(default="new", max_length=16)), ("created_at", models.DateTimeField(auto_now_add=True)),
    ], options={"db_table": "user_feedback", "managed": False})]
