from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-27"}
CARDS = (
    ("health-zdrowie", "zdrowie", "здоровье", "Zdrowie jest bardzo ważne."),
    ("health-lekarz", "lekarz", "врач", "Idę dziś do lekarza."),
    ("health-apteka", "apteka", "аптека", "Apteka jest obok przychodni."),
    ("health-gardlo", "gardło", "горло", "Boli mnie gardło."),
    ("health-glowa", "głowa", "голова", "Boli mnie głowa."),
    ("health-brzuch", "brzuch", "живот", "Po obiedzie boli mnie brzuch."),
    ("health-temperatura", "temperatura", "температура", "Mam wysoką temperaturę."),
    ("health-lekarstwo", "lekarstwo", "лекарство", "Biorę lekarstwo po jedzeniu."),
    ("health-bolec", "boleć", "болеть", "Co cię boli?"),
    ("health-kaszlec", "kaszleć", "кашлять", "Od rana kaszlę."),
    ("health-katar", "katar", "насморк", "Mam katar i źle się czuję."),
    ("health-goraczka", "gorączka", "жар; высокая температура", "Dziecko ma gorączkę."),
    ("health-chory", "chory", "больной", "Piotr jest chory i zostaje w domu."),
    ("health-odpoczywac", "odpoczywać", "отдыхать", "Musisz dużo odpoczywać."),
    ("health-czuc", "czuć się", "чувствовать себя", "Dziś czuję się lepiej."),
)
GRAMMAR = (
    ("Boli mnie ___.", ["głowa", "głowę", "głowy"], 0, "С одним больным местом используем boli и именительный падеж: boli mnie głowa."),
    ("Bolą mnie ___.", ["oko", "plecy", "gardło"], 1, "С формой множественного числа употребляем bolą: bolą mnie plecy."),
    ("Mam wysoką ___.", ["temperatura", "temperaturę", "temperaturą"], 1, "После mam нужен винительный падеж: mam temperaturę."),
    ("Ola ma ___.", ["katar", "katarem", "kataru"], 0, "У существительного мужского рода katar форма после ma не меняется."),
    ("Как спросить пациента о самочувствии?", ["Jak się pan czuje?", "Gdzie pan jest?", "Co pan lubi?"], 0, "Jak się pan czuje? — вежливый вопрос «Как вы себя чувствуете?»."),
)
QUIZ = (
    ("Что означает gardło?", ["голова", "горло", "живот"], 1, "Gardło — горло."),
    ("___ mnie brzuch.", ["Boli", "Bolą", "Mam"], 0, "Brzuch — единственное число, поэтому boli mnie brzuch."),
    ("___ mnie plecy.", ["Boli", "Bolą", "Jest"], 1, "Plecy имеют форму множественного числа: bolą mnie plecy."),
    ("Mam ___.", ["gorączka", "gorączkę", "gorączką"], 1, "После mam употребляем винительный падеж: gorączkę."),
    ("Где покупают лекарство?", ["W aptece.", "W parku.", "W szkole."], 0, "Lekarstwo kupujemy w aptece."),
    ("Как сказать «я плохо себя чувствую»?", ["Źle się czuję.", "Źle się boli.", "Mam źle."], 0, "Czuć się описывает самочувствие: źle się czuję."),
    ("Lekarz mówi: musisz dużo ___.", ["odpoczywać", "odpoczywasz", "odpoczywa"], 0, "После musisz ставим инфинитив: odpoczywać."),
    ("У пациента кашель. Что он скажет?", ["Kaszlę.", "Czytam.", "Gotuję."], 0, "Kaszlę — «я кашляю»."),
)
READING = {
    "id": "ola-u-lekarza",
    "title": "Ola u lekarza",
    "description": "Оля рассказывает врачу о самочувствии",
    "level": "A1",
    "minutes": 4,
    "emoji": "🩺",
    "position": 10,
    "paragraphs": [
        "Ola źle się dziś czuje. Boli ją gardło i głowa, ma też katar. Rano mierzy temperaturę. Ma trzydzieści osiem stopni, dlatego nie idzie do pracy i dzwoni do przychodni.",
        "Po południu Ola jest u lekarza. Lekarz pyta: „Co panią boli?”. Ola odpowiada, że boli ją gardło i że od wczoraj kaszle. Lekarz bada Olę i mówi, że musi zostać w domu.",
        "Ola dostaje receptę. W drodze do domu idzie do apteki po lekarstwo. Potem pije ciepłą herbatę, bierze tabletkę i odpoczywa. Wieczorem czuje się trochę lepiej.",
    ],
    "glossary": {
        "czuje": {"lemma": "czuć się", "translation": "чувствовать себя", "part_of_speech": "глагол"},
        "boli": {"lemma": "boleć", "translation": "болеть", "part_of_speech": "глагол"},
        "mierzy": {"lemma": "mierzyć", "translation": "измерять", "part_of_speech": "глагол"},
        "stopni": {"lemma": "stopień", "translation": "градус", "part_of_speech": "существительное"},
        "przychodni": {"lemma": "przychodnia", "translation": "поликлиника", "part_of_speech": "существительное"},
        "pyta": {"lemma": "pytać", "translation": "спрашивать", "part_of_speech": "глагол"},
        "odpowiada": {"lemma": "odpowiadać", "translation": "отвечать", "part_of_speech": "глагол"},
        "kaszle": {"lemma": "kaszleć", "translation": "кашлять", "part_of_speech": "глагол"},
        "bada": {"lemma": "badać", "translation": "осматривать", "part_of_speech": "глагол"},
        "receptę": {"lemma": "recepta", "translation": "рецепт", "part_of_speech": "существительное"},
        "lekarstwo": {"lemma": "lekarstwo", "translation": "лекарство", "part_of_speech": "существительное"},
        "tabletkę": {"lemma": "tabletka", "translation": "таблетка", "part_of_speech": "существительное"},
        "odpoczywa": {"lemma": "odpoczywać", "translation": "отдыхать", "part_of_speech": "глагол"},
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
    Topic.objects.filter(course=course, position__gte=10).update(position=11)
    topic, _ = Topic.objects.update_or_create(
        id="health",
        defaults={"course": course, "title": "Здоровье", "description": "Описываем самочувствие, симптомы и простой визит к врачу", "emoji": "🩺", "position": 10, "is_active": True},
    )
    rows = (
        ("health-words", "words", "Zdrowie", "Самочувствие", "8 карточек · A1", "Назови части тела и места помощи", 7, "🩺"),
        ("health-grammar", "grammar", "Co cię boli?", "Описываем симптомы", "5 заданий · A1", "Используй boli, bolą и конструкции с mam", 8, "✏️"),
        ("health-review", "review", "U lekarza", "Визит к врачу", "7 карточек · A1", "Расскажи о самочувствии и рекомендации", 6, "🔄"),
        ("health-quiz", "quiz", "Quiz: zdrowie", "Проверка темы", "8 вопросов · A1", "Проверь симптомы и полезные фразы", 5, "🎯"),
    )
    made = {}
    for position, row in enumerate(rows, 40):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(
            id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE}
        )
    grammar = made["health-grammar"]
    grammar.theory_title = "Boli mnie głowa — bolą mnie plecy"
    grammar.theory_sections = [
        ["Одна часть тела", "Boli + место в единственном числе: boli mnie głowa, gardło, brzuch."],
        ["Несколько или форма множественного числа", "Bolą + множественное число: bolą mnie nogi, oczy, plecy."],
        ["Симптом как состояние", "С mam называем симптом: mam katar, kaszel; mam gorączkę, temperaturę."],
    ]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 150):
        card, _ = Flashcard.objects.update_or_create(
            id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE}
        )
        cards.append(card)
    for lesson_id, chosen in (("health-words", cards[:8]), ("health-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("health-grammar", GRAMMAR), ("health-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(
        id=READING["id"],
        defaults={
            **{key: value for key, value in READING.items() if key != "id"},
            "topic": topic,
            "source_metadata": SOURCE,
            "is_active": True,
        },
    )


class Migration(migrations.Migration):
    dependencies = [("learning", "0016_sm2_personal_words")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
