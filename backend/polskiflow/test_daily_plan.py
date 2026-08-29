from datetime import date

from django.test import SimpleTestCase

from polskiflow.domain.daily_plan import build_daily_plan


class DailyPlanTests(SimpleTestCase):
    def setUp(self):
        self.lessons = [
            {
                "id": lesson_id,
                "kind": "words",
                "title": lesson_id,
                "description": "Описание",
                "minutes": 5,
                "emoji": "📘",
                "level": level,
            }
            for lesson_id, level in (
                ("a1-one", "A1"),
                ("a2-one", "A2"),
                ("a2-two", "A2"),
                ("a2-three", "A2"),
                ("a2-four", "A2"),
            )
        ]

    def test_plan_prefers_unfinished_lessons_at_current_level(self):
        plan = build_daily_plan(
            self.lessons,
            level="A2",
            completed_all_time=frozenset({"a2-one"}),
            completed_today=frozenset({"a2-two"}),
            personal_words=[],
            today=date(2026, 8, 28),
        )

        self.assertEqual(
            [task["id"] for task in plan],
            ["a2-two", "a2-three", "a2-four", "a2-one"],
        )
        self.assertTrue(plan[0]["completed"])

    def test_completed_today_stays_in_plan_after_it_enters_history(self):
        plan = build_daily_plan(
            self.lessons,
            level="A2",
            completed_all_time=frozenset({"a2-one"}),
            completed_today=frozenset({"a2-one"}),
            personal_words=[],
            today=date(2026, 8, 28),
        )

        self.assertEqual(
            [task["id"] for task in plan],
            ["a2-one", "a2-two", "a2-three", "a2-four"],
        )
        self.assertTrue(plan[0]["completed"])
        self.assertEqual(sum(task["completed"] for task in plan), 1)

    def test_due_dictionary_review_replaces_fourth_lesson(self):
        words = [
            {
                "id": str(index),
                "next_review_date": "2026-08-28" if index < 2 else "2026-09-10",
            }
            for index in range(4)
        ]

        plan = build_daily_plan(
            self.lessons,
            level="A2",
            completed_all_time=frozenset(),
            completed_today=frozenset({"dictionary-practice"}),
            personal_words=words,
            today=date(2026, 8, 28),
        )

        self.assertEqual(len(plan), 4)
        self.assertEqual(plan[-1]["id"], "dictionary-practice")
        self.assertEqual(plan[-1]["description"], "2 слова по расписанию SM-2")
        self.assertTrue(plan[-1]["completed"])

    def test_review_is_not_offered_until_four_words_exist(self):
        plan = build_daily_plan(
            self.lessons,
            level="A2",
            completed_all_time=frozenset(),
            completed_today=frozenset(),
            personal_words=[{"next_review_date": None}] * 3,
            today=date(2026, 8, 28),
        )

        self.assertNotIn("dictionary-practice", {task["id"] for task in plan})
