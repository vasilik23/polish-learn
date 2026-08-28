from django.test import SimpleTestCase

from polskiflow.domain.password_policy import password_error


class PasswordPolicyTests(SimpleTestCase):
    def test_accepts_long_mixed_password(self):
        self.assertIsNone(password_error("Bezpieczne2026"))

    def test_rejects_short_password(self):
        self.assertIn("10 символов", password_error("Aa123456"))

    def test_rejects_common_password_before_character_rules(self):
        self.assertIn("распространён", password_error("Password123"))

    def test_requires_lowercase_uppercase_and_digit(self):
        self.assertIn("строчную", password_error("POLSKA2026!"))
        self.assertIn("заглавную", password_error("polska2026!"))
        self.assertIn("цифру", password_error("Bezpieczne!"))
