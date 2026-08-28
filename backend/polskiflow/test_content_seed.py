from django.test import TestCase

from polskiflow.learning.models import (
    Course,
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


class FoodShoppingContentTests(TestCase):
    def test_food_shopping_is_sixth_complete_topic(self):
        topic = Topic.objects.get(id="food-shopping")
        self.assertEqual(topic.position, 5)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="food-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="food-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="food-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="food-review").count(), 7)

    def test_food_reading_has_lemma_aware_glossary(self):
        reading = ReadingText.objects.get(id="zakupy-oli")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["idzie"]["lemma"], "iść")
        self.assertEqual(reading.glossary["torby"]["lemma"], "torba")

    def test_catalog_lists_first_six_curriculum_topics(self):
        self.assertEqual(
            [topic["id"] for topic in course_topics()[:6]],
            ["introductions", "countries-languages", "family", "daily-routine", "home", "food-shopping"],
        )


class CityDirectionsContentTests(TestCase):
    def test_city_directions_is_seventh_complete_topic(self):
        topic = Topic.objects.get(id="city-directions")
        self.assertEqual(topic.position, 6)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="city-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="city-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="city-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="city-review").count(), 7)

    def test_city_reading_uses_normalized_lemmas(self):
        reading = ReadingText.objects.get(id="droga-do-muzeum")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["drogę"]["lemma"], "droga")
        self.assertEqual(reading.glossary["skrzyżowaniu"]["lemma"], "skrzyżowanie")
        self.assertEqual(reading.glossary["wychodzi"]["part_of_speech"], "глагол")

    def test_catalog_lists_first_seven_curriculum_topics(self):
        self.assertEqual(
            [topic["id"] for topic in course_topics()[:7]],
            ["introductions", "countries-languages", "family", "daily-routine", "home", "food-shopping", "city-directions"],
        )


class TimeMeetingsContentTests(TestCase):
    def test_time_meetings_is_eighth_complete_topic(self):
        topic = Topic.objects.get(id="time-meetings")
        self.assertEqual(topic.position, 7)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="time-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="time-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="time-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="time-review").count(), 7)

    def test_time_reading_uses_normalized_lemmas(self):
        reading = ReadingText.objects.get(id="spotkanie-w-piatek")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["tygodniu"]["lemma"], "tydzień")
        self.assertEqual(reading.glossary["jedzie"]["lemma"], "jechać")
        self.assertEqual(reading.glossary["cieszą"]["lemma"], "cieszyć się")

    def test_catalog_lists_first_eight_curriculum_topics(self):
        self.assertEqual(
            [topic["id"] for topic in course_topics()[:8]],
            ["introductions", "countries-languages", "family", "daily-routine", "home", "food-shopping", "city-directions", "time-meetings"],
        )


class WorkStudyContentTests(TestCase):
    def test_work_study_is_ninth_complete_topic(self):
        topic = Topic.objects.get(id="work-study")
        self.assertEqual(topic.position, 8)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="work-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="work-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="work-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="work-review").count(), 7)

    def test_work_reading_uses_normalized_lemmas(self):
        reading = ReadingText.objects.get(id="pierwszy-dzien-w-pracy")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["pracowników"]["lemma"], "pracownik")
        self.assertEqual(reading.glossary["zmęczona"]["lemma"], "zmęczony")
        self.assertEqual(reading.glossary["rozumie"]["lemma"], "rozumieć")

    def test_catalog_lists_first_nine_curriculum_topics(self):
        self.assertEqual(
            [topic["id"] for topic in course_topics()[:9]],
            ["introductions", "countries-languages", "family", "daily-routine", "home", "food-shopping", "city-directions", "time-meetings", "work-study"],
        )


