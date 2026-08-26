from django.db import migrations, models


SOURCE_METADATA = {
    "origin": "original",
    "created_for": "PolskiFlow",
    "verified_at": "2026-08-26",
}


FLASHCARDS = (
    ("czesc", "cześć", "привет / пока", "Cześć, mam na imię Anna."),
    ("dzien-dobry", "dzień dobry", "добрый день", "Dzień dobry, pani Mario!"),
    ("do-widzenia", "do widzenia", "до свидания", "Do widzenia, do jutra!"),
    ("mam-na-imie", "mam na imię", "меня зовут", "Mam na imię Oleg."),
    ("jak-masz-na-imie", "jak masz na imię?", "как тебя зовут?", "Cześć! Jak masz na imię?"),
    ("milo-mi", "miło mi", "приятно познакомиться", "Jestem Ewa. Miło mi!"),
    ("jak-sie-masz", "jak się masz?", "как ты?", "Cześć, Piotr! Jak się masz?"),
    ("dobrze", "dobrze", "хорошо", "Dobrze, dziękuję."),
    ("jestem", "jestem", "я являюсь / я есть", "Jestem Anna."),
    ("jestes", "jesteś", "ты являешься / ты есть", "Jesteś z Polski?"),
    ("pan", "pan", "господин / Вы", "Czy pan jest nauczycielem?"),
    ("pani", "pani", "госпожа / Вы", "Czy pani jest z Warszawy?"),
    ("skad-jestes", "skąd jesteś?", "откуда ты?", "Skąd jesteś? Jestem z Ukrainy."),
    ("z-polski", "z Polski", "из Польши", "Marek jest z Polski."),
    ("tez", "też", "тоже", "Ja też jestem na kursie."),
)


GRAMMAR_QUESTIONS = (
    ("Как сказать «Я Анна»?", ["Jesteś Anna.", "Jestem Anna.", "Jest Anna."], 1, "Для «я» используется форма jestem: Jestem Anna."),
    ("Выберите форму для «ты»: Ty ___ z Polski.", ["jestem", "jesteś", "jest"], 1, "С местоимением ty используется jesteś."),
    ("Как вежливо спросить женщину: «Вы из Варшавы?»", ["Czy pani jest z Warszawy?", "Czy jesteś pan z Warszawy?", "Jestem z Warszawy?"], 0, "Pani — вежливое обращение к женщине; используется форма jest."),
    ("My ___ na kursie. Вставьте форму być.", ["są", "jesteście", "jesteśmy"], 2, "My jesteśmy — «мы являемся / мы находимся»."),
    ("Oni ___ z Polski. Вставьте форму być.", ["są", "jest", "jesteś"], 0, "Oni są — «они являются»."),
)


QUIZ_QUESTIONS = (
    ("Как неформально поздороваться?", ["Do widzenia", "Cześć", "Dziękuję", "Przepraszam"], 1, "Cześć — неформальное приветствие; оно также может означать «пока»."),
    ("Что значит «Mam na imię Lena»?", ["Мне нравится Лена", "Меня зовут Лена", "Я вижу Лену", "Это Лена"], 1, "Mam na imię… — стандартная конструкция «Меня зовут…»."),
    ("Как спросить «Как тебя зовут?»", ["Skąd jesteś?", "Jak się masz?", "Jak masz na imię?", "Kim jesteś?"], 2, "Jak masz na imię? — «Как тебя зовут?»"),
    ("Выберите ответ на «Jak się masz?»", ["Dobrze, dziękuję.", "Mam na imię.", "Do widzenia?", "Z Polski."], 0, "Dobrze, dziękuję — естественный короткий ответ: «Хорошо, спасибо»."),
    ("Как сказать «Я из Украины»?", ["Jesteś z Ukrainy.", "Jest z Ukrainy.", "Jestem z Ukrainy.", "Są z Ukrainy."], 2, "Для «я» нужна форма jestem: Jestem z Ukrainy."),
    ("Что означает «Miło mi» при знакомстве?", ["Мне холодно", "Очень хорошо", "Приятно познакомиться", "До завтра"], 2, "Miło mi — краткое «Приятно познакомиться»."),
    ("Как вежливо обратиться к незнакомой женщине?", ["pan", "pani", "ty", "oni"], 1, "Pani — вежливое обращение к женщине."),
    ("Выберите правильное про Марека: Marek ___ z Polski.", ["jestem", "jesteś", "jest", "są"], 2, "Для он/она/оно используется форма jest."),
)


