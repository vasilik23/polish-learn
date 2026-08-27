from django.db import migrations

SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-27"}
CARDS = (
    ("city-miasto", "miasto", "город", "To miasto jest duże."),
    ("city-ulica", "ulica", "улица", "To jest ulica Długa."),
    ("city-plac", "plac", "площадь", "Spotykamy się na placu."),
    ("city-dworzec", "dworzec", "вокзал", "Dworzec jest blisko centrum."),
    ("city-przystanek", "przystanek", "остановка", "Czekam na przystanku."),
    ("city-apteka", "apteka", "аптека", "Apteka jest obok banku."),
    ("city-bank", "bank", "банк", "Bank jest naprzeciwko kawiarni."),
    ("city-centrum", "centrum", "центр", "Idziemy do centrum."),
    ("city-prosto", "prosto", "прямо", "Proszę iść prosto."),
    ("city-lewo", "w lewo", "налево", "Potem proszę skręcić w lewo."),
    ("city-prawo", "w prawo", "направо", "Na skrzyżowaniu skręć w prawo."),
    ("city-obok", "obok", "рядом", "Muzeum jest obok parku."),
    ("city-naprzeciwko", "naprzeciwko", "напротив", "Kino jest naprzeciwko hotelu."),
    ("city-skrecac", "skręcać", "поворачивать", "Tutaj trzeba skręcić."),
    ("city-przechodzic", "przechodzić", "переходить", "Proszę przejść przez ulicę."),
)
GRAMMAR = (
    ("Proszę iść ___.", ["prosto", "prosty", "prosta"], 0, "После iść направление передаёт наречие prosto: идти прямо."),
    ("Na skrzyżowaniu proszę skręcić ___.", ["na lewo", "w lewo", "do lewa"], 1, "Устойчивое направление — w lewo: повернуть налево."),
    ("Apteka jest ___ banku.", ["obok", "prosto", "przez"], 0, "Obok + родительный падеж обозначает расположение рядом: obok banku."),
    ("Proszę ___ przez ulicę.", ["przejść", "przechodzi", "idzie"], 0, "В вежливой инструкции после proszę употребляем инфинитив: proszę przejść."),
    ("Как вежливо спросить дорогу к вокзалу?", ["Gdzie dworzec robi?", "Jak dojść do dworca?", "Czy dworzec idzie?"], 1, "Jak dojść do…? — естественный вопрос о пути к месту."),
)
QUIZ = (
    ("Что означает przystanek?", ["остановка", "площадь", "вокзал"], 0, "Przystanek — остановка общественного транспорта."),
    ("Proszę iść ___.", ["prosto", "prostą", "proste"], 0, "Направление движения выражает наречие prosto."),
    ("Как сказать «поверните направо»?", ["Proszę skręcić w prawo.", "Proszę iść na prawy.", "Proszę prawo jest."], 0, "Skręcić w prawo — повернуть направо."),
    ("Bank jest ___ kawiarni.", ["przez", "naprzeciwko", "w lewo"], 1, "Naprzeciwko означает «напротив» и требует родительного падежа."),
    ("Выберите «вокзал».", ["dworzec", "przystanek", "plac"], 0, "Dworzec — вокзал."),
    ("Proszę ___ przez ulicę.", ["przejść", "przejdzie", "przechodzę"], 0, "После вежливого proszę используем инфинитив przejść."),
    ("Где встречаются на площади?", ["na placu", "w plac", "do plac"], 0, "Для местонахождения на площади употребляем na placu."),
    ("Выберите естественный вопрос о дороге.", ["Jak dojść do apteki?", "Jak apteka chodzi?", "Gdzie iść aptekę?"], 0, "Jak dojść do apteki? — «Как дойти до аптеки?»."),
)
READING = {
    "id": "droga-do-muzeum", "title": "Droga do muzeum", "description": "Анна спрашивает дорогу к городскому музею", "level": "A1", "minutes": 4, "emoji": "🗺️", "position": 6,
    "paragraphs": [
        "Anna jest pierwszy raz w tym mieście. Wychodzi z dworca i chce dojść do muzeum w centrum. Nie zna drogi, więc pyta kobietę na przystanku: „Przepraszam, jak dojść do muzeum?”.",
        "Kobieta odpowiada: „Proszę iść prosto ulicą Dworcową. Na drugim skrzyżowaniu proszę skręcić w lewo i przejść przez plac. Potem proszę skręcić w prawo przy banku”.",
        "Anna dziękuje i idzie zgodnie z instrukcją. Muzeum jest obok parku, naprzeciwko małej kawiarni. Droga zajmuje dziesięć minut. Anna bez problemu znajduje wejście.",
    ],
    "glossary": {
        "wychodzi": {"lemma": "wychodzić", "translation": "выходить", "part_of_speech": "глагол"},
        "chce": {"lemma": "chcieć", "translation": "хотеть", "part_of_speech": "глагол"},
        "dojść": {"lemma": "dojść", "translation": "дойти", "part_of_speech": "глагол"},
        "zna": {"lemma": "znać", "translation": "знать", "part_of_speech": "глагол"},
        "drogę": {"lemma": "droga", "translation": "дорога; путь", "part_of_speech": "существительное"},
        "pyta": {"lemma": "pytać", "translation": "спрашивать", "part_of_speech": "глагол"},
        "odpowiada": {"lemma": "odpowiadać", "translation": "отвечать", "part_of_speech": "глагол"},
        "skrzyżowaniu": {"lemma": "skrzyżowanie", "translation": "перекрёсток", "part_of_speech": "существительное"},
        "przejść": {"lemma": "przejść", "translation": "перейти; пройти", "part_of_speech": "глагол"},
        "zgodnie": {"lemma": "zgodnie", "translation": "согласно", "part_of_speech": "наречие"},
        "zajmuje": {"lemma": "zajmować", "translation": "занимать (время)", "part_of_speech": "глагол"},
        "znajduje": {"lemma": "znajdować", "translation": "находить", "part_of_speech": "глагол"},
        "wejście": {"lemma": "wejście", "translation": "вход", "part_of_speech": "существительное"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course = apps.get_model("learning", "Course"); Topic = apps.get_model("learning", "Topic"); Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard"); Link = apps.get_model("learning", "LessonFlashcard"); Question = apps.get_model("learning", "Question"); ReadingText = apps.get_model("learning", "ReadingText")
    course = Course.objects.get(id="a1-foundations")
    Topic.objects.filter(course=course, position__gte=6).update(position=7)
    topic, _ = Topic.objects.update_or_create(id="city-directions", defaults={"course": course, "title": "Город и дорога", "description": "Спрашиваем дорогу, называем места и объясняем маршрут", "emoji": "🗺️", "position": 6, "is_active": True})
    rows = (("city-words", "words", "W mieście", "Места в городе", "8 карточек · A1", "Назови городские места", 7, "🏙️"), ("city-grammar", "grammar", "Jak dojść?", "Как пройти?", "5 заданий · A1", "Объясни маршрут вежливыми клише", 8, "✏️"), ("city-review", "review", "Prosto i w lewo", "Направления", "7 карточек · A1", "Закрепи ориентиры и движения", 6, "🔄"), ("city-quiz", "quiz", "Quiz: miasto", "Проверка темы", "8 вопросов · A1", "Проверь места и объяснение пути", 5, "🎯"))
    made = {}
    for position, row in enumerate(rows, 24):
        id_, kind, title, plan, subtitle, desc, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": desc, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["city-grammar"]
    grammar.theory_title = "Proszę iść prosto — proszę skręcić w lewo"
    grammar.theory_sections = [["Вежливая инструкция", "Proszę + инфинитив: proszę iść, proszę skręcić, proszę przejść."], ["Направления", "Iść prosto — идти прямо; skręcić w lewo / w prawo — повернуть налево / направо."], ["Ориентиры", "Obok — рядом, naprzeciwko — напротив, przy — у. Спрашиваем: Jak dojść do dworca?"]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 90):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE}); cards.append(card)
    for lesson_id, chosen in (("city-words", cards[:8]), ("city-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen): Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("city-grammar", GRAMMAR), ("city-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions): Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": SOURCE})


class Migration(migrations.Migration):
    dependencies = [("learning", "0011_a1_food_shopping_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
