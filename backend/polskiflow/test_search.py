from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.catalog_search import search_learning_catalog
from polskiflow.learning.models import Course, Lesson, ReadingText, Topic


class GlobalSearchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        course = Course.objects.create(id="search-a2", title="A2", level="A2", position=1)
        topic = Topic.objects.create(
            id="search-travel",
            course=course,
            title="Путешествия по Польше",
            description="Экспедиция, транспорт и гостиница",
            emoji="🧳",
            position=0,
        )
        Lesson.objects.create(
            id="search-tickets",
            topic=topic,
            kind="words",
            title="Bilety i perony",
            plan_title="Билеты и вокзал",
            subtitle="A2",
            description="покупаем билет для экспедиции",
            minutes=8,
            emoji="🚆",
        )
        ReadingText.objects.create(
            id="search-weekend",
            topic=topic,
            title="Weekend w Krakowie",
            description="короткий рассказ об экспедиции",
            level="A2",
            paragraphs=["Tekst"],
            emoji="📖",
        )
        Topic.objects.create(
            id="search-hidden",
            course=course,
            title="Скрытые путешествия",
            is_active=False,
            position=1,
        )

    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        auth = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser("user-1", "a@example.com"),
        )
        auth.start()
        self.addCleanup(auth.stop)

    def test_search_finds_active_topics_lessons_and_readings(self):
        result = search_learning_catalog("экспедици")

        self.assertEqual([item["id"] for item in result["topics"]], ["search-travel"])
        self.assertEqual([item["id"] for item in result["lessons"]], ["search-tickets"])
        self.assertEqual([item["id"] for item in result["readings"]], ["search-weekend"])
        self.assertEqual(result["total"], 3)

    def test_view_renders_grouped_results_and_navigation_entries(self):
        response = self.client.get("/search/?q=экспедици")

        self.assertContains(response, "Путешествия по Польше")
        self.assertContains(response, "Билеты и вокзал")
        self.assertContains(response, "Weekend w Krakowie")
        self.assertContains(response, 'href="/course/?level=A2#topic-search-travel"')
        self.assertContains(response, 'href="/lesson/search-tickets/"')
        self.assertContains(response, 'href="/reading/search-weekend/"')
        self.assertContains(response, 'href="/search/"')
        self.assertContains(response, "Поиск по приложению")

    def test_short_and_unknown_queries_have_honest_states(self):
        short = self.client.get("/search/?q=я")
        missing = self.client.get("/search/?q=несуществующийзапрос")

        self.assertContains(short, "Можно начать с этого")
        self.assertContains(missing, "Ничего не найдено")

    def test_search_requires_authentication(self):
        self.client.cookies.clear()
        self.assertRedirects(
            self.client.get("/search/"),
            "/login/?next=%2Fsearch%2F",
            fetch_redirect_response=False,
        )
