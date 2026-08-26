from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-26"}

CARDS = (
    ("rodzina", "rodzina", "семья", "To jest moja rodzina."),
    ("mama", "mama", "мама", "Moja mama ma na imię Ewa."),
    ("tata", "tata", "папа", "Mój tata lubi kawę."),
    ("rodzice", "rodzice", "родители", "Moi rodzice mieszkają w Gdańsku."),
    ("brat", "brat", "брат", "Mam jednego brata."),
    ("siostra", "siostra", "сестра", "Moja siostra ma osiemnaście lat."),
    ("syn", "syn", "сын", "Ich syn chodzi do szkoły."),
    ("corka", "córka", "дочь", "Nasza córka ma pięć lat."),
    ("babcia", "babcia", "бабушка", "Babcia mieszka blisko nas."),
    ("dziadek", "dziadek", "дедушка", "Mój dziadek czyta gazetę."),
    ("maz", "mąż", "муж", "Jej mąż ma na imię Adam."),
    ("zona", "żona", "жена", "Jego żona jest lekarką."),
    ("dziecko", "dziecko", "ребёнок", "To dziecko ma dwa lata."),
    ("dzieci", "dzieci", "дети", "Oni mają dwoje dzieci."),
    ("ile-lat", "ile lat?", "сколько лет?", "Ile lat ma twój brat?"),
)

GRAMMAR = (
    ("Выберите: ___ tata ma na imię Piotr.", ["Mój", "Moja", "Moje"], 0, "Tata — существительное мужского рода, поэтому mój tata."),
    ("Выберите: ___ siostra ma dwadzieścia lat.", ["Mój", "Moja", "Moi"], 1, "Siostra — женского рода: moja siostra."),
    ("Как сказать «его мама»?", ["jego mama", "jej mama", "mój mama"], 0, "Jego не изменяется по роду и означает «его»."),
    ("Как спросить возраст сестры?", ["Ile siostra?", "Ile lat ma twoja siostra?", "Jaki rok siostra?"], 1, "Возраст спрашивают конструкцией Ile lat ma…?"),
    ("Ania ma 12 ___. Выберите форму.", ["rok", "lata", "lat"], 2, "После 12 используется форма lat: dwanaście lat."),
)

QUIZ = (
    ("Кто такие rodzice?", ["дети", "родители", "бабушка и дедушка"], 1, "Rodzice — родители."),
    ("Выберите «моя мама».", ["mój mama", "moja mama", "moje mama"], 1, "С существительным женского рода употребляется moja."),
    ("Что означает «Mam jednego brata»?", ["У меня один брат", "У меня одна сестра", "Я вижу брата"], 0, "Mam… сообщает, кто есть в семье."),
    ("Как сказать «их дети»?", ["ich dzieci", "jego dzieci", "nasz dzieci"], 0, "Ich означает «их» и не изменяется."),
    ("Ola ma 4 ___. Вставьте форму.", ["rok", "lata", "lat"], 1, "После 2, 3 и 4 употребляется lata: cztery lata."),
    ("Piotr ma 15 ___. Вставьте форму.", ["rok", "lata", "lat"], 2, "После 15 употребляется lat."),
    ("Кто такая córka?", ["дочь", "жена", "бабушка"], 0, "Córka — дочь; syn — сын."),
    ("Как спросить «Сколько лет твоему брату?»", ["Ile lat ma twój brat?", "Kto jest brat?", "Czy brat ma rodzina?"], 0, "Ile lat ma…? — стандартный вопрос о возрасте."),
)

READING = {
    "id": "niedziela-u-babci",
    "title": "Niedziela u babci",
    "description": "Майя рассказывает о семейной встрече",
    "level": "A1", "minutes": 4, "emoji": "🏡", "position": 2,
    "paragraphs": [
        "W niedzielę Maja odwiedza babcię i dziadka. Babcia ma sześćdziesiąt osiem lat, a dziadek siedemdziesiąt. Mieszkają w małym domu blisko Krakowa. Maja bardzo lubi ich ogród.",
        "Na obiad przyjeżdżają też rodzice Mai. Jej mama Ewa jest nauczycielką, a tata Paweł pracuje w banku. Maja ma jednego brata. Kuba ma szesnaście lat i interesuje się sportem.",
        "Przy stole każdy opowiada o swoim tygodniu. Potem Maja pokazuje rodzinne zdjęcia. Na jednym zdjęciu jest jej ciocia z mężem i dwojgiem dzieci. To spokojne, dobre popołudnie razem.",
    ],
    "glossary": {"niedzielę": "воскресенье", "odwiedza": "навещает", "ogród": "сад", "obiad": "обед", "przyjeżdżają": "приезжают", "pracuje": "работает", "interesuje": "интересуется", "stole": "столе", "każdy": "каждый", "opowiada": "рассказывает", "tygodniu": "неделе", "pokazuje": "показывает", "rodzinne": "семейные", "zdjęcia": "фотографии", "ciocia": "тётя", "dwojgiem": "двумя", "spokojne": "спокойное", "popołudnie": "вторая половина дня"},
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
    Topic.objects.filter(course=course, position__gte=2).update(position=3)
    topic, _ = Topic.objects.update_or_create(id="family", defaults={"course": course, "title": "Семья", "description": "Рассказываем о близких, возрасте и родстве", "emoji": "👨‍👩‍👧", "position": 2, "is_active": True})
    lessons = (
        ("family-words", "words", "Moja rodzina", "Члены семьи", "8 карточек · A1", "Назови близких и расскажи, кто есть в семье", 7, "👨‍👩‍👧"),
        ("family-grammar", "grammar", "Mój, moja, moje", "Моя семья", "5 заданий · A1", "Используй притяжательные местоимения и возраст", 8, "✏️"),
        ("family-review", "review", "Ile masz lat?", "Родство и возраст", "7 карточек · A1", "Закрепи родство и вопросы о возрасте", 6, "🔄"),
        ("family-quiz", "quiz", "Quiz: rodzina", "Проверка темы", "8 вопросов · A1", "Проверь лексику семьи, местоимения и числа", 5, "🎯"),
    )
    created = {}
    for position, (id_, kind, title, plan, subtitle, desc, minutes, emoji) in enumerate(lessons, 8):
        created[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": desc, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = created["family-grammar"]
    grammar.theory_title = "Mój, moja, moje — чей это?"
    grammar.theory_sections = [["Согласование", "mój tata · moja mama · moje dziecko · moi rodzice. Форма зависит от рода и числа предмета."], ["Его и её", "jego brat — его брат; jej siostra — её сестра. Jego и jej не изменяются."], ["Возраст", "Ile masz lat? Mam rok, dwa/trzy/cztery lata, пять и больше — lat: Mam dwanaście lat."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": 30 + position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, selected in (("family-words", cards[:8]), ("family-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(selected):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("family-grammar", GRAMMAR), ("family-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    defaults = {key: value for key, value in READING.items() if key != "id"}
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**defaults, "topic": topic, "source_metadata": SOURCE})


class Migration(migrations.Migration):
    dependencies = [("learning", "0007_a1_countries_languages")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
