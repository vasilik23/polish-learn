from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-29"}
CARDS = (
    ("office-urzad", "urząd", "государственное учреждение", "Jutro idę do urzędu miasta."),
    ("office-wniosek", "wniosek", "заявление", "Wniosek można złożyć przez internet."),
    ("office-formularz", "formularz", "бланк; форма", "Proszę wypełnić ten formularz."),
    ("office-dokument", "dokument tożsamości", "документ, удостоверяющий личность", "Trzeba okazać dokument tożsamości."),
    ("office-rubryka", "rubryka", "поле формы", "W tej rubryce wpisuje się adres."),
    ("office-podpis", "podpis", "подпись", "Na końcu potrzebny jest czytelny podpis."),
    ("office-zalacznik", "załącznik", "приложение к документу", "Do wniosku brakuje jednego załącznika."),
    ("office-termin", "termin", "срок; назначенное время", "Najbliższy wolny termin jest w środę."),
    ("office-zlozyc", "złożyć wniosek", "подать заявление", "Chciałbym złożyć wniosek o kartę mieszkańca."),
    ("office-odebrac", "odebrać dokument", "получить готовый документ", "Dokument będzie można odebrać za tydzień."),
    ("office-potwierdzenie", "potwierdzenie", "подтверждение", "Proszę zachować potwierdzenie złożenia wniosku."),
    ("office-numer", "numer sprawy", "номер дела", "Numer sprawy znajduje się na potwierdzeniu."),
    ("office-dane", "dane osobowe", "персональные данные", "Proszę sprawdzić, czy dane osobowe są poprawne."),
    ("office-wazny", "ważny", "действительный", "Paszport jest ważny do przyszłego roku."),
    ("office-brakowac", "brakować", "не хватать", "W formularzu brakuje daty urodzenia."),
)
GRAMMAR = (
    ("Как вежливо сказать «Я хотел бы подать заявление»?", ["Chciałbym złożyć wniosek.", "Chcę wniosek dawaj.", "Złożyłem by formularz."], 0, "Chciałbym/chciałabym — стандартная вежливая форма просьбы."),
    ("___ mi powiedzieć, gdzie jest pokój numer pięć?", ["Czy może pani", "Pani musi", "Czy pani daj"], 0, "Czy może pani…? — нейтральная официальная просьба."),
    ("Data 12.03.2026 to:", ["dwunasty marca dwa tysiące dwudziestego szóstego roku", "dwanaście marzec dwa tysiące dwadzieścia sześć", "dwunasta marcem dwa tysiące szósty"], 0, "В датах день — порядковое числительное, месяц обычно в родительном падеже."),
    ("Составьте: Пожалуйста, подпишите форму здесь.", ["Proszę podpisać formularz tutaj.", "Proszę podpisuje tutaj formularzem.", "Tutaj proszę formularz podpisany."], 0, "Формальная инструкция строится как proszę + инфинитив."),
    ("Wniosek należy złożyć do ___ maja.", ["piętnastego", "piętnaście", "piętnasty"], 0, "После do в обозначении срока используется родительный: do piętnastego maja."),
)
QUIZ = (
    ("Что означает załącznik?", ["приложение к документу", "очередь", "подпись"], 0, "Załącznik — дополнительный документ, приложенный к заявлению."),
    ("Gdzie wpisuje się adres?", ["w odpowiedniej rubryce", "na bilecie", "w recepcie"], 0, "Rubryka — отдельное поле формы."),
    ("Как вежливо попросить повторить?", ["Czy może pan powtórzyć?", "Powtarzaj natychmiast.", "Pan powtórzyłby jest."], 0, "Czy może pan…? сохраняет нейтральный официальный тон."),
    ("Dokument można odebrać ___ 20 kwietnia.", ["od", "o", "do"], 0, "Od + дата обозначает начало доступного периода."),
    ("Что подтверждает подачу заявления?", ["potwierdzenie złożenia wniosku", "numer pokoju", "ważny paszport"], 0, "После подачи выдают или отправляют подтверждение."),
    ("В форме не хватает подписи.", ["W formularzu brakuje podpisu.", "Formularz podpis jest brak.", "Podpis brakuje formularzem."], 0, "Brakować требует родительного: brakuje podpisu."),
    ("Termin wizyty jest ___ 8 maja.", ["na", "w", "z"], 0, "Назначенный срок оформляется: termin na + дата."),
    ("Что нужно проверить перед подачей?", ["czy dane są poprawne", "czy film jest ciekawy", "czy pogoda się zmieni"], 0, "В заявлении важно проверить корректность данных."),
)
CHECK = (
    ("Po co Natalia przyszła do urzędu?", ["Złożyć wniosek o kartę mieszkańca", "Odebrać receptę", "Kupić bilet"], 0, "Наталия пришла подать заявление на карту жителя."),
    ("Czego brakowało w formularzu?", ["Daty urodzenia", "Adresu urzędu", "Numeru pokoju"], 0, "Сотрудница заметила отсутствие даты рождения."),
    ("Jaki dokument Natalia okazała?", ["Paszport", "Bilet miesięczny", "Legitymację biblioteczną"], 0, "Для подтверждения личности Наталия показала паспорт."),
    ("Kiedy karta ma być gotowa?", ["Po około dwóch tygodniach", "Tego samego dnia", "Za pół roku"], 0, "Изготовление карты займёт около двух недель."),
    ("Po co Natalia zachowała potwierdzenie?", ["Jest na nim numer sprawy", "Daje zniżkę w kinie", "Zastępuje paszport"], 0, "В подтверждении указан номер дела для проверки статуса."),
)
READING = {
    "id": "natalia-sklada-wniosek",
    "title": "Natalia składa wniosek",
    "description": "Форма, документы и получение подтверждения",
    "level": "A2",
    "minutes": 6,
    "emoji": "🏛️",
    "position": 20,
    "paragraphs": [
        "Natalia umówiła wizytę w urzędzie miasta, ponieważ chciała złożyć wniosek o kartę mieszkańca. W domu pobrała formularz, wpisała dane osobowe i przygotowała wymagany załącznik. Przed wyjściem sprawdziła też termin ważności paszportu.",
        "W urzędzie pracownica poprosiła Natalię o dokument tożsamości. Potem razem przejrzały formularz. W jednej rubryce brakowało daty urodzenia, więc Natalia ją dopisała. Następnie podpisała wniosek i zapytała, kiedy karta będzie gotowa.",
        "Pracownica wyjaśniła, że dokument będzie można odebrać po około dwóch tygodniach. Natalia dostała potwierdzenie z numerem sprawy. Zachowała je, ponieważ dzięki temu numerowi może sprawdzić status wniosku przez internet i nie musi ponownie podawać wszystkich danych.",
    ],
    "glossary": {
        "umówiła": {"lemma": "umówić", "translation": "назначить", "part_of_speech": "глагол"},
        "pobrała": {"lemma": "pobrać", "translation": "скачать; получить", "part_of_speech": "глагол"},
        "wymagany": {"lemma": "wymagany", "translation": "обязательный", "part_of_speech": "прилагательное"},
        "ważności": {"lemma": "ważność", "translation": "срок действия", "part_of_speech": "существительное"},
        "przejrzały": {"lemma": "przejrzeć", "translation": "просмотреть", "part_of_speech": "глагол"},
        "rubryce": {"lemma": "rubryka", "translation": "поле формы", "part_of_speech": "существительное"},
        "dopisała": {"lemma": "dopisać", "translation": "дописать", "part_of_speech": "глагол"},
        "odebrać": {"lemma": "odebrać", "translation": "получить", "part_of_speech": "глагол"},
        "potwierdzenie": {"lemma": "potwierdzenie", "translation": "подтверждение", "part_of_speech": "существительное"},
        "wniosku": {"lemma": "wniosek", "translation": "заявление", "part_of_speech": "существительное"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(id="institutions", defaults={"course": Course.objects.get(id="a2-independence"), "title": "Учреждения", "description": "Заполняем форму и вежливо решаем вопрос в учреждении", "emoji": "🏛️", "position": 8, "is_active": True})
    rows = (
        ("office-words", "words", "W urzędzie", "Документы и форма", "8 карточек · A2", "Назови части заявления и необходимые документы", 8, "🏛️"),
        ("office-grammar", "grammar", "Uprzejmie i konkretnie", "Формальный регистр и даты", "5 заданий · A2", "Проси вежливо и правильно называй сроки", 9, "✏️"),
        ("office-review", "review", "Od wniosku do odbioru", "Подача и получение", "7 карточек · A2", "Повтори действия и статусы обращения", 7, "🔄"),
        ("office-quiz", "quiz", "Quiz: w urzędzie", "Проверка темы", "8 вопросов · A2", "Проверь лексику, даты и вежливые просьбы", 6, "🎯"),
        ("office-reading-check", "quiz", "Czy rozumiesz procedurę?", "Понимание текста", "5 вопросов · A2", "Проверь детали визита Наталии", 5, "📖"),
    )
    made = {}
    for position, row in enumerate(rows, 88):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["office-grammar"]
    grammar.theory_title = "Вежливые просьбы, инструкции и даты"
    grammar.theory_sections = [
        ["Вежливая просьба", "Chciałbym/chciałabym… и Czy może pan/pani… смягчают официальный вопрос."],
        ["Инструкция", "Proszę + инфинитив: Proszę podpisać formularz."],
        ["Срок и дата", "Do + родительный задаёт крайний срок: do piętnastego maja."],
    ]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 301):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("office-words", cards[:8]), ("office-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("office-grammar", GRAMMAR), ("office-quiz", QUIZ), ("office-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "office-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0027_a2_culture_media_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
