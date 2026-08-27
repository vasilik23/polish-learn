from django.test import TestCase

from polskiflow.learning.models import (
    Flashcard,
    Lesson,
    LessonFlashcard,
    Question,
    ReadingText,
    Topic,
)
from polskiflow.content import course_topics


class IntroductionsContentTests(TestCase):
    def test_introductions_topic_is_first(self):
        topic = Topic.objects.get(id="introductions")

        self.assertEqual(topic.position, 0)
        self.assertEqual(topic.title, "Знакомство")
        self.assertEqual(topic.course_id, "a1-foundations")

    def test_daily_plan_contains_complete_introductions_block(self):
        lessons = Lesson.objects.filter(topic_id="introductions")

        self.assertEqual(lessons.count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="quiz").count(), 8)
        self.assertEqual(
            LessonFlashcard.objects.filter(lesson_id="words").count(), 8
        )
        self.assertEqual(
            LessonFlashcard.objects.filter(lesson_id="review").count(), 7
        )

    def test_original_content_has_source_metadata(self):
        expected_origin = "original"

        self.assertEqual(
            Lesson.objects.get(id="words").source_metadata["origin"],
            expected_origin,
        )
        self.assertEqual(
            Flashcard.objects.get(id="mam-na-imie").source_metadata["origin"],
            expected_origin,
        )
        self.assertEqual(
            ReadingText.objects.get(
                id="pierwszy-dzien-na-kursie"
            ).source_metadata["origin"],
            expected_origin,
        )

    def test_introductions_reading_has_glossary(self):
        reading = ReadingText.objects.get(id="pierwszy-dzien-na-kursie")

        self.assertEqual(reading.level, "A1")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertIn("przedstawia", reading.glossary)


class CountriesLanguagesContentTests(TestCase):
    def test_topic_follows_introductions(self):
        topic = Topic.objects.get(id="countries-languages")

        self.assertEqual(topic.position, 1)
        self.assertEqual(topic.course_id, "a1-foundations")

    def test_topic_has_complete_vertical_block(self):
        lessons = Lesson.objects.filter(topic_id="countries-languages")

        self.assertEqual(lessons.count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="countries-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="countries-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="countries-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="countries-review").count(), 7)

    def test_new_content_is_original_and_reading_has_glossary(self):
        reading = ReadingText.objects.get(id="rozmowa-w-miedzynarodowej-grupie")

        self.assertEqual(Lesson.objects.get(id="countries-words").source_metadata["origin"], "original")
        self.assertEqual(Flashcard.objects.get(id="pochodzic").source_metadata["origin"], "original")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertIn("międzynarodowa", reading.glossary)

    def test_course_catalog_groups_lessons_by_topic(self):
        topics = course_topics()

        self.assertEqual([topic["id"] for topic in topics[:2]], ["introductions", "countries-languages"])
        self.assertEqual(len(topics[0]["lessons"]), 4)
        self.assertEqual(len(topics[1]["lessons"]), 4)


class FamilyContentTests(TestCase):
    def test_family_topic_is_third(self):
        topic = Topic.objects.get(id="family")

        self.assertEqual(topic.position, 2)
        self.assertEqual(topic.course_id, "a1-foundations")

    def test_family_has_complete_vertical_block(self):
        self.assertEqual(Lesson.objects.filter(topic_id="family").count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="family-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="family-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="family-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="family-review").count(), 7)

    def test_family_content_is_original_and_reading_has_glossary(self):
        reading = ReadingText.objects.get(id="niedziela-u-babci")

        self.assertEqual(Lesson.objects.get(id="family-words").source_metadata["origin"], "original")
        self.assertEqual(Flashcard.objects.get(id="rodzina").source_metadata["origin"], "original")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertIn("odwiedza", reading.glossary)

    def test_course_catalog_lists_family_after_first_topics(self):
        topics = course_topics()

        self.assertEqual([topic["id"] for topic in topics[:3]], ["introductions", "countries-languages", "family"])
        self.assertEqual(len(topics[2]["lessons"]), 4)


class DailyRoutineContentTests(TestCase):
    def test_daily_routine_is_fourth_complete_topic(self):
        topic = Topic.objects.get(id="daily-routine")

        self.assertEqual(topic.position, 3)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="daily-routine-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="daily-routine-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="daily-routine-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="daily-routine-review").count(), 7)

    def test_daily_reading_uses_lemma_aware_glossary(self):
        reading = ReadingText.objects.get(id="zwykly-dzien-oli")

        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["budzi"]["lemma"], "budzić się")
        self.assertEqual(reading.glossary["kanapkę"]["lemma"], "kanapka")

    def test_catalog_lists_first_four_curriculum_topics(self):
        topics = course_topics()

        self.assertEqual(
            [topic["id"] for topic in topics[:4]],
            ["introductions", "countries-languages", "family", "daily-routine"],
        )


class HomeContentTests(TestCase):
    def test_home_is_fifth_complete_topic(self):
        topic = Topic.objects.get(id="home")
        self.assertEqual(topic.position, 4)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="home-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="home-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="home-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="home-review").count(), 7)

    def test_home_reading_has_lemma_glossary(self):
        reading = ReadingText.objects.get(id="nowe-mieszkanie-marty")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["piętrze"]["lemma"], "piętro")
        self.assertEqual(reading.glossary["stoją"]["lemma"], "stać")

    def test_catalog_lists_home_after_daily_routine(self):
        self.assertEqual(
            [topic["id"] for topic in course_topics()[:5]],
            ["introductions", "countries-languages", "family", "daily-routine", "home"],
        )
