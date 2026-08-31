from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-31", "level_status": "curriculum_target"}

TOPICS = (
    {
        "id": "c2-critical-polemics", "prefix": "c23", "title": "Критическая полемика", "emoji": "⚖️",
        "description": "Отвечаем на сильную позицию без упрощения и подмены тезиса",
        "terms": (
            ("teza oponenta", "тезис оппонента", "wyrażenie rzeczownikowe"), ("zasada życzliwości", "принцип благожелательности", "wyrażenie rzeczownikowe"),
            ("argument stalowy", "усиленная версия аргумента", "wyrażenie rzeczownikowe"), ("chochoł argumentacyjny", "соломенное чучело", "wyrażenie rzeczownikowe"),
            ("punkt sporny", "предмет разногласия", "wyrażenie rzeczownikowe"), ("przesłanka", "предпосылка", "rzeczownik"),
            ("konkluzja", "заключение", "rzeczownik"), ("ciężar dowodu", "бремя доказательства", "wyrażenie rzeczownikowe"),
            ("przyznać rację częściowo", "частично признать правоту", "wyrażenie czasownikowe"), ("zakwestionować przesłankę", "оспорить предпосылку", "wyrażenie czasownikowe"),
            ("odróżnić fakt od oceny", "отличить факт от оценки", "wyrażenie czasownikowe"), ("uniknąć nadinterpretacji", "избежать сверхинтерпретации", "wyrażenie czasownikowe"),
            ("sformułować zastrzeżenie", "сформулировать оговорку", "wyrażenie czasownikowe"), ("dochować rzetelności", "соблюсти добросовестность", "wyrażenie czasownikowe"),
            ("pozostać przy swoim stanowisku", "остаться при своей позиции", "fraza"),
        ),
        "extra": (("spójność rozumowania", "связность рассуждения", "wyrażenie rzeczownikowe"), ("zakres zgody", "границы согласия", "wyrażenie rzeczownikowe"), ("uczciwa rekonstrukcja", "честная реконструкция", "wyrażenie rzeczownikowe")),
        "theory": (("Сильная реконструкция", "Сначала изложи позицию собеседника так, чтобы он мог её признать. Отдели тезис, предпосылки и вывод, затем укажи точную область согласия и спора."), ("Несогласие без подмены", "Критикуй сильнейшую разумную версию аргумента. Уступка не отменяет возражение: она показывает его границы и сохраняет интеллектуальную добросовестность.")),
        "grammar": (
            ("Составьте: Даже если диагноз верен, предложенное лечение из него не следует.", ["Nawet jeśli diagnoza jest trafna, nie wynika z niej proponowane leczenie.", "Trafna diagnoza zawsze dowodzi każdego leczenia.", "Leczenie diagnoza z niej nawet wynika."], 0, "Nawet jeśli вводит уступку, а nie wynika отделяет вывод от предпосылки."),
            ("Составьте: Я принимаю исходные данные, но оспариваю способ их интерпретации.", ["Przyjmuję dane wyjściowe, kwestionuję jednak sposób ich interpretacji.", "Odrzucam dane, więc zgadzam się z interpretacją.", "Dane sposób interpretacji jednak przyjmuję."], 0, "Jednak точно маркирует границу частичного согласия."),
            ("Która odpowiedź stosuje zasadę życzliwości?", ["Jeśli dobrze rozumiem, bronisz priorytetu bezpieczeństwa; różnimy się co do kosztu środka.", "Twierdzisz, że koszty nie istnieją.", "To absurd i nie warto odpowiadać."], 0, "Ответ точно реконструирует приоритет и локализует разногласие."),
            ("Gdzie zbudowano chochoła argumentacyjnego?", ["Oponent proponuje ograniczyć ruch, więc chce zakazać ludziom wychodzenia z domu.", "Oponent proponuje pilotaż ograniczenia ruchu.", "Koszt pilotażu wymaga oszacowania."], 0, "Первая версия карикатурно усиливает исходный тезис."),
            ("Jak wskazać ciężar dowodu?", ["To autor tej tezy powinien wykazać związek przyczynowy.", "Każdy musi obalić wszystko.", "Dowody są zbędne."], 0, "Формулировка связывает доказательную обязанность с конкретным утверждением."),
            ("Która konkluzja zachowuje zakres zastrzeżenia?", ["Argument uzasadnia pilotaż, lecz nie przesądza o wdrożeniu ogólnokrajowym.", "Argument dowodzi sukcesu wszędzie.", "Nie wynika z niego nic."], 0, "Вывод признаёт силу аргумента, не расширяя её сверх данных."),
        ),
        "paragraphs": (
            "W debacie o automatyzacji bibliotek Marta twierdziła, że system rekomendacji skróci czas poszukiwania książek. Paweł odpowiedział, że jej zdaniem bibliotekarze są zbędni. Marta zaprotestowała: mówiła o wsparciu jednej czynności, nie o zastąpieniu zawodu.",
            "Moderator zatrzymał rozmowę i poprosił Pawła o uczciwą rekonstrukcję stanowiska. Paweł przyznał, że główną tezą jest poprawa dostępności katalogu, a nie redukcja zatrudnienia. Wzmocnił nawet argument Marty, dodając, że narzędzie może pomagać osobom z ograniczoną mobilnością.",
            "Dopiero potem wskazał punkt sporny. Dane z pilotażu pokazywały krótsze wyszukiwanie, ale nie mierzyły jakości wyboru ani ochrony prywatności. Paweł przyjął pierwszą przesłankę, zakwestionował natomiast przejście od szybkości do ogólnej poprawy usługi.",
            "Marta częściowo przyznała mu rację. Zawęziła konkluzję do kontynuacji pilotażu i zaproponowała niezależny audyt rekomendacji. Nie porzuciła swojego stanowiska, lecz oddzieliła to, co już wykazano, od tego, co nadal wymaga dowodu.",
            "Debata nie zakończyła się pełną zgodą, ale stała się użyteczna. Uczestnicy przestali walczyć z uproszczonymi obrazami cudzych poglądów. Zakres sporu zmalał, a ciężar dowodu został przypisany konkretnym tezom, dzięki czemu możliwy stał się następny krok badania.",
        ),
        "reading": (
            ("Jak Paweł początkowo zniekształcił tezę Marty?", ["Uznał, że chce zastąpić bibliotekarzy", "Powiedział, że odrzuca automatyzację", "Przypisał jej sprzeciw wobec katalogów"], 0, "Он заменил ограниченный тезис утверждением о ненужности профессии."),
            ("Co zrobił po prośbie moderatora?", ["Uczciwie zrekonstruował i wzmocnił argument", "Zmienił temat", "Wycofał wszystkie zastrzeżenia"], 0, "Он назвал реальный тезис и добавил сильный пример доступности."),
            ("Jaki był rzeczywisty punkt sporny?", ["Przejście od szybkości do ogólnej jakości usługi", "Istnienie katalogu", "Liczba bibliotekarzy"], 0, "Спор касался обоснованности широкого вывода."),
            ("Jak Marta odpowiedziała na zastrzeżenie?", ["Zawęziła wniosek i zaproponowała audyt", "Zignorowała dane", "Zażądała natychmiastowego wdrożenia"], 0, "Она ограничила вывод продолжением пилота."),
            ("Dlaczego debata stała się użyteczna?", ["Przypisano ciężar dowodu konkretnym tezom", "Wszyscy natychmiast się zgodzili", "Usunięto wszystkie pytania"], 0, "Доказательные обязанности стали точными."),
            ("Co pokazuje tekst o częściowej zgodzie?", ["Może precyzować spór bez rezygnacji ze stanowiska", "Zawsze kończy polemikę", "Jest oznaką słabości"], 0, "Частичное согласие помогло сузить область разногласия."),
        ),
    },
    {
        "id": "c2-professional-editing", "prefix": "c24", "title": "Профессиональная редактура", "emoji": "✒️",
        "description": "Редактируем стиль, логику и информационную структуру сложного текста",
        "terms": (
            ("redakcja merytoryczna", "содержательная редактура", "wyrażenie rzeczownikowe"), ("redakcja stylistyczna", "стилистическая редактура", "wyrażenie rzeczownikowe"),
            ("spójność globalna", "глобальная связность", "wyrażenie rzeczownikowe"), ("tok wywodu", "ход рассуждения", "wyrażenie rzeczownikowe"),
            ("hierarchia informacji", "иерархия информации", "wyrażenie rzeczownikowe"), ("remat", "рема, новая информация", "rzeczownik"),
            ("temat zdania", "тема предложения", "wyrażenie rzeczownikowe"), ("nominalizacja", "номинализация", "rzeczownik"),
            ("rozluźnić składnię", "облегчить синтаксис", "wyrażenie czasownikowe"), ("usunąć redundancję", "устранить избыточность", "wyrażenie czasownikowe"),
            ("ujednolicić rejestr", "унифицировать регистр", "wyrażenie czasownikowe"), ("wyeksponować wniosek", "выделить вывод", "wyrażenie czasownikowe"),
            ("przestawić akapit", "переставить абзац", "wyrażenie czasownikowe"), ("zachować głos autora", "сохранить авторский голос", "wyrażenie czasownikowe"),
            ("uzasadnić ingerencję", "обосновать вмешательство", "wyrażenie czasownikowe"),
        ),
        "extra": (("wersja robocza", "рабочая версия", "wyrażenie rzeczownikowe"), ("ślad redakcyjny", "редакторский след", "wyrażenie rzeczownikowe"), ("intencja komunikacyjna", "коммуникативное намерение", "wyrażenie rzeczownikowe")),
        "theory": (("Редакторская диагностика", "Сначала определи цель, адресата и основной вывод. Исправляй глобальную структуру до локального стиля: иначе идеально отшлифованное предложение может остаться в ненужном абзаце."), ("Минимально достаточное вмешательство", "Устраняй двусмысленность, перегрузку и смену регистра, но сохраняй голос автора. Каждое существенное изменение должно иметь объяснимую функцию.")),
        "grammar": (
            ("Составьте: Только после проверки структуры редактор сократил отдельные предложения.", ["Dopiero po sprawdzeniu struktury redaktor skrócił poszczególne zdania.", "Redaktor przed strukturą skrócił dopiero.", "Poszczególne zdania sprawdziły redaktora."], 0, "Dopiero po выстраивает правильную иерархию этапов."),
            ("Составьте: Чем сложнее тезис, тем яснее должна быть структура текста.", ["Im bardziej złożona teza, tym przejrzystsza powinna być struktura tekstu.", "Teza złożona, ponieważ struktura mniej jasna.", "Tym teza, im struktura tekstu."], 0, "Парная конструкция im..., tym... выражает пропорциональную зависимость."),
            ("Która wersja usuwa ciężką nominalizację?", ["Zespół ocenił ryzyko i zmienił procedurę.", "Dokonano przeprowadzenia oceny ryzyka i zmiany procedury.", "Ocena dokonania procedury nastąpiła."], 0, "Глаголы ocenił и zmienił возвращают действующее лицо и действие."),
            ("Jak poprawić hierarchię informacji?", ["Najpierw podać główny wniosek, potem dane, które go ograniczają.", "Ukryć wniosek w przypisie.", "Powtórzyć każdy szczegół trzykrotnie."], 0, "Читатель сначала получает опорный вывод, затем его границы."),
            ("Która ingerencja zachowuje głos autora?", ["Skraca powtórzenie, pozostawiając charakterystyczną metaforę.", "Zastępuje wszystkie zdania stylem urzędowym.", "Dodaje poglądy redaktora."], 0, "Изменение убирает помеху, но сохраняет индивидуальный образ."),
            ("Gdzie rejestr jest niespójny?", ["Raport przedstawia wyniki, a potem stwierdza: «wynik totalnie rozwala system».", "Esej konsekwentnie używa stylu popularnonaukowego.", "Dialog świadomie cytuje język potoczny."], 0, "Немотивированный разговорный фрагмент ломает регистр отчёта."),
        ),
        "paragraphs": (
            "Redaktorka otrzymała esej o miejskich ogrodach. Autor zebrał wartościowe dane, lecz pierwszy akapit zawierał historię projektu, metodologię, trzy zastrzeżenia i końcowy wniosek. Każde zdanie było poprawne, a mimo to czytelnik nie wiedział, dokąd prowadzi tekst.",
            "Zamiast od razu wygładzać styl, redaktorka sporządziła mapę wywodu. Odkryła, że najważniejsza teza pojawia się dopiero na końcu: ogrody poprawiają lokalną retencję wody, ale ich efekt zależy od jakości gleby. Przeniosła tę myśl na początek i podporządkowała jej kolejne akapity.",
            "Następnie rozluźniła składnię. Konstrukcję «dokonanie przeprowadzenia pomiarów» zastąpiła zdaniem «zespół przeprowadził pomiary». Usunęła dwa powtórzenia, połączyła sąsiednie przykłady i ujednoliciła naukowy rejestr, nie kasując obrazowej metafory miasta jako gąbki.",
            "Każdą większą ingerencję opatrzyła komentarzem. Wyjaśniła, że przesunięcie akapitu eksponuje związek danych z tezą, a skrót nie usuwa zastrzeżenia, tylko zapobiega redundancji. Autor odrzucił jedną propozycję, ponieważ zmieniała stopień pewności jego wniosku.",
            "Ostateczna wersja była krótsza, lecz nie uboższa. Zachowała głos autora i wszystkie istotne ograniczenia, a jednocześnie prowadziła czytelnika od tezy przez dowody do konsekwencji. Redakcja okazała się nie kosmetyką, ale świadomym projektowaniem drogi odbiorcy przez tekst.",
        ),
        "reading": (
            ("Dlaczego tekst był trudny mimo poprawnych zdań?", ["Brakowało czytelnego kierunku wywodu", "Nie miał żadnych danych", "Zawierał błędy ortograficzne"], 0, "Проблема была глобальной, а не локально грамматической."),
            ("Co redaktorka zrobiła przed korektą stylu?", ["Sporządziła mapę wywodu", "Usunęła wszystkie metafory", "Zmieniła temat eseju"], 0, "Сначала она диагностировала структуру."),
            ("Jak rozluźniła nominalizację?", ["Przywróciła podmiot i czasownik", "Dodała kolejne rzeczowniki", "Usunęła wykonawcę działania"], 0, "Zespół przeprowadził заменяет тяжёлую именную конструкцию."),
            ("Po co komentowała większe ingerencje?", ["Aby uzasadnić ich funkcję", "Aby narzucić własne poglądy", "Aby wydłużyć dokument"], 0, "Комментарии делали логику правок прозрачной."),
            ("Dlaczego autor odrzucił jedną zmianę?", ["Zmieniała stopień pewności wniosku", "Nie lubił krótkich zdań", "Usuwała błąd ortograficzny"], 0, "Правка искажала эпистемическую силу авторского вывода."),
            ("Co oznacza redakcja jako projektowanie drogi odbiorcy?", ["Porządkowanie przejścia od tezy przez dowody do konsekwencji", "Dodawanie ozdobników", "Skracanie każdego tekstu o połowę"], 0, "Финал определяет редактуру как управление пониманием структуры."),
        ),
    },
)


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic, Lesson = (apps.get_model("learning", name) for name in ("Course", "Topic", "Lesson"))
    Flashcard, Link, Question, Reading = (apps.get_model("learning", name) for name in ("Flashcard", "LessonFlashcard", "Question", "ReadingText"))
    course = Course.objects.get(id="c2-mastery")
    lesson_specs = (("words", "words", "Лексика в точном контексте", 8), ("grammar", "grammar", "Точность конструкции", 6), ("review", "review", "Активное повторение", 7), ("quiz", "quiz", "Итог", 10), ("reading-check", "quiz", "Аналитическая проверка текста", 6))
    for topic_offset, data in enumerate(TOPICS):
        topic, _ = Topic.objects.update_or_create(id=data["id"], defaults={"course": course, "title": data["title"], "description": data["description"], "emoji": data["emoji"], "position": 2 + topic_offset, "is_active": True})
        lessons = {}
        for offset, (suffix, kind, title, count) in enumerate(lesson_specs):
            lessons[suffix], _ = Lesson.objects.update_or_create(id=f"{data['prefix']}-{suffix}", defaults={"topic": topic, "kind": kind, "title": f"{title}: {data['title']}" if suffix == "quiz" else title, "plan_title": title, "subtitle": f"{count} заданий · целевой C2", "description": data["description"], "minutes": 14, "emoji": data["emoji"], "theory_title": data["title"] if suffix == "grammar" else "", "theory_sections": list(data["theory"]) if suffix == "grammar" else [], "source_metadata": SOURCE, "position": 302 + topic_offset * 5 + offset, "is_active": True})
        cards = []
        for index, (polish, translation, _pos) in enumerate(data["terms"]):
            card, _ = Flashcard.objects.update_or_create(id=f"{data['prefix']}-{index + 1}", defaults={"polish": polish, "translation": translation, "example": f"W redagowanym tekście świadomie stosujemy pojęcie „{polish}”.", "source_metadata": SOURCE, "position": 902 + topic_offset * 15 + index, "is_active": True})
            cards.append(card)
        for suffix, subset in (("words", cards[:8]), ("review", cards[8:])):
            Link.objects.filter(lesson=lessons[suffix]).delete()
            for position, card in enumerate(subset):
                Link.objects.create(lesson=lessons[suffix], flashcard=card, position=position)
        quiz = tuple((f"Co znaczy „{p}”?", [t, data["terms"][(i + 1) % 15][1], data["terms"][(i + 2) % 15][1]], 0, f"„{p}” oznacza: {t}.") for i, (p, t, _pos) in enumerate(data["terms"][:10]))
        for suffix, questions in (("grammar", data["grammar"]), ("quiz", quiz), ("reading-check", data["reading"])):
            Question.objects.filter(lesson=lessons[suffix]).delete()
            for position, (prompt, options, correct, explanation) in enumerate(questions):
                Question.objects.create(lesson=lessons[suffix], prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
        glossary = {p: {"lemma": p, "translation": t, "part_of_speech": pos} for p, t, pos in data["terms"] + data["extra"]}
        Reading.objects.update_or_create(id=f"{data['prefix']}-tekst", defaults={"topic": topic, "title": data["title"], "description": data["description"], "level": "C2", "minutes": 16, "emoji": data["emoji"], "paragraphs": list(data["paragraphs"]), "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": f"{data['prefix']}-reading-check"}, "position": 59 + topic_offset, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0056_c2_first_topics")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
