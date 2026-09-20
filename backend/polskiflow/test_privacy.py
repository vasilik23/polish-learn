from django.test import SimpleTestCase


class PrivacyPageTests(SimpleTestCase):
    def test_public_page_has_factual_inventory_controls_and_limits(self):
        response = self.client.get("/privacy/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Приватность и данные")
        self.assertContains(response, "Supabase")
        self.assertContains(response, "Vercel")
        self.assertContains(response, "Черновики письма")
        self.assertContains(response, "Автоматическое удаление Auth-аккаунта ещё не запущено")
        self.assertContains(response, "юридическое имя контролёра")
        self.assertContains(response, "https://commission.europa.eu/")
        self.assertContains(response, "https://uodo.gov.pl/")
        self.assertEqual(response["Cache-Control"], "public, max-age=300")

    def test_public_page_does_not_expose_authenticated_export_action(self):
        response = self.client.get("/privacy/")
        self.assertNotContains(response, "Скачать мои данные")
        self.assertContains(response, 'href="/login/"')
