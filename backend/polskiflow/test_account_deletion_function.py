from pathlib import Path

from django.test import SimpleTestCase


class AccountDeletionFunctionContractTests(SimpleTestCase):
    def test_worker_is_jwt_scoped_reauthenticates_and_never_accepts_user_id(self):
        source = (
            Path(__file__).resolve().parents[2]
            / "supabase/functions/delete-account/index.ts"
        ).read_text()
        self.assertIn('request.method !== "POST"', source)
        self.assertIn("auth.getUser(token)", source)
        self.assertIn("auth.signInWithPassword", source)
        self.assertIn("reauthData.user?.id !== user.id", source)
        self.assertIn("auth.admin.deleteUser(user.id, false)", source)
        self.assertIn('fields.length !== 1', source)
        self.assertNotIn("body.user_id", source)
        self.assertNotIn("Access-Control-Allow-Origin", source)
