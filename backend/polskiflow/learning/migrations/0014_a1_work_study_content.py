from django.db import migrations

SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-27"}
CARDS = (
    ("work-praca", "praca", "работа", "Mam nową pracę."),
    ("work-szkola", "szkoła", "школа", "Szkoła jest blisko domu."),
    ("work-biuro", "biuro", "офис", "Pracuję w małym biurze."),
    ("work-firma", "firma", "компания", "Ta firma jest w centrum."),
    ("work-student", "student", "студент", "Jestem studentem."),
    ("work-nauczyciel", "nauczyciel", "учитель", "Nauczyciel prowadzi lekcję."),
    ("work-pracownik", "pracownik", "сотрудник", "Pracownik zaczyna o ósmej."),
    ("work-uczyc-sie", "uczyć się", "учиться", "Uczę się języka polskiego."),
    ("work-pracowac", "pracować", "работать", "Pracuję od poniedziałku do piątku."),
    ("work-studiowac", "studiować", "учиться в вузе", "Studiuję informatykę."),
    ("work-zaczynac", "zaczynać", "начинать", "Zaczynam pracę o dziewiątej."),
    ("work-konczyc", "kończyć", "заканчивать", "Kończę kurs o szóstej."),
    ("work-zadanie", "zadanie", "задание", "Mam dziś ważne zadanie."),
    ("work-moc", "móc", "мочь", "Mogę pracować w domu."),
    ("work-music", "musieć", "быть должным", "Muszę wysłać wiadomość."),
)
GRAMMAR = (
    ("Dzisiaj ___ pracować w domu.", ["mogę", "może", "możesz"], 0, "Для ja форма глагола móc — mogę."),
    ("Anna ___ skończyć zadanie.", ["muszę", "musisz", "musi"], 2, "Для ona форма musieć — musi; после неё употребляем инфинитив."),
    ("Czy ___ mi pomóc?", ["możesz", "mogę", "może"], 0, "К одному собеседнику обращаемся: Czy możesz…?"),
    ("My ___ uczyć się codziennie.", ["musimy", "musicie", "musi"], 0, "Для my форма musieć — musimy."),
    ("Что ставим после mogę / muszę?", ["инфинитив", "прошедшее время", "существительное только"], 0, "Модальный глагол соединяется с инфинитивом: mogę pracować, muszę skończyć."),
)
QUIZ = (
    ("Что означает biuro?", ["офис", "школа", "задание"], 0, "Biuro — офис."),
    ("Ja ___ pracować jutro.", ["może", "mogę", "możesz"], 1, "С ja употребляем mogę."),
    ("Paweł ___ wysłać email.", ["muszę", "musisz", "musi"], 2, "Для on форма — musi."),
    ("Выберите базовую форму «учиться».", ["uczyć się", "uczę się", "uczy"], 0, "Словарная форма — uczyć się."),
    ("Как сказать «я работаю в офисе»?", ["Pracuję w biurze.", "Praca jestem biuro.", "Pracować na biuro."], 0, "Естественная конструкция: pracuję w biurze."),
    ("My ___ o ósmej.", ["zaczynamy", "zaczyna", "zaczynasz"], 0, "Для my: zaczynamy."),
    ("Что означает zadanie?", ["компания", "занятие", "задание"], 2, "Zadanie — задание или задача."),
    ("Выберите естественное предложение.", ["Muszę skończyć pracę.", "Muszę kończę pracę.", "Musi ja praca."], 0, "После muszę нужен инфинитив: skończyć."),
)
READING = {
    "id": "pierwszy-dzien-w-pracy", "title": "Pierwszy dzień w pracy", "description": "Касия начинает новую работу и продолжает учить польский", "level": "A1", "minutes": 4, "emoji": "💼", "position": 8,
    "paragraphs": [
        "Kasia ma nową pracę w małej firmie w centrum. Pracuje w biurze od poniedziałku do piątku. Zaczyna o ósmej, ale pierwszego dnia przychodzi dziesięć minut wcześniej.",
        "Kierownik pokazuje jej biurko i przedstawia innych pracowników. Kasia musi przeczytać krótką instrukcję i napisać pierwszą wiadomość. Może pytać koleżankę, kiedy czegoś nie rozumie.",
        "Po pracy Kasia jedzie do szkoły językowej. Uczy się polskiego dwa razy w tygodniu. Lekcja kończy się o siódmej. Kasia jest zmęczona, ale zadowolona: może pracować i studiować w tym samym mieście.",
    ],
    "glossary": {
        "pracuje": {"lemma": "pracować", "translation": "работать", "part_of_speech": "глагол"},
        "przychodzi": {"lemma": "przychodzić", "translation": "приходить", "part_of_speech": "глагол"},
        "kierownik": {"lemma": "kierownik", "translation": "руководитель", "part_of_speech": "существительное"},
        "pokazuje": {"lemma": "pokazywać", "translation": "показывать", "part_of_speech": "глагол"},
        "biurko": {"lemma": "biurko", "translation": "письменный стол", "part_of_speech": "существительное"},
        "przedstawia": {"lemma": "przedstawiać", "translation": "представлять", "part_of_speech": "глагол"},
        "pracowników": {"lemma": "pracownik", "translation": "сотрудник", "part_of_speech": "существительное"},
        "przeczytać": {"lemma": "przeczytać", "translation": "прочитать", "part_of_speech": "глагол"},
        "wiadomość": {"lemma": "wiadomość", "translation": "сообщение", "part_of_speech": "существительное"},
        "pytać": {"lemma": "pytać", "translation": "спрашивать", "part_of_speech": "глагол"},
        "rozumie": {"lemma": "rozumieć", "translation": "понимать", "part_of_speech": "глагол"},
        "zmęczona": {"lemma": "zmęczony", "translation": "уставший", "part_of_speech": "прилагательное"},
        "zadowolona": {"lemma": "zadowolony", "translation": "довольный", "part_of_speech": "прилагательное"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite": return
    Course = apps.get_model("learning", "Course"); Topic = apps.get_model("learning", "Topic"); Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard"); Link = apps.get_model("learning", "LessonFlashcard"); Question = apps.get_model("learning", "Question"); ReadingText = apps.get_model("learning", "ReadingText")
    course = Course.objects.get(id="a1-foundations")
    Topic.objects.filter(course=course, position__gte=8).update(position=9)
    topic, _ = Topic.objects.update_or_create(id="work-study", defaults={"course": course, "title": "Работа и учёба", "description": "Рассказываем о занятии, месте и простых обязанностях", "emoji": "💼", "position": 8, "is_active": True})
    rows = (("work-words", "words", "Praca i szkoła", "Работа и учёба", "8 карточек · A1", "Назови места и людей", 7, "💼"), ("work-grammar", "grammar", "Mogę i muszę", "Возможности и обязанности", "5 заданий · A1", "Используй móc и musieć с инфинитивом", 8, "✏️"), ("work-review", "review", "Co robisz?", "Задачи дня", "7 карточек · A1", "Расскажи о работе и занятиях", 6, "🔄"), ("work-quiz", "quiz", "Quiz: praca", "Проверка темы", "8 вопросов · A1", "Проверь занятия и модальные глаголы", 5, "🎯"))
    made = {}
    for position, row in enumerate(rows, 32):
        id_, kind, title, plan, subtitle, desc, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": desc, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["work-grammar"]; grammar.theory_title = "Mogę pracować — muszę skończyć"
    grammar.theory_sections = [["Возможность", "Móc + инфинитив: mogę pracować, możesz pomóc, on/ona może przyjść."], ["Обязанность", "Musieć + инфинитив: muszę skończyć, musisz napisać, on/ona musi przeczytać."], ["Множественное число", "My możemy / musimy, wy możecie / musicie. После модального глагола форма действия не меняется."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 120):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE}); cards.append(card)
    for lesson_id, chosen in (("work-words", cards[:8]), ("work-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen): Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("work-grammar", GRAMMAR), ("work-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions): Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": SOURCE})


class Migration(migrations.Migration):
    dependencies = [("learning", "0013_a1_time_meetings_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