class FreeTimeContentTests(TestCase):
    def test_free_time_is_tenth_complete_topic(self):
        topic = Topic.objects.get(id="free-time")
        self.assertEqual(topic.position, 9)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="free-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="free-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="free-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="free-review").count(), 7)

    def test_free_time_reading_uses_normalized_lemmas(self):
        reading = ReadingText.objects.get(id="wolna-sobota-marka")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["przyjaciółmi"]["lemma"], "przyjaciel")
        self.assertEqual(reading.glossary["jeżdżą"]["lemma"], "jeździć")
        self.assertEqual(reading.glossary["woli"]["lemma"], "woleć")

    def test_catalog_lists_first_ten_curriculum_topics(self):
        self.assertEqual(
            [topic["id"] for topic in course_topics()[:10]],
            ["introductions", "countries-languages", "family", "daily-routine", "home", "food-shopping", "city-directions", "time-meetings", "work-study", "free-time"],
        )


class HealthContentTests(TestCase):
    def test_health_is_eleventh_complete_topic(self):
        topic = Topic.objects.get(id="health")
        self.assertEqual(topic.position, 10)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="health-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="health-quiz").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="health-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="health-review").count(), 7)

    def test_health_reading_has_original_metadata_and_normalized_lemmas(self):
        reading = ReadingText.objects.get(id="ola-u-lekarza")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["czuje"]["lemma"], "czuć się")
        self.assertEqual(reading.glossary["receptę"]["lemma"], "recepta")
        self.assertEqual(reading.glossary["odpoczywa"]["lemma"], "odpoczywać")

    def test_catalog_lists_first_eleven_curriculum_topics(self):
        self.assertEqual(
            [topic["id"] for topic in course_topics()[:11]],
            [
                "introductions", "countries-languages", "family", "daily-routine",
                "home", "food-shopping", "city-directions", "time-meetings",
                "work-study", "free-time", "health",
            ],
        )


class A1FinalReviewContentTests(TestCase):
    def test_final_review_is_twelfth_complete_topic(self):
        topic = Topic.objects.get(id="a1-final-review")
        self.assertEqual(topic.position, 11)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Question.objects.filter(lesson_id="final-grammar").count(), 6)
        self.assertEqual(Question.objects.filter(lesson_id="final-quiz").count(), 12)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="final-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="final-review").count(), 8)

    def test_final_reading_is_original_and_uses_normalized_lemmas(self):
        reading = ReadingText.objects.get(id="samodzielny-dzien-leny")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["umawia"]["lemma"], "umawiać się")
        self.assertEqual(reading.glossary["sprzedawcę"]["lemma"], "sprzedawca")
        self.assertEqual(reading.glossary["załatwiła"]["lemma"], "załatwić")

    def test_a1_catalog_has_all_twelve_curriculum_topics(self):
        topics = course_topics()
        self.assertEqual(len([topic for topic in topics if topic["level"] == "A1"]), 12)
        self.assertEqual(topics[11]["id"], "a1-final-review")


class A2PastWeekendContentTests(TestCase):
    def test_past_weekend_is_first_complete_a2_topic(self):
        course = Course.objects.get(id="a2-independence")
        topic = Topic.objects.get(id="past-weekend")
        self.assertEqual(course.level, "A2")
        self.assertEqual(topic.course, course)
        self.assertEqual(topic.position, 0)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="past-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="past-quiz").count(), 8)
        self.assertEqual(
            Question.objects.filter(lesson_id="weekend-reading-check").count(), 5
        )
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="past-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="past-review").count(), 7)

    def test_a2_reading_has_original_metadata_and_normalized_lemmas(self):
        reading = ReadingText.objects.get(id="weekend-kasi-i-pawla")
        self.assertEqual(reading.level, "A2")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(
            reading.source_metadata["comprehension_lesson_id"],
            "weekend-reading-check",
        )
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["pojechała"]["lemma"], "pojechać")
        self.assertEqual(reading.glossary["poszły"]["lemma"], "pójść")
        self.assertEqual(reading.glossary["odpoczął"]["lemma"], "odpocząć")

    def test_catalog_starts_a2_with_past_weekend(self):
        a2_topics = [topic for topic in course_topics() if topic["level"] == "A2"]
        self.assertEqual(a2_topics[0]["id"], "past-weekend")
        self.assertEqual(len(a2_topics[0]["lessons"]), 5)


