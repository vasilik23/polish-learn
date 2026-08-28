from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-28"}
CARDS = (
    ("travel-planowac", "planować", "планировать", "Planujemy wyjazd nad morze."),
    ("travel-podroz", "podróż", "путешествие", "Podróż pociągiem potrwa pięć godzin."),
    ("travel-wyjazd", "wyjazd", "поездка; отъезд", "Wyjazd jest w sobotę rano."),
    ("travel-bilet", "bilet", "билет", "Kupię bilet przez internet."),
    ("travel-nocleg", "nocleg", "ночлег", "Zarezerwowaliśmy nocleg blisko centrum."),
    ("travel-walizka", "walizka", "чемодан", "Wieczorem spakuję walizkę."),
    ("travel-pociag", "pociąg", "поезд", "Pociąg odjeżdża o siódmej."),
    ("travel-samolot", "samolot", "самолёт", "Samolot ląduje w Gdańsku."),
    ("travel-zamierzac", "zamierzać", "намереваться", "Zamierzam odwiedzić Gdańsk."),
    ("travel-rezerwowac", "rezerwować", "бронировать", "Musimy zarezerwować hotel."),
    ("travel-pakowac", "pakować się", "собирать вещи", "Będę się pakować w piątek."),
    ("travel-wyruszyc", "wyruszyć", "отправиться в путь", "Wyruszymy wcześnie rano."),
    ("travel-dojechac", "dojechać", "доехать", "Jak dojedziemy na dworzec?"),
    ("travel-przesiasc", "przesiąść się", "пересесть", "W Warszawie przesiądziemy się do innego pociągu."),
    ("travel-wracac", "wracać", "возвращаться", "Będziemy wracać w niedzielę."),
)
GRAMMAR = (
    ("Завтра я буду паковать чемодан.", ["Jutro będę pakować walizkę.", "Jutro pakowałem walizkę.", "Jutro będę pakowałeś walizkę."], 0, "Для длительного будущего действия: личная форма być + инфинитив: będę pakować."),
    ("My ___ wracać w niedzielę.", ["będziemy", "będziecie", "będą"], 0, "Для my используется форма będziemy: będziemy wracać."),
    ("Ola ___ bilet wieczorem.", ["kupi", "kupowała", "kupuje wczoraj"], 0, "Совершенный глагол kupić образует простое будущее: Ola kupi."),
    ("Мы намерены посетить Гданьск.", ["Zamierzamy odwiedzić Gdańsk.", "Zamierzacie odwiedzili Gdańsk.", "Zamierzamy odwiedzamy Gdańsk."], 0, "После zamierzać нужен инфинитив: zamierzamy odwiedzić."),
    ("W Warszawie ___ się do innego pociągu.", ["przesiądziemy", "przesiadaliśmy", "przesiada"], 0, "Совершенная форма przesiądziemy обозначает однократное будущее действие."),
)
QUIZ = (
    ("Что означает planować?", ["опаздывать", "планировать", "возвращаться"], 1, "Planować — планировать."),
    ("Ja ___ podróżować latem.", ["będę", "będzie", "będziemy"], 0, "Для ja: będę podróżować."),
    ("Kasia ___ nocleg jutro.", ["zarezerwowała wczoraj", "zarezerwuje", "rezerwować"], 1, "Zarezerwuje — совершенная форма будущего времени."),
    ("Как спросить, каким путём добраться до вокзала?", ["Jak dojedziemy na dworzec?", "Kiedy jest walizka?", "Dlaczego bilet wraca?"], 0, "Jak dojedziemy na dworzec? — Как мы доберёмся до вокзала?"),
    ("После zamierzam употребляется…", ["инфинитив", "только прошедшее время", "существительное в творительном падеже"], 0, "Намерение выражается конструкцией zamierzam + инфинитив."),
    ("Pociąg ___ o siódmej.", ["odjeżdża", "pakuje", "nocuje"], 0, "Odjeżdża — отправляется по расписанию."),
    ("My ___ wcześnie rano.", ["wyruszymy", "wyruszy", "wyruszycie"], 0, "Для my: wyruszymy — мы отправимся."),
    ("W niedzielę ___ wracać do domu.", ["będziemy", "byliśmy", "jesteśmy wczoraj"], 0, "Будущее длительное действие: będziemy wracać."),
)
COMPREHENSION = (
    ("Kiedy Marta i Kuba wyjadą z Krakowa?", ["W piątek wieczorem", "W sobotę po południu", "W niedzielę rano"], 0, "Они планируют выехать из Кракова в пятницу вечером."),
    ("Gdzie przesiądą się do innego pociągu?", ["W Krakowie", "W Warszawie", "W Gdańsku"], 1, "Пересадка запланирована в Варшаве."),
    ("Dlaczego kupią bilety przez internet?", ["Żeby nie stać w kolejce", "Żeby zmienić hotel", "Żeby zabrać dwie walizki"], 0, "Они купят билеты онлайн, чтобы не стоять в очереди."),
    ("Co zrobią, jeśli pogoda będzie dobra?", ["Wrócą do Krakowa", "Zjedzą obiad na plaży", "Zostaną na dworcu"], 1, "При хорошей погоде они пообедают на пляже."),
    ("Dlaczego spakują tylko jedną walizkę?", ["Bo lecą samolotem", "Bo hotel jest zamknięty", "Bo podróż potrwa dwa dni"], 2, "Им достаточно одного чемодана, потому что поездка продлится два дня."),
)
READING = {
    "id": "plan-wyjazdu-do-gdanska", "title": "Plan wyjazdu do Gdańska", "description": "Маршрут, планы и решения перед поездкой", "level": "A2", "minutes": 5, "emoji": "🧳", "position": 13,
    "paragraphs": [
        "W przyszły weekend Marta i Kuba pojadą do Gdańska. Zamierzają wyjechać z Krakowa w piątek wieczorem. Najpierw dojadą tramwajem na dworzec, a potem wsiądą do pociągu. W Warszawie przesiądą się do innego pociągu. Bilety kupią przez internet, żeby nie stać w kolejce.",
        "W sobotę będą spacerować po centrum i odwiedzą Europejskie Centrum Solidarności. Po południu pojadą nad morze. Jeśli pogoda będzie dobra, zjedzą obiad na plaży. Nocleg zarezerwują w małym hotelu blisko starówki.",
        "W niedzielę Marta chce zwiedzić muzeum, a Kuba planuje spotkać się z kolegą. Wieczorem będą wracać do Krakowa. Spakują tylko jedną walizkę, bo podróż potrwa dwa dni. Oboje cieszą się na wyjazd.",
    ],
    "glossary": {
        "pojadą": {"lemma": "pojechać", "translation": "поехать", "part_of_speech": "глагол"}, "zamierzają": {"lemma": "zamierzać", "translation": "намереваться", "part_of_speech": "глагол"},
        "dojadą": {"lemma": "dojechać", "translation": "доехать", "part_of_speech": "глагол"}, "wsiądą": {"lemma": "wsiąść", "translation": "сесть в транспорт", "part_of_speech": "глагол"},
        "przesiądą": {"lemma": "przesiąść się", "translation": "пересесть", "part_of_speech": "глагол"}, "kolejce": {"lemma": "kolejka", "translation": "очередь", "part_of_speech": "существительное"},
        "odwiedzą": {"lemma": "odwiedzić", "translation": "посетить", "part_of_speech": "глагол"}, "zarezerwują": {"lemma": "zarezerwować", "translation": "забронировать", "part_of_speech": "глагол"},
        "starówki": {"lemma": "starówka", "translation": "старый город", "part_of_speech": "существительное"}, "potrwa": {"lemma": "potrwać", "translation": "продлиться", "part_of_speech": "глагол"},
        "cieszą": {"lemma": "cieszyć się", "translation": "радоваться", "part_of_speech": "глагол"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    course = Course.objects.get(id="a2-independence")
    topic, _ = Topic.objects.update_or_create(id="travel-plans", defaults={"course": course, "title": "Планы и поездки", "description": "Планируем маршрут и говорим о будущих действиях", "emoji": "🧳", "position": 1, "is_active": True})
    rows = (
        ("travel-words", "words", "Planujemy podróż", "План поездки", "8 карточек · A2", "Назови транспорт, билеты и багаж", 7, "🧳"),
        ("travel-grammar", "grammar", "Co będziemy robić?", "Планы на будущее", "5 заданий · A2", "Различай составное и простое будущее время", 9, "✏️"),
        ("travel-review", "review", "W drogę!", "Маршрут и намерения", "7 карточек · A2", "Повтори действия перед поездкой и в пути", 7, "🔄"),
        ("travel-quiz", "quiz", "Quiz: plany i podróże", "Проверка темы", "8 вопросов · A2", "Проверь лексику и формы будущего времени", 6, "🎯"),
        ("travel-reading-check", "quiz", "Czy rozumiesz plan?", "Понимание текста", "5 вопросов · A2", "Проверь детали поездки Марты и Кубы", 5, "📖"),
    )
    made = {}
    for position, row in enumerate(rows, 53):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["travel-grammar"]
    grammar.theory_title = "Będę podróżować czy pojadę?"
    grammar.theory_sections = [["Процесс в будущем", "С несовершенным глаголом: личная форма być + инфинитив — będę podróżować, będziemy wracać."], ["Результат в будущем", "Совершенный глагол имеет простую форму: kupię bilet, zarezerwujemy nocleg, pojedziemy."], ["Намерение", "Используй zamierzam, mam zamiar или chcę + инфинитив: zamierzam odwiedzić Gdańsk."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 196):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("travel-words", cards[:8]), ("travel-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("travel-grammar", GRAMMAR), ("travel-quiz", QUIZ), ("travel-reading-check", COMPREHENSION)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "travel-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0020_a2_reading_comprehension")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
