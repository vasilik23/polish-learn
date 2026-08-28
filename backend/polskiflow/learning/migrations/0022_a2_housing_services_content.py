from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-28"}
CARDS = (
    ("housing-mieszkanie", "mieszkanie", "квартира", "Szukamy mieszkania blisko centrum."),
    ("housing-wynajmowac", "wynajmować", "снимать; сдавать", "Chcemy wynajmować to mieszkanie przez rok."),
    ("housing-czynsz", "czynsz", "арендная плата", "Czynsz wynosi trzy tysiące złotych."),
    ("housing-kaucja", "kaucja", "залог", "Właściciel prosi o miesięczną kaucję."),
    ("housing-umowa", "umowa", "договор", "Przeczytam umowę przed podpisaniem."),
    ("housing-wlasciciel", "właściciel", "владелец", "Właściciel mieszkania mieszka za granicą."),
    ("housing-ogrzewanie", "ogrzewanie", "отопление", "Ogrzewanie nie działa od rana."),
    ("housing-usterka", "usterka", "неисправность", "Zgłosiłam usterkę administracji."),
    ("housing-naprawa", "naprawa", "ремонт; починка", "Naprawa potrwa około godziny."),
    ("housing-hydraulik", "hydraulik", "сантехник", "Hydraulik sprawdzi kran w kuchni."),
    ("housing-prad", "prąd", "электричество", "W łazience nie ma prądu."),
    ("housing-woda", "ciepła woda", "горячая вода", "Od wczoraj nie ma ciepłej wody."),
    ("housing-zglaszac", "zgłaszać", "сообщать; заявлять", "Proszę zgłaszać problemy telefonicznie."),
    ("housing-administracja", "administracja", "управляющая компания", "Administracja odpowie jutro rano."),
    ("housing-termin", "termin", "срок; назначенное время", "Ustaliliśmy termin naprawy na wtorek."),
)
GRAMMAR = (
    ("W mieszkaniu nie ma ___.", ["ciepła woda", "ciepłej wody", "ciepłą wodą"], 1, "После nie ma употребляется родительный падеж: ciepłej wody."),
    ("Szukamy małego ___.", ["mieszkanie", "mieszkaniem", "mieszkania"], 2, "Глагол szukać требует родительного падежа: szukamy mieszkania."),
    ("Mamy problem z ___.", ["ogrzewaniem", "ogrzewania", "ogrzewanie"], 0, "После z в значении «с чем?» нужен творительный падеж: z ogrzewaniem."),
    ("Разговариваю с владельцем.", ["Rozmawiam z właścicielem.", "Rozmawiam z właściciela.", "Rozmawiam właściciel."], 0, "После z в значении совместности употребляется творительный: z właścicielem."),
    ("Potrzebujemy ___.", ["hydraulik", "hydraulika", "hydraulikiem"], 1, "Potrzebować требует родительного падежа: potrzebujemy hydraulika."),
)
QUIZ = (
    ("Что означает kaucja?", ["отопление", "залог", "счётчик"], 1, "Kaucja — залог, который обычно возвращают после окончания аренды."),
    ("Nie ma ___.", ["prądu", "prądem", "prąd"], 0, "Отрицательная конструкция nie ma требует родительного: prądu."),
    ("Problem z ___.", ["kran", "kranu", "kranem"], 2, "После z в конструкции problem z нужен творительный: kranem."),
    ("Куда сообщить о неисправности?", ["Zgłosić usterkę administracji.", "Wynająć hydraulika umową.", "Szukać czynsz z wodą."], 0, "Zgłosić usterkę administracji — сообщить управляющей компании о неисправности."),
    ("Szukamy ___.", ["nowego mieszkania", "nowym mieszkaniem", "nowe mieszkanie"], 0, "Szukać управляет родительным падежом: nowego mieszkania."),
    ("Rozmawiam z ___.", ["hydraulika", "hydraulikiem", "hydraulik"], 1, "Лицо после z ставится в творительном падеже: z hydraulikiem."),
    ("Что обычно подписывают при аренде?", ["usterkę", "umowę", "ogrzewanie"], 1, "При аренде стороны подписывают umowę — договор."),
    ("Ustaliliśmy ___ naprawy.", ["termin", "czynszem", "kaucji nie ma"], 0, "Ustalić termin naprawy — назначить время ремонта."),
)
COMPREHENSION = (
    ("Jaki problem zauważyła Lena?", ["Nie działało ogrzewanie", "Zgubiła umowę", "Nie miała kluczy"], 0, "Утром Лена заметила, что отопление не работает."),
    ("Do kogo Lena najpierw zadzwoniła?", ["Do koleżanki", "Do właściciela", "Do hydraulika"], 1, "Сначала она позвонила владельцу квартиры."),
    ("Dlaczego właściciel poprosił o wiadomość?", ["Potrzebował opisu usterki", "Chciał podnieść czynsz", "Szukał nowego mieszkania"], 0, "Ему нужны были описание проблемы и фотография счётчика."),
    ("Kiedy fachowiec ma przyjść?", ["W poniedziałek rano", "We wtorek między 16 a 18", "W niedzielę wieczorem"], 1, "Администрация назначила визит на вторник с 16 до 18."),
    ("Co Lena zrobi, jeśli naprawa się opóźni?", ["Wyprowadzi się natychmiast", "Podpisze nową umowę", "Ponownie skontaktuje się z administracją"], 2, "Если специалист не придёт вовремя, она снова свяжется с администрацией."),
)
READING = {
    "id": "usterka-w-mieszkaniu", "title": "Usterka w mieszkaniu", "description": "Лена договаривается о ремонте отопления", "level": "A2", "minutes": 5, "emoji": "🔧", "position": 14,
    "paragraphs": [
        "Lena wynajmuje małe mieszkanie w Poznaniu. W poniedziałek rano zauważyła, że ogrzewanie nie działa, a w sypialni jest bardzo zimno. Najpierw zadzwoniła do właściciela. Powiedziała, że od wieczora nie ma ciepłych kaloryferów i potrzebuje szybkiej pomocy.",
        "Właściciel poprosił Lenę o krótką wiadomość z opisem usterki i zdjęciem licznika. Potem zgłosił problem administracji. Po godzinie administracja odpowiedziała, że fachowiec może przyjść we wtorek między szesnastą a osiemnastą. Lena potwierdziła termin i zapytała, czy naprawa będzie płatna.",
        "Zgodnie z umową właściciel zapłaci za naprawę ogrzewania. Lena będzie rozmawiać z fachowcem i pokaże mu kaloryfer w sypialni. Jeśli fachowiec się spóźni, ponownie skontaktuje się z administracją. Lena ma nadzieję, że wieczorem mieszkanie znów będzie ciepłe.",
    ],
    "glossary": {
        "wynajmuje": {"lemma": "wynajmować", "translation": "снимать", "part_of_speech": "глагол"}, "zauważyła": {"lemma": "zauważyć", "translation": "заметить", "part_of_speech": "глагол"},
        "ogrzewanie": {"lemma": "ogrzewanie", "translation": "отопление", "part_of_speech": "существительное"}, "kaloryferów": {"lemma": "kaloryfer", "translation": "радиатор", "part_of_speech": "существительное"},
        "usterki": {"lemma": "usterka", "translation": "неисправность", "part_of_speech": "существительное"}, "licznika": {"lemma": "licznik", "translation": "счётчик", "part_of_speech": "существительное"},
        "fachowiec": {"lemma": "fachowiec", "translation": "специалист", "part_of_speech": "существительное"}, "potwierdziła": {"lemma": "potwierdzić", "translation": "подтвердить", "part_of_speech": "глагол"},
        "płatna": {"lemma": "płatny", "translation": "платный", "part_of_speech": "прилагательное"}, "zgodnie": {"lemma": "zgodnie z", "translation": "согласно", "part_of_speech": "выражение"},
        "spóźni": {"lemma": "spóźnić się", "translation": "опоздать", "part_of_speech": "глагол"}, "ponownie": {"lemma": "ponownie", "translation": "повторно", "part_of_speech": "наречие"},
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
    topic, _ = Topic.objects.update_or_create(id="housing-services", defaults={"course": course, "title": "Жильё и услуги", "description": "Обсуждаем аренду и договариваемся о бытовом ремонте", "emoji": "🔧", "position": 2, "is_active": True})
    rows = (
        ("housing-words", "words", "Mieszkanie do wynajęcia", "Аренда жилья", "8 карточек · A2", "Обсуди квартиру, договор и условия оплаты", 7, "🏠"),
        ("housing-grammar", "grammar", "Nie ma ogrzewania", "Проблема в квартире", "5 заданий · A2", "Используй родительный и творительный падежи", 9, "✏️"),
        ("housing-review", "review", "Zgłaszam usterkę", "Ремонт и услуги", "7 карточек · A2", "Сообщи о проблеме и назначь время ремонта", 7, "🔄"),
        ("housing-quiz", "quiz", "Quiz: mieszkanie", "Проверка темы", "8 вопросов · A2", "Проверь лексику аренды и падежное управление", 6, "🎯"),
        ("housing-reading-check", "quiz", "Czy rozumiesz zgłoszenie?", "Понимание текста", "5 вопросов · A2", "Проверь детали обращения Лены", 5, "📖"),
    )
    made = {}
    for position, row in enumerate(rows, 58):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["housing-grammar"]
    grammar.theory_title = "Nie ma wody, problem z ogrzewaniem"
    grammar.theory_sections = [["Родительный после отрицания", "После nie ma: nie ma prądu, ciepłej wody, ogrzewania."], ["Глагольное управление", "Szukać и potrzebować требуют родительного: szukam mieszkania, potrzebuję hydraulika."], ["Творительный после z", "Когда z означает «с»: problem z ogrzewaniem, rozmowa z właścicielem."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 211):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("housing-words", cards[:8]), ("housing-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("housing-grammar", GRAMMAR), ("housing-quiz", QUIZ), ("housing-reading-check", COMPREHENSION)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "housing-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0021_a2_travel_plans_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
