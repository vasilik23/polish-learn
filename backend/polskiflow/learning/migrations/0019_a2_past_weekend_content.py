from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-28"}
CARDS = (
    ("past-weekend", "weekend", "выходные", "W weekend byliśmy poza miastem."),
    ("past-wczoraj", "wczoraj", "вчера", "Wczoraj długo pracowałam."),
    ("past-przedwczoraj", "przedwczoraj", "позавчера", "Przedwczoraj spotkałem znajomych."),
    ("past-ostatnio", "ostatnio", "в последнее время", "Ostatnio często chodziliśmy do kina."),
    ("past-wycieczka", "wycieczka", "экскурсия; поездка", "Wycieczka była bardzo udana."),
    ("past-koncert", "koncert", "концерт", "W sobotę byliśmy na koncercie."),
    ("past-muzeum", "muzeum", "музей", "W niedzielę zwiedziliśmy muzeum."),
    ("past-odpoczynek", "odpoczynek", "отдых", "Po podróży potrzebowałam odpoczynku."),
    ("past-spedzic", "spędzić", "провести (время)", "Spędziliśmy weekend w górach."),
    ("past-pojechac", "pojechać", "поехать", "Rano pojechaliśmy pociągiem."),
    ("past-odwiedzic", "odwiedzić", "навестить; посетить", "Odwiedziłam babcię w sobotę."),
    ("past-zobaczyc", "zobaczyć", "увидеть", "Zobaczyliśmy stary zamek."),
    ("past-spotkac", "spotkać się", "встретиться", "Wieczorem spotkałem się z kolegą."),
    ("past-wrocic", "wrócić", "вернуться", "Wróciliśmy późno do domu."),
    ("past-wydarzyc", "wydarzyć się", "произойти", "Co wydarzyło się w weekend?"),
)
GRAMMAR = (
    ("В субботу Марек работал дома.", ["W sobotę Marek pracował w domu.", "W sobotę Marek pracowała w domu.", "W sobotę Marek pracuje w domu."], 0, "В мужском роде прошедшее время имеет окончание -ł: pracował."),
    ("Ania ___ do kina.", ["poszedł", "poszła", "poszli"], 1, "Для Ania нужна женская форма poszła."),
    ("My (мужчина и женщина) ___ w Krakowie.", ["byliśmy", "byłyśmy", "byłem"], 0, "Для смешанной группы употребляется форма męskoosobowa: byliśmy."),
    ("Kasia i Ola ___ muzeum.", ["zwiedzili", "zwiedziły", "zwiedziła"], 1, "Для группы только из женщин нужна форма niemęskoosobowa: zwiedziły."),
    ("Ja (женщина) długo ___.", ["odpoczywałem", "odpoczywałam", "odpoczywali"], 1, "Говорящая женщина выбирает форму odpoczywałam."),
)
QUIZ = (
    ("Что означает przedwczoraj?", ["завтра", "позавчера", "недавно"], 1, "Przedwczoraj — позавчера."),
    ("Paweł ___ film.", ["oglądał", "oglądała", "oglądali"], 0, "Paweł — мужской род: oglądał."),
    ("Ewa ___ książkę.", ["czytał", "czytała", "czytali"], 1, "Ewa — женский род: czytała."),
    ("Tomek i Adam ___ na koncert.", ["poszły", "poszli", "poszedł"], 1, "Группа мужчин: poszli."),
    ("Mama i córka ___ w domu.", ["zostały", "zostali", "została"], 0, "Группа женщин: zostały."),
    ("Как спросить о прошлых выходных?", ["Co robiłeś w weekend?", "Co robisz jutro?", "Gdzie robi weekend?"], 0, "Co robiłeś/robiłaś w weekend? — вопрос о завершённом прошлом."),
    ("My (смешанная группа) ___ późno.", ["wróciliśmy", "wróciłyśmy", "wróciłem"], 0, "Для смешанной группы: wróciliśmy."),
    ("Ja (мужчина) ___ weekend w domu.", ["spędziłam", "spędziłem", "spędzili"], 1, "Мужская форма первого лица: spędziłem."),
)
READING = {
    "id": "weekend-kasi-i-pawla",
    "title": "Weekend Kasi i Pawła",
    "description": "Два разных рассказа о прошедших выходных",
    "level": "A2",
    "minutes": 5,
    "emoji": "📆",
    "position": 12,
    "paragraphs": [
        "W piątek po pracy Kasia pojechała pociągiem do Wrocławia. Odwiedziła koleżankę ze studiów. Wieczorem poszły razem na mały koncert, a potem długo rozmawiały w kawiarni.",
        "W sobotę Kasia i jej koleżanka zwiedziły muzeum i zobaczyły rynek. Pogoda była słoneczna, więc dużo spacerowały. Kasia wróciła do Krakowa w niedzielę wieczorem. Była zmęczona, ale bardzo zadowolona.",
        "Paweł spędził weekend inaczej. Został w domu, ugotował obiad i obejrzał dwa filmy. W niedzielę spotkał się z bratem i razem pojechali na rowerach do parku. Paweł odpoczął i w poniedziałek miał dużo energii.",
    ],
    "glossary": {
        "pojechała": {"lemma": "pojechać", "translation": "поехать", "part_of_speech": "глагол"},
        "odwiedziła": {"lemma": "odwiedzić", "translation": "навестить", "part_of_speech": "глагол"},
        "poszły": {"lemma": "pójść", "translation": "пойти", "part_of_speech": "глагол"},
        "zwiedziły": {"lemma": "zwiedzić", "translation": "осмотреть; посетить", "part_of_speech": "глагол"},
        "rynek": {"lemma": "rynek", "translation": "рыночная площадь", "part_of_speech": "существительное"},
        "spacerowały": {"lemma": "spacerować", "translation": "гулять", "part_of_speech": "глагол"},
        "zmęczona": {"lemma": "zmęczony", "translation": "уставший", "part_of_speech": "прилагательное"},
        "spędził": {"lemma": "spędzić", "translation": "провести (время)", "part_of_speech": "глагол"},
        "ugotował": {"lemma": "ugotować", "translation": "приготовить", "part_of_speech": "глагол"},
        "obejrzał": {"lemma": "obejrzeć", "translation": "посмотреть", "part_of_speech": "глагол"},
        "odpoczął": {"lemma": "odpocząć", "translation": "отдохнуть", "part_of_speech": "глагол"},
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
    course, _ = Course.objects.update_or_create(
        id="a2-independence",
        defaults={"title": "Самостоятельность", "description": "Связное общение в знакомых повседневных ситуациях", "level": "A2", "position": 1, "is_active": True},
    )
    Topic.objects.filter(course=course, position__gte=0).update(position=1)
    topic, _ = Topic.objects.update_or_create(
        id="past-weekend",
        defaults={"course": course, "title": "Прошедшие выходные", "description": "Рассказываем о завершённых событиях и впечатлениях", "emoji": "📆", "position": 0, "is_active": True},
    )
    rows = (
        ("past-words", "words", "Miniony weekend", "События выходных", "8 карточек · A2", "Назови время, места и впечатления", 7, "📆"),
        ("past-grammar", "grammar", "Co robiłeś?", "Прошедшее время", "5 заданий · A2", "Согласуй прошедшую форму с родом и группой", 9, "✏️"),
        ("past-review", "review", "Jak było?", "Рассказ о прошлом", "7 карточек · A2", "Расскажи, куда ездил и что делал", 7, "🔄"),
        ("past-quiz", "quiz", "Quiz: miniony weekend", "Проверка темы", "8 вопросов · A2", "Проверь формы прошедшего времени", 6, "🎯"),
    )
    made = {}
    for position, row in enumerate(rows, 48):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["past-grammar"]
    grammar.theory_title = "Byłem, byłam — что происходило раньше"
    grammar.theory_sections = [
        ["Он и она", "В единственном числе форма показывает род: on pracował/był, ona pracowała/była."],
        ["Я", "Говорящий выбирает форму по своему роду: robiłem/byłem или robiłam/byłam."],
        ["Мы и они", "Для группы с мужчиной: byliśmy, robili; для группы только из женщин/предметов: byłyśmy, robiły."],
    ]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 181):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("past-words", cards[:8]), ("past-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("past-grammar", GRAMMAR), ("past-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(
        id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": SOURCE, "is_active": True}
    )


class Migration(migrations.Migration):
    dependencies = [("learning", "0018_a1_final_review_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
