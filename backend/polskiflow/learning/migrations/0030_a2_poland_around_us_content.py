from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-29"}
CARDS = (
    ("poland-region", "region", "регион", "Każdy region Polski ma własne tradycje."),
    ("poland-stolica", "stolica", "столица", "Warszawa jest stolicą Polski."),
    ("poland-zabytek", "zabytek", "памятник истории; достопримечательность", "Na rynku stoi znany zabytek."),
    ("poland-rynek", "rynek", "главная площадь", "Spotkamy się na rynku o południu."),
    ("poland-muzeum", "muzeum", "музей", "W muzeum poznaliśmy historię miasta."),
    ("poland-krajobraz", "krajobraz", "пейзаж", "Górski krajobraz zachwycił turystów."),
    ("poland-wybrzeze", "wybrzeże", "побережье", "Latem jedziemy nad polskie wybrzeże."),
    ("poland-gory", "góry", "горы", "Zimą wielu ludzi odpoczywa w górach."),
    ("poland-tradycja", "tradycja", "традиция", "Ta tradycja łączy całą rodzinę."),
    ("poland-swietowac", "świętować", "праздновать", "Mieszkańcy wspólnie świętują dzień miasta."),
    ("poland-odbywac", "odbywać się", "проходить; состояться", "Festiwal odbywa się w czerwcu."),
    ("poland-zwiedzac", "zwiedzać", "осматривать достопримечательности", "Rano zwiedzaliśmy stare miasto."),
    ("poland-podroz", "podróż", "путешествие", "Podróż pociągiem trwała trzy godziny."),
    ("poland-mieszkaniec", "mieszkaniec", "житель", "Mieszkaniec polecił nam lokalną kawiarnię."),
    ("poland-lokalny", "lokalny", "местный", "Spróbowaliśmy lokalnego dania."),
)
GRAMMAR = (
    ("Что лучше начинает связный рассказ о поездке?", ["Najpierw pojechaliśmy do Gdańska.", "Na końcu pojechaliśmy najpierw.", "Potem przed początkiem Gdańsk."], 0, "Najpierw вводит первое событие рассказа."),
    ("Najpierw zwiedziliśmy muzeum, ___ poszliśmy na rynek.", ["potem", "ponieważ", "ale najpierw"], 0, "Potem показывает следующее действие в хронологической последовательности."),
    ("___ kupiliśmy bilety, weszliśmy do muzeum.", ["Kiedy", "Na końcu", "Dlatego"], 0, "Kiedy связывает действие или момент с последующим событием."),
    ("Составьте: Сначала мы осмотрели замок, а затем пошли на рынок.", ["Najpierw zwiedziliśmy zamek, a następnie poszliśmy na rynek.", "Następnie najpierw zamek poszliśmy rynek.", "Zwiedzaliśmy na końcu, ponieważ rynek."], 0, "Najpierw …, a następnie … ясно передаёт порядок двух действий."),
    ("Как естественно завершить рассказ?", ["Na końcu wróciliśmy pociągiem do domu.", "Najpierw na końcu wracamy wczoraj.", "Kiedy koniec, dlatego pociąg."], 0, "Na końcu вводит последнее событие и завершает последовательность."),
)
QUIZ = (
    ("Что означает zabytek?", ["исторический памятник", "расписание", "побережье"], 0, "Zabytek — исторически или культурно ценный объект."),
    ("Gdzie leży Gdańsk?", ["nad polskim wybrzeżem", "w Tatrach", "na południe od Krakowa"], 0, "Гданьск расположен на балтийском побережье Польши."),
    ("Festiwal ___ w czerwcu.", ["odbywa się", "zwiedza", "podróżuje się region"], 0, "О событии говорят: festiwal odbywa się — фестиваль проходит."),
    ("Как сказать «местные жители»?", ["lokalni mieszkańcy", "stoliczne zabytki", "górskie podróże"], 0, "Lokalni mieszkańcy — жители конкретного места."),
    ("Najpierw byliśmy w muzeum, a ___ zjedliśmy obiad.", ["później", "zanim najpierw", "dlatego że koniec"], 0, "Później продолжает хронологический рассказ."),
    ("Что можно zwiedzać?", ["stare miasto", "tradycję wczoraj", "podróż pociągiem jako czas"], 0, "Zwiedzać можно город, музей, замок и другие места."),
    ("Выберите естественное описание Польши.", ["Na północy jest morze, a na południu są góry.", "Morze jest pod górami w stolicy.", "Region świętuje pociągiem krajobraz."], 0, "Польское побережье находится на севере, а горные районы — на юге."),
    ("Как завершить рассказ о празднике?", ["Na końcu wszyscy obejrzeli koncert.", "Najpierw koniec ogląda koncert.", "Kiedy wszyscy, potem ponieważ."], 0, "Na końcu естественно вводит заключительное событие."),
)
CHECK = (
    ("Dokąd pojechała grupa Mai?", ["Do Torunia", "Do Zakopanego", "Do Gdańska"], 0, "Группа Майи отправилась на однодневную поездку в Торунь."),
    ("Co grupa zrobiła najpierw?", ["Spotkała się z przewodniczką na rynku", "Kupiła pierniki na dworcu", "Wróciła do szkoły"], 0, "Первым событием была встреча с экскурсоводом на площади."),
    ("Czego uczniowie dowiedzieli się w muzeum?", ["Jak dawniej przygotowywano pierniki", "Jak buduje się statki", "Jak chodzić po górach"], 0, "В музее они узнали о старом способе приготовления пряников."),
    ("Dlaczego na rynku było dużo ludzi?", ["Odbywał się lokalny festiwal", "Przyjechał pociąg", "Muzeum było zamknięte"], 0, "На площади проходил местный фестиваль."),
    ("Co Maja zapamiętała z wyjazdu?", ["Historię miasta i atmosferę festiwalu", "Tylko czas podróży", "Adres szkolnej biblioteki"], 0, "Майе запомнились история Торуни и атмосфера местного события."),
)
READING = {
    "id": "poland-maja-odkrywa-torun",
    "title": "Maja odkrywa Toruń",
    "description": "Однодневная поездка, история города и местный праздник",
    "level": "A2",
    "minutes": 6,
    "emoji": "🇵🇱",
    "position": 22,
    "paragraphs": [
        "W sobotę Maja pojechała z grupą językową na jednodniową wycieczkę do Torunia. Najpierw spotkali się z przewodniczką na rynku. Pokazała im stare kamienice, ratusz i pomnik Mikołaja Kopernika. Opowiedziała też krótko o historii miasta.",
        "Następnie grupa zwiedziła muzeum piernika. Uczniowie dowiedzieli się, jak dawniej przygotowywano ciasto, a potem sami zrobili małe pierniki. Kiedy wyszli z muzeum, na rynku było już dużo ludzi, ponieważ odbywał się tam lokalny festiwal.",
        "Później Maja spróbowała regionalnego dania i rozmawiała z mieszkańcami. Na końcu wszyscy obejrzeli koncert i wrócili pociągiem do domu. Maja była zmęczona, ale z wyjazdu zapamiętała ciekawą historię Torunia i przyjazną atmosferę festiwalu.",
    ],
    "glossary": {
        "jednodniową": {"lemma": "jednodniowy", "translation": "однодневный", "part_of_speech": "прилагательное"},
        "przewodniczką": {"lemma": "przewodniczka", "translation": "экскурсовод", "part_of_speech": "существительное"},
        "kamienice": {"lemma": "kamienica", "translation": "старинный городской дом", "part_of_speech": "существительное"},
        "ratusz": {"lemma": "ratusz", "translation": "ратуша", "part_of_speech": "существительное"},
        "piernika": {"lemma": "piernik", "translation": "пряник", "part_of_speech": "существительное"},
        "dowiedzieli": {"lemma": "dowiedzieć się", "translation": "узнать", "part_of_speech": "глагол"},
        "dawniej": {"lemma": "dawniej", "translation": "раньше; в прошлом", "part_of_speech": "наречие"},
        "odbywał": {"lemma": "odbywać się", "translation": "проходить", "part_of_speech": "глагол"},
        "regionalnego": {"lemma": "regionalny", "translation": "региональный", "part_of_speech": "прилагательное"},
        "mieszkańcami": {"lemma": "mieszkaniec", "translation": "житель", "part_of_speech": "существительное"},
        "zmęczona": {"lemma": "zmęczony", "translation": "уставший", "part_of_speech": "прилагательное"},
        "atmosferę": {"lemma": "atmosfera", "translation": "атмосфера", "part_of_speech": "существительное"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(id="poland-around-us", defaults={"course": Course.objects.get(id="a2-independence"), "title": "Польша вокруг нас", "description": "Рассказываем о польском месте, традиции и местном событии", "emoji": "🇵🇱", "position": 10, "is_active": True})
    rows = (
        ("poland-words", "words", "Miejsca w Polsce", "Регионы и места", "8 карточек · A2", "Назови польские места и элементы городского пейзажа", 8, "🇵🇱"),
        ("poland-grammar", "grammar", "Opowiadamy po kolei", "Связный рассказ", "5 заданий · A2", "Связывай события в ясной последовательности", 9, "✏️"),
        ("poland-review", "review", "Tradycja i wydarzenie", "Традиции и события", "7 карточек · A2", "Повтори лексику путешествия и местной культуры", 7, "🔄"),
        ("poland-quiz", "quiz", "Quiz: Polska wokół nas", "Проверка темы", "8 вопросов · A2", "Проверь лексику и маркеры последовательности", 6, "🎯"),
        ("poland-reading-check", "quiz", "Czy rozumiesz wycieczkę?", "Понимание текста", "5 вопросов · A2", "Проверь детали поездки Майи в Торунь", 5, "📖"),
    )
    made = {}
    for position, row in enumerate(rows, 98):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["poland-grammar"]
    grammar.theory_title = "Как выстроить события по порядку"
    grammar.theory_sections = [
        ["Начало", "Najpierw вводит первое действие: Najpierw spotkaliśmy się na rynku."],
        ["Продолжение", "Potem, następnie и później показывают следующие этапы рассказа."],
        ["Связь и завершение", "Kiedy связывает события во времени, а na końcu вводит последний этап."],
    ]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 331):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("poland-words", cards[:8]), ("poland-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("poland-grammar", GRAMMAR), ("poland-quiz", QUIZ), ("poland-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "poland-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0029_a2_nature_weather_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
