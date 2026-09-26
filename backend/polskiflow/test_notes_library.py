import json
from unittest.mock import MagicMock, patch

from django.test import TestCase, override_settings

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.learning.models import Course, Lesson, Topic
from polskiflow.lesson_note_store import load_lesson_notes


@override_settings(SUPABASE_URL="https://project.supabase.co", SUPABASE_ANON_KEY="anon", SUPABASE_AUTH_TIMEOUT=2)
class LessonNoteIndexStoreTests(TestCase):
    @patch("polskiflow.lesson_note_store.urlopen")
    def test_index_is_owner_scoped_ordered_and_bounded(self, urlopen):
        response = MagicMock()
        response.__enter__.return_value = response
        response.read.return_value = json.dumps([{"lesson_id": "grammar", "body": "Przypadki"}]).encode()
        urlopen.return_value = response
        self.assertEqual(load_lesson_notes("token", "owner")[0]["body"], "Przypadki")
        url = urlopen.call_args.args[0].full_url
        self.assertIn("user_id=eq.owner", url)
        self.assertIn("order=updated_at.desc", url)
        self.assertIn("limit=200", url)


class LessonNotesLibraryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        course = Course.objects.create(id="notes-a1", title="A1", level="A1", position=90)
        topic = Topic.objects.create(id="notes-topic", course=course, title="Падежи", position=0)
        Lesson.objects.create(id="notes-lesson", topic=topic, kind="grammar", title="Grammar", plan_title="Родительный падеж", subtitle="A1", description="", minutes=8, emoji="✎")

    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        auth = patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser("11111111-1111-4111-8111-111111111111", "a@example.com"))
        auth.start()
        self.addCleanup(auth.stop)

    @patch("polskiflow.note_views.load_lesson_notes", return_value=[{"lesson_id": "notes-lesson", "body": "После szukać нужен родительный падеж", "updated_at": "2026-09-26T08:00:00Z"}])
    def test_library_maps_notes_to_lessons_and_searches(self, _load):
        response = self.client.get("/notes/")
        self.assertContains(response, "Родительный падеж")
        self.assertContains(response, "После szukać")
        self.assertContains(response, 'href="/lesson/notes-lesson/#lesson-note"')
        self.assertNotContains(self.client.get("/notes/?q=винительный"), "После szukać")
        self.assertContains(self.client.get("/notes/?q=SZUKAĆ"), "После szukać")

    @patch("polskiflow.note_views.save_lesson_note", return_value=True)
    def test_delete_is_csrf_protected_and_owner_scoped(self, save):
        response = self.client.post("/notes/notes-lesson/delete/")
        self.assertRedirects(response, "/notes/?status=deleted", fetch_redirect_response=False)
        save.assert_called_once_with("access", "11111111-1111-4111-8111-111111111111", "notes-lesson", "")

    @patch("polskiflow.note_views.load_lesson_notes", return_value=[])
    def test_empty_state_and_auth_boundary(self, _load):
        self.assertContains(self.client.get("/notes/"), "Заметок пока нет")
        self.client.cookies.clear()
        self.assertEqual(self.client.get("/notes/").status_code, 302)
