import json
from pathlib import Path
from unittest.mock import MagicMock, patch

from django.test import TestCase, override_settings

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.mistake_store import load_mistakes, set_mistake


class MistakeStoreTests(TestCase):
    def test_supabase_migration_enforces_owner_rls_and_explicit_grants(self):
        sql = (Path(__file__).parents[2] / "supabase/migrations/20260925072443_learner_mistakes.sql").read_text()
        self.assertIn("enable row level security", sql)
        self.assertIn("revoke all on table public.learner_mistakes from anon", sql)
        self.assertIn("with check ((select auth.uid()) = user_id)", sql)
        self.assertIn("on delete cascade", sql)

    @override_settings(SUPABASE_URL="https://project.supabase.co", SUPABASE_ANON_KEY="public", SUPABASE_AUTH_TIMEOUT=2)
    @patch("polskiflow.mistake_store.urlopen")
    def test_load_is_owner_scoped(self, urlopen):
        response = MagicMock()
        response.read.return_value = json.dumps([{"lesson_id": "quiz", "question_position": 1}]).encode()
        urlopen.return_value.__enter__.return_value = response
        self.assertEqual(load_mistakes("token", "owner")[0]["lesson_id"], "quiz")
        request = urlopen.call_args.args[0]
        self.assertIn("user_id=eq.owner", request.full_url)
        self.assertEqual(request.headers["Authorization"], "Bearer token")

    @override_settings(SUPABASE_URL="https://project.supabase.co", SUPABASE_ANON_KEY="public", SUPABASE_AUTH_TIMEOUT=2)
    @patch("polskiflow.mistake_store.urlopen")
    def test_wrong_upserts_and_correct_deletes(self, urlopen):
        urlopen.return_value.__enter__.return_value.status = 204
        self.assertTrue(set_mistake("token", "owner", "quiz", 2, True))
        insert = urlopen.call_args.args[0]
        self.assertEqual(insert.method, "POST")
        payload = json.loads(insert.data)
        self.assertEqual({key: payload[key] for key in ("user_id", "lesson_id", "question_position")}, {"user_id": "owner", "lesson_id": "quiz", "question_position": 2})
        self.assertIn("last_wrong_at", payload)
        self.assertTrue(set_mistake("token", "owner", "quiz", 2, False))
        self.assertEqual(urlopen.call_args.args[0].method, "DELETE")


class MistakeViewTests(TestCase):
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        patcher = patch("polskiflow.auth.authenticate_access_token", return_value=SupabaseUser("user-1", "a@example.com"))
        patcher.start()
        self.addCleanup(patcher.stop)

    @patch("polskiflow.mistake_views.tasks", return_value=[{"id": "quiz", "plan_title": "Мини-тест", "emoji": "✓", "level": "A1"}])
    @patch("polskiflow.mistake_views.Question.objects")
    @patch("polskiflow.mistake_views.load_mistakes", return_value=[])
    def test_empty_notebook_is_honest(self, _load, questions, _tasks):
        questions.filter.return_value.only.return_value = []
        response = self.client.get("/mistakes/")
        self.assertContains(response, "Ошибок для повторения пока нет")

    def test_requires_authentication(self):
        self.client.cookies.clear()
        self.assertEqual(self.client.get("/mistakes/").status_code, 302)
