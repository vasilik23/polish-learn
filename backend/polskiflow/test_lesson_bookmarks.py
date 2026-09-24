import json
from pathlib import Path
from unittest.mock import MagicMock, patch

from django.test import TestCase, override_settings

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.learning.models import Course, Lesson, ReadingText, Topic
from polskiflow.lesson_bookmark_store import load_lesson_bookmarks, set_lesson_bookmark


@override_settings(SUPABASE_URL="https://project.supabase.co", SUPABASE_ANON_KEY="anon", SUPABASE_AUTH_TIMEOUT=2)
class LessonBookmarkStoreTests(TestCase):
    @patch("polskiflow.lesson_bookmark_store.urlopen")
    def test_loads_only_valid_lesson_ids(self, urlopen):
        response = MagicMock()
        response.__enter__.return_value = response
        response.read.return_value = json.dumps([{"lesson_id": "lesson-a"}, {"other": "ignored"}]).encode()
        urlopen.return_value = response
        self.assertEqual(load_lesson_bookmarks("token", "user-1"), {"lesson-a"})
        request = urlopen.call_args.args[0]
        self.assertIn("user_id=eq.user-1", request.full_url)
        self.assertEqual(request.headers["Authorization"], "Bearer token")

    @patch("polskiflow.lesson_bookmark_store.urlopen")
    def test_insert_and_delete_are_owner_scoped(self, urlopen):
        response = MagicMock(status=201)
        response.__enter__.return_value = response
        urlopen.return_value = response
        self.assertTrue(set_lesson_bookmark("token", "user-1", "lesson-a", True))
        self.assertEqual(json.loads(urlopen.call_args.args[0].data), {"user_id": "user-1", "lesson_id": "lesson-a"})
        response.status = 204
        self.assertTrue(set_lesson_bookmark("token", "user-1", "lesson-a", False))
        request = urlopen.call_args.args[0]
        self.assertEqual(request.method, "DELETE")
        self.assertIn("user_id=eq.user-1", request.full_url)
        self.assertIn("lesson_id=eq.lesson-a", request.full_url)


class SavedLearningViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        course = Course.objects.create(id="saved-a1", title="A1", level="A1", position=20)
        topic = Topic.objects.create(id="saved-topic", course=course, title="Saved topic", position=0)
        Lesson.objects.create(id="saved-lesson", topic=topic, kind="words", title="Słowa", plan_title="Сохранённый урок", subtitle="A1", description="Полезный урок", minutes=7, emoji="★")
        ReadingText.objects.create(id="saved-reading", topic=topic, title="Zapisany tekst", description="Текст в подборке", level="A1", paragraphs=["Tekst"], emoji="▤")

    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        auth = patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser("11111111-1111-4111-8111-111111111111", "a@example.com"))
        auth.start()
        self.addCleanup(auth.stop)

    @patch("polskiflow.saved_views.load_reading_bookmarks", return_value={"saved-reading"})
    @patch("polskiflow.saved_views.load_lesson_bookmarks", return_value={"saved-lesson"})
    def test_saved_page_groups_owner_lessons_and_readings(self, _lessons, _readings):
        response = self.client.get("/saved/")
        self.assertContains(response, "Сохранённый урок")
        self.assertContains(response, "Zapisany tekst")
        self.assertContains(response, 'href="/lesson/saved-lesson/"')
        self.assertContains(response, 'href="/reading/saved-reading/"')

    @patch("polskiflow.saved_views.set_lesson_bookmark", return_value=True)
    def test_toggle_uses_owner_and_rejects_external_redirect(self, save):
        response = self.client.post("/lesson/saved-lesson/bookmark/", {"saved": "1", "next": "https://evil.example/"})
        self.assertRedirects(response, "/lesson/saved-lesson/", fetch_redirect_response=False)
        save.assert_called_once_with("access", "11111111-1111-4111-8111-111111111111", "saved-lesson", True)

    @patch("polskiflow.lesson_views.load_lesson_bookmarks", return_value={"words"})
    @patch("polskiflow.lesson_views.load_lesson_draft", return_value=None)
    def test_lesson_exposes_saved_state(self, _draft, _bookmarks):
        response = self.client.get("/lesson/words/")
        self.assertContains(response, "Убрать урок из сохранённого")

    def test_schema_has_owner_rls_and_no_anon_grant(self):
        sql = (Path(__file__).parents[2] / "supabase/migrations/20260924102513_lesson_bookmarks.sql").read_text()
        self.assertIn("enable row level security", sql)
        self.assertIn("revoke all on table public.lesson_bookmarks from anon", sql)
        self.assertIn("grant select, insert, delete", sql)
        self.assertGreaterEqual(sql.count("(select auth.uid()) = user_id"), 3)

    def test_saved_page_requires_authentication(self):
        self.client.cookies.clear()
        self.assertRedirects(self.client.get("/saved/"), "/login/?next=%2Fsaved%2F", fetch_redirect_response=False)
