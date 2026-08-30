from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}

SPEC = {
    "id": "b2-literature-cinema", "title": "Литература и кино",
    "description": "Интерпретируем произведение, обсуждаем образность и пишем аргументированную рецензию", "emoji": "🎬", "position": 7,
    "prefix": "b2lit", "lesson_start": 203, "card_start": 647,
    "theory": ("Интерпретация, цитирование и пересказ", [
        ["Интерпретация", "Формулы można odczytać jako…, motyw sugeruje, że… и scena skłania do wniosku… отделяют анализ от пересказа сюжета."],
        ["Цитата", "Короткая цитата вводится через autor pisze, że… или bohater mówi: «…» и обязательно сопровождается объяснением её функции."],
        ["Пересказ", "Косвенная речь меняет перспективу: Powiedziała: «Wrócę» → Powiedziała, że wróci. В рецензии настоящее время может описывать действие произведения."],
    ]),
    "cards": (
        ("fabuła", "сюжет", "Fabuła rozwija się powoli, ale konsekwentnie."),
        ("narrator", "рассказчик", "Narrator nie ujawnia wszystkich informacji."),
        ("punkt widzenia", "точка зрения", "Zmiana punktu widzenia wpływa na ocenę bohatera."),
        ("motyw", "мотив, повторяющийся образ", "Motyw pustego domu powraca w kilku scenach."),
        ("symbolizować", "символизировать", "Zgaszone światło może symbolizować utratę nadziei."),
        ("budować napięcie", "создавать напряжение", "Krótkie ujęcia skutecznie budują napięcie."),
        ("niejednoznaczny", "неоднозначный", "Finał pozostaje niejednoznaczny."),
        ("przemiana bohatera", "трансформация героя", "Najważniejsza jest stopniowa przemiana bohatera."),
        ("interpretować", "интерпретировать", "Ten gest można interpretować na dwa sposoby."),
        ("przywołać cytat", "привести цитату", "Recenzent przywołał krótki cytat z dialogu."),
        ("odwoływać się do", "отсылать к", "Film odwołuje się do historii miasta."),
        ("warstwa wizualna", "визуальная составляющая", "Warstwa wizualna wzmacnia nastrój opowieści."),
        ("przekonujący", "убедительный", "Portret głównej bohaterki jest przekonujący."),
        ("skłaniać do refleksji", "побуждать к размышлению", "Zakończenie skłania do refleksji nad pamięcią."),
        ("można odczytać jako", "можно истолковать как", "Podróż można odczytać jako próbę pogodzenia się z przeszłością."),
    ),
    "grammar": (
        ("Motyw zamkniętego okna można ___ jako znak izolacji.", ["odczytać", "przeczytał", "odczytując się"], 0, "Można + infinitiv вводит допустимую интерпретацию, а не единственный ответ."),
        ("Narratorka powiedziała: «Nie znam zakończenia». → Narratorka powiedziała, że ___ zakończenia.", ["nie zna", "nie znam", "nie znała będzie"], 0, "При передаче реплики меняется лицо: znam → zna."),
        ("Reżyser przywołuje obraz pustego peronu, ___ podkreślić samotność bohatera.", ["aby", "mimo że", "natomiast"], 0, "Aby + infinitiv выражает цель художественного приёма."),
        ("Finał jest niejednoznaczny; ___ widz może stworzyć własną interpretację.", ["dzięki temu", "pomimo", "rzekomo że"], 0, "Dzięki temu связывает особенность финала с её эффектом."),
        ("Составьте: Этот образ можно истолковать как символ утраченной близости.", ["Ten obraz można odczytać jako symbol utraconej bliskości.", "Ten obraz czyta jako utracił symbol bliskość.", "Obrazem można odczytał utraconej bliskości symbol."], 0, "Można odczytać jako — готовая аналитическая рамка; symbol требует родительного определения."),
        ("Составьте: Героиня сказала, что вернётся, но рассказчик ставит её слова под сомнение.", ["Bohaterka powiedziała, że wróci, ale narrator poddaje jej słowa w wątpliwość.", "Bohaterka mówiła wrócę, narrator wątpliwość jej słowami.", "Powiedziała że wracała, lecz narrator poddawać słowa."], 0, "Косвенная речь использует że wróci; устойчивое сочетание — poddawać coś w wątpliwość."),
    ),
    "quiz": (
        ("Co to jest fabuła?", ["последовательность событий произведения", "только мнение критика", "список актёров"], 0, "Fabuła организует события истории."),
        ("Które zdanie jest interpretacją, a nie streszczeniem?", ["Pusty peron można odczytać jako znak samotności.", "Bohater wysiada z pociągu.", "Film trwa dziewięćdziesiąt minut."], 0, "Первая фраза объясняет возможный смысл образа."),
        ("Krótki cytat w recenzji powinien…", ["wspierać argument i zostać objaśniony", "zastąpić całą analizę", "pozostać bez kontekstu"], 0, "Цитата — доказательство, её функцию нужно объяснить."),
        ("Co buduje napięcie w filmie?", ["tempo, montaż i ograniczenie informacji", "wyłącznie tytuł", "lista źródeł"], 0, "Напряжение создаётся системой повествовательных и визуальных средств."),
        ("Finał niejednoznaczny…", ["dopuszcza kilka uzasadnionych odczytań", "nie ma żadnego znaczenia", "zawsze jest błędem autora"], 0, "Неоднозначность открывает несколько интерпретаций, если они опираются на текст."),
        ("Film ___ do dawnej legendy miejskiej.", ["odwołuje się", "przywołuje się cytatem", "symbolizuje do"], 0, "Odwoływać się do требует родительного падежа."),
        ("Powiedział: «Nie wrócę». → Powiedział, że…", ["nie wróci", "nie wrócę", "nie wracałem jutro"], 0, "В косвенной речи первое лицо меняется на третье."),
        ("Co powinna zawierać przekonująca recenzja?", ["tezę, przykłady i wyjaśnienie oceny", "sam opis zakończenia", "wyłącznie oceny liczbowe"], 0, "Аргументированная рецензия связывает оценку с конкретными средствами произведения."),
        ("Warstwa wizualna oznacza…", ["цвет, кадр, свет и композицию изображения", "порядок глав книги", "биографию зрителя"], 0, "Это система визуальных средств фильма."),
        ("Która formuła sygnalizuje, że odczytanie nie jest jedyne?", ["można interpretować jako", "bez wątpienia oznacza tylko", "autor udowodnił raz na zawsze"], 0, "Można interpretować jako оставляет место другим обоснованным прочтениям."),
    ),
    "reading": {
        "id": "b2lit-recenzja-filmu-swiatlo-na-peronie", "title": "Recenzja filmu «Światło na peronie»",
        "description": "Оригинальная рецензия вымышленного фильма: образ, перспектива и неоднозначный финал", "emoji": "🎬", "minutes": 13,
        "paragraphs": [
            "Film «Światło na peronie» opowiada o Idzie, fotografce, która po latach wraca do rodzinnego miasta. Fabuła wydaje się prosta: bohaterka ma uporządkować mieszkanie po dziadku i szybko wyjechać. Reżyserka stopniowo ujawnia jednak, że prawdziwym celem podróży jest konfrontacja z pamięcią o nagłym rozstaniu z siostrą. Narrator pozostaje blisko punktu widzenia Idy, dlatego widz długo zna tylko jej wersję wydarzeń.",
            "Najważniejszym motywem jest światło zapalające się co wieczór na nieczynnym peronie. Ida uważa je za przypadkową awarię, ale kamera wielokrotnie zatrzymuje się na pustej ławce pod lampą. Obraz można odczytać jako symbol oczekiwania: bohaterka twierdzi, że nie chce wracać do przeszłości, a jednocześnie stale szuka znaku od nieobecnej siostry. Chłodne kolory miasta kontrastują z ciepłym światłem peronu i wzmacniają ten sens.",
            "Film skutecznie buduje napięcie, choć nie korzysta z gwałtownych zwrotów akcji. Zamiast nich pojawiają się krótkie rozmowy i urwane wiadomości. W jednej scenie Ida mówi: «Pamiętam tylko to, co pozwala mi odejść». Cytat nie wyjaśnia jej decyzji, lecz poddaje wiarygodność wspomnień w wątpliwość. Później siostra przekazuje przez znajomego, że również próbowała nawiązać kontakt. Ta informacja zmienia ocenę wcześniejszego milczenia.",
            "Przemiana bohaterki jest przekonująca właśnie dlatego, że pozostaje niepełna. Ida zaczyna dostrzegać cudzy punkt widzenia, ale nie otrzymuje prostego pojednania. W finale czeka na peronie, gdy światło nagle gaśnie. Po chwili w ciemności słychać kroki, lecz film nie pokazuje, kto nadchodzi. Dla jednych będzie to zapowiedź spotkania, dla innych — znak, że bohaterka musi zaakceptować niepewność.",
            "Niejednoznaczne zakończenie może rozczarować odbiorców oczekujących rozwiązania wszystkich wątków. Jest jednak spójne z warstwą wizualną i tematem zawodnej pamięci. «Światło na peronie» nie daje gotowej odpowiedzi, ale skłania do refleksji nad tym, ile naszych opowieści o bliskich powstaje bez poznania ich perspektywy.",
        ],
        "glossary": {
            "uporządkować": ("uporządkować", "привести в порядок", "глагол"), "ujawnia": ("ujawniać", "раскрывает", "глагол"),
            "rozstaniu": ("rozstanie", "расставании", "существительное"), "wydarzeń": ("wydarzenie", "событий", "существительное"),
            "nieczynnym": ("nieczynny", "неработающем", "прилагательное"), "przypadkową": ("przypadkowy", "случайную", "прилагательное"),
            "zatrzymuje": ("zatrzymywać się", "задерживается", "глагол"), "oczekiwania": ("oczekiwanie", "ожидания", "существительное"),
            "nieobecnej": ("nieobecny", "отсутствующей", "прилагательное"), "wzmacniają": ("wzmacniać", "усиливают", "глагол"),
            "gwałtownych": ("gwałtowny", "резких", "прилагательное"), "urwane": ("urwany", "оборванные", "прилагательное"),
            "wiarygodność": ("wiarygodność", "достоверность", "существительное"), "nawiązać": ("nawiązać", "установить", "глагол"),
            "przemiana": ("przemiana", "трансформация", "существительное"), "pojednania": ("pojednanie", "примирения", "существительное"),
            "nadchodzi": ("nadchodzić", "приближается", "глагол"), "niepewność": ("niepewność", "неопределённость", "существительное"),
            "rozczarować": ("rozczarować", "разочаровать", "глагол"), "zawodnej": ("zawodny", "ненадёжной", "прилагательное"),
        },
        "check": (
            ("Dlaczego Ida wraca do miasta?", ["Ma uporządkować mieszkanie po dziadku", "Zaczyna pracę na stacji", "Kręci film o pociągach"], 0, "Это её внешняя практическая задача."),
            ("Co może symbolizować światło na peronie?", ["Oczekiwanie i szukanie kontaktu", "Wyłącznie awarię techniczną", "Sukces zawodowy Idy"], 0, "Рецензия связывает повторяющийся образ с ожиданием."),
            ("Jak film buduje napięcie?", ["Przez krótkie rozmowy i urwane wiadomości", "Przez ciągłe pościgi", "Przez narrację dokumentalną"], 0, "Напряжение возникает из ограниченной информации."),
            ("Co zmienia ocenę milczenia siostry?", ["Wiadomość, że także próbowała nawiązać kontakt", "Nowa fotografia peronu", "Decyzja o sprzedaży mieszkania"], 0, "Эта информация добавляет другую перспективу."),
            ("Dlaczego finał jest niejednoznaczny?", ["Nie wiadomo, kto nadchodzi w ciemności", "Ida nie przyjeżdża na peron", "Film kończy się przed podróżą"], 0, "Звук шагов допускает разные прочтения."),
            ("Jak recenzent ostatecznie ocenia zakończenie?", ["Jako spójne z obrazem i tematem pamięci", "Jako przypadkowe i pozbawione sensu", "Jako pełne rozwiązanie wszystkich wątków"], 0, "Финальный абзац обосновывает положительную оценку его связности."),
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
    rows = ((f"{p}-words", "words", "Słowa w kontekście", "Новая лексика", "8 карточек · B2", s["description"], 10, s["emoji"]), (f"{p}-grammar", "grammar", "Jak to wyrazić?", "Языковой фокус", "6 заданий · B2", s["theory"][0], 13, "✏️"), (f"{p}-review", "review", "Powtórka aktywna", "Активное повторение", "7 карточек · B2", "Закрепи лексику темы", 9, "🔄"), (f"{p}-quiz", "quiz", f"Quiz: {s['title']}", "Проверка темы", "10 вопросов · B2", "Проверь лексику и языковой фокус", 10, "🎯"), (f"{p}-reading-check", "quiz", "Czy rozumiesz tekst?", "Понимание текста", "6 вопросов · B2", "Найди детали и главный вывод", 8, "📖"))
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
    ReadingText.objects.update_or_create(id=reading["id"], defaults={"topic": topic, "title": reading["title"], "description": reading["description"], "level": "B2", "minutes": reading["minutes"], "emoji": reading["emoji"], "position": 43, "paragraphs": reading["paragraphs"], "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": f"{p}-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0047_b2_psychology_relationships_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
