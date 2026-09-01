from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.domain.diagnostic import score_diagnostic


class DiagnosticScoringTests(TestCase):
    def test_recommendation_is_capped_one_step_above_weakest_mode(self):
        result = score_diagnostic(
            {
                "reception": "5",
                "production": "0",
                "interaction": "5",
                "mediation": "5",
            }
        )

        self.assertEqual(result.level, "A2")
        self.assertEqual(result.focus_modes, ("Продукция", "Восприятие"))
        self.assertIn("самый слабый режим: A1", result.calculation)

    def test_balanced_answers_use_average_rounded_down(self):
        result = score_diagnostic(
            {
                "reception": "3",
                "production": "2",
                "interaction": "3",
                "mediation": "2",
            }
        )

        self.assertEqual(result.level, "B1")
        self.assertEqual(result.focus_modes, ("Продукция", "Медиация"))

    def test_all_four_valid_answers_are_required(self):
        with self.assertRaisesMessage(ValueError, "все четыре режима"):
            score_diagnostic(
                {"reception": "1", "production": "1", "interaction": "1"}
            )

    def test_unknown_level_is_rejected(self):
        with self.assertRaisesMessage(ValueError, "предложенных уровней"):
            score_diagnostic(
                {
                    "reception": "6",
                    "production": "1",
                    "interaction": "1",
                    "mediation": "1",
                }
            )


class DiagnosticViewTests(TestCase):
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        self.auth_patch = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser("user-123", "learner@example.com"),
        )
        self.auth_patch.start()
        self.addCleanup(self.auth_patch.stop)

    def test_page_is_discoverable_from_course_and_describes_limitations(self):
        course = self.client.get("/course/")
        page = self.client.get("/diagnostic/")

        self.assertContains(course, 'href="/diagnostic/"')
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, "Предварительная диагностика")
        self.assertContains(page, "не тест уровня, экзамен или сертификат")
        self.assertContains(page, 'name="reception"')
        self.assertContains(page, 'name="production"')
        self.assertContains(page, 'name="interaction"')
        self.assertContains(page, 'name="mediation"')
        self.assertContains(page, 'name="csrfmiddlewaretoken"')
        self.assertContains(page, "понимаю длинную сложную речь")
        self.assertContains(page, "точно и гибко строю сложное")
        self.assertContains(page, "гибко веду сложное общение")
        self.assertContains(page, "перестраиваю сложную информацию")

    def test_post_returns_transparent_preliminary_recommendation(self):
        response = self.client.post(
            "/diagnostic/",
            {
                "reception": "3",
                "production": "2",
                "interaction": "3",
                "mediation": "2",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Начни с B1")
        self.assertContains(response, "Продукция, Медиация")
        self.assertContains(response, "Среднее с округлением вниз: B1")
        self.assertContains(response, "нигде не сохраняется")
        self.assertContains(response, 'href="/course/?level=B1"')

    def test_incomplete_post_is_rejected_and_preserves_answer(self):
        response = self.client.post(
            "/diagnostic/",
            {"reception": "3", "production": "2", "interaction": "3"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertContains(response, "Нужно оценить все четыре режима", status_code=400)
        self.assertContains(response, '<option value="3" selected>', status_code=400)

    def test_page_requires_authentication(self):
        self.auth_patch.stop()
        self.client.cookies.clear()

        response = self.client.get("/diagnostic/")

        self.assertRedirects(
            response,
            "/login/?next=%2Fdiagnostic%2F",
            fetch_redirect_response=False,
        )
