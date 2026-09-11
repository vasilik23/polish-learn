from pathlib import Path

from django.test import SimpleTestCase


SOURCE = (Path(__file__).parent / "learning/static/polskiflow/result-queue.js").read_text()
SYNC_SOURCE = (Path(__file__).parent / "learning/static/polskiflow/lesson-result-sync.js").read_text()


class OfflineResultQueueContractTests(SimpleTestCase):
    def test_queue_is_namespaced_and_deduplicated_by_event(self):
        self.assertIn('return `user:${userId}`', SOURCE)
        self.assertIn('key: `${owner}:${payload.event_id}`', SOURCE)
        self.assertIn('throw new Error("Idempotency conflict")', SOURCE)
        self.assertIn("store.put(item)", SOURCE)

    def test_sensitive_fields_cannot_enter_persisted_payload(self):
        self.assertIn('"access_token", "refresh_token", "token", "email", "user_id"', SOURCE)
        self.assertNotIn("localStorage", SOURCE)
        self.assertNotIn("sessionStorage", SOURCE)

    def test_bearer_exists_only_at_flush_boundary(self):
        self.assertIn("async function flush(userId, accessToken)", SOURCE)
        self.assertIn('"Authorization": `Bearer ${accessToken}`', SOURCE)

    def test_browser_session_flush_uses_csrf_without_exposing_bearer(self):
        session_source = SOURCE[SOURCE.index("async function flushSession"):]
        self.assertIn('"/api/v1/me/lesson-results/session/"', session_source)
        self.assertIn('"X-CSRFToken": csrfToken', session_source)
        self.assertIn('credentials: "same-origin"', session_source)
        self.assertNotIn("Authorization", session_source)

    def test_retries_and_permanent_failures_have_bounded_visible_states(self):
        self.assertIn("const MAX_ATTEMPTS = 5", SOURCE)
        self.assertIn('item.state = "needs-attention"', SOURCE)
        self.assertIn('state: "retry-paused"', SOURCE)
        self.assertIn('state: "auth-required"', SOURCE)

    def test_only_matching_confirmations_are_removed(self):
        self.assertIn("response.status === 200 || response.status === 201", SOURCE)
        self.assertIn("body?.data?.event_id === item.payload.event_id", SOURCE)
        self.assertIn("await remove(item.key)", SOURCE)

    def test_lesson_pilot_uses_cookie_session_and_has_visible_retry(self):
        self.assertIn("queue.flushSession(namespace, csrfToken)", SYNC_SOURCE)
        self.assertIn('retry.addEventListener("click", flush)', SYNC_SOURCE)
        self.assertIn('window.addEventListener("online", flush)', SYNC_SOURCE)
        self.assertNotIn("Authorization", SYNC_SOURCE)
        self.assertNotIn("user_id", SYNC_SOURCE)
        self.assertNotIn("email", SYNC_SOURCE)