READING = {
    "id": "pierwszy-dzien-na-kursie",
    "title": "Pierwszy dzień na kursie",
    "description": "Анна знакомится с группой на первом уроке польского",
    "level": "A1",
    "minutes": 4,
    "emoji": "👋",
    "paragraphs": [
        "To jest pierwszy dzień Anny na kursie języka polskiego. Anna wchodzi do sali i mówi: Dzień dobry! Nauczyciel uśmiecha się i odpowiada: Dzień dobry, zapraszam.",
        "Obok Anny siedzi nowy kolega. Mam na imię Marek — mówi. A jak ty masz na imię? Jestem Anna. Miło mi! Marek jest z Polski, a Anna jest z Ukrainy.",
        "Na początku lekcji każdy krótko się przedstawia. Potem nauczyciel pyta: Jak się masz? Anna odpowiada: Dobrze, dziękuję. Po lekcji Anna mówi nowym znajomym: Do widzenia! To był dobry początek.",
    ],
    "glossary": {
        "pierwszy": "первый", "dzień": "день", "kursie": "курсе",
        "wchodzi": "входит", "sali": "аудитории", "mówi": "говорит",
        "nauczyciel": "преподаватель", "uśmiecha": "улыбается",
        "odpowiada": "отвечает", "zapraszam": "прошу / проходите",
        "obok": "рядом", "siedzi": "сидит", "nowy": "новый",
        "kolega": "знакомый / одногруппник", "początku": "начале",
        "lekcji": "урока", "każdy": "каждый", "krótko": "кратко",
        "przedstawia": "представляется", "potem": "потом",
        "pyta": "спрашивает", "znajomym": "знакомым", "początek": "начало",
    },
    "position": 0,
}


def seed_a1_introductions(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return

    Course = apps.get_model("learning", "Course")
    Topic = apps.get_model("learning", "Topic")
    Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard")
    LessonFlashcard = apps.get_model("learning", "LessonFlashcard")
    Question = apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")

    course = Course.objects.get(id="a1-foundations")
    Topic.objects.filter(course=course, position=0).update(position=1)
    topic, _ = Topic.objects.update_or_create(
        id="introductions",
        defaults={
            "course": course,
            "title": "Знакомство",
            "description": "Приветствия, представление и первые вопросы о человеке",
            "emoji": "👋",
            "position": 0,
            "is_active": True,
        },
    )

    lesson_updates = {
        "words": ("Pierwsze słowa", "Знакомство: слова", "8 фраз · A1", "Поздоровайся и представься", 6, "👋"),
        "grammar": ("Czasownik być", "Грамматика", "Глагол być", "Научись говорить, кто ты и откуда", 8, "✏️"),
        "review": ("Przedstaw się", "Фразы знакомства", "7 карточек · A1", "Закрепи вопросы и вежливые обращения", 6, "🔄"),
        "quiz": ("Quiz: poznajmy się", "Мини-тест", "8 вопросов · A1", "Проверь тему «Знакомство»", 5, "🎯"),
    }
    for lesson_id, values in lesson_updates.items():
        title, plan_title, subtitle, description, minutes, emoji = values
        lesson = Lesson.objects.get(id=lesson_id)
        lesson.title = title
        lesson.plan_title = plan_title
        lesson.subtitle = subtitle
        lesson.description = description
        lesson.minutes = minutes
        lesson.emoji = emoji
        lesson.topic = topic
        lesson.source_metadata = SOURCE_METADATA
        if lesson_id == "grammar":
            lesson.theory_title = "Być — быть"
            lesson.theory_sections = [
                ["Формы настоящего времени", "ja jestem · ty jesteś · on/ona/ono jest · my jesteśmy · wy jesteście · oni/one są"],
                ["Представляемся", "Jestem Anna. — Я Анна. Jestem z Polski. — Я из Польши."],
                ["Вежливое обращение", "С pan и pani используется третье лицо: Czy pan jest z Polski? Czy pani jest nauczycielką?"],
            ]
        lesson.save()

    cards = []
    for position, (card_id, polish, translation, example) in enumerate(FLASHCARDS):
        card, _ = Flashcard.objects.update_or_create(
            id=card_id,
            defaults={
                "polish": polish,
                "translation": translation,
                "example": example,
                "position": position,
                "is_active": True,
                "source_metadata": SOURCE_METADATA,
            },
        )
        cards.append(card)

    LessonFlashcard.objects.filter(lesson_id__in=("words", "review")).delete()
    for position, card in enumerate(cards[:8]):
        LessonFlashcard.objects.create(lesson_id="words", flashcard=card, position=position)
    for position, card in enumerate(cards[8:]):
        LessonFlashcard.objects.create(lesson_id="review", flashcard=card, position=position)

    Question.objects.filter(lesson_id__in=("grammar", "quiz")).delete()
    for lesson_id, questions in (("grammar", GRAMMAR_QUESTIONS), ("quiz", QUIZ_QUESTIONS)):
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(
                lesson_id=lesson_id,
                prompt=prompt,
                options=options,
                correct=correct,
                explanation=explanation,
                position=position,
            )

    reading_defaults = {key: value for key, value in READING.items() if key != "id"}
    ReadingText.objects.update_or_create(
        id=READING["id"],
        defaults={
            **reading_defaults,
            "topic": topic,
            "source_metadata": SOURCE_METADATA,
        },
    )


class Migration(migrations.Migration):
    dependencies = [("learning", "0005_reading_library_dictionary")]
    operations = [
        migrations.AddField(
            model_name="flashcard",
            name="source_metadata",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="lesson",
            name="source_metadata",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="readingtext",
            name="source_metadata",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.RunPython(seed_a1_introductions, migrations.RunPython.noop),
    ]
