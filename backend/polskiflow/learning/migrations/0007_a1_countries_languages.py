from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-26"}

CARDS = (
    ("polska", "Polska", "Польша", "Polska leży w Europie."),
    ("polak", "Polak", "поляк", "Marek to Polak."),
    ("polka", "Polka", "полька", "Anna to Polka."),
    ("polski", "polski", "польский", "Uczę się języka polskiego."),
    ("ukraina", "Ukraina", "Украина", "Oksana pochodzi z Ukrainy."),
    ("ukrainiec", "Ukrainiec", "украинец", "Andrij to Ukrainiec."),
    ("ukrainka", "Ukrainka", "украинка", "Oksana to Ukrainka."),
    ("ukrainski", "ukraiński", "украинский", "Mówię po ukraińsku."),
    ("niemcy", "Niemcy", "Германия", "Berlin leży w Niemczech."),
    ("niemiec", "Niemiec", "немец", "Thomas to Niemiec."),
    ("niemiecki", "niemiecki", "немецкий", "Znam język niemiecki."),
    ("jezyk", "język", "язык", "Jaki język znasz?"),
    ("mowic", "mówić", "говорить", "Mówię trochę po polsku."),
    ("znac", "znać", "знать", "Znam polski i angielski."),
    ("pochodzic", "pochodzić", "быть родом", "Skąd pochodzisz?"),
)

GRAMMAR = (
    ("Какого рода слово Polska?", ["мужского", "женского", "среднего"], 1, "Названия стран на -a обычно женского рода: ta Polska."),
    ("Выберите правильную пару.", ["Polska — polski", "Polska — polska język", "Polska — polsko"], 0, "Прилагательное мужского рода: język polski."),
    ("Ona jest ___. Вставьте «полька».", ["Polak", "Polką", "polski"], 1, "После jest при указании национальности употребляется творительный падеж: jest Polką."),
    ("Как сказать «Я говорю по-польски»?", ["Mówię polski.", "Mówię po polsku.", "Znam z Polski."], 1, "Для языка общения используется конструкция mówić po + наречие: po polsku."),
    ("Skąd pochodzisz? Выберите естественный ответ.", ["Pochodzę z Ukrainy.", "Mówię Ukraina.", "Jestem język."], 0, "Pochodzę z… означает «Я родом из…»."),
)

QUIZ = (
    ("Что означает «Skąd pochodzisz?»", ["Где ты живёшь?", "Откуда ты родом?", "На каком языке ты говоришь?"], 1, "Pochodzić — быть родом, происходить."),
    ("Как сказать «польский язык»?", ["język polska", "polski język", "język polski"], 2, "Нейтральный порядок: język polski."),
    ("Выберите женскую национальность.", ["Polak", "Polka", "polski"], 1, "Polka — полька; Polak — поляк."),
    ("Mówię ___ ukraińsku.", ["na", "z", "po"], 2, "Язык общения выражается через po: po ukraińsku."),
    ("Thomas pochodzi z Niemiec. Kim jest?", ["Niemcem", "Polakiem", "Ukraińcem"], 0, "Человек из Германии — Niemiec; после jest: Niemcem."),
    ("Что значит «Trochę znam język polski»?", ["Я немного знаю польский", "Я родом из Польши", "Я не говорю по-польски"], 0, "Znać język — знать язык."),
    ("Выберите название страны.", ["ukraiński", "Ukrainiec", "Ukraina"], 2, "Ukraina — страна; Ukrainiec — человек; ukraiński — прилагательное."),
    ("Как спросить «На каких языках ты говоришь?»", ["Jakimi językami mówisz?", "Skąd jesteś język?", "Jaki kraj znasz?"], 0, "Jakimi językami mówisz? — естественный вопрос о языках общения."),
)

READING = {
    "id": "rozmowa-w-miedzynarodowej-grupie",
    "title": "Rozmowa w międzynarodowej grupie",
    "description": "Участники курса рассказывают о странах и языках",
    "level": "A1", "minutes": 4, "emoji": "🌍", "position": 1,
    "paragraphs": [
        "Na kursie języka polskiego jest międzynarodowa grupa. Oksana pochodzi z Ukrainy. Mówi po ukraińsku, po rosyjsku i trochę po polsku. Chce dobrze znać polski, ponieważ mieszka w Krakowie.",
        "Thomas jest Niemcem i pochodzi z Berlina. Jego język ojczysty to niemiecki, ale zna też angielski. Z Anną rozmawia po polsku. Anna jest Polką i pomaga nowym osobom.",
        "Nauczyciel pyta każdego: Skąd pochodzisz i jakimi językami mówisz? Wszyscy odpowiadają inaczej, ale razem uczą się jednego języka. Dzięki temu grupa szybko się poznaje.",
    ],
    "glossary": {"międzynarodowa": "международная", "pochodzi": "родом", "rosyjsku": "по-русски", "ponieważ": "потому что", "dobrze": "хорошо", "ojczysty": "родной", "angielski": "английский", "rozmawia": "разговаривает", "pomaga": "помогает", "każdego": "каждого", "jakimi": "какими", "wszyscy": "все", "inaczej": "по-разному", "razem": "вместе", "dzięki": "благодаря", "szybko": "быстро"},
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
    Topic.objects.filter(course=course, position__gte=1).update(position=2)
    topic, _ = Topic.objects.update_or_create(id="countries-languages", defaults={"course": course, "title": "Страны и языки", "description": "Рассказываем, откуда мы и на каких языках говорим", "emoji": "🌍", "position": 1, "is_active": True})
    lessons = (
        ("countries-words", "words", "Kraje i ludzie", "Страны и люди", "8 карточек · A1", "Назови страну, жителя и язык", 7, "🌍"),
        ("countries-grammar", "grammar", "Język polski", "Род и прилагательные", "5 заданий · A1", "Свяжи страну, человека и язык", 8, "✏️"),
        ("countries-review", "review", "Mówię po polsku", "Языки общения", "7 карточек · A1", "Расскажи, какие языки знаешь", 6, "🔄"),
        ("countries-quiz", "quiz", "Quiz: kraje i języki", "Проверка темы", "8 вопросов · A1", "Закрепи страны, жителей и языки", 5, "🎯"),
    )
    created = {}
    for position, (id_, kind, title, plan, subtitle, desc, minutes, emoji) in enumerate(lessons, 4):
        created[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": desc, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = created["countries-grammar"]
    grammar.theory_title = "Страна, человек и язык"
    grammar.theory_sections = [["Род", "Polak — мужчина, Polka — женщина; Polska — название страны женского рода."], ["Прилагательные", "język polski, język ukraiński, język niemiecki. Прилагательное согласуется с существительным."], ["Как сказать о языке", "Mówię po polsku. Znam język polski. Pochodzę z Polski."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": 15 + position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, selected in (("countries-words", cards[:8]), ("countries-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(selected): Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("countries-grammar", GRAMMAR), ("countries-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions): Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    defaults = {k: v for k, v in READING.items() if k != "id"}
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**defaults, "topic": topic, "source_metadata": SOURCE})


class Migration(migrations.Migration):
    dependencies = [("learning", "0006_a1_introductions_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
