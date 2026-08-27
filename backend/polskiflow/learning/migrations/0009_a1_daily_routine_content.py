from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-27"}

CARDS = (
    ("wstawac", "wstawać", "вставать", "Wstaję o siódmej."),
    ("budzic-sie", "budzić się", "просыпаться", "Budzę się wcześnie."),
    ("myc-sie", "myć się", "мыться", "Rano myję się i ubieram."),
    ("ubierac-sie", "ubierać się", "одеваться", "Ubieram się szybko."),
    ("jesc-sniadanie", "jeść śniadanie", "завтракать", "Jem śniadanie w domu."),
    ("isc-do-pracy", "iść do pracy", "идти на работу", "O ósmej idę do pracy."),
    ("zaczynac", "zaczynać", "начинать", "Zaczynam pracę o dziewiątej."),
    ("konczyc", "kończyć", "заканчивать", "Kończę pracę o siedemnastej."),
    ("wracac", "wracać", "возвращаться", "Wieczorem wracam do domu."),
    ("gotowac", "gotować", "готовить", "Często gotuję kolację."),
    ("odpoczywac", "odpoczywać", "отдыхать", "Po pracy odpoczywam."),
    ("czytac", "czytać", "читать", "Czasem czytam książkę."),
    ("klasc-sie-spac", "kłaść się spać", "ложиться спать", "Kładę się spać o jedenastej."),
    ("codziennie", "codziennie", "каждый день", "Codziennie piję rano kawę."),
    ("czasem", "czasem", "иногда", "Czasem jadę do pracy rowerem."),
)

GRAMMAR = (
    ("Ja ___ o siódmej. Выберите форму wstawać.", ["wstaję", "wstajesz", "wstaje"], 0, "Для ja употребляется форма wstaję."),
    ("Ty ___ śniadanie w domu. Выберите форму jeść.", ["jem", "jesz", "je"], 1, "Для ty глагол jeść имеет форму jesz."),
    ("Ona ___ pracę o dziewiątej. Выберите форму zaczynać.", ["zaczynam", "zaczynasz", "zaczyna"], 2, "Для ona используется форма zaczyna."),
    ("Как сказать «Я часто читаю вечером»?", ["Często czytam wieczorem.", "Czytać często wieczór.", "Wieczorem często czytasz."], 0, "Наречие często можно поставить перед глаголом."),
    ("Выберите естественную фразу.", ["Nigdy nie piję kawy wieczorem.", "Nigdy piję nie kawę.", "Nie nigdy kawa piję."], 0, "С nigdy отрицание оформляется конструкцией nigdy nie + глагол."),
)

QUIZ = (
    ("Что означает wstawać?", ["вставать", "работать", "возвращаться"], 0, "Wstawać — вставать."),
    ("Выберите «Я завтракаю дома».", ["Jem śniadanie w domu.", "Gotuję dom rano.", "Idę śniadanie."], 0, "Jeść śniadanie — завтракать."),
    ("My ___ do domu o szóstej. Форма wracać.", ["wracam", "wracacie", "wracamy"], 2, "Для my используется окончание -my: wracamy."),
    ("Как сказать «иногда»?", ["zawsze", "czasem", "codziennie"], 1, "Czasem означает «иногда»."),
    ("Что происходит раньше?", ["kładę się spać", "budzę się", "wracam wieczorem"], 1, "Сначала человек просыпается: budzę się."),
    ("Выберите правильную фразу с nigdy.", ["Nigdy nie pracuję w niedzielę.", "Nigdy pracuję w niedzielę.", "Nie pracować nigdy niedziela."], 0, "После nigdy используется nie перед личной формой глагола."),
    ("O której zaczynasz pracę? — ___", ["O dziewiątej.", "Codziennie.", "Do domu."], 0, "На вопрос o której? отвечают временем с o."),
    ("Выберите логичный порядок.", ["wstaję → jem śniadanie → idę do pracy", "idę spać → wstaję → jem kolację", "wracam → budzę się → zaczynam dzień"], 0, "Обычный утренний порядок: встать, позавтракать, пойти на работу."),
)

READING = {
    "id": "zwykly-dzien-oli", "title": "Zwykły dzień Oli", "description": "Оля рассказывает о своём обычном дне",
    "level": "A1", "minutes": 4, "emoji": "☀️", "position": 3,
    "paragraphs": [
        "Ola budzi się o szóstej trzydzieści, ale wstaje o siódmej. Najpierw myje się i ubiera. Potem je śniadanie. Zwykle pije herbatę i je kanapkę z serem.",
        "O ósmej Ola idzie do pracy. Pracę zaczyna o dziewiątej. W południe je obiad z koleżanką. Kończy pracę o siedemnastej i wraca autobusem do domu.",
        "Wieczorem Ola gotuje kolację, a potem odpoczywa. Czasem czyta książkę, a czasem rozmawia z rodziną. Nigdy nie pracuje w nocy. O jedenastej kładzie się spać.",
    ],
    "glossary": {
        "budzi": {"lemma": "budzić się", "translation": "просыпаться", "part_of_speech": "глагол"},
        "najpierw": {"lemma": "najpierw", "translation": "сначала", "part_of_speech": "наречие"},
        "myje": {"lemma": "myć się", "translation": "мыться", "part_of_speech": "глагол"},
        "ubiera": {"lemma": "ubierać się", "translation": "одеваться", "part_of_speech": "глагол"},
        "zwykle": {"lemma": "zwykle", "translation": "обычно", "part_of_speech": "наречие"},
        "kanapkę": {"lemma": "kanapka", "translation": "бутерброд", "part_of_speech": "существительное"},
        "serem": {"lemma": "ser", "translation": "сыр", "part_of_speech": "существительное"},
        "południe": {"lemma": "południe", "translation": "полдень", "part_of_speech": "существительное"},
        "koleżanką": {"lemma": "koleżanka", "translation": "коллега", "part_of_speech": "существительное"},
        "kończy": {"lemma": "kończyć", "translation": "заканчивать", "part_of_speech": "глагол"},
        "wraca": {"lemma": "wracać", "translation": "возвращаться", "part_of_speech": "глагол"},
        "gotuje": {"lemma": "gotować", "translation": "готовить", "part_of_speech": "глагол"},
        "odpoczywa": {"lemma": "odpoczywać", "translation": "отдыхать", "part_of_speech": "глагол"},
        "rozmawia": {"lemma": "rozmawiać", "translation": "разговаривать", "part_of_speech": "глагол"},
        "kładzie": {"lemma": "kłaść się", "translation": "ложиться", "part_of_speech": "глагол"},
    },
}

