import uuid
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("learning", "0116_lesson_notes")]
    operations = [
        migrations.CreateModel(name="LearningCollection", fields=[("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)), ("user_id", models.UUIDField()), ("name", models.CharField(max_length=60)), ("created_at", models.DateTimeField(auto_now_add=True))], options={"db_table": "learning_collections", "managed": False}),
        migrations.CreateModel(name="LearningCollectionItem", fields=[("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)), ("collection_id", models.UUIDField()), ("user_id", models.UUIDField()), ("content_type", models.CharField(max_length=16)), ("content_id", models.TextField()), ("created_at", models.DateTimeField(auto_now_add=True))], options={"db_table": "learning_collection_items", "managed": False}),
    ]
