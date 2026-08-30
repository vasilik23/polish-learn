from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}

SPEC = {
    "id": "b2-professional-communication", "title": "Профессиональная коммуникация",
    "description": "Проводим рабочую встречу и пишем точное деловое сообщение", "emoji": "💼", "position": 2,
    "prefix": "b2prof", "lesson_start": 178, "card_start": 572,
    "theory": ("Регистр, номинализация и этикет", [
        ["Регистр", "В деловой переписке просьбу смягчают формулы Zwracam się z prośbą o… и Czy mogliby Państwo…"],
        ["Номинализация", "Существительные на -anie/-enie уплотняют сообщение: omówić plan → omówienie planu."],
        ["Результат встречи", "Фиксируй decyzję, osobę odpowiedzialną и termin, используя bezosobowe ustalono/uzgodniono."],
    ]),
    "cards": (
        ("porządek obrad", "повестка встречи", "Porządek obrad wysłano dzień wcześniej."),
        ("zabrać głos", "взять слово", "Czy mogę zabrać głos w tej sprawie?"),
        ("ustalić priorytety", "определить приоритеты", "Najpierw ustalmy priorytety zespołu."),
        ("zgłosić zastrzeżenie", "высказать возражение", "Aneta zgłosiła zastrzeżenie do harmonogramu."),
        ("dojść do porozumienia", "достичь соглашения", "Po dyskusji doszliśmy do porozumienia."),
        ("podsumowanie", "резюме, итог", "Wyślę krótkie podsumowanie spotkania."),
        ("termin realizacji", "срок выполнения", "Termin realizacji przypada na piątek."),
        ("osoba odpowiedzialna", "ответственное лицо", "Każde zadanie ma osobę odpowiedzialną."),
        ("w nawiązaniu do", "в продолжение, ссылаясь на", "Piszę w nawiązaniu do naszej rozmowy."),
        ("zwracać się z prośbą", "обращаться с просьбой", "Zwracam się z prośbą o potwierdzenie."),
        ("uprzejmie przypominać", "вежливо напоминать", "Uprzejmie przypominam o terminie."),
        ("załącznik", "вложение", "Szczegóły znajdują się w załączniku."),
        ("uzgodnienie", "согласование", "Uzgodnienie warunków zajęło dwa dni."),
        ("wdrożenie", "внедрение", "Wdrożenie rozwiązania rozpocznie się w maju."),
        ("pozostawać do dyspozycji", "оставаться в распоряжении", "W razie pytań pozostaję do dyspozycji."),
    ),
    "grammar": (
        ("___ z prośbą o przesłanie poprawionej wersji umowy.", ["Zwracam się", "Żądam się", "Mówię się"], 0, "Zwracam się z prośbą o — нейтральная формальная просьба."),
        ("Czasownik «omówić» można zastąpić nominalizacją ___.", ["omówienie", "omawiający", "omówiony"], 0, "Omówienie — отглагольное существительное, называющее процесс."),
        ("Na spotkaniu ___, że raport przygotuje dział analiz.", ["ustalono", "ustalił się", "ustalając"], 0, "Ustalono — безличная форма на -no, фокусирующая решение, а не исполнителя."),
        ("Proszę ___ potwierdzenie terminu do środy.", ["o", "na", "za"], 0, "Формула prosić o требует винительного падежа."),
        ("Составьте: В продолжение нашей встречи отправляю согласованное резюме.", ["W nawiązaniu do naszego spotkania przesyłam uzgodnione podsumowanie.", "Nawiązując nasze spotkanie wysyłam podsumowaniem.", "Do spotkania przesyłam uzgodnić podsumowanie."], 0, "W nawiązaniu do + родительный задаёт формальную связь с предыдущим контактом."),
        ("Составьте: Было решено перенести внедрение на следующий месяц.", ["Ustalono, że wdrożenie zostanie przesunięte na przyszły miesiąc.", "Ustalili wdrożenie przesuwa przyszły miesiąc.", "Wdrożenie ustalając przesunęło miesiącem."], 0, "Ustalono и пассив zostanie przesunięte сохраняют официальный безличный регистр."),
    ),
    "quiz": (
        ("Что означает porządek obrad?", ["повестка встречи", "трудовой договор", "отпуск"], 0, "Это список вопросов для обсуждения."),
        ("Jak grzecznie wejść do dyskusji?", ["Czy mogę zabrać głos?", "Przestańcie mówić!", "Ja teraz."], 0, "Вопрос уважает очередь и участников."),
        ("Po spotkaniu warto wysłać ___.", ["podsumowanie", "zastrzeżać", "dyspozycję się"], 0, "Резюме фиксирует решения и следующие шаги."),
        ("Uprzejmie ___ o jutrzejszym terminie.", ["przypominam", "żądam", "rozkazuję"], 0, "Uprzejmie przypominam — корректная деловая формула."),
        ("Która forma jest nominalizacją?", ["wdrożenie", "wdrażać", "wdrożony"], 0, "Wdrożenie — существительное, называющее процесс."),
        ("Na końcu protokołu wpisujemy ___.", ["osoby odpowiedzialne i terminy", "tylko powitanie", "prywatne komentarze"], 0, "Так решение становится исполнимым."),
        ("Proszę o przesłanie ___.", ["załącznika", "załącznikiem", "załącznikowi"], 0, "Отглагольное существительное przesłanie управляет родительным: przesłanie czego? załącznika."),
        ("Co znaczy zgłosić zastrzeżenie?", ["высказать обоснованное возражение", "подтвердить отпуск", "закрыть встречу"], 0, "Zastrzeżenie сообщает о риске или несогласии."),
        ("Które zakończenie e-maila jest profesjonalne?", ["W razie pytań pozostaję do dyspozycji.", "No to pa!", "Odpisz natychmiast!!!"], 0, "Первая формула нейтральна и вежлива."),
        ("Uzgodniono nowy termin — na czym skupia się zdanie?", ["на достигнутом решении", "на имени автора", "на эмоциях адресата"], 0, "Безличная форма выдвигает результат на первый план."),
    ),
    "reading": {
        "id": "b2prof-spotkanie-ktore-konczy-sie-decyzja", "title": "Spotkanie, które kończy się decyzją",
        "description": "Как команда превратила сложное обсуждение в ясный план", "emoji": "💼", "minutes": 10,
        "paragraphs": [
            "Zespół Mai przygotowywał wdrożenie nowego systemu obsługi klientów. Przed spotkaniem wszyscy otrzymali porządek obrad, projekt harmonogramu oraz pytania wymagające decyzji. Maja, która prowadziła rozmowę, poprosiła uczestników, by najpierw ustalili priorytety, a dopiero później omawiali szczegóły techniczne.",
            "Kiedy przedstawiciel działu sprzedaży zabrał głos, zgłosił zastrzeżenie do terminu realizacji. Uważał, że pracownicy nie zdążą przejść szkolenia. Zamiast odrzucić uwagę, Maja poprosiła o konkretne dane. Po krótkiej analizie uzgodniono podział wdrożenia na dwa etapy, dzięki czemu zespół doszedł do porozumienia.",
            "Na zakończenie Maja przeczytała decyzje na głos. Każde zadanie otrzymało termin realizacji i osobę odpowiedzialną. Ustalono również, że ryzyka zostaną ponownie omówione za tydzień. Takie bezosobowe sformułowania pozwoliły skupić protokół na rezultatach, choć odpowiedzialność poszczególnych osób nadal była wyraźna.",
            "Po spotkaniu Maja wysłała wiadomość: „W nawiązaniu do dzisiejszej rozmowy przesyłam podsumowanie. Uprzejmie proszę o zgłoszenie uwag do środy”. Dołączyła harmonogram w załączniku i zakończyła e-mail formułą „W razie pytań pozostaję do dyspozycji”. Dzięki temu uczestnicy wiedzieli nie tylko, co ustalono, lecz także jaki jest kolejny krok.",
        ],
        "glossary": {
            "wdrożenie": ("wdrożenie", "внедрение", "существительное"), "obsługi": ("obsługa", "обслуживание", "существительное"),
            "porządek": ("porządek", "порядок", "существительное"), "wymagające": ("wymagać", "требующие", "причастие"),
            "prowadziła": ("prowadzić", "вела", "глагол"), "ustalili": ("ustalić", "определили", "глагол"),
            "zastrzeżenie": ("zastrzeżenie", "возражение", "существительное"), "zdążą": ("zdążyć", "успеют", "глагол"),
            "odrzucić": ("odrzucić", "отклонить", "глагол"), "uzgodniono": ("uzgodnić", "согласовали", "глагол"),
            "etapy": ("etap", "этапы", "существительное"), "doszedł": ("dojść", "достиг", "глагол"),
            "zakończenie": ("zakończenie", "завершение", "существительное"), "odpowiedzialną": ("odpowiedzialny", "ответственную", "прилагательное"),
            "ryzyka": ("ryzyko", "риски", "существительное"), "sformułowania": ("sformułowanie", "формулировки", "существительное"),
            "poszczególnych": ("poszczególny", "отдельных", "прилагательное"), "przesyłam": ("przesyłać", "отправляю", "глагол"),
        },
        "check": (
            ("Co uczestnicy otrzymali przed spotkaniem?", ["Porządek obrad i materiały", "Gotową umowę z klientem", "Prywatny list"], 0, "Материалы позволили подготовиться к решениям."),
            ("Jakie zastrzeżenie zgłosił dział sprzedaży?", ["Za krótki czas na szkolenie", "Brak sali", "Zbyt długą przerwę"], 0, "Он опасался, что сотрудники не успеют обучиться."),
            ("Jak rozwiązano problem?", ["Podzielono wdrożenie na etapy", "Odwołano projekt", "Zignorowano uwagę"], 0, "Этапность стала компромиссом."),
            ("Co przypisano każdemu zadaniu?", ["Termin i osobę odpowiedzialną", "Kolor i zdjęcie", "Tylko tytuł"], 0, "Это два обязательных элемента плана."),
            ("Dlaczego użyto form bezosobowych?", ["Aby podkreślić rezultaty", "Aby ukryć wszystkie terminy", "Aby zmienić temat"], 0, "Протокол фокусируется на решениях."),
            ("Czego oczekiwała Maja do środy?", ["Uwag do podsumowania", "Nowego budżetu", "Rezygnacji zespołu"], 0, "Она попросила прислать замечания."),
        ),
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    s, course = SPEC, Course.objects.get(id="b2-advanced")
    topic, _ = Topic.objects.update_or_create(id=s["id"], defaults={"course": course, "title": s["title"], "description": s["description"], "emoji": s["emoji"], "position": s["position"], "is_active": True})
    p = s["prefix"]
    rows = ((f"{p}-words", "words", "Słowa w kontekście", "Новая лексика", "8 карточек · B2", s["description"], 10, s["emoji"]), (f"{p}-grammar", "grammar", "Jak to wyrazić?", "Языковой фокус", "6 заданий · B2", s["theory"][0], 13, "✏️"), (f"{p}-review", "review", "Powtórka aktywna", "Активное повторение", "7 карточек · B2", "Закрепи лексику темы", 9, "🔄"), (f"{p}-quiz", "quiz", f"Quiz: {s['title']}", "Проверка темы", "10 вопросов · B2", "Проверь лексику и регистр", 10, "🎯"), (f"{p}-reading-check", "quiz", "Czy rozumiesz tekst?", "Понимание текста", "6 вопросов · B2", "Найди детали, решение и вывод", 8, "📖"))
    lessons = {}
    for position, row in enumerate(rows, s["lesson_start"]):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        lessons[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = lessons[f"{p}-grammar"]
    grammar.theory_title, grammar.theory_sections = s["theory"]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for offset, (polish, translation, example) in enumerate(s["cards"]):
        card, _ = Flashcard.objects.update_or_create(id=f"{p}-{offset + 1}", defaults={"polish": polish, "translation": translation, "example": example, "position": s["card_start"] + offset, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, selected in ((f"{p}-words", cards[:8]), (f"{p}-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(selected):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in ((f"{p}-grammar", s["grammar"]), (f"{p}-quiz", s["quiz"]), (f"{p}-reading-check", s["reading"]["check"])):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, question in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=question[0], options=question[1], correct=question[2], explanation=question[3], position=position)
    reading = s["reading"]
    glossary = {surface: {"lemma": entry[0], "translation": entry[1], "part_of_speech": entry[2]} for surface, entry in reading["glossary"].items()}
    ReadingText.objects.update_or_create(id=reading["id"], defaults={"topic": topic, "title": reading["title"], "description": reading["description"], "level": "B2", "minutes": reading["minutes"], "emoji": reading["emoji"], "position": 38, "paragraphs": reading["paragraphs"], "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": f"{p}-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0042_b2_news_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
