from unittest.mock import patch

from django.test import TestCase

from polskiflow.auth import ACCESS_COOKIE, SupabaseUser
from polskiflow.learning.models import Course, Flashcard, Lesson, LessonFlashcard, Question, Topic
from polskiflow.progress_store import DashboardProgress


class LessonViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Lesson.objects.all().delete()
        Flashcard.objects.all().delete()
        course = Course.objects.create(id="lesson-test-course", title="A1", level="A1")
        topic = Topic.objects.create(id="lesson-test-topic", course=course, title="Основы")
        lesson_data = [
            ("words", "Słówka dnia", "Новые слова"),
            ("grammar", "Gramatyka", "Грамматика"),
            ("review", "Powtórka", "Повторение"),
            ("quiz", "Quiz", "Мини-тест"),
        ]
        for position, (lesson_id, title, plan_title) in enumerate(lesson_data):
            Lesson.objects.create(
                id=lesson_id,
                topic=topic,
                kind=lesson_id,
                title=title,
                plan_title=plan_title,
                subtitle="5 заданий",
                description="Описание",
                position=position,
                theory_title="Rodzajnik i ród rzeczownika" if lesson_id == "grammar" else "",
                theory_sections=[["Род существительных", "Короткая теория"]] if lesson_id == "grammar" else [],
            )
        cards = [
            ("czesc", "cześć", "привет"),
            ("dziekuje", "dziękuję", "спасибо"),
            ("prosze", "proszę", "пожалуйста"),
            ("tak", "tak", "да"),
            ("nie", "nie", "нет"),
        ]
        for position, (card_id, polish, translation) in enumerate(cards):
            card = Flashcard.objects.create(id=card_id, polish=polish, translation=translation, position=position)
            LessonFlashcard.objects.create(
                lesson_id="words", flashcard=card, position=position
            )
        review_card = Flashcard.objects.create(
            id="jestem", polish="jestem", translation="я есть", position=5
        )
        LessonFlashcard.objects.create(
            lesson_id="review", flashcard=review_card, position=0
        )
        grammar_prompts = ["Слово «kawa»", "Слово «dom»", "Слово «miasto»"]
        for position, prompt in enumerate(grammar_prompts):
            Question.objects.create(lesson_id="grammar", prompt=prompt, options=["мужской", "женский", "средний"], correct=position % 3, explanation="Пояснение", position=position)
        Question.objects.create(
            lesson_id="grammar",
            prompt="Составьте: Марек работает сегодня дома.",
            options=[
                "Marek dzisiaj pracuje w domu.",
                "Marek pracuje dzisiaj w domu.",
                "Dzisiaj dom Marek w pracuje.",
            ],
            correct=1,
            explanation="Нейтральный порядок: подлежащее, сказуемое, время и место.",
            position=3,
        )
        quiz_prompts = ["Как переводится «cześć»?", "Что значит «dziękuję»?", "Выберите перевод", "Как будет «да»?", "Как будет «нет»?"]
        for position, prompt in enumerate(quiz_prompts):
            Question.objects.create(lesson_id="quiz", prompt=prompt, options=["нет", "привет", "спасибо"], correct=1, explanation="Cześć — неформальное «привет».", position=position)
    def setUp(self):
        self.client.cookies[ACCESS_COOKIE] = "access"
        self.auth_patch = patch(
            "polskiflow.auth.authenticate_access_token",
            return_value=SupabaseUser("user-123", "learner@example.com"),
        )
        self.auth_patch.start()
        self.addCleanup(self.auth_patch.stop)

    def test_daily_tasks_lists_all_lessons_and_home_only_shows_goal(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Цель на сегодня")
        self.assertContains(response, "Начать занятия")
        self.assertContains(response, 'role="progressbar"')
        self.assertContains(response, 'aria-label="Выполнение цели на сегодня"')
        self.assertContains(response, 'aria-valuenow="0"')
        self.assertNotContains(response, "Słówka dnia")
        self.assertNotContains(response, "Задания на сегодня")

        tasks_page = self.client.get("/tasks/")
        self.assertEqual(tasks_page.status_code, 200)
        self.assertContains(tasks_page, "Słówka dnia")
        self.assertContains(tasks_page, "Gramatyka")
        self.assertContains(tasks_page, "Powtórka")
        self.assertContains(tasks_page, "Quiz")

    def test_listening_pilot_scores_public_domain_clips(self):
        page = self.client.get("/listening/")
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, "Узнай слово на слух")
        self.assertContains(page, "polskiflow/audio/tecza.ogg")
        self.assertContains(page, "polskiflow/audio/wrobel.ogg")
        self.assertContains(page, "polskiflow/audio/mysz.ogg")
        self.assertContains(page, "public domain")

        result = self.client.post(
            "/listening/", {"tecza": "tęcza", "wrobel": "wybór", "mysz": "mysz"}
        )
        self.assertEqual(result.status_code, 200)
        self.assertContains(result, "2 / 3")
        self.assertContains(result, "Правильный ответ")
        self.assertContains(result, "wróbel")

    def test_course_links_to_listening_pilot(self):
        page = self.client.get("/course/?level=A1")
        self.assertContains(page, 'href="/listening/"')
        self.assertContains(page, "Аудиопилот A1")

    def test_home_keeps_daily_plan_short_and_course_page_lists_topics(self):
        course = Course.objects.create(id="catalog-test", title="A1", level="A1")
        topic = Topic.objects.create(id="catalog-topic", course=course, title="Новая тема")
        extra = Lesson.objects.create(id="extra-lesson", topic=topic, title="Extra", plan_title="Extra", subtitle="A1", description="Каталог", position=5)

        response = self.client.get("/")

        self.assertContains(response, "0 из 4")
        self.assertNotContains(response, "Новая тема")
        self.assertNotContains(response, "Задания на сегодня")

        course_page = self.client.get("/course/")
        self.assertContains(course_page, "Новая тема")
        self.assertContains(course_page, extra.title)

    def test_course_catalog_separates_topics_by_cefr_level(self):
        a2_course = Course.objects.create(
            id="a2-catalog-test", title="A2", level="A2", position=2
        )
        a2_topic = Topic.objects.create(
            id="a2-catalog-topic", course=a2_course, title="Прошедшие выходные"
        )
        Lesson.objects.create(
            id="a2-extra-lesson",
            topic=a2_topic,
            title="Miniony weekend",
            plan_title="Weekend",
            subtitle="A2",
            description="Прошедшее время",
            position=50,
        )

        a1_page = self.client.get("/course/")
        self.assertContains(a1_page, 'aria-label="Уровни курса"')
        self.assertContains(a1_page, 'href="?level=A1" aria-current="page"')
        self.assertNotContains(a1_page, "Miniony weekend")

        a2_page = self.client.get("/course/?level=A2")
        self.assertContains(a2_page, 'href="?level=A2" aria-current="page"')
        self.assertContains(a2_page, "1 тема")
        self.assertContains(a2_page, "Прошедшие выходные")
        self.assertContains(a2_page, "Miniony weekend")
        self.assertNotContains(a2_page, "Новая тема")

    def test_course_catalog_falls_back_to_a1_for_unknown_level(self):
        response = self.client.get("/course/?level=Z9")
        self.assertContains(response, 'href="?level=A1" aria-current="page"')

    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_course_catalog_defaults_to_profile_level(self, mocked_progress):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A2",
            streak_days=0,
            completed_lesson_ids=frozenset(),
            available=True,
        )

        response = self.client.get("/course/")

        self.assertContains(response, 'href="?level=A2" aria-current="page"')

    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_course_catalog_explicit_level_overrides_profile_level(self, mocked_progress):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A2",
            streak_days=0,
            completed_lesson_ids=frozenset(),
            available=True,
        )

        response = self.client.get("/course/?level=A1")

        self.assertContains(response, 'href="?level=A1" aria-current="page"')

    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_course_catalog_invalid_level_falls_back_to_profile_level(self, mocked_progress):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A2",
            streak_days=0,
            completed_lesson_ids=frozenset(),
            available=True,
        )

        response = self.client.get("/course/?level=Z9")

        self.assertContains(response, 'href="?level=A2" aria-current="page"')

    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_course_catalog_invalid_profile_level_falls_back_to_a1(self, mocked_progress):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="Z9",
            streak_days=0,
            completed_lesson_ids=frozenset(),
            available=True,
        )

        response = self.client.get("/course/")

        self.assertContains(response, 'href="?level=A1" aria-current="page"')

    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_course_topic_shows_all_time_progress_and_next_lesson(self, mocked_progress):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A1",
            streak_days=4,
            completed_lesson_ids=frozenset(),
            available=True,
            all_completed_lesson_ids=frozenset({"words", "grammar"}),
        )

        response = self.client.get("/course/")

        self.assertContains(response, "2 / 4 уроков")
        self.assertContains(response, 'aria-label="Прогресс темы «Основы»"')
        self.assertContains(response, 'aria-valuenow="2"')
        self.assertContains(response, 'href="/lesson/review/">Продолжить')

    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_course_topic_shows_completed_status(self, mocked_progress):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A1",
            streak_days=4,
            completed_lesson_ids=frozenset(),
            available=True,
            all_completed_lesson_ids=frozenset(
                {"words", "grammar", "review", "quiz"}
            ),
        )

        response = self.client.get("/course/")

        self.assertContains(response, "4 / 4 уроков")
        self.assertContains(response, "Все уроки пройдены")
        self.assertNotContains(response, 'href="/lesson/words/">Продолжить')

    def test_user_menu_contains_logout(self):
        response = self.client.get("/")
        content = response.content.decode()

        self.assertContains(response, "Открыть меню пользователя")
        self.assertContains(response, 'class="user-menu app-user-menu"')
        self.assertContains(response, 'action="/logout/"')
        self.assertContains(response, 'href="/profile/"')
        self.assertGreater(content.index("</nav>"), content.index('class="nav-links"'))
        self.assertLess(content.index("</nav>"), content.index('class="user-menu app-user-menu"'))

    def test_base_template_offers_persisted_accessible_theme_selection(self):
        response = self.client.get("/")

        self.assertContains(response, 'data-theme-select')
        self.assertContains(response, 'aria-label="Цветовая тема"')
        self.assertContains(response, 'value="system"')
        self.assertContains(response, 'value="light"')
        self.assertContains(response, 'value="dark"')
        self.assertContains(response, 'localStorage.setItem(theme.storageKey')
        self.assertContains(response, 'prefers-color-scheme: dark')

    def test_base_template_has_no_render_blocking_external_font(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "fonts.googleapis.com")
        self.assertNotContains(response, "fonts.gstatic.com")

    @patch("polskiflow.auth_views.load_personal_words")
    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_profile_shows_identity_progress_and_settings(
        self, mocked_progress, mocked_words
    ):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A2",
            streak_days=4,
            completed_lesson_ids=frozenset({"words"}),
            available=True,
            all_completed_lesson_ids=frozenset({"words", "grammar"}),
            active_days=7,
            weekly_active_days=4,
            weekly_completed_count=6,
            previous_week_active_days=2,
            previous_week_completed_count=3,
            daily_goal_lessons=2,
            recent_daily_completion_counts=(2,) * 14 + (0,) * 14,
        )
        mocked_words.return_value = [{"word": "dom"}, {"word": "dzień"}]

        response = self.client.get("/profile/")
        self.assertContains(response, "Недельная активность")
        self.assertContains(response, "Месячный обзор")
        self.assertContains(response, "6")
        self.assertContains(response, "4 / 7")
        self.assertContains(response, "на 3 больше")
        self.assertContains(response, "на 2 больше")
        self.assertContains(response, "В прошлый период: 3 уроков за 2 активных дней")
        self.assertContains(response, "Насколько подходит нагрузка")
        self.assertContains(response, "14 / 28")
        self.assertContains(response, "50%")
        self.assertContains(response, "Нагрузка выглядит посильной")
        self.assertContains(response, "это ориентир, а не оценка")
        self.assertContains(response, 'data-goal-status="sustainable"')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Василий")
        self.assertContains(response, "learner@example.com")
        self.assertContains(response, "2 / 4")
        self.assertContains(response, "50%")
        self.assertContains(response, "7")
        self.assertContains(response, "слов в словаре")
        self.assertContains(response, "Достижения")
        self.assertContains(response, "Первый шаг")
        self.assertContains(response, "Три дня подряд")
        self.assertContains(response, "4 / 7")
        self.assertContains(response, 'aria-label="Неделя в ритме"')
        self.assertContains(response, "Настройки")
        self.assertContains(response, 'role="progressbar"')
        self.assertContains(response, 'name="csrfmiddlewaretoken"')
        self.assertContains(response, 'name="display_name"')
        self.assertContains(response, 'name="level"')
        self.assertContains(response, "Сохранить профиль")
        self.assertContains(response, "плане на день, курсе и библиотеке")
        self.assertNotContains(response, "Сейчас используется светлая тема")
        self.assertNotContains(response, 'class="settings-list"')

    def test_profile_requires_authentication(self):
        self.auth_patch.stop()
        self.client.cookies.clear()

        response = self.client.get("/profile/")

        self.assertRedirects(response, "/login/?next=%2Fprofile%2F", fetch_redirect_response=False)

    def test_b1_course_links_to_writing_practice(self):
        response = self.client.get("/course/?level=B1")

        self.assertContains(response, "Письменная практика B1")
        self.assertContains(response, 'href="/writing/?level=B1"')

    def test_b2_course_links_to_level_specific_writing_practice(self):
        response = self.client.get("/course/?level=B2")

        self.assertContains(response, "Письменная практика B2")
        self.assertContains(response, 'href="/writing/?level=B2"')

    def test_writing_practice_has_local_drafts_and_honest_self_check(self):
        response = self.client.get("/writing/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Письменные ответы")
        self.assertContains(response, "нет автоматической проверки")
        self.assertContains(response, 'data-writing-draft="formal-request"')
        self.assertContains(response, "Самопроверка перед завершением", count=4)
        self.assertContains(response, 'localStorage.setItem(key, textarea.value)')
        self.assertContains(response, 'window.confirm("Удалить черновик этого задания?')

    def test_writing_practice_supports_b2_and_separates_local_storage(self):
        response = self.client.get("/writing/?level=B2")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Практика B2")
        self.assertContains(response, "Сравнение двух сообщений")
        self.assertContains(response, 'data-writing-draft="source-comparison"')
        self.assertContains(response, "polskiflow-writing-b2:")
        self.assertContains(response, 'href="?level=B2" aria-current="page"')

    def test_writing_practice_falls_back_to_b1_for_unknown_level(self):
        response = self.client.get("/writing/?level=C1")

        self.assertContains(response, "Практика B1")
        self.assertNotContains(response, "Сравнение двух сообщений")

    def test_writing_practice_requires_authentication(self):
        self.auth_patch.stop()
        self.client.cookies.clear()

        response = self.client.get("/writing/")

        self.assertRedirects(response, "/login/?next=%2Fwriting%2F", fetch_redirect_response=False)

    @patch("polskiflow.auth_views.save_profile_settings", return_value=True)
    @patch("polskiflow.auth_views.load_personal_words", return_value=[])
    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_profile_updates_name_and_level(
        self, mocked_progress, _mocked_words, mocked_save
    ):
        mocked_progress.return_value = DashboardProgress(
            "learner", "A1", 0, frozenset(), True
        )

        response = self.client.post(
            "/profile/", {"display_name": "  Анна  ", "level": "b1", "daily_goal_lessons": "6"}
        )

        self.assertEqual(response.status_code, 200)
        mocked_save.assert_called_once_with("access", "user-123", "Анна", "B1", 6)
        self.assertContains(response, "Профиль сохранён")
        self.assertContains(response, "Анна")
        self.assertContains(response, 'value="B1" selected')

    @patch("polskiflow.auth_views.save_profile_settings")
    @patch("polskiflow.auth_views.load_personal_words", return_value=[])
    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_profile_rejects_invalid_name_and_level(
        self, mocked_progress, _mocked_words, mocked_save
    ):
        mocked_progress.return_value = DashboardProgress(
            "learner", "A1", 0, frozenset(), True
        )

        empty_name = self.client.post(
            "/profile/", {"display_name": " ", "level": "A2"}
        )
        invalid_level = self.client.post(
            "/profile/", {"display_name": "Анна", "level": "C3"}
        )
        invalid_goal = self.client.post(
            "/profile/", {"display_name": "Анна", "level": "A2", "daily_goal_lessons": "11"}
        )

        self.assertContains(empty_name, "Укажите имя")
        self.assertContains(invalid_level, "Выберите уровень от A1 до C2")
        self.assertContains(invalid_goal, "Цель должна быть от 1 до 10")
        mocked_save.assert_not_called()

    @patch("polskiflow.auth_views.load_personal_words", return_value=[])
    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_course_catalog_offers_c2_and_profile_can_select_it(self, mocked_progress, _words):
        mocked_progress.return_value = DashboardProgress(
            "Learner", "C2", 0, frozenset(), True
        )

        course_response = self.client.get("/course/")
        profile_response = self.client.get("/profile/")

        self.assertContains(course_response, "Траектория A1 → C2")
        self.assertContains(course_response, 'href="?level=C2"')
        self.assertContains(profile_response, '<option value="C2" selected>')

    @patch("polskiflow.auth_views.save_profile_settings", return_value=False)
    @patch("polskiflow.auth_views.load_personal_words", return_value=[])
    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_profile_reports_store_failure(
        self, mocked_progress, _mocked_words, _mocked_save
    ):
        mocked_progress.return_value = DashboardProgress(
            "learner", "A1", 0, frozenset(), True
        )

        response = self.client.post(
            "/profile/", {"display_name": "Анна", "level": "A2"}
        )

        self.assertContains(response, "Не удалось сохранить профиль")
        self.assertContains(response, 'value="A2" selected')

    def test_sources_explains_original_content_feeds_and_references(self):
        response = self.client.get("/sources/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "создаются специально для PolskiFlow")
        self.assertContains(response, "Внешние новостные ленты")
        self.assertContains(response, "Główny Urząd Statystyczny")
        self.assertContains(response, "RMF24")
        self.assertContains(response, "Polsat Sport")
        self.assertContains(response, "Лингвистические и методические ориентиры")
        self.assertContains(response, "Wielki słownik języka polskiego PAN")
        self.assertContains(response, "не копируем статьи")

    def test_sources_is_publicly_available(self):
        self.auth_patch.stop()
        self.client.cookies.clear()

        response = self.client.get("/sources/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Источники и лицензии")

    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_home_marks_today_progress(self, mocked_progress):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A2",
            streak_days=4,
            completed_lesson_ids=frozenset({"words", "grammar"}),
            available=True,
        )

        response = self.client.get("/")

        self.assertContains(response, "Cześć, Василий!")
        self.assertContains(response, "Уровень A2")
        self.assertContains(response, "4 дн. подряд")
        self.assertContains(response, "2 из 4")

        tasks_page = self.client.get("/tasks/")
        self.assertContains(tasks_page, 'class="task-complete"', count=2)

    @patch("polskiflow.auth_views.load_personal_words", return_value=[])
    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_today_and_tasks_keep_a_newly_completed_lesson_in_daily_progress(
        self, mocked_progress, _mocked_words
    ):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A1",
            streak_days=1,
            completed_lesson_ids=frozenset({"words"}),
            available=True,
            all_completed_lesson_ids=frozenset({"words"}),
        )

        home = self.client.get("/")
        tasks_page = self.client.get("/tasks/")

        self.assertContains(home, "1 из 4")
        self.assertContains(home, "25%")
        self.assertContains(tasks_page, "1 из 4 выполнено")
        self.assertContains(tasks_page, 'class="task-complete"', count=1)

    @patch("polskiflow.auth_views.load_personal_words")
    @patch("polskiflow.auth_views.load_dashboard_progress")
    def test_daily_plan_includes_due_dictionary_review(
        self, mocked_progress, mocked_words
    ):
        mocked_progress.return_value = DashboardProgress(
            display_name="Василий",
            level="A1",
            streak_days=1,
            completed_lesson_ids=frozenset(),
            available=True,
        )
        mocked_words.return_value = [
            {
                "id": str(index),
                "word": f"word-{index}",
                "translation": f"слово-{index}",
                "next_review_date": "2026-01-01" if index == 0 else "2999-01-01",
            }
            for index in range(4)
        ]

        response = self.client.get("/tasks/")

        self.assertContains(response, "Повторение словаря")
        self.assertContains(response, "1 слово по расписанию SM-2")
        self.assertContains(response, 'href="/dictionary/practice/"')
        self.assertEqual(len(response.context["tasks"]), 4)

    def test_unknown_lesson_returns_404(self):
        self.assertEqual(self.client.get("/lesson/unknown/").status_code, 404)

    def test_flashcard_can_be_revealed_and_completed(self):
        revealed = self.client.post(
            "/lesson/words/step/", {"action": "reveal", "index": 0, "score": 0}
        )
        self.assertContains(revealed, "привет")

        response = None
        for index in range(5):
            response = self.client.post(
                "/lesson/words/step/",
                {"action": "know", "index": index, "score": index},
            )
        self.assertContains(response, "5 / 5")
        self.assertContains(response, "Урок завершён")

    def test_quiz_answer_shows_explanation_and_next_question(self):
        answered = self.client.post(
            "/lesson/quiz/step/",
            {"action": "answer", "index": 0, "score": 0, "choice": 1},
        )
        self.assertContains(answered, "Cześć — неформальное")
        next_question = self.client.post(
            "/lesson/quiz/step/",
            {"action": "next", "index": 0, "score": 0, "selected": 1},
        )
        self.assertContains(next_question, "Что значит")

    def test_grammar_theory_starts_exercises(self):
        page = self.client.get("/lesson/grammar/")
        self.assertContains(page, "Род существительных")
        exercise = self.client.post(
            "/lesson/grammar/step/", {"action": "start", "index": 0, "score": 0}
        )
        self.assertContains(exercise, "Слово «kawa»")

    def test_grammar_sentence_builder_is_accessible_and_server_validated(self):
        question = self.client.post(
            "/lesson/grammar/step/",
            {"action": "next", "index": 2, "score": 0, "selected": 2},
        )
        self.assertContains(question, "Составь предложение")
        self.assertContains(question, "data-sentence-builder")
        self.assertContains(question, 'type="button" class="sentence-token"')
        self.assertContains(question, "Сбросить")
        self.assertContains(question, "Проверить")

        missing_word = self.client.post(
            "/lesson/grammar/step/",
            {"action": "answer", "index": 3, "score": 0, "answer_order": "[0]"},
        )
        self.assertEqual(missing_word.status_code, 400)

        question_context = question.context
        shuffled = question_context["builder_tokens"]
        correct_words = "Marek pracuje dzisiaj w domu.".split()
        correct_order = [shuffled.index(word) for word in correct_words]
        answered = self.client.post(
            "/lesson/grammar/step/",
            {
                "action": "answer",
                "index": 3,
                "score": 0,
                "answer_order": __import__("json").dumps(correct_order),
            },
        )
        self.assertContains(answered, "Верно")
        self.assertContains(answered, "Нейтральный порядок")

        tampered_next = self.client.post(
            "/lesson/grammar/step/",
            {"action": "next", "index": 3, "score": 0, "answer_order": "[0, 0, 1, 2, 3]"},
        )
        self.assertEqual(tampered_next.status_code, 400)

    def test_review_uses_only_its_linked_flashcards(self):
        page = self.client.get("/lesson/review/")

        self.assertContains(page, "jestem")
        self.assertContains(page, "Карточка 1 из 1")
        self.assertNotContains(page, "cześć")

    def test_invalid_lesson_state_is_rejected(self):
        response = self.client.post(
            "/lesson/quiz/step/",
            {"action": "answer", "index": 999, "score": 0, "choice": 0},
        )
        self.assertEqual(response.status_code, 400)
