from django.db import migrations

SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}
CARDS = (
    ("b1media-publikacja", "publikacja", "публикация", "Publikacja opisuje wyniki miejskiego badania."),
    ("b1media-naglowek", "nagłówek", "заголовок", "Nagłówek powinien odpowiadać treści artykułu."),
    ("b1media-zrodlo", "źródło informacji", "источник информации", "Zawsze sprawdzam źródło informacji."),
    ("b1media-wiarygodny", "wiarygodny", "достоверный", "Wiarygodny autor podaje konkretne dane."),
    ("b1media-udostepnic", "udostępnić", "поделиться; опубликовать", "Nie udostępniaj wiadomości bez sprawdzenia."),
    ("b1media-komentarz", "komentarz", "комментарий", "Komentarz nie zawsze opisuje fakt."),
    ("b1media-relacjonowac", "relacjonować", "освещать; рассказывать", "Reporter relacjonował wydarzenie na żywo."),
    ("b1media-twierdzic", "twierdzić", "утверждать", "Autor twierdzi, że projekt zakończył się sukcesem."),
    ("b1media-podkreslac", "podkreślać", "подчёркивать", "Ekspert podkreśla znaczenie kontekstu."),
    ("b1media-zaprzeczyc", "zaprzeczyć", "опровергнуть; отрицать", "Organizator zaprzeczył tej informacji."),
    ("b1media-wynikac", "wynikać z", "следовать из", "Z raportu wynika, że ruch w mieście zmalał."),
    ("b1media-glowna-mysl", "główna myśl", "основная мысль", "Najpierw znajdź główną myśl tekstu."),
    ("b1media-strescic", "streścić", "кратко пересказать", "Potrafisz streścić artykuł w trzech zdaniach?"),
    ("b1media-porownac", "porównać źródła", "сравнить источники", "Warto porównać źródła przed wyciągnięciem wniosku."),
    ("b1media-wprowadzac-blad", "wprowadzać w błąd", "вводить в заблуждение", "Zdjęcie bez daty może wprowadzać w błąd."),
)
GRAMMAR = (
    ("Autor ___, że nowa aplikacja poprawi bezpieczeństwo.", ["twierdzi", "wynika", "streszcza się"], 0, "Twierdzić вводит утверждение автора и сочетается с że."),
    ("Z raportu ___, że większość czytelników sprawdza datę.", ["wynika", "zaprzecza", "relacjonuje"], 0, "Безличная конструкция z raportu wynika, że передаёт вывод из источника."),
    ("Reporter powiedział: «Mieszkańcy protestują». Reporter relacjonował, ___.", ["że mieszkańcy protestują", "czy mieszkańcy protestują", "żeby mieszkańcy protestują"], 0, "В пересказе сообщения содержание вводится союзом że."),
    ("Najpierw podaj temat, ___ przedstaw główną myśl i szczegóły.", ["następnie", "ponieważ", "mimo że"], 0, "Następnie связывает последовательные части пересказа."),
    ("Составьте: Автор подчёркивает, что заголовок не передаёт главную мысль.", ["Autor podkreśla, że nagłówek nie oddaje głównej myśli.", "Autor wynika, czy nagłówek nie oddaje główną myśl.", "Autor podkreślać, żeby nagłówek nie oddaje."], 0, "После podkreśla содержание вводится że; oddawać требует родительного падежа."),
    ("Составьте: Сначала я проверил источник, а затем кратко пересказал публикацию.", ["Najpierw sprawdziłem źródło, a następnie krótko streściłem publikację.", "Ponieważ sprawdziłem źródło, następnie streszczam publikacją.", "Najpierw źródło sprawdzałem, mimo że streścił publikację."], 0, "Najpierw… a następnie задаёт ясную структуру; streścić принимает винительный падеж."),
)
QUIZ = (
    ("Что означает wiarygodne źródło?", ["источник, которому можно доверять", "популярный комментарий", "короткий заголовок"], 0, "Wiarygodne źródło содержит проверяемые сведения и прозрачное авторство."),
    ("Nie znam autora ani daty, więc nie będę ___ tej wiadomości.", ["udostępniać", "wynikać", "nagłówkować"], 0, "Udostępniać wiadomość — делиться сообщением."),
    ("Który czasownik wprowadza zdecydowaną opinię autora?", ["twierdzić", "wynikać z", "porównać"], 0, "Twierdzić показывает, что именно утверждает автор."),
    ("Z danych ___, że zainteresowanie wzrosło.", ["wynika", "podkreśla", "udostępnia"], 0, "Форма wynika используется для вывода, основанного на данных."),
    ("Jak zacząć uporządkowane streszczenie?", ["Tekst dotyczy…, a jego główna myśl to…", "Wszystko w tekście jest ważne.", "Nie pamiętam źródła, ale…"], 0, "Хороший пересказ называет тему и основную мысль."),
    ("Autor zaprzeczył, ___ opublikował nieprawdziwe dane.", ["że", "czy", "więc"], 0, "После zaprzeczył содержание сообщения вводится że."),
    ("Co najlepiej pomaga sprawdzić wiadomość?", ["Porównanie daty, autora i kilku źródeł", "Przeczytanie tylko komentarzy", "Udostępnienie samego nagłówka"], 0, "Сопоставление реквизитов и независимых источников снижает риск ошибки."),
    ("Выберите естественное сочетание.", ["streścić publikację", "wynikać komentarz", "zaprzeczyć źródłem"], 0, "Streścić publikację — кратко передать содержание публикации."),
    ("Reporter ___ przebieg debaty, a ekspert wyjaśniał dane.", ["relacjonował", "wynikał", "udostępniał się"], 0, "Relacjonować означает последовательно освещать событие."),
    ("Które zdanie oddziela fakt od opinii?", ["Raport podaje liczbę, natomiast autor ocenia jej znaczenie.", "Każdy popularny wpis jest prawdziwy.", "Nagłówek zawsze wystarcza."], 0, "Первый вариант явно различает данные и авторскую оценку."),
)
CHECK = (
    ("Co zobaczyła Marta rano?", ["Wpis o rzekomym zamknięciu biblioteki", "Relację z koncertu", "Reklamę nowej książki"], 0, "В ленте появился пост о якобы закрывающейся библиотеке."),
    ("Dlaczego nagłówek wzbudził jej wątpliwości?", ["Nie podawał autora ani daty decyzji", "Był napisany po polsku", "Zawierał nazwę dzielnicy"], 0, "В заголовке не было проверяемых реквизитов."),
    ("Jak Marta sprawdziła informację?", ["Porównała wpis z oficjalną stroną i lokalnym portalem", "Zapytała tylko autora komentarza", "Natychmiast udostępniła wpis"], 0, "Она обратилась к двум более прозрачным источникам."),
    ("Co naprawdę planowała biblioteka?", ["Krótki remont jednego piętra", "Całkowite zamknięcie", "Przeprowadzkę do innego miasta"], 0, "Речь шла лишь о ремонте одного этажа."),
    ("Jak Marta streściła sytuację znajomym?", ["Podała główną myśl, źródła i ważne szczegóły", "Powtórzyła sam alarmujący nagłówek", "Usunęła wszystkie informacje"], 0, "Её пересказ отделял подтверждённую суть от преувеличения."),
    ("Jaki jest główny wniosek tekstu?", ["Przed udostępnieniem trzeba sprawdzić kontekst i źródła", "Najpopularniejszy wpis jest zawsze dokładny", "Komentarze zastępują oficjalne informacje"], 0, "Главная мысль — осознанная проверка до распространения сообщения."),
)
READING = {"id": "b1media-wiadomosc-ktora-wymagala-sprawdzenia", "title": "Wiadomość, która wymagała sprawdzenia", "description": "Как проверить публикацию и передать её главную мысль", "level": "B1", "minutes": 8, "emoji": "📰", "position": 30, "paragraphs": [
    "Rano Marta zobaczyła w mediach społecznościowych alarmujący wpis: biblioteka w jej dzielnicy miała zostać zamknięta. Nagłówek brzmiał poważnie, ale publikacja nie zawierała nazwiska autora ani daty decyzji. W komentarzach jedni mieszkańcy wyrażali złość, a inni od razu udostępniali wiadomość znajomym.",
    "Marta postanowiła sprawdzić źródło informacji. Na oficjalnej stronie biblioteki znalazła komunikat o remoncie jednego piętra. Następnie porównała go z artykułem lokalnego portalu, który relacjonował posiedzenie rady dzielnicy i podawał dokładny termin prac.",
    "Z obu źródeł wynikało, że biblioteka pozostanie otwarta, chociaż przez dwa tygodnie część sal będzie niedostępna. Dyrektorka podkreślała, że wszystkie zajęcia dla dzieci odbędą się zgodnie z planem. Zaprzeczyła też, że instytucji grozi całkowite zamknięcie.",
    "Marta napisała znajomym krótkie streszczenie. Najpierw podała główną myśl, następnie wymieniła sprawdzone źródła, a na końcu wyjaśniła, skąd wzięło się nieporozumienie. Zrozumiała, że alarmujący nagłówek może wprowadzać w błąd, jeśli czytelnik nie sprawdzi daty, autora i szerszego kontekstu.",
], "glossary": {
    "alarmujący": {"lemma": "alarmujący", "translation": "тревожный", "part_of_speech": "прилагательное"}, "miała zostać": {"lemma": "mieć zostać", "translation": "должна была быть", "part_of_speech": "глагольная конструкция"}, "zawierała": {"lemma": "zawierać", "translation": "содержать", "part_of_speech": "глагол"}, "wyrażali": {"lemma": "wyrażać", "translation": "выражать", "part_of_speech": "глагол"}, "postanowiła": {"lemma": "postanowić", "translation": "решить", "part_of_speech": "глагол"}, "komunikat": {"lemma": "komunikat", "translation": "сообщение; объявление", "part_of_speech": "существительное"}, "remoncie": {"lemma": "remont", "translation": "ремонт", "part_of_speech": "существительное"}, "posiedzenie": {"lemma": "posiedzenie", "translation": "заседание", "part_of_speech": "существительное"}, "pozostanie": {"lemma": "pozostać", "translation": "остаться", "part_of_speech": "глагол"}, "niedostępna": {"lemma": "niedostępny", "translation": "недоступный", "part_of_speech": "прилагательное"}, "odbędą się": {"lemma": "odbyć się", "translation": "состояться", "part_of_speech": "глагол"}, "grozi": {"lemma": "grozić", "translation": "угрожать", "part_of_speech": "глагол"}, "streszczenie": {"lemma": "streszczenie", "translation": "краткий пересказ", "part_of_speech": "существительное"}, "wymieniła": {"lemma": "wymienić", "translation": "перечислить", "part_of_speech": "глагол"}, "nieporozumienie": {"lemma": "nieporozumienie", "translation": "недоразумение", "part_of_speech": "существительное"}, "szerszego": {"lemma": "szeroki", "translation": "более широкий", "part_of_speech": "прилагательное"},
}}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(id="b1-media-internet", defaults={"course": Course.objects.get(id="b1-independent"), "title": "Медиа и интернет", "description": "Проверяем публикации и связно передаём их главную мысль", "emoji": "📰", "position": 6, "is_active": True})
    rows = (("b1media-words", "words", "Co naprawdę napisano?", "Публикация и источник", "8 карточек · B1", "Назови части публикации и оцени источник", 9, "📰"), ("b1media-grammar", "grammar", "Jak przekazać wiadomość?", "Структура пересказа", "6 заданий · B1", "Используй глаголы речи и маркеры последовательности", 12, "✏️"), ("b1media-review", "review", "Sprawdzam i streszczam", "Проверка информации", "7 карточек · B1", "Сравни источники и сформулируй главную мысль", 8, "🔄"), ("b1media-quiz", "quiz", "Quiz: media i internet", "Проверка темы", "10 вопросов · B1", "Проверь лексику и структуру пересказа", 9, "🎯"), ("b1media-reading-check", "quiz", "Czy wiadomość była prawdziwa?", "Понимание текста", "6 вопросов · B1", "Отдели заголовок от подтверждённой главной мысли", 7, "📖"))
    made = {}
    for position, row in enumerate(rows, 138):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["b1media-grammar"]
    grammar.theory_title = "Глаголы речи и ясный пересказ"
    grammar.theory_sections = [["Кто сообщает", "Twierdzić и podkreślać передают позицию автора, relacjonować — ход события, a zaprzeczać — отрицание сообщения."], ["Вывод из источника", "Конструкция z tekstu wynika, że показывает, что вывод основан на публикации, а не является личным фактом."], ["Структура", "Назови тему и главную мысль, затем используй najpierw, następnie, na końcu для существенных деталей."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 452):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("b1media-words", cards[:8]), ("b1media-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("b1media-grammar", GRAMMAR), ("b1media-quiz", QUIZ), ("b1media-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, question in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=question[0], options=question[1], correct=question[2], explanation=question[3], position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "b1media-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0037_b1_healthy_lifestyle_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
