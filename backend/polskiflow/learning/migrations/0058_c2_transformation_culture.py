from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-31", "level_status": "curriculum_target"}

TOPICS = (
    {
        "id": "c2-cross-genre", "prefix": "c25", "title": "Межжанровая трансформация", "emoji": "🔄",
        "description": "Переносим содержание между жанрами, сохраняя факты, нюансы и авторскую позицию",
        "terms": (
            ("konwencja gatunkowa", "жанровая конвенция", "wyrażenie rzeczownikowe"), ("dominanta tekstu", "доминанта текста", "wyrażenie rzeczownikowe"),
            ("kompresja treści", "сжатие содержания", "wyrażenie rzeczownikowe"), ("eksplicytacja", "экспликация", "rzeczownik"),
            ("zmiana rejestru", "смена регистра", "wyrażenie rzeczownikowe"), ("rama interpretacyjna", "интерпретационная рамка", "wyrażenie rzeczownikowe"),
            ("adresat docelowy", "целевая аудитория", "wyrażenie rzeczownikowe"), ("hierarchia faktów", "иерархия фактов", "wyrażenie rzeczownikowe"),
            ("przeformułować przekaz", "переформулировать сообщение", "wyrażenie czasownikowe"), ("zachować zastrzeżenie", "сохранить оговорку", "wyrażenie czasownikowe"),
            ("dopowiedzieć kontekst", "эксплицировать контекст", "wyrażenie czasownikowe"), ("skondensować argument", "сжать аргумент", "wyrażenie czasownikowe"),
            ("zmienić punkt widzenia", "изменить точку зрения", "wyrażenie czasownikowe"), ("uniknąć spłaszczenia sensu", "избежать упрощения смысла", "wyrażenie czasownikowe"),
            ("przełożyć formę na funkcję", "перевести форму в функцию", "fraza"),
        ),
        "extra": (("notatka prasowa", "пресс-релиз", "wyrażenie rzeczownikowe"), ("esej osobisty", "личное эссе", "wyrażenie rzeczownikowe"), ("streszczenie wykonawcze", "резюме для руководства", "wyrażenie rzeczownikowe")),
        "theory": (("Инвариант содержания", "Перед трансформацией выпиши факты, степень уверенности, оговорки и основную функцию текста. Жанр может изменить порядок и регистр, но не должен незаметно усиливать вывод."), ("Новый адресат", "Экспликация добавляет необходимый контекст, а компрессия убирает второстепенное. Проверяй, понимает ли новый адресат связи и отличает ли исходные слова автора от редакторской рамки.")),
        "grammar": (
            ("Составьте: Хотя формат стал короче, оговорка о недостатке данных сохранилась.", ["Choć forma stała się krótsza, zachowano zastrzeżenie dotyczące braku danych.", "Forma była krótka, więc usunięto wszystkie zastrzeżenia.", "Brak danych krótszą formę zachowano."], 0, "Choć вводит уступку, а zachowano точно фиксирует сохранённый элемент."),
            ("Составьте: То, что в отчёте было предпосылкой, в подкасте нужно назвать прямо.", ["To, co w raporcie było założeniem, w podcaście trzeba nazwać wprost.", "Raport wprost ukrywa wszystko w podcaście.", "Założenie trzeba raportem było nazwać."], 0, "Конструкция to, co... связывает функцию элемента в двух жанрах."),
            ("Która wersja zachowuje stopień pewności?", ["Badanie sugeruje związek, ale go nie dowodzi.", "Badanie bezsprzecznie dowodzi związku.", "Związku na pewno nie ma."], 0, "Sugeruje сохраняет исходную эпистемическую осторожность."),
            ("Jak skompresować argument bez spłaszczenia?", ["Zachować tezę, kluczowy dowód i ograniczenie.", "Pozostawić tylko efektowną puentę.", "Usunąć wszystkie warunki."], 0, "Минимальный инвариант включает тезис, основание и границы вывода."),
            ("Która eksplicytacja jest uzasadniona?", ["Wyjaśnienie skrótu nieznanego nowej grupie odbiorców.", "Dopisanie autorowi ukrytej motywacji.", "Zamiana hipotezy w fakt."], 0, "Раскрытие неизвестной аббревиатуры помогает адресату и не меняет позицию автора."),
            ("Co należy oznaczyć jako redakcyjną ramę?", ["Tytuł interpretujący materiał, którego nie było w oryginale.", "Dosłowny cytat z raportu.", "Datę publikacji źródła."], 0, "Новый интерпретирующий заголовок должен быть отделён от исходного материала."),
        ),
        "paragraphs": (
            "Fundacja opublikowała obszerny raport o nocnym oświetleniu miasta. Autorzy stwierdzili spadek zużycia energii po wymianie lamp, lecz zastrzegli, że nie badali wpływu światła na owady. Redakcja lokalnego radia miała zamienić raport w trzyminutową audycję.",
            "Pierwszy scenariusz brzmiał atrakcyjnie: «Nowe lampy rozwiązują miejski problem energii». Usuwał jednak warunek porównania i zamieniał częściowy wynik w całościowy sukces. Producentka wypisała więc inwarianty: zakres badania, zaobserwowany spadek, okres pomiaru oraz brak danych ekologicznych.",
            "W audycji liczby skondensowano do dwóch najważniejszych wartości. Termin techniczny wyjaśniono krótkim porównaniem, a tabelę zastąpiła wypowiedź badaczki. Zastrzeżenie o owadach przesunięto bliżej głównego wniosku, aby słuchacz nie odebrał go jako drobnego dodatku.",
            "Zmienił się też punkt widzenia. Raport prowadził czytelnika przez metodę, natomiast radio zaczynało od nocnego spaceru mieszkanki. Ta scena pełniła funkcję wejścia w temat, lecz producentka zaznaczyła, że jest rekonstrukcją, a nie dowodem naukowym.",
            "Gotowy materiał różnił się rytmem, językiem i kompozycją od raportu. Zachował jednak hierarchię faktów oraz stopień pewności autorów. Transformacja nie była skrótem mechanicznym: wymagała rozpoznania funkcji każdego elementu i znalezienia dla niej uczciwego odpowiednika w nowym gatunku.",
        ),
        "reading": (
            ("Jakie zastrzeżenie zawierał raport?", ["Nie badano wpływu światła na owady", "Nie mierzono zużycia energii", "Nie podano okresu badania"], 0, "Экологическое влияние не входило в исследование."),
            ("Co zniekształcał pierwszy scenariusz?", ["Zamieniał częściowy wynik w całościowy sukces", "Dodawał zbyt wiele tabel", "Cytował badaczkę dosłownie"], 0, "Он неоправданно расширял область вывода."),
            ("Jak zastąpiono tabelę?", ["Wypowiedzią badaczki", "Muzyką", "Reklamą fundacji"], 0, "В аудиоформате данные сопровождались репликой исследовательницы."),
            ("Dlaczego zastrzeżenie przesunięto bliżej wniosku?", ["Aby nie wyglądało na mało ważny dodatek", "Aby je ukryć", "Aby wydłużyć audycję"], 0, "Композиция сохранила вес ограничения."),
            ("Jak oznaczono scenę spaceru?", ["Jako rekonstrukcję, nie dowód", "Jako wynik eksperymentu", "Jako cytat z raportu"], 0, "Редакционная рамка была обозначена прозрачно."),
            ("Co pozostało niezmienne między gatunkami?", ["Hierarchia faktów i stopień pewności", "Kolejność wszystkich zdań", "Długość materiału"], 0, "Именно эти инварианты названы в финале."),
        ),
    },
    {
        "id": "c2-cultural-interpretation", "prefix": "c26", "title": "Интерпретация культуры", "emoji": "🎭",
        "description": "Связываем форму, исторический контекст и конкурирующие прочтения произведения",
        "terms": (
            ("kontekst kulturowy", "культурный контекст", "wyrażenie rzeczownikowe"), ("aluzja literacka", "литературная аллюзия", "wyrażenie rzeczownikowe"),
            ("intertekstualność", "интертекстуальность", "rzeczownik"), ("symbolika", "символика", "rzeczownik"),
            ("konwencja epoki", "конвенция эпохи", "wyrażenie rzeczownikowe"), ("strategia narracyjna", "нарративная стратегия", "wyrażenie rzeczownikowe"),
            ("perspektywa odbiorcy", "перспектива читателя", "wyrażenie rzeczownikowe"), ("konkurencyjne odczytanie", "конкурирующее прочтение", "wyrażenie rzeczownikowe"),
            ("osadzić w kontekście", "поместить в контекст", "wyrażenie czasownikowe"), ("uruchomić skojarzenie", "активировать ассоциацию", "wyrażenie czasownikowe"),
            ("podważyć interpretację", "поставить интерпретацию под сомнение", "wyrażenie czasownikowe"), ("uzasadnić odczytanie", "обосновать прочтение", "wyrażenie czasownikowe"),
            ("oddzielić intencję od efektu", "отделить намерение от эффекта", "wyrażenie czasownikowe"), ("uwzględnić anachronizm", "учесть анахронизм", "wyrażenie czasownikowe"),
            ("pozostawać w dialogu z tradycją", "вести диалог с традицией", "fraza"),
        ),
        "extra": (("pamięć zbiorowa", "коллективная память", "wyrażenie rzeczownikowe"), ("kod wizualny", "визуальный код", "wyrażenie rzeczownikowe"), ("horyzont oczekiwań", "горизонт ожиданий", "wyrażenie rzeczownikowe")),
        "theory": (("Интерпретация как гипотеза", "Связывай наблюдаемую форму с контекстом через аргумент, а не свободную ассоциацию. Сильное прочтение объясняет несколько деталей и допускает проверку конкурирующей версией."), ("Исторический и современный читатель", "Различай вероятное намерение автора, эффект для первой аудитории и сегодняшнее восприятие. Анахроничное прочтение может быть продуктивным, если оно честно обозначено.")),
        "grammar": (
            ("Составьте: Это прочтение убедительно постольку, поскольку объясняет повторяющийся образ окна.", ["Odczytanie jest przekonujące o tyle, o ile wyjaśnia powracający obraz okna.", "Odczytanie przekonuje, mimo że niczego nie wyjaśnia.", "Obraz okna o tyle odczytanie."], 0, "O tyle, o ile ограничивает силу вывода объяснительной способностью."),
            ("Составьте: Нельзя исключить, что современный зритель видит в сцене другой конфликт.", ["Nie można wykluczyć, że współczesny widz dostrzega w scenie inny konflikt.", "Współczesny widz musi widzieć dokładnie to samo.", "Scena wyklucza widza konflikt."], 0, "Nie można wykluczyć сохраняет открытость альтернативной интерпретации."),
            ("Co jest argumentem, a nie luźnym skojarzeniem?", ["Motyw powraca w trzech scenach i za każdym razem poprzedza zmianę decyzji bohatera.", "Okno kojarzy mi się z wolnością.", "Autor na pewno myślał tak jak ja."], 0, "Повторяемая формальная связь делает гипотезу проверяемой."),
            ("Jak oddzielić intencję od efektu?", ["Autor mógł nawiązać do mitu, ale dzisiejsi widzowie odczytują scenę także ekologicznie.", "Efekt zawsze dowodzi intencji.", "Intencja odbiorcy nie ma znaczenia."], 0, "Формулировка отдельно описывает вероятный замысел и современную реакцию."),
            ("Które zdanie uczciwie oznacza anachronizm?", ["Z dzisiejszej perspektywy można zobaczyć tu problem, którego epoka nie nazywała w ten sposób.", "Bohater używał pojęcia powstałego sto lat później.", "Kontekst historyczny jest zbędny."], 0, "Современная рамка явно названа, а не приписана эпохе."),
            ("Jak porównać konkurencyjne odczytania?", ["Sprawdzić, które wyjaśnia więcej szczegółów przy mniejszej liczbie założeń.", "Wybrać bardziej efektowne.", "Uznać każde za równie mocne."], 0, "Сравнение опирается на объяснительную силу и экономность предпосылок."),
        ),
        "paragraphs": (
            "W małej galerii pokazano instalację złożoną z pustego stołu, pękniętego lustra i nagrania kroków. Kuratorka opisała ją jako rozmowę z tradycją rodzinnego portretu. Część publiczności widziała przede wszystkim opowieść o emigracji, inni — krytykę pamięci tworzonej przez muzea.",
            "Pierwsze odczytanie wspierał rytm nagrania: kroki oddalały się, gdy na lustrze pojawiało się światło. Pusty stół przywoływał nieobecnych, a podpis artystki wspominał o przeprowadzce jej rodziny. Interpretacja emigracyjna łączyła więc formę, biografię i powtarzalny motyw.",
            "Drugie odczytanie zwracało uwagę na sposób ekspozycji. Lustro odbijało etykiety muzealne zamiast twarzy widza, a stół stał za barierą typową dla cennych zabytków. Instalacja mogła pytać, kto decyduje, które ślady codzienności stają się oficjalnym dziedzictwem.",
            "Kuratorka nie rozstrzygnęła sporu. Zaznaczyła, że wypowiedzi artystki wspierają temat migracji, lecz efekt muzealnej aranżacji wykracza poza deklarowaną intencję. Obie interpretacje wyjaśniały inne elementy i mogły się uzupełniać, dopóki nie ignorowały niewygodnych szczegółów.",
            "Rozmowa pokazała, że kontekst nie jest kluczem otwierającym jedno poprawne znaczenie. Ogranicza dowolność, dostarcza przesłanek i ujawnia anachronizmy, ale dzieło działa również w nowych horyzontach oczekiwań. Odpowiedzialna interpretacja pozostaje mocną, lecz rewizowalną hipotezą.",
        ),
        "reading": (
            ("Jakie dwa odczytania pojawiły się w galerii?", ["Emigracyjne i dotyczące muzealnej pamięci", "Sportowe i ekonomiczne", "Wyłącznie biograficzne"], 0, "Оба прочтения названы в первом абзаце."),
            ("Co wspierało interpretację emigracyjną?", ["Rytm kroków, pusty stół i biograficzny podpis", "Tylko kolor ścian", "Cena instalacji"], 0, "Версия связывала несколько независимых деталей."),
            ("Na co wskazywało odbicie etykiet w lustrze?", ["Na rolę muzeum w tworzeniu dziedzictwa", "Na błąd techniczny", "Na portret kuratorki"], 0, "Этот элемент поддерживал институциональное прочтение."),
            ("Dlaczego kuratorka nie wybrała jednej interpretacji?", ["Obie wyjaśniały różne elementy", "Nie znała instalacji", "Artystka zakazała rozmowy"], 0, "Конкурирующие гипотезы имели разную объяснительную область."),
            ("Co wykraczało poza deklarowaną intencję artystki?", ["Efekt muzealnej aranżacji", "Motyw przeprowadzki", "Nagranie kroków"], 0, "Текст отделяет авторскую декларацию от эффекта экспозиции."),
            ("Jak tekst definiuje odpowiedzialną interpretację?", ["Jako mocną, ale rewizowalną hipotezę", "Jako dowolne skojarzenie", "Jako odtworzenie jednej intencji"], 0, "Финал подчёркивает одновременно обоснованность и открытость пересмотру."),
        ),
    },
)


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite": return
    Course, Topic, Lesson = (apps.get_model("learning", n) for n in ("Course", "Topic", "Lesson"))
    Flashcard, Link, Question, Reading = (apps.get_model("learning", n) for n in ("Flashcard", "LessonFlashcard", "Question", "ReadingText"))
    course = Course.objects.get(id="c2-mastery")
    specs = (("words", "words", "Лексика в точном контексте", 8), ("grammar", "grammar", "Точность конструкции", 6), ("review", "review", "Активное повторение", 7), ("quiz", "quiz", "Итог", 10), ("reading-check", "quiz", "Аналитическая проверка текста", 6))
    for ti, data in enumerate(TOPICS):
        topic, _ = Topic.objects.update_or_create(id=data["id"], defaults={"course": course, "title": data["title"], "description": data["description"], "emoji": data["emoji"], "position": 4 + ti, "is_active": True})
        lessons = {}
        for offset, (suffix, kind, title, count) in enumerate(specs):
            lessons[suffix], _ = Lesson.objects.update_or_create(id=f"{data['prefix']}-{suffix}", defaults={"topic": topic, "kind": kind, "title": f"{title}: {data['title']}" if suffix == "quiz" else title, "plan_title": title, "subtitle": f"{count} заданий · целевой C2", "description": data["description"], "minutes": 14, "emoji": data["emoji"], "theory_title": data["title"] if suffix == "grammar" else "", "theory_sections": list(data["theory"]) if suffix == "grammar" else [], "source_metadata": SOURCE, "position": 312 + ti * 5 + offset, "is_active": True})
        cards = []
        for i, (polish, translation, _pos) in enumerate(data["terms"]):
            card, _ = Flashcard.objects.update_or_create(id=f"{data['prefix']}-{i + 1}", defaults={"polish": polish, "translation": translation, "example": f"W transformowanym tekście świadomie stosujemy pojęcie „{polish}”.", "source_metadata": SOURCE, "position": 932 + ti * 15 + i, "is_active": True}); cards.append(card)
        for suffix, subset in (("words", cards[:8]), ("review", cards[8:])):
            Link.objects.filter(lesson=lessons[suffix]).delete()
            for position, card in enumerate(subset): Link.objects.create(lesson=lessons[suffix], flashcard=card, position=position)
        quiz = tuple((f"Co znaczy „{p}”?", [t, data["terms"][(i + 1) % 15][1], data["terms"][(i + 2) % 15][1]], 0, f"„{p}” oznacza: {t}.") for i, (p, t, _pos) in enumerate(data["terms"][:10]))
        for suffix, questions in (("grammar", data["grammar"]), ("quiz", quiz), ("reading-check", data["reading"])):
            Question.objects.filter(lesson=lessons[suffix]).delete()
            for position, (prompt, options, correct, explanation) in enumerate(questions): Question.objects.create(lesson=lessons[suffix], prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
        glossary = {p: {"lemma": p, "translation": t, "part_of_speech": pos} for p, t, pos in data["terms"] + data["extra"]}
        Reading.objects.update_or_create(id=f"{data['prefix']}-tekst", defaults={"topic": topic, "title": data["title"], "description": data["description"], "level": "C2", "minutes": 16, "emoji": data["emoji"], "paragraphs": list(data["paragraphs"]), "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": f"{data['prefix']}-reading-check"}, "position": 61 + ti, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0057_c2_polemics_editing")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
