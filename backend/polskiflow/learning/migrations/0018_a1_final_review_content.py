from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-28"}
CARDS = (
    ("final-przedstawic", "przedstawić się", "представиться", "Na początku krótko się przedstawiam."),
    ("final-pochodzic", "pochodzić", "быть родом", "Pochodzę z Ukrainy, ale mieszkam w Polsce."),
    ("final-rodzina", "rodzina", "семья", "Moja rodzina mieszka blisko."),
    ("final-codziennie", "codziennie", "каждый день", "Codziennie rano piję herbatę."),
    ("final-mieszkanie", "mieszkanie", "квартира", "Moje mieszkanie ma dwa pokoje."),
    ("final-poprosic", "poprosić", "попросить", "Chcę poprosić o wodę."),
    ("final-droga", "droga", "дорога; путь", "Czy to dobra droga do centrum?"),
    ("final-spotkanie", "spotkanie", "встреча", "Mamy spotkanie o piątej."),
    ("final-pracowac", "pracować", "работать", "Pracuję od poniedziałku do piątku."),
    ("final-uczyc", "uczyć się", "учиться", "Wieczorem uczę się polskiego."),
    ("final-odpoczywac", "odpoczywać", "отдыхать", "W weekend lubię odpoczywać."),
    ("final-potrzebowac", "potrzebować", "нуждаться", "Potrzebuję pomocy."),
    ("final-umawiac", "umawiać się", "договариваться о встрече", "Umawiamy się na sobotę."),
    ("final-czuc", "czuć się", "чувствовать себя", "Dzisiaj czuję się dobrze."),
    ("final-zalatwic", "załatwić", "уладить; сделать", "Muszę załatwić jedną sprawę."),
    ("final-poradzic", "poradzić sobie", "справиться", "Potrafię poradzić sobie po polsku."),
)
GRAMMAR = (
    ("Ja ___ z Polski.", ["jestem", "jesteś", "są"], 0, "Для ja форма być — jestem."),
    ("To jest ___ siostra.", ["mój", "moja", "moje"], 1, "Siostra — женский род, поэтому moja."),
    ("Codziennie Anna ___ o siódmej.", ["wstaję", "wstaje", "wstajesz"], 1, "Для Anna/ona нужна форма wstaje."),
    ("Poproszę ___.", ["kawa", "kawę", "kawą"], 1, "После poproszę предмет стоит в винительном падеже: kawę."),
    ("Spotykamy się ___ poniedziałek ___ osiemnastej.", ["w, o", "o, w", "na, z"], 0, "С днём употребляем w, со временем — o."),
    ("Boli mnie ___, ale bolą mnie ___.", ["głowę, noga", "głowa, nogi", "głowy, nogę"], 1, "Boli сочетается с единственным числом, bolą — с множественным."),
)
QUIZ = (
    ("Как естественно представиться?", ["Mam na imię Lena.", "Jest imię Lena.", "Nazywam do Lena."], 0, "Mam na imię… — базовая форма представления."),
    ("On ___ po polsku.", ["mówię", "mówisz", "mówi"], 2, "Для on форма глагола mówić — mówi."),
    ("To są ___ rodzice.", ["mój", "moja", "moi"], 2, "Во множественном числе о людях: moi rodzice."),
    ("Rano najpierw ___, potem jem śniadanie.", ["wstaję", "wstaje", "wstajesz"], 0, "Для ja употребляем wstaję."),
    ("Książka jest ___ stole.", ["w", "na", "do"], 1, "Предмет находится na stole."),
    ("Poproszę kilogram ___.", ["jabłka", "jabłek", "jabłkami"], 1, "После количества употребляется родительный падеж: kilogram jabłek."),
    ("Как спросить дорогу?", ["Jak dojść do dworca?", "Jaki dworzec robi?", "Gdzie idziesz dworzec?"], 0, "Jak dojść do…? — естественный вопрос о маршруте."),
    ("Spotkanie jest ___ środę ___ piętnastej.", ["w, o", "o, w", "na, od"], 0, "W środę, o piętnastej."),
    ("Muszę ___ raport.", ["kończę", "skończyć", "skończy"], 1, "После muszę ставим инфинитив."),
    ("Lubię ___ książki.", ["czytać", "czytam", "czyta"], 0, "После lubię действие выражается инфинитивом."),
    ("Bolą mnie ___.", ["gardło", "plecy", "głowa"], 1, "Plecy имеют форму множественного числа."),
    ("Что показывает готовность действовать самостоятельно?", ["Potrafię poradzić sobie po polsku.", "Nie znam żadnego słowa.", "Zawsze potrzebuję tłumacza."], 0, "Фраза означает «Я умею справиться на польском»."),
)
READING = {
    "id": "samodzielny-dzien-leny",
    "title": "Samodzielny dzień Leny",
    "description": "Лена решает несколько повседневных задач по-польски",
    "level": "A1",
    "minutes": 5,
    "emoji": "🏁",
    "position": 11,
    "paragraphs": [
        "Lena pochodzi z Ukrainy i od roku mieszka w Krakowie. Dzisiaj ma dużo planów. Rano dzwoni do przychodni, bo boli ją gardło. Umawia się z lekarzem na czwartek o dziewiątej.",
        "Potem Lena idzie do sklepu. Kupuje chleb, mleko i kilogram jabłek. Pyta też sprzedawcę o aptekę. Apteka jest blisko: trzeba iść prosto, a potem skręcić w lewo.",
        "Po pracy Lena spotyka się z koleżanką w kawiarni. Rozmawiają o rodzinie, pracy i planach na weekend. Lena zamawia herbatę i mówi, że lubi czytać polskie książki. Wieczorem wraca do domu i jest zadowolona: wszystkie sprawy załatwiła po polsku.",
    ],
    "glossary": {
        "pochodzi": {"lemma": "pochodzić", "translation": "быть родом", "part_of_speech": "глагол"},
        "przychodni": {"lemma": "przychodnia", "translation": "поликлиника", "part_of_speech": "существительное"},
        "umawia": {"lemma": "umawiać się", "translation": "договариваться о встрече", "part_of_speech": "глагол"},
        "sprzedawcę": {"lemma": "sprzedawca", "translation": "продавец", "part_of_speech": "существительное"},
        "skręcić": {"lemma": "skręcić", "translation": "повернуть", "part_of_speech": "глагол"},
        "koleżanką": {"lemma": "koleżanka", "translation": "подруга; знакомая", "part_of_speech": "существительное"},
        "zamawia": {"lemma": "zamawiać", "translation": "заказывать", "part_of_speech": "глагол"},
        "zadowolona": {"lemma": "zadowolony", "translation": "довольный", "part_of_speech": "прилагательное"},
        "sprawy": {"lemma": "sprawa", "translation": "дело", "part_of_speech": "существительное"},
        "załatwiła": {"lemma": "załatwić", "translation": "уладить; сделать", "part_of_speech": "глагол"},
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
    Topic.objects.filter(course=course, position__gte=11).update(position=12)
    topic, _ = Topic.objects.update_or_create(
        id="a1-final-review",
        defaults={"course": course, "title": "Повторение A1", "description": "Соединяем пройденные темы и проверяем готовность к повседневным ситуациям", "emoji": "🏁", "position": 11, "is_active": True},
    )
    rows = (
        ("final-words", "words", "A1: najważniejsze", "Ключевые слова A1", "8 карточек · A1", "Повтори опорные слова бытового общения", 7, "🏁"),
        ("final-grammar", "grammar", "A1 w praktyce", "Грамматика в ситуациях", "6 заданий · A1", "Соедини основные конструкции уровня", 9, "✏️"),
        ("final-review", "review", "Codzienne sytuacje", "Самостоятельное общение", "8 карточек · A1", "Закрепи действия для реальных задач", 7, "🔄"),
        ("final-quiz", "quiz", "Diagnoza A1", "Итоговая диагностика", "12 вопросов · A1", "Проверь все темы и готовность к A2", 8, "🎯"),
    )
    made = {}
    for position, row in enumerate(rows, 44):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["final-grammar"]
    grammar.theory_title = "A1 — связываем знакомые конструкции"
    grammar.theory_sections = [
        ["О себе", "Согласуй лицо глагола: jestem, mieszkam, pracuję, lubię; для on/ona: jest, mieszka, pracuje, lubi."],
        ["Предметы и места", "Проверяй род и падеж: moja siostra, poproszę kawę, w domu, na stole."],
        ["Время, возможность и здоровье", "W poniedziałek o ósmej; mogę/muszę + инфинитив; boli + одно, bolą + множественное число."],
    ]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 165):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("final-words", cards[:8]), ("final-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("final-grammar", GRAMMAR), ("final-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(
        id=READING["id"],
        defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": SOURCE, "is_active": True},
    )


class Migration(migrations.Migration):
    dependencies = [("learning", "0017_a1_health_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
