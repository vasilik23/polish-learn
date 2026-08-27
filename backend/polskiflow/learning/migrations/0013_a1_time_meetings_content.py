from django.db import migrations

SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-27"}
CARDS = (
    ("time-godzina", "godzina", "час; время", "Która jest godzina?"),
    ("time-minuta", "minuta", "минута", "Spotkanie zaczyna się za pięć minut."),
    ("time-poniedzialek", "poniedziałek", "понедельник", "W poniedziałek pracuję."),
    ("time-wtorek", "wtorek", "вторник", "We wtorek mam kurs."),
    ("time-sroda", "środa", "среда", "W środę spotykam się z Olą."),
    ("time-czwartek", "czwartek", "четверг", "W czwartek jestem w domu."),
    ("time-piatek", "piątek", "пятница", "W piątek idziemy do kina."),
    ("time-weekend", "weekend", "выходные", "W weekend mam czas."),
    ("time-dzisiaj", "dzisiaj", "сегодня", "Dzisiaj jest środa."),
    ("time-jutro", "jutro", "завтра", "Jutro mam spotkanie."),
    ("time-rano", "rano", "утром", "Rano piję kawę."),
    ("time-wieczorem", "wieczorem", "вечером", "Wieczorem czytam książkę."),
    ("time-spotkanie", "spotkanie", "встреча", "Spotkanie jest o szóstej."),
    ("time-o-ktorej", "o której?", "в котором часу?", "O której zaczynamy?"),
    ("time-pasowac", "pasować", "подходить; быть удобным", "Czy pasuje ci piątek?"),
)
GRAMMAR = (
    ("Spotkanie jest ___ szóstej.", ["w", "o", "na"], 1, "Точное время вводим предлогом o: o szóstej."),
    ("Kurs jest ___ poniedziałek.", ["o", "w", "na"], 1, "С днями недели употребляем w: w poniedziałek."),
    ("Spotykamy się ___ wtorek.", ["we", "o", "do"], 0, "Перед wtorek для удобства произношения употребляем we: we wtorek."),
    ("Как спросить время встречи?", ["Który spotkanie?", "O której się spotykamy?", "Gdzie godzina?"], 1, "O której się spotykamy? — естественный вопрос «Во сколько встречаемся?»."),
    ("Czy pasuje ci piątek?", ["Тебе подходит пятница?", "Ты работаешь в пятницу?", "Сегодня пятница?"], 0, "Pasować в договорённостях означает «подходить, быть удобным»."),
)
QUIZ = (
    ("Что означает jutro?", ["сегодня", "завтра", "утром"], 1, "Jutro — завтра."),
    ("Film zaczyna się ___ ósmej.", ["o", "w", "we"], 0, "Перед точным временем используем o."),
    ("___ wtorek mam lekcję.", ["O", "We", "Na"], 1, "Говорим we wtorek."),
    ("Как сказать «в среду»?", ["o środzie", "w środę", "na środa"], 1, "Устойчивое сочетание — w środę."),
    ("O ___ zaczynamy?", ["której", "który", "która"], 0, "О времени спрашиваем o której?"),
    ("Что означает spotkanie?", ["расписание", "встреча", "опоздание"], 1, "Spotkanie — встреча."),
    ("Выберите естественный ответ на предложение встретиться.", ["Tak, pasuje mi.", "Tak, jestem godzina.", "Tak, spotkanie robi."], 0, "Pasuje mi — «мне подходит»."),
    ("Dzisiaj jest czwartek, a ___ piątek.", ["rano", "jutro", "wieczorem"], 1, "Если сегодня четверг, завтра — пятница: jutro."),
)
READING = {
    "id": "spotkanie-w-piatek", "title": "Spotkanie w piątek", "description": "Марта и Павел договариваются встретиться после работы", "level": "A1", "minutes": 4, "emoji": "🕒", "position": 7,
    "paragraphs": [
        "W środę Marta pisze do Pawła. Chce spotkać się z nim w tym tygodniu. Pyta: „Czy pasuje ci czwartek wieczorem?”. Paweł odpowiada, że w czwartek ma kurs języka polskiego.",
        "Paweł proponuje piątek. Marta ma czas, więc pyta: „O której się spotykamy?”. Ustalają spotkanie o szóstej. Chcą wypić kawę w małej kawiarni obok parku.",
        "W piątek Marta kończy pracę o piątej. Jedzie autobusem do centrum i przychodzi pięć minut wcześniej. Paweł już czeka przy wejściu. Oboje cieszą się, że zaczynają weekend razem.",
    ],
    "glossary": {
        "pisze": {"lemma": "pisać", "translation": "писать", "part_of_speech": "глагол"},
        "spotkać": {"lemma": "spotkać się", "translation": "встретиться", "part_of_speech": "глагол"},
        "tygodniu": {"lemma": "tydzień", "translation": "неделя", "part_of_speech": "существительное"},
        "odpowiada": {"lemma": "odpowiadać", "translation": "отвечать", "part_of_speech": "глагол"},
        "proponuje": {"lemma": "proponować", "translation": "предлагать", "part_of_speech": "глагол"},
        "ustalają": {"lemma": "ustalać", "translation": "договариваться; определять", "part_of_speech": "глагол"},
        "wypić": {"lemma": "wypić", "translation": "выпить", "part_of_speech": "глагол"},
        "kończy": {"lemma": "kończyć", "translation": "заканчивать", "part_of_speech": "глагол"},
        "jedzie": {"lemma": "jechać", "translation": "ехать", "part_of_speech": "глагол"},
        "przychodzi": {"lemma": "przychodzić", "translation": "приходить", "part_of_speech": "глагол"},
        "wcześniej": {"lemma": "wcześnie", "translation": "раньше", "part_of_speech": "наречие"},
        "czeka": {"lemma": "czekać", "translation": "ждать", "part_of_speech": "глагол"},
        "cieszą": {"lemma": "cieszyć się", "translation": "радоваться", "part_of_speech": "глагол"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course = apps.get_model("learning", "Course"); Topic = apps.get_model("learning", "Topic"); Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard"); Link = apps.get_model("learning", "LessonFlashcard"); Question = apps.get_model("learning", "Question"); ReadingText = apps.get_model("learning", "ReadingText")
    course = Course.objects.get(id="a1-foundations")
    Topic.objects.filter(course=course, position__gte=7).update(position=8)
    topic, _ = Topic.objects.update_or_create(id="time-meetings", defaults={"course": course, "title": "Время и встречи", "description": "Называем время и дни недели, договариваемся о встрече", "emoji": "🕒", "position": 7, "is_active": True})
    rows = (("time-words", "words", "Dni i godziny", "Дни и время", "8 карточек · A1", "Назови дни и единицы времени", 7, "📅"), ("time-grammar", "grammar", "O której?", "Договариваемся", "5 заданий · A1", "Используй o, w и we со временем", 8, "✏️"), ("time-review", "review", "Kiedy się spotykamy?", "Планы на неделю", "7 карточек · A1", "Предложи время встречи", 6, "🔄"), ("time-quiz", "quiz", "Quiz: czas", "Проверка темы", "8 вопросов · A1", "Проверь время, дни и договорённости", 5, "🎯"))
    made = {}
    for position, row in enumerate(rows, 28):
        id_, kind, title, plan, subtitle, desc, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": desc, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["time-grammar"]
    grammar.theory_title = "O szóstej — w poniedziałek — we wtorek"
    grammar.theory_sections = [["Точное время", "Перед часом используем o: o szóstej, o ósmej, o dziesiątej."], ["Дни недели", "W poniedziałek, w środę, w piątek, но we wtorek. Для выходных: w weekend."], ["Договорённость", "Спрашиваем: O której się spotykamy? Czy pasuje ci piątek? Отвечаем: Tak, pasuje mi."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 105):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE}); cards.append(card)
    for lesson_id, chosen in (("time-words", cards[:8]), ("time-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen): Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("time-grammar", GRAMMAR), ("time-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions): Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": SOURCE})


class Migration(migrations.Migration):
    dependencies = [("learning", "0012_a1_city_directions_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
