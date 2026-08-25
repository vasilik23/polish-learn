from django.db import connections


class SupabaseSchemaRouter:
    """Keep Supabase-owned learning DDL out of PostgreSQL migrations."""

    content_models = {
        "course",
        "topic",
        "lesson",
        "flashcard",
        "lessonflashcard",
        "question",
    }

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "learning" and model_name in self.content_models:
            return connections[db].vendor != "postgresql"
        return None
