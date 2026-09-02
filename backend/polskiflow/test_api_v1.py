from unittest.mock import patch
from datetime import date

from django.test import TestCase, override_settings

from polskiflow.auth import SupabaseUser
from polskiflow.learning.models import Course, Lesson, Topic
from polskiflow.progress_store import DashboardProgress


class PublicCatalogApiV1Tests(TestCase):
    def setUp(self):
        Course.objects.all().delete()
        first_course = Course.objects.create(
            id="api-a1", title="A1", description="Start", level="A1", position=2
        )
        later_course = Course.objects.create(
            id="api-b1", title="B1", description="Dalej", level="B1", position=8
        )
        first_topic = Topic.objects.create(
            id="api-a1-topic",
            course=first_course,
            title="Pierwszy temat",
            description="Opis",
            emoji="👋",
            position=3,
        )
        later_topic = Topic.objects.create(
            id="api-b1-topic",
            course=later_course,
            title="Drugi temat",
            position=1,
        )
        Lesson.objects.create(
            id="api-a1-second",
            topic=first_topic,
            title="Druga lekcja",
            plan_title="Druga",
            subtitle="A1",
            description="Opis lekcji",
            kind="grammar",
            minutes=12,
            position=4,
        )
        Lesson.objects.create(
            id="api-a1-first",
            topic=first_topic,
            title="Pierwsza lekcja",
            plan_title="Pierwsza",
            subtitle="A1",
            description="Opis lekcji",
            kind="words",
            minutes=7,
            position=1,
        )
        Lesson.objects.create(
            id="api-b1-lesson",
            topic=later_topic,
            title="Lekcja B1",
            plan_title="B1",
            subtitle="B1",
            description="Opis lekcji",
            position=1,
        )

    def test_catalog_is_public_versioned_and_deterministically_ordered(self):
        response = self.client.get("/api/v1/catalog/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertIn("public", response["Cache-Control"])
        payload = response.json()
        self.assertEqual(payload["api_version"], "v1")
        self.assertEqual(payload["meta"]["contract_version"], "1.0.0")
        self.assertEqual(payload["meta"]["levels"], ["A1", "A2", "B1", "B2", "C1", "C2"])
        self.assertEqual(
            [course["id"] for course in payload["data"]["courses"]],
            ["api-a1", "api-b1"],
        )
        lessons = payload["data"]["courses"][0]["topics"][0]["lessons"]
        self.assertEqual(
            [lesson["id"] for lesson in lessons],
            ["api-a1-first", "api-a1-second"],
        )

    def test_catalog_excludes_inactive_content_and_private_or_answer_fields(self):
        hidden_course = Course.objects.create(
            id="api-hidden", title="Hidden", level="C2", is_active=False
        )
        hidden_topic = Topic.objects.create(
            id="api-hidden-topic", course=hidden_course, title="Hidden"
        )
        Lesson.objects.create(
            id="api-hidden-lesson",
            topic=hidden_topic,
            title="Hidden",
            plan_title="Hidden",
            subtitle="C2",
            description="Hidden",
        )

        payload = self.client.get("/api/v1/catalog/").json()
        serialized = str(payload)

        self.assertNotIn("api-hidden", serialized)
        self.assertNotIn("profile", serialized.lower())
        self.assertNotIn("progress", serialized.lower())
        self.assertNotIn("personal_words", serialized.lower())
        lesson = payload["data"]["courses"][0]["topics"][0]["lessons"][0]
        self.assertEqual(
            set(lesson),
            {"id", "title", "description", "kind", "minutes", "emoji", "position"},
        )
        self.assertNotIn("theory_sections", lesson)
        self.assertNotIn("questions", lesson)

    def test_catalog_supports_head_and_rejects_mutation_methods(self):
        head = self.client.head("/api/v1/catalog/")
        post = self.client.post("/api/v1/catalog/", data={})

        self.assertEqual(head.status_code, 200)
        self.assertEqual(head.content, b"")
        self.assertEqual(head["Content-Type"], "application/json")
        self.assertEqual(post.status_code, 405)
        self.assertEqual(post["Allow"], "GET, HEAD")


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class LearnerApiV1Tests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer learner-token"}

    def _user_patch(self):
        return patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser(id="user-123", email="ada@example.com"),
        )

    def test_learner_contracts_require_authentication_and_are_read_only(self):
        self.assertEqual(self.client.get("/api/v1/me/progress/").status_code, 401)
        self.assertEqual(self.client.get("/api/v1/me/sm2/").status_code, 401)

        with self._user_patch(), patch(
            "polskiflow.api_views.load_dashboard_progress",
            return_value=DashboardProgress("Ada", "B1", 0, frozenset(), True),
        ):
            response = self.client.post("/api/v1/me/progress/", **self.authorization)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response["Allow"], "GET, HEAD")

    def test_progress_contract_is_private_owner_scoped_and_stable(self):
        progress = DashboardProgress(
            display_name="Ada",
            level="B1",
            streak_days=5,
            completed_lesson_ids=frozenset({"lesson-today"}),
            available=True,
            all_completed_lesson_ids=frozenset({"lesson-z", "lesson-a"}),
            active_days=9,
            weekly_active_days=4,
            weekly_completed_count=7,
            previous_week_active_days=3,
            previous_week_completed_count=5,
            monthly_active_days=9,
            monthly_completed_count=18,
            daily_goal_lessons=3,
        )
        with self._user_patch(), patch(
            "polskiflow.api_views.load_dashboard_progress", return_value=progress
        ) as load:
            response = self.client.get("/api/v1/me/progress/", **self.authorization)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Cache-Control"], "private, no-store")
        self.assertIn("Authorization", response["Vary"])
        load.assert_called_once_with("learner-token", "user-123", "ada@example.com")
        payload = response.json()
        self.assertEqual(payload["meta"]["contract"], "learner-progress")
        self.assertEqual(payload["meta"]["contract_version"], "1.0.0")
        self.assertEqual(payload["data"]["completed_lesson_ids"], ["lesson-a", "lesson-z"])
        self.assertEqual(payload["data"]["periods"]["week"]["completed_lessons"], 7)
        self.assertNotIn("user-123", str(payload))
        self.assertNotIn("learner-token", str(payload))

    def test_sm2_contract_marks_due_items_and_does_not_cross_user_boundary(self):
        words = [
            {
                "id": "word-later",
                "word": "później",
                "translation": "позже",
                "context": "Zrobię to później.",
                "source_text_id": "tekst-1",
                "ease_factor": 2.6,
                "interval_days": 6,
                "repetitions": 2,
                "next_review_date": "2026-09-04",
                "last_reviewed_at": "2026-09-01T10:00:00Z",
            },
            {
                "id": "word-due",
                "word": "dzisiaj",
                "translation": "сегодня",
                "context": "Uczę się dzisiaj.",
                "source_text_id": "tekst-2",
                "ease_factor": 2.5,
                "interval_days": 1,
                "repetitions": 1,
                "next_review_date": "2026-09-02",
                "last_reviewed_at": None,
            },
        ]
        with self._user_patch(), patch(
            "polskiflow.api_views.load_personal_words", return_value=words
        ) as load, patch(
            "polskiflow.api_views.timezone.localdate", return_value=date(2026, 9, 2)
        ):
            response = self.client.get("/api/v1/me/sm2/", **self.authorization)

        self.assertEqual(response.status_code, 200)
        load.assert_called_once_with("learner-token", "user-123")
        data = response.json()["data"]
        self.assertEqual(data["as_of"], "2026-09-02")
        self.assertEqual(data["due_count"], 1)
        self.assertEqual([item["id"] for item in data["reviews"]], ["word-due", "word-later"])
        self.assertTrue(data["reviews"][0]["due"])
        self.assertFalse(data["reviews"][1]["due"])

    def test_upstream_failure_is_explicit_and_not_cached(self):
        with self._user_patch(), patch(
            "polskiflow.api_views.load_personal_words", return_value=None
        ):
            response = self.client.get("/api/v1/me/sm2/", **self.authorization)

        self.assertEqual(response.status_code, 503)
        self.assertEqual(response["Cache-Control"], "private, no-store")
        self.assertEqual(response.json()["error"]["code"], "upstream_unavailable")
