import json

from django.test import SimpleTestCase
from django.urls import reverse


class PwaPrototypeTests(SimpleTestCase):
    def test_manifest_describes_root_scoped_standalone_app(self):
        response = self.client.get(reverse("web-app-manifest"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/manifest+json")
        manifest = json.loads(response.content)
        self.assertEqual(manifest["id"], "/")
        self.assertEqual(manifest["start_url"], "/")
        self.assertEqual(manifest["scope"], "/")
        self.assertEqual(manifest["display"], "standalone")
        self.assertEqual({icon["purpose"] for icon in manifest["icons"]}, {"any", "maskable"})
        self.assertTrue(all(icon["type"] == "image/svg+xml" for icon in manifest["icons"]))

    def test_service_worker_is_root_scoped_and_not_http_cached(self):
        response = self.client.get(reverse("service-worker"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response["Content-Type"].startswith("text/javascript"))
        self.assertEqual(response["Service-Worker-Allowed"], "/")
        self.assertEqual(response["Cache-Control"], "no-cache, no-store, must-revalidate")

    def test_service_worker_only_precaches_public_shell_assets(self):
        source = self.client.get(reverse("service-worker")).content.decode()

        self.assertIn('const OFFLINE_URL = "/offline/?shell=v1"', source)
        self.assertIn('const PUBLIC_ASSETS = ["/static/polskiflow/favicon.svg?shell=v1"]', source)
        self.assertIn('if (request.method !== "GET") return', source)
        self.assertIn('if (request.mode === "navigate")', source)
        self.assertIn("fetch(request).catch(() => caches.match(OFFLINE_URL))", source)
        self.assertNotIn("cache.put(request", source)
        self.assertNotIn('"/api/', source)
        self.assertNotIn('"/login/', source)

    def test_service_worker_removes_old_caches(self):
        source = self.client.get(reverse("service-worker")).content.decode()

        self.assertIn("key !== CACHE_NAME", source)
        self.assertIn("caches.delete(key)", source)

    def test_offline_shell_is_public_and_honest_about_sync_boundary(self):
        response = self.client.get(reverse("offline-shell"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Сейчас нет подключения")
        self.assertContains(response, "не сохраняет ответы и прогресс офлайн")
        self.assertNotContains(response, "request.supabase_user")