LEMMA_UPDATES = {
    "pierwszy-dzien-na-kursie": {
        "przedstawia": ("przedstawiać", "представляться", "глагол"),
        "mówi": ("mówić", "говорить", "глагол"),
        "pochodzi": ("pochodzić", "быть родом", "глагол"),
        "mieszka": ("mieszkać", "жить", "глагол"),
    },
    "rozmowa-w-miedzynarodowej-grupie": {
        "międzynarodowa": ("międzynarodowy", "международный", "прилагательное"),
        "pochodzi": ("pochodzić", "быть родом", "глагол"),
        "rozmawia": ("rozmawiać", "разговаривать", "глагол"),
        "pomaga": ("pomagać", "помогать", "глагол"),
        "każdego": ("każdy", "каждый", "местоимение"),
        "jakimi": ("jaki", "какой", "местоимение"),
    },
    "niedziela-u-babci": {
        "odwiedza": ("odwiedzać", "навещать", "глагол"),
        "przyjeżdżają": ("przyjeżdżać", "приезжать", "глагол"),
        "pracuje": ("pracować", "работать", "глагол"),
        "interesuje": ("interesować się", "интересоваться", "глагол"),
        "stole": ("stół", "стол", "существительное"),
        "tygodniu": ("tydzień", "неделя", "существительное"),
        "pokazuje": ("pokazywać", "показывать", "глагол"),
        "zdjęcia": ("zdjęcie", "фотография", "существительное"),
        "dwojgiem": ("dwoje", "двое", "числительное"),
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course = apps.get_model("learning", "Course")
    Topic = apps.get_model("learning", "Topic")
    Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard")
    Link = apps.get_model("learning", "LessonFlashcard")
    Question = apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    course = Course.objects.get(id="a1-foundations")
    Topic.objects.filter(course=course, position__gte=3).update(position=4)
    topic, _ = Topic.objects.update_or_create(id="daily-routine", defaults={"course": course, "title": "Мой день", "description": "Описываем распорядок дня и частые действия", "emoji": "☀️", "position": 3, "is_active": True})
    rows = (
        ("daily-routine-words", "words", "Mój dzień", "Распорядок дня", "8 карточек · A1", "Назови главные действия своего дня", 7, "☀️"),
        ("daily-routine-grammar", "grammar", "Co robisz codziennie?", "Настоящее время", "5 заданий · A1", "Используй личные формы и наречия частоты", 8, "✏️"),
        ("daily-routine-review", "review", "Rano i wieczorem", "Утро и вечер", "7 карточек · A1", "Закрепи последовательность ежедневных действий", 6, "🔄"),
        ("daily-routine-quiz", "quiz", "Quiz: mój dzień", "Проверка темы", "8 вопросов · A1", "Проверь глаголы, порядок дня и частотность", 5, "🎯"),
    )
    made = {}
    for position, (id_, kind, title, plan, subtitle, desc, minutes, emoji) in enumerate(rows, 12):
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": desc, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["daily-routine-grammar"]
    grammar.theory_title = "Настоящее время в распорядке дня"
    grammar.theory_sections = [["Личные формы", "Глагол меняется по лицам: ja wstaję, ty wstajesz, on/ona wstaje; ja czytam, ty czytasz, ona czyta."], ["Частотность", "zawsze — всегда, często — часто, czasem — иногда, nigdy — никогда. С nigdy говорим: nigdy nie pracuję."], ["Время и порядок", "O której? — O siódmej. Сначала: najpierw, затем: potem, вечером: wieczorem."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": 45 + position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("daily-routine-words", cards[:8]), ("daily-routine-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("daily-routine-grammar", GRAMMAR), ("daily-routine-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{k: v for k, v in READING.items() if k != "id"}, "topic": topic, "source_metadata": SOURCE})
    for text_id, updates in LEMMA_UPDATES.items():
        existing = ReadingText.objects.filter(id=text_id).first()
        if not existing or not isinstance(existing.glossary, dict):
            continue
        glossary = dict(existing.glossary)
        for surface, (lemma, translation, part_of_speech) in updates.items():
            if surface in glossary:
                glossary[surface] = {"lemma": lemma, "translation": translation, "part_of_speech": part_of_speech}
        existing.glossary = glossary
        existing.save(update_fields=("glossary",))


class Migration(migrations.Migration):
    dependencies = [("learning", "0008_a1_family_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
