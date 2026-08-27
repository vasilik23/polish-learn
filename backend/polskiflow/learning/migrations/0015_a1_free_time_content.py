from django.db import migrations

SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-27"}
CARDS = (
    ("free-czas", "czas wolny", "свободное время", "W weekend mam czas wolny."),
    ("free-ksiazka", "książka", "книга", "Czytam ciekawą książkę."),
    ("free-film", "film", "фильм", "Wieczorem oglądam film."),
    ("free-muzyka", "muzyka", "музыка", "Lubię polską muzykę."),
    ("free-sport", "sport", "спорт", "Sport daje mi energię."),
    ("free-spacer", "spacer", "прогулка", "Idziemy na spacer do parku."),
    ("free-rower", "rower", "велосипед", "Latem często jeżdżę na rowerze."),
    ("free-przyjaciel", "przyjaciel", "друг", "Spotykam się z przyjacielem."),
    ("free-czytac", "czytać", "читать", "Lubię czytać wieczorem."),
    ("free-ogladac", "oglądać", "смотреть", "Oglądamy nowy film."),
    ("free-sluchac", "słuchać", "слушать", "Słucham muzyki w domu."),
    ("free-grac", "grać", "играть", "Gram w piłkę z kolegami."),
    ("free-jezdzic", "jeździć", "ездить", "W weekend jeżdżę na rowerze."),
    ("free-lubic", "lubić", "любить; нравиться", "Lubię dobrą kawę."),
    ("free-interesowac", "interesować się", "интересоваться", "Interesuję się kinem."),
)
GRAMMAR = (
    ("Lubię ___ książki.", ["czytać", "czytam", "czyta"], 0, "После lubię можно поставить инфинитив: lubię czytać."),
    ("Ola lubi ___.", ["muzyka", "muzykę", "muzyki"], 1, "После lubić предмет обычно стоит в винительном падеже: muzykę."),
    ("My lubimy ___ filmy.", ["oglądać", "oglądamy", "ogląda"], 0, "После lubimy действие остаётся в инфинитиве: oglądać."),
    ("Paweł interesuje się ___.", ["sport", "sportem", "sportu"], 1, "Interesować się требует творительного падежа: sportem."),
    ("Как спросить о любимом занятии?", ["Co lubisz robić?", "Co robisz lubi?", "Jaki lubić?"], 0, "Co lubisz robić? — естественный вопрос «Что ты любишь делать?»."),
)
QUIZ = (
    ("Что означает spacer?", ["спорт", "прогулка", "выходные"], 1, "Spacer — прогулка."),
    ("Lubię ___ muzyki.", ["słuchać", "słucham", "słucha"], 0, "После lubię употребляем инфинитив słuchać."),
    ("Anna lubi ___.", ["książka", "książkę", "książką"], 1, "После lubi нужна форма książkę."),
    ("Как сказать «я играю в футбол»?", ["Gram w piłkę.", "Jestem piłka.", "Gram na piłkę."], 0, "С играми и спортом употребляем grać w: gram w piłkę."),
    ("Interesuję się ___.", ["kino", "kinem", "kina"], 1, "После interesuję się употребляем творительный падеж: kinem."),
    ("Что означает jeździć na rowerze?", ["ездить на велосипеде", "гулять пешком", "смотреть гонки"], 0, "Jeździć na rowerze — регулярно ездить на велосипеде."),
    ("Выберите естественный вопрос.", ["Co lubisz robić w weekend?", "Co weekend lubi robi?", "Jaki ty czas robić?"], 0, "Co lubisz robić…? спрашивает о предпочтениях."),
    ("My ___ oglądać filmy.", ["lubicie", "lubimy", "lubi"], 1, "Для my форма lubić — lubimy."),
)
READING = {
    "id": "wolna-sobota-marka", "title": "Wolna sobota Marka", "description": "Марк проводит свободный день с друзьями", "level": "A1", "minutes": 4, "emoji": "🎨", "position": 9,
    "paragraphs": [
        "Marek pracuje od poniedziałku do piątku, dlatego lubi spokojne soboty. Rano długo pije kawę i czyta książkę. Interesuje się historią, ale czasem wybiera też prosty kryminał.",
        "Po południu Marek spotyka się z przyjaciółmi w parku. Kiedy jest ciepło, jeżdżą na rowerach albo grają w piłkę. Dzisiaj pada deszcz, więc idą do małej kawiarni.",
        "Wieczorem wszyscy oglądają film u Marka. Jego przyjaciółka Ania lubi komedie, a Marek woli filmy podróżnicze. Wybierają krótką komedię i zamawiają pizzę. To prosty, ale bardzo dobry weekend.",
    ],
    "glossary": {
        "dlatego": {"lemma": "dlatego", "translation": "поэтому", "part_of_speech": "наречие"},
        "spokojne": {"lemma": "spokojny", "translation": "спокойный", "part_of_speech": "прилагательное"},
        "wybiera": {"lemma": "wybierać", "translation": "выбирать", "part_of_speech": "глагол"},
        "kryminał": {"lemma": "kryminał", "translation": "детектив", "part_of_speech": "существительное"},
        "spotyka": {"lemma": "spotykać się", "translation": "встречаться", "part_of_speech": "глагол"},
        "przyjaciółmi": {"lemma": "przyjaciel", "translation": "друг", "part_of_speech": "существительное"},
        "jeżdżą": {"lemma": "jeździć", "translation": "ездить", "part_of_speech": "глагол"},
        "grają": {"lemma": "grać", "translation": "играть", "part_of_speech": "глагол"},
        "pada": {"lemma": "padać", "translation": "идти (о дожде)", "part_of_speech": "глагол"},
        "wszyscy": {"lemma": "wszyscy", "translation": "все", "part_of_speech": "местоимение"},
        "woli": {"lemma": "woleć", "translation": "предпочитать", "part_of_speech": "глагол"},
        "podróżnicze": {"lemma": "podróżniczy", "translation": "о путешествиях", "part_of_speech": "прилагательное"},
        "zamawiają": {"lemma": "zamawiać", "translation": "заказывать", "part_of_speech": "глагол"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite": return
    Course = apps.get_model("learning", "Course"); Topic = apps.get_model("learning", "Topic"); Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard"); Link = apps.get_model("learning", "LessonFlashcard"); Question = apps.get_model("learning", "Question"); ReadingText = apps.get_model("learning", "ReadingText")
    course = Course.objects.get(id="a1-foundations")
    Topic.objects.filter(course=course, position__gte=9).update(position=10)
    topic, _ = Topic.objects.update_or_create(id="free-time", defaults={"course": course, "title": "Свободное время", "description": "Рассказываем об интересах, любимых занятиях и планах на выходные", "emoji": "🎨", "position": 9, "is_active": True})
    rows = (("free-words", "words", "Czas wolny", "Досуг и интересы", "8 карточек · A1", "Назови занятия и увлечения", 7, "🎨"), ("free-grammar", "grammar", "Co lubisz robić?", "Говорим о предпочтениях", "5 заданий · A1", "Используй lubić с инфинитивом и предметом", 8, "✏️"), ("free-review", "review", "Weekend", "Любимые занятия", "7 карточек · A1", "Расскажи, как проводишь свободное время", 6, "🔄"), ("free-quiz", "quiz", "Quiz: czas wolny", "Проверка темы", "8 вопросов · A1", "Проверь досуг и предпочтения", 5, "🎯"))
    made = {}
    for position, row in enumerate(rows, 36):
        id_, kind, title, plan, subtitle, desc, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": desc, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["free-grammar"]; grammar.theory_title = "Lubię czytać — lubię muzykę"
    grammar.theory_sections = [["Любимое действие", "Lubić + инфинитив: lubię czytać, lubisz oglądać, lubimy grać."], ["Любимый предмет", "После lubić предмет стоит в винительном падеже: lubię muzykę, książkę, sport."], ["Интерес", "Interesować się + творительный падеж: interesuję się kinem, muzyką, sportem."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 135):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE}); cards.append(card)
    for lesson_id, chosen in (("free-words", cards[:8]), ("free-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen): Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("free-grammar", GRAMMAR), ("free-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions): Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": SOURCE})


class Migration(migrations.Migration):
    dependencies = [("learning", "0014_a1_work_study_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
