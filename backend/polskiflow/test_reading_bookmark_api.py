from unittest.mock import patch
from django.test import TestCase, override_settings
from polskiflow.auth import SupabaseUser
from polskiflow.learning.models import Course, ReadingText, Topic

@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class ReadingBookmarkApiTests(TestCase):
    def setUp(self):
        course = Course.objects.create(id="bookmark-api", title="A1", level="A1")
        topic = Topic.objects.create(id="bookmark-api-topic", course=course, title="Reading")
        ReadingText.objects.create(id="bookmark-story", topic=topic, title="Story", description="", paragraphs=["Tekst."], glossary={})
        auth = patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser("user-1", "a@example.com"))
        auth.start(); self.addCleanup(auth.stop)
        self.headers = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    @patch("polskiflow.api_views.load_reading_bookmarks", return_value={"z", "a"})
    def test_list_is_private_owner_scoped_and_sorted(self, load):
        response = self.client.get("/api/v1/me/reading-bookmarks/", **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["reading_text_ids"], ["a", "z"])
        self.assertEqual(response["Cache-Control"], "private, no-store")
        load.assert_called_once_with("owner-token", "user-1")

    @patch("polskiflow.api_views.set_reading_bookmark", return_value=True)
    def test_put_and_delete_are_bearer_only_and_owner_scoped(self, save):
        put = self.client.put("/api/v1/me/reading-bookmarks/bookmark-story/", **self.headers)
        delete = self.client.delete("/api/v1/me/reading-bookmarks/bookmark-story/", **self.headers)
        self.assertEqual((put.status_code, delete.status_code), (200, 200))
        self.assertTrue(put.json()["data"]["saved"])
        self.assertFalse(delete.json()["data"]["saved"])
        self.assertEqual(save.call_args_list[0].args, ("owner-token", "user-1", "bookmark-story", True))

    def test_mutation_rejects_cookie_only_and_unknown_text(self):
        self.client.cookies["polskiflow_access_token"] = "owner-token"
        self.assertEqual(self.client.put("/api/v1/me/reading-bookmarks/bookmark-story/").status_code, 401)
        self.assertEqual(self.client.put("/api/v1/me/reading-bookmarks/missing/", **self.headers).status_code, 404)
