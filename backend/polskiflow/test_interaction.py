from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.domain.interaction_scenarios import (
    SCENARIOS,
    SEQUENCE_SCENARIOS,
    validate_answer,
    validate_sequence_answer,
)


class InteractionScenarioTests(TestCase):
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        self.auth_patch = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser("user-123", "learner@example.com"),
        )
        self.auth_patch.start()
        self.addCleanup(self.auth_patch.stop)

    def test_page_shows_b1_b2_scenarios_and_honest_scope(self):
        response = self.client.get("/interaction/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(SCENARIOS), 5)
        self.assertContains(response, "Взаимодействие и медиация")
        self.assertContains(response, "Договориться о плане")
        self.assertContains(response, "Выбрать подходящий регистр")
        self.assertContains(response, "не экзамен, сертификат")
        self.assertContains(response, 'name="scenario_id"', count=8)

    def test_page_shows_sequence_tasks_beyond_multiple_choice(self):
        response = self.client.get("/interaction/")

        self.assertEqual(len(SEQUENCE_SCENARIOS), 3)
        self.assertContains(response, "Собери ответ по смысловым шагам")
        self.assertContains(response, "Собрать вежливую просьбу")
        self.assertContains(response, 'name="block_id"', count=9)

    def test_correct_answer_has_transparent_explanation(self):
        response = self.client.post(
            "/interaction/",
            {"scenario_id": "meeting-position", "option_id": "a"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Подходящий ответ")
        self.assertContains(response, "сохраняет главное опасение")

    def test_wrong_answer_shows_better_option_and_reason(self):
        response = self.client.post(
            "/interaction/",
            {"scenario_id": "formal-reply", "option_id": "a"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Есть более подходящий ответ")
        self.assertContains(response, "Szanowna Pani")
        self.assertContains(response, "слишком разговорные")

    def test_invalid_and_ambiguous_payloads_are_rejected(self):
        invalid = self.client.post(
            "/interaction/", {"scenario_id": "missing", "option_id": "a"}
        )
        unexpected = self.client.post(
            "/interaction/",
            {"scenario_id": "weekend-plan", "option_id": "b", "score": "100"},
        )
        ambiguous = self.client.post(
            "/interaction/",
            {"scenario_id": "weekend-plan", "option_id": ["a", "b"]},
        )

        self.assertEqual(invalid.status_code, 400)
        self.assertContains(invalid, "Неизвестный сценарий", status_code=400)
        self.assertEqual(unexpected.status_code, 400)
        self.assertEqual(ambiguous.status_code, 400)

    def test_domain_validation_rejects_option_from_another_scenario(self):
        with self.assertRaisesRegex(ValueError, "Выберите один"):
            validate_answer("weekend-plan", "unknown")

    def test_sequence_answer_is_checked_and_explained(self):
        correct = self.client.post(
            "/interaction/",
            {
                "task_type": "sequence",
                "scenario_id": "delay-mediation",
                "block_id": ["cause", "effect", "reservation"],
            },
        )
        wrong = self.client.post(
            "/interaction/",
            {
                "task_type": "sequence",
                "scenario_id": "delay-mediation",
                "block_id": ["reservation", "effect", "cause"],
            },
        )

        self.assertContains(correct, "Логичная последовательность")
        self.assertContains(correct, "причина → последствие")
        self.assertContains(wrong, "Порядок стоит изменить")
        self.assertContains(wrong, "Dostawca poinformował")

    def test_sequence_payload_must_be_exact_permutation(self):
        duplicate = self.client.post(
            "/interaction/",
            {
                "task_type": "sequence",
                "scenario_id": "library-request",
                "block_id": ["context", "context", "request"],
            },
        )
        injected = self.client.post(
            "/interaction/",
            {
                "task_type": "sequence",
                "scenario_id": "library-request",
                "block_id": ["context", "question", "other"],
            },
        )

        self.assertContains(duplicate, "каждый предложенный блок", status_code=400)
        self.assertContains(injected, "каждый предложенный блок", status_code=400)
        with self.assertRaisesRegex(ValueError, "ровно один раз"):
            validate_sequence_answer(
                "library-request", ("context", "context", "request")
            )

    def test_route_requires_authentication(self):
        self.auth_patch.stop()
        self.client.cookies.clear()

        response = self.client.get("/interaction/")

        self.assertRedirects(
            response,
            "/login/?next=%2Finteraction%2F",
            fetch_redirect_response=False,
        )

    def test_course_b1_and_b2_link_to_scenarios(self):
        for level in ("B1", "B2"):
            with self.subTest(level=level):
                response = self.client.get(f"/course/?level={level}")
                self.assertContains(response, f"Сценарии {level}")
                self.assertContains(response, 'href="/interaction/"')
