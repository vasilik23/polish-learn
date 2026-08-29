from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-29"}
CARDS = (
    ("weather-prognoza", "prognoza pogody", "прогноз погоды", "Sprawdzam prognozę pogody przed wycieczką."),
    ("weather-temperatura", "temperatura", "температура", "Temperatura spadnie dziś w nocy."),
    ("weather-upal", "upał", "жара", "Podczas upału trzeba pić dużo wody."),
    ("weather-mroz", "mróz", "мороз", "Rano był silny mróz."),
    ("weather-burza", "burza", "гроза", "Nad miastem zbliża się burza."),
    ("weather-wiatr", "wiatr", "ветер", "Silny wiatr łamie gałęzie."),
    ("weather-chmura", "chmura", "облако", "Ciemne chmury zapowiadają deszcz."),
    ("weather-tecza", "tęcza", "радуга", "Po deszczu pojawiła się tęcza."),
    ("weather-srodowisko", "środowisko", "окружающая среда", "Warto dbać o środowisko."),
    ("weather-segregowac", "segregować odpady", "сортировать отходы", "W domu segregujemy odpady."),
    ("weather-oszczedzac", "oszczędzać wodę", "экономить воду", "Należy oszczędzać wodę podczas suszy."),
    ("weather-zanieczyszczenie", "zanieczyszczenie", "загрязнение", "Zanieczyszczenie powietrza szkodzi zdrowiu."),
    ("weather-szlak", "szlak", "туристический маршрут", "Ten szlak prowadzi przez las."),
    ("weather-krajobraz", "krajobraz", "пейзаж", "Ze szczytu widać piękny krajobraz."),
    ("weather-chronić", "chronić przyrodę", "защищать природу", "Musimy chronić przyrodę w parku narodowym."),
)
GRAMMAR = (
    ("Kiedy jest upał, ___ pić dużo wody.", ["trzeba", "może", "wolno"], 0, "Trzeba + инфинитив выражает общую необходимость."),
    ("Przed wycieczką ___ sprawdzić prognozę.", ["warto", "nie wolno", "udało się"], 0, "Warto + инфинитив означает полезную рекомендацию."),
    ("W rezerwacie nie ___ schodzić ze szlaku.", ["wolno", "trzeba", "warto"], 0, "Nie wolno + инфинитив выражает запрет."),
    ("Jutro ___ padać, więc zabierz parasol.", ["może", "musi", "należy"], 0, "Może + инфинитив сообщает о возможности или вероятности."),
    ("Составьте: Во время засухи необходимо экономить воду.", ["Podczas suszy należy oszczędzać wodę.", "Podczas suszy może oszczędza wodę.", "Suszę należy woda oszczędzać."], 0, "Należy + инфинитив выражает безличную необходимость; podczas требует родительного падежа."),
)
QUIZ = (
    ("Что означает prognoza pogody?", ["прогноз погоды", "температура воды", "горный маршрут"], 0, "Prognoza pogody сообщает об ожидаемой погоде."),
    ("Po burzy na niebie może pojawić się ___.", ["tęcza", "mróz", "upał"], 0, "После дождя и грозы иногда появляется радуга."),
    ("Как сказать «сортировать отходы»?", ["segregować odpady", "chronić krajobraz", "oszczędzać wiatr"], 0, "Segregować odpady — разделять мусор по видам."),
    ("W parku narodowym nie ___ hałasować.", ["wolno", "warto", "może"], 0, "Nie wolno выражает запрет."),
    ("Что может вредить воздуху?", ["zanieczyszczenie", "tęcza", "szlak"], 0, "Zanieczyszczenie — загрязнение среды."),
    ("Silny ___ może łamać gałęzie.", ["wiatr", "krajobraz", "mróz"], 0, "Сильный ветер может ломать ветки."),
    ("Как дать мягкий совет проверить прогноз?", ["Warto sprawdzić prognozę.", "Nie wolno prognoza.", "Prognoza trzeba sprawdziła."], 0, "Warto + инфинитив — мягкая рекомендация."),
    ("Ten ___ prowadzi na szczyt góry.", ["szlak", "upał", "odpad"], 0, "Szlak — обозначенный туристический маршрут."),
)
CHECK = (
    ("Dokąd pojechali Lena i Kuba?", ["Do parku narodowego", "Nad morze", "Do centrum handlowego"], 0, "Они отправились в национальный парк."),
    ("Co zapowiadała prognoza?", ["Słońce rano i burzę po południu", "Mróz przez cały dzień", "Silny śnieg rano"], 0, "Утром ожидалось солнце, а после обеда — гроза."),
    ("Dlaczego zmienili trasę?", ["Nadchodziła burza", "Zgubili mapę", "Szlak był zamknięty od rana"], 0, "Они увидели тёмные облака и услышали гром."),
    ("Co zrobili z butelką?", ["Wrzucili ją do odpowiedniego pojemnika", "Zostawili ją w lesie", "Wyrzucili ją do rzeki"], 0, "Бутылку отсортировали в подходящий контейнер."),
    ("Co zobaczyli po deszczu?", ["Tęczę nad lasem", "Śnieg na szlaku", "Pożar w parku"], 0, "После дождя над лесом появилась радуга."),
)
READING = {
    "id": "weather-wycieczka-przed-burza", "title": "Wycieczka przed burzą", "description": "Прогноз, безопасный маршрут и забота о природе", "level": "A2", "minutes": 6, "emoji": "🌦️", "position": 21,
    "paragraphs": [
        "W sobotę Lena i Kuba pojechali do parku narodowego. Prognoza pogody zapowiadała słońce rano, ale po południu mogła nadejść burza. Dlatego zabrali lekkie kurtki, wodę i mapę. Przed wejściem na szlak przeczytali też zasady dla turystów.",
        "Na początku było ciepło i bezwietrznie. Ze wzgórza podziwiali zielony krajobraz, lecz później zobaczyli ciemne chmury i usłyszeli grzmot. Uznali, że nie należy iść dalej. Mogli wrócić krótszą trasą, więc spokojnie zeszli do schroniska przed silnym deszczem.",
        "Po drodze znaleźli pustą plastikową butelkę. Zabrali ją i wrzucili do odpowiedniego pojemnika obok parkingu, ponieważ warto segregować odpady i chronić przyrodę. Gdy deszcz się skończył, nad lasem pojawiła się tęcza. Wycieczka była krótsza, ale bezpieczna i udana.",
    ],
    "glossary": {
        "zapowiadała": {"lemma": "zapowiadać", "translation": "предвещать; прогнозировать", "part_of_speech": "глагол"},
        "nadejść": {"lemma": "nadejść", "translation": "наступить; приблизиться", "part_of_speech": "глагол"},
        "szlak": {"lemma": "szlak", "translation": "туристический маршрут", "part_of_speech": "существительное"},
        "bezwietrznie": {"lemma": "bezwietrznie", "translation": "безветренно", "part_of_speech": "наречие"},
        "wzgórza": {"lemma": "wzgórze", "translation": "холм", "part_of_speech": "существительное"},
        "krajobraz": {"lemma": "krajobraz", "translation": "пейзаж", "part_of_speech": "существительное"},
        "grzmot": {"lemma": "grzmot", "translation": "гром", "part_of_speech": "существительное"},
        "schroniska": {"lemma": "schronisko", "translation": "туристический приют", "part_of_speech": "существительное"},
        "pojemnika": {"lemma": "pojemnik", "translation": "контейнер", "part_of_speech": "существительное"},
        "chronić": {"lemma": "chronić", "translation": "защищать", "part_of_speech": "глагол"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(id="weather-nature", defaults={"course": Course.objects.get(id="a2-independence"), "title": "Природа и погода", "description": "Обсуждаем прогноз, безопасность и заботу о природе", "emoji": "🌦️", "position": 9, "is_active": True})
    rows = (
        ("weather-words", "words", "Pogoda wokół nas", "Погода", "8 карточек · A2", "Опиши прогноз и погодные явления", 8, "🌦️"),
        ("weather-grammar", "grammar", "Trzeba czy można?", "Необходимость и возможность", "5 заданий · A2", "Говори о правилах, советах и вероятности", 9, "✏️"),
        ("weather-review", "review", "Dbamy o przyrodę", "Природа и экология", "7 карточек · A2", "Повтори действия для защиты природы", 7, "🌿"),
        ("weather-quiz", "quiz", "Quiz: natura i pogoda", "Проверка темы", "8 вопросов · A2", "Проверь лексику и конструкции темы", 6, "🎯"),
        ("weather-reading-check", "quiz", "Czy rozumiesz wycieczkę?", "Понимание текста", "5 вопросов · A2", "Проверь детали поездки Лены и Кубы", 5, "📖"),
    )
    made = {}
    for position, row in enumerate(rows, 93):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["weather-grammar"]
    grammar.theory_title = "Необходимость, совет, запрет и возможность"
    grammar.theory_sections = [["Необходимость", "Trzeba/należy + инфинитив: Trzeba zabrać wodę."], ["Совет и запрет", "Warto советует, а nie wolno запрещает действие."], ["Возможность", "Można говорит о доступной возможности, а może — о вероятности."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 316):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("weather-words", cards[:8]), ("weather-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("weather-grammar", GRAMMAR), ("weather-quiz", QUIZ), ("weather-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "weather-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0028_a2_institutions_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