class A2TravelPlansContentTests(TestCase):
    def test_travel_plans_is_second_complete_a2_topic(self):
        topic = Topic.objects.get(id="travel-plans")
        self.assertEqual(topic.course_id, "a2-independence")
        self.assertEqual(topic.position, 1)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="travel-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="travel-quiz").count(), 8)
        self.assertEqual(Question.objects.filter(lesson_id="travel-reading-check").count(), 5)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="travel-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="travel-review").count(), 7)

    def test_travel_reading_is_lemma_aware_and_links_comprehension(self):
        reading = ReadingText.objects.get(id="plan-wyjazdu-do-gdanska")
        self.assertEqual(reading.level, "A2")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(reading.source_metadata["comprehension_lesson_id"], "travel-reading-check")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["pojadą"]["lemma"], "pojechać")
        self.assertEqual(reading.glossary["przesiądą"]["lemma"], "przesiąść się")
        self.assertEqual(reading.glossary["starówki"]["lemma"], "starówka")

    def test_catalog_lists_both_a2_topics_in_order(self):
        a2_topics = [topic for topic in course_topics() if topic["level"] == "A2"]
        self.assertEqual([topic["id"] for topic in a2_topics[:2]], ["past-weekend", "travel-plans"])
        self.assertEqual([len(topic["lessons"]) for topic in a2_topics[:2]], [5, 5])


class A2HousingServicesContentTests(TestCase):
    def test_housing_services_is_third_complete_a2_topic(self):
        topic = Topic.objects.get(id="housing-services")
        self.assertEqual(topic.course_id, "a2-independence")
        self.assertEqual(topic.position, 2)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="housing-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="housing-quiz").count(), 8)
        self.assertEqual(Question.objects.filter(lesson_id="housing-reading-check").count(), 5)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="housing-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="housing-review").count(), 7)

    def test_housing_reading_is_lemma_aware_and_links_comprehension(self):
        reading = ReadingText.objects.get(id="usterka-w-mieszkaniu")
        self.assertEqual(reading.level, "A2")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(reading.source_metadata["comprehension_lesson_id"], "housing-reading-check")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["kaloryferów"]["lemma"], "kaloryfer")
        self.assertEqual(reading.glossary["usterki"]["lemma"], "usterka")
        self.assertEqual(reading.glossary["spóźni"]["lemma"], "spóźnić się")

    def test_catalog_lists_three_a2_topics_in_order(self):
        a2_topics = [topic for topic in course_topics() if topic["level"] == "A2"]
        self.assertEqual(
            [topic["id"] for topic in a2_topics[:3]],
            ["past-weekend", "travel-plans", "housing-services"],
        )
        self.assertEqual([len(topic["lessons"]) for topic in a2_topics[:3]], [5, 5, 5])


class A2WorkContentTests(TestCase):
    def test_work_is_fourth_complete_a2_topic(self):
        topic = Topic.objects.get(id="a2-work")
        self.assertEqual(topic.position, 3)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="a2work-grammar").count(), 5)
        self.assertEqual(Question.objects.filter(lesson_id="a2work-quiz").count(), 8)
        self.assertEqual(Question.objects.filter(lesson_id="a2work-reading-check").count(), 5)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="a2work-words").count(), 8)
        self.assertEqual(LessonFlashcard.objects.filter(lesson_id="a2work-review").count(), 7)

    def test_work_reading_is_original_and_lemma_aware(self):
        reading = ReadingText.objects.get(id="pierwszy-tydzien-mai")
        self.assertEqual(reading.source_metadata["origin"], "original")
        self.assertEqual(reading.source_metadata["comprehension_lesson_id"], "a2work-reading-check")
        self.assertEqual(len(reading.paragraphs), 3)
        self.assertEqual(reading.glossary["obsłudze"]["lemma"], "obsługa")
        self.assertEqual(reading.glossary["wykonała"]["lemma"], "wykonać")

    def test_catalog_lists_four_a2_topics(self):
        topics = [topic for topic in course_topics() if topic["level"] == "A2"]
        self.assertEqual([topic["id"] for topic in topics], ["past-weekend", "travel-plans", "housing-services", "a2-work"])
