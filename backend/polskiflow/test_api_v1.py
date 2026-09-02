from django.test import TestCase

from polskiflow.learning.models import Course, Lesson, Topic


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
