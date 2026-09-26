import json
from pathlib import Path
from unittest.mock import MagicMock, patch
from django.test import TestCase, override_settings
from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.collection_store import load_collections
from polskiflow.learning.models import Course, Lesson, ReadingText, Topic

@override_settings(SUPABASE_URL="https://project.supabase.co", SUPABASE_ANON_KEY="anon", SUPABASE_AUTH_TIMEOUT=2)
class CollectionStoreTests(TestCase):
    @patch("polskiflow.collection_store.urlopen")
    def test_loads_both_owner_scoped_tables(self, urlopen):
        responses = []
        for payload in ([{"id":"c1","name":"Работа"}], [{"id":"i1","collection_id":"c1","content_type":"lesson","content_id":"l1"}]):
            response = MagicMock(); response.__enter__.return_value=response; response.read.return_value=json.dumps(payload).encode(); responses.append(response)
        urlopen.side_effect = responses
        collections, items = load_collections("token", "owner")
        self.assertEqual(collections[0]["name"], "Работа"); self.assertEqual(items[0]["content_id"], "l1")
        self.assertTrue(all("user_id=eq.owner" in call.args[0].full_url for call in urlopen.call_args_list))

    def test_schema_blocks_cross_owner_links_and_anon(self):
        sql=(Path(__file__).parents[2]/"supabase/migrations/20260926100331_learning_collections.sql").read_text()
        self.assertIn("foreign key (collection_id, user_id)", sql)
        self.assertIn("revoke all on table public.learning_collections, public.learning_collection_items from anon", sql)
        self.assertGreaterEqual(sql.count("(select auth.uid()) = user_id"), 7)

class CollectionViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        c=Course.objects.create(id="col-a1",title="A1",level="A1"); t=Topic.objects.create(id="col-topic",course=c,title="Работа")
        Lesson.objects.create(id="col-lesson",topic=t,kind="words",title="Słowa",plan_title="Рабочая лексика",subtitle="",description="",minutes=5,emoji="💼")
        ReadingText.objects.create(id="col-reading",topic=t,title="Rozmowa",description="",level="A1",paragraphs=["Tekst"],glossary={})
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE]="access"; p=patch("polskiflow.auth.authenticate_access_token",return_value=SupabaseUser("11111111-1111-4111-8111-111111111111","a@example.com")); p.start(); self.addCleanup(p.stop)
    @patch("polskiflow.collection_views.load_reading_bookmarks",return_value={"col-reading"})
    @patch("polskiflow.collection_views.load_lesson_bookmarks",return_value={"col-lesson"})
    @patch("polskiflow.collection_views.load_collections",return_value=([{"id":"11111111-1111-4111-8111-111111111112","name":"Для работы"}],[{"id":"11111111-1111-4111-8111-111111111113","collection_id":"11111111-1111-4111-8111-111111111112","content_type":"lesson","content_id":"col-lesson"}]))
    def test_page_groups_items_and_saved_choices(self,*_):
        r=self.client.get("/collections/"); self.assertContains(r,"Для работы"); self.assertContains(r,"Рабочая лексика"); self.assertContains(r,"Rozmowa")
    @patch("polskiflow.collection_views.create_collection",return_value=True)
    def test_create_validates_and_uses_owner(self,create):
        self.assertEqual(self.client.post("/collections/create/",{"name":""}).status_code,400)
        self.assertEqual(self.client.post("/collections/create/",{"name":"  Экзамен  "}).status_code,302)
        create.assert_called_once_with("access","11111111-1111-4111-8111-111111111111","Экзамен")
