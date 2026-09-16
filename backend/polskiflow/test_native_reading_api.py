import json
import uuid
from unittest.mock import patch

from django.test import TestCase, override_settings

from polskiflow.auth import SupabaseUser
from polskiflow.learning.models import Course, ReadingText, Topic


@override_settings(SUPABASE_URL="https://example.supabase.co", SUPABASE_ANON_KEY="anon")
class NativeReadingApiTests(TestCase):
    authorization = {"HTTP_AUTHORIZATION": "Bearer owner-token"}

    @classmethod
    def setUpTestData(cls):
        course = Course.objects.create(id="native-reading-course", title="A2", level="A2")
        topic = Topic.objects.create(id="native-reading-topic", course=course, title="Podróże")
        ReadingText.objects.create(
            id="native-reading-story", topic=topic, title="Wyjątkowa podróż", description="Unikalny opis API",
            level="A2", minutes=7, emoji="🚆", paragraphs=["Ala jedzie pociągiem.", "Podróż jest spokojna."],
            glossary={
                "jedzie": {"lemma": "jechać", "translation": "ехать", "part_of_speech": "глагол"},
                "spokojna": "спокойная",
            },
            source_metadata={
                "origin": "original", "author": "PolskiFlow", "license": "original",
                "verified_at": "2026-09-16", "comprehension_lesson_id": "native-reading-check",
                "internal_note": "must not leak",
            },
            position=999,
        )

    def _auth(self):
        return patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser(id="owner-1", email="owner@example.com"))

    def test_library_requires_bearer_and_is_owner_scoped(self):
        self.client.cookies["polskiflow_access_token"] = "cookie-token"
        with self._auth(), patch("polskiflow.api_views.load_reading_bookmarks") as load:
            rejected = self.client.get("/api/v1/reading/")
        self.assertEqual(rejected.status_code, 401)
        load.assert_not_called()

        with self._auth(), patch("polskiflow.api_views.load_reading_bookmarks", return_value={"native-reading-story"}) as load:
            response = self.client.get("/api/v1/reading/?level=A2&q=Wyjątkowa", **self.authorization)
        self.assertEqual(response.status_code, 200)
        texts = response.json()["data"]["texts"]
        self.assertEqual([item["id"] for item in texts], ["native-reading-story"])
        self.assertTrue(texts[0]["saved"])
        self.assertEqual(texts[0]["api_path"], "/api/v1/reading/native-reading-story/")
        load.assert_called_once_with("owner-token", "owner-1")

    def test_detail_returns_paragraphs_lemma_glossary_and_safe_source(self):
        with self._auth(), patch("polskiflow.api_views.load_reading_bookmarks", return_value={"native-reading-story"}), patch(
            "polskiflow.api_views.task", return_value={"id": "native-reading-check"}
        ):
            response = self.client.get("/api/v1/reading/native-reading-story/", **self.authorization)
        self.assertEqual(response.status_code, 200)
        text = response.json()["data"]["text"]
        self.assertEqual(len(text["paragraphs"]), 2)
        self.assertEqual(text["glossary"][0]["lemma"], "jechać")
        self.assertEqual(text["glossary"][1]["lemma"], "spokojna")
        self.assertEqual(text["comprehension_api_path"], "/api/v1/lessons/native-reading-check/")
        self.assertNotIn("internal_note", text["source"])
        self.assertNotIn("owner-1", str(text))

    def test_filters_and_pagination_are_strict(self):
        for query in ("level=Z9", "page=0", "page=101", f"q={'x' * 121}"):
            with self.subTest(query=query), self._auth():
                response = self.client.get(f"/api/v1/reading/?{query}", **self.authorization)
            self.assertEqual(response.status_code, 400)

    def test_missing_text_and_bookmark_failure_are_explicit(self):
        with self._auth():
            missing = self.client.get("/api/v1/reading/not-found/", **self.authorization)
        with self._auth(), patch("polskiflow.api_views.load_reading_bookmarks", return_value=None):
            unavailable = self.client.get("/api/v1/reading/native-reading-story/", **self.authorization)
        self.assertEqual(missing.status_code, 404)
        self.assertEqual(unavailable.status_code, 503)

    def test_library_supports_head_and_rejects_mutation(self):
        with self._auth(), patch("polskiflow.api_views.load_reading_bookmarks", return_value=set()):
            head = self.client.head("/api/v1/reading/?q=Wyjątkowa", **self.authorization)
            post = self.client.post("/api/v1/reading/", **self.authorization)
        self.assertEqual(head.status_code, 200)
        self.assertEqual(post.status_code, 405)

    def test_save_glossary_word_uses_server_canonical_lemma_translation_and_context(self):
        with self._auth(), patch("polskiflow.api_views.save_personal_word", return_value=True) as save:
            response = self.client.post(
                "/api/v1/reading/native-reading-story/dictionary/",
                data=json.dumps({"surface": "JEDZIE"}), content_type="application/json",
                **self.authorization,
            )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["word"], "jechać")
        save.assert_called_once_with(
            "owner-token", "owner-1", "jechać", "ехать", "Ala jedzie pociągiem.", "native-reading-story"
        )

    def test_save_word_rejects_client_translation_unknown_surface_and_upstream_failure(self):
        cases = (
            ({"surface": "jedzie", "translation": "fake"}, 400),
            ({"surface": "nie-ma"}, 404),
            ({"surface": ""}, 400),
        )
        for payload, status in cases:
            with self.subTest(payload=payload), self._auth(), patch("polskiflow.api_views.save_personal_word") as save:
                response = self.client.post(
                    "/api/v1/reading/native-reading-story/dictionary/", data=json.dumps(payload),
                    content_type="application/json", **self.authorization,
                )
            self.assertEqual(response.status_code, status)
            save.assert_not_called()
        with self._auth(), patch("polskiflow.api_views.save_personal_word", return_value=False):
            unavailable = self.client.post(
                "/api/v1/reading/native-reading-story/dictionary/", data=json.dumps({"surface": "jedzie"}),
                content_type="application/json", **self.authorization,
            )
        self.assertEqual(unavailable.status_code, 503)

    def test_delete_dictionary_word_is_bearer_only_and_owner_scoped(self):
        word_id = uuid.UUID("22222222-2222-4222-8222-222222222222")
        self.client.cookies["polskiflow_access_token"] = "cookie-token"
        with self._auth(), patch("polskiflow.api_views.delete_personal_word") as delete:
            rejected = self.client.delete(f"/api/v1/me/dictionary/{word_id}/")
        self.assertEqual(rejected.status_code, 401)
        delete.assert_not_called()
        with self._auth(), patch("polskiflow.api_views.delete_personal_word", return_value=True) as delete:
            response = self.client.delete(f"/api/v1/me/dictionary/{word_id}/", **self.authorization)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["data"]["deleted"])
        delete.assert_called_once_with("owner-token", "owner-1", str(word_id))
