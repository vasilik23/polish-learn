from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-31", "level_status": "curriculum_target"}

TOPICS = (
    {
        "id": "c2-authorial-voice", "prefix": "c29", "title": "Авторский голос", "emoji": "🖋️",
        "description": "Осознанно управляем ритмом, тоном и синтаксисом, сохраняя собственную позицию",
        "terms": (
            ("głos autorski", "авторский голос", "wyrażenie rzeczownikowe"), ("ton wypowiedzi", "тон высказывания", "wyrażenie rzeczownikowe"),
            ("rytm prozy", "ритм прозы", "wyrażenie rzeczownikowe"), ("kadencja zdania", "каденция предложения", "wyrażenie rzeczownikowe"),
            ("fraza rozpoznawalna", "узнаваемая фраза", "wyrażenie rzeczownikowe"), ("dystans narracyjny", "нарративная дистанция", "wyrażenie rzeczownikowe"),
            ("ironia dyskretna", "тонкая ирония", "wyrażenie rzeczownikowe"), ("zagęszczenie składni", "синтаксическое уплотнение", "wyrażenie rzeczownikowe"),
            ("modulować tempo", "модулировать темп", "wyrażenie czasownikowe"), ("przełamać regularność", "нарушить регулярность", "wyrażenie czasownikowe"),
            ("wyciszyć puentę", "приглушить финальный акцент", "wyrażenie czasownikowe"), ("wyostrzyć kontrast", "обострить контраст", "wyrażenie czasownikowe"),
            ("unikać manieryzmu", "избегать манерности", "wyrażenie czasownikowe"), ("zachować idiomatyczność", "сохранить идиоматичность", "wyrażenie czasownikowe"),
            ("pisać we własnym rejestrze", "писать в собственном регистре", "fraza"),
        ),
        "extra": (("pauza retoryczna", "риторическая пауза", "wyrażenie rzeczownikowe"), ("perspektywa pierwszoosobowa", "перспектива первого лица", "wyrażenie rzeczownikowe"), ("spójność tonalna", "тональная связность", "wyrażenie rzeczownikowe")),
        "theory": (("Голос как система решений", "Авторский голос возникает из повторяемых решений о дистанции, ритме, образности и степени прямоты. Его нельзя свести к декоративным словам или постоянной необычности."), ("Вариативность без манерности", "Меняй длину и рисунок фразы по функции: ускоряй действие, замедляй наблюдение, оставляй паузу перед выводом. Редактируй эффект, не стирая характер текста.")),
        "grammar": (
            ("Составьте: Короткая фраза прерывает плавный ритм и обнажает сомнение.", ["Krótkie zdanie przełamuje płynny rytm i odsłania wątpliwość.", "Płynny rytm ukrywa każde krótkie zdanie.", "Wątpliwość rytmem zdanie przełamała."], 0, "Два глагола описывают формальный приём и его смысловую функцию."),
            ("Составьте: Не отказываясь от иронии, автор смягчает её последней оговоркой.", ["Nie rezygnując z ironii, autor łagodzi ją końcowym zastrzeżeniem.", "Autor rezygnuje z ironii, więc ją wzmacnia.", "Ironia autora zastrzeżenie łagodzić."], 0, "Nie rezygnując сохраняет приём, а łagodzi обозначает изменение интенсивности."),
            ("Która zmiana świadomie moduluje tempo?", ["Seria krótkich zdań przyspiesza scenę po długim opisie.", "Każde zdanie ma identyczną długość bez powodu.", "Usunięto wszystkie czasowniki."], 0, "Контраст длины предложений связан с динамикой сцены."),
            ("Gdzie ironia pozostaje dyskretna?", ["Bohater «punktualnie» przyszedł tylko godzinę po terminie.", "Autor pisze: to jest ironia.", "Bohater przyszedł punktualnie."], 0, "Кавычки и контекст создают иронию без прямого комментария."),
            ("Co grozi manieryzmem?", ["Powtarzanie efektownego chwytu niezależnie od funkcji.", "Dobór rytmu do sceny.", "Korekta niejasnego zaimka."], 0, "Манерность возникает, когда заметный приём становится автоматическим."),
            ("Która puenta jest celowo wyciszona?", ["I może właśnie dlatego nikt więcej o tym nie wspomniał.", "OTO JEDYNA PRAWDA!", "Wniosek numer jeden brzmi następująco."], 0, "Модальность и спокойный ритм оставляют послевкусие вместо декларации."),
        ),
        "paragraphs": (
            "Maja pisała felieton o ciszy w pociągach. Pierwsza wersja była poprawna, lecz każda fraza miała ten sam rytm: teza, przykład, komentarz. Tekst brzmiał jak sprawne sprawozdanie, choć autorka chciała połączyć obserwację z dyskretnym humorem.",
            "W drugim szkicu zaczęła od długiego zdania o rozmowach, stukocie kół i sygnałach telefonów. Potem postawiła dwa słowa: «Nagle cisza». Krótka fraza nie była ozdobą; odtwarzała zmianę, której doświadczyli pasażerowie po wjeździe do tunelu.",
            "Maja usunęła trzy dowcipy, które tłumaczyły własną ironię. Zostawiła scenę z panem ogłaszającym przez telefon, że właśnie korzysta ze strefy ciszy. Komizm wynikał z kontrastu między deklaracją a zachowaniem, więc komentarz autorki stał się zbędny.",
            "Redaktorka zwróciła uwagę na zakończenie. Mocna puenta oskarżała wszystkich podróżnych o egoizm i łamała wcześniejszy ton ciekawości. Maja zastąpiła ją pytaniem, czy cisza jest jeszcze wspólną przestrzenią, czy już usługą zamawianą przez słuchawki.",
            "Felieton nie stał się bardziej «literacki» przez nagromadzenie figur. Stał się bardziej jej: uważny, lekko ironiczny i rytmicznie zmienny. Autorstwo ujawniło się w konsekwencji wyborów oraz w gotowości do usunięcia efektu, który nie służył perspektywie tekstu.",
        ),
        "reading": (
            ("Dlaczego pierwszy szkic nie miał wyraźnego głosu?", ["Każda fraza miała ten sam schemat", "Zawierał błędy ortograficzne", "Nie miał żadnych przykładów"], 0, "Монотонная композиция не поддерживала желаемый эффект."),
            ("Jaką funkcję pełniło «Nagle cisza»?", ["Odtwarzało nagłą zmianę doświadczenia", "Wyjaśniało termin techniczny", "Podsumowywało cały tekst"], 0, "Короткая фраза моделировала событие."),
            ("Dlaczego usunięto komentarz do sceny telefonicznej?", ["Kontrast sam tworzył komizm", "Scena była nieprawdziwa", "Humor był zakazany"], 0, "Ирония работала без авторского объяснения."),
            ("Co było problemem pierwszej puenty?", ["Łamała ton ciekawości oskarżeniem", "Była zbyt krótka", "Zawierała pytanie"], 0, "Резкая декларация не совпадала с голосом текста."),
            ("Czym zastąpiono mocną puentę?", ["Pytaniem o znaczenie wspólnej ciszy", "Listą zasad", "Cytatem z regulaminu"], 0, "Открытый вопрос сохранил наблюдательный тон."),
            ("Co ostatecznie tworzyło głos Mai?", ["Konsekwencja funkcjonalnych wyborów", "Liczba figur stylistycznych", "Wyłącznie pierwsza osoba"], 0, "Финал определяет голос как систему решений."),
        ),
    },
    {
        "id": "c2-capstone-project", "prefix": "c210", "title": "Проект C2", "emoji": "🏁",
        "description": "Создаём и защищаем сложный многожанровый проект с прозрачной самооценкой",
        "terms": (
            ("projekt wielogatunkowy", "многожанровый проект", "wyrażenie rzeczownikowe"), ("brief komunikacyjny", "коммуникационный бриф", "wyrażenie rzeczownikowe"),
            ("kryterium sukcesu", "критерий успеха", "wyrażenie rzeczownikowe"), ("łańcuch argumentacji", "цепочка аргументации", "wyrażenie rzeczownikowe"),
            ("wersja dla odbiorcy", "версия для аудитории", "wyrażenie rzeczownikowe"), ("nota metodologiczna", "методологическая записка", "wyrażenie rzeczownikowe"),
            ("arkusz samooceny", "лист самооценки", "wyrażenie rzeczownikowe"), ("informacja zwrotna", "обратная связь", "wyrażenie rzeczownikowe"),
            ("zdefiniować zakres", "определить объём", "wyrażenie czasownikowe"), ("uzasadnić wybór gatunku", "обосновать выбор жанра", "wyrażenie czasownikowe"),
            ("udokumentować źródło", "задокументировать источник", "wyrażenie czasownikowe"), ("skalibrować wniosek", "калибровать вывод", "wyrażenie czasownikowe"),
            ("obronić decyzję redakcyjną", "защитить редакторское решение", "wyrażenie czasownikowe"), ("zrewidować szkic", "переработать черновик", "wyrażenie czasownikowe"),
            ("wyciągnąć wnioski z procesu", "сделать выводы из процесса", "fraza"),
        ),
        "extra": (("portfolio", "портфолио", "rzeczownik"), ("wersja finalna", "финальная версия", "wyrażenie rzeczownikowe"), ("ślad zmian", "история изменений", "wyrażenie rzeczownikowe")),
        "theory": (("Единый замысел, разные жанры", "Проект объединяет аналитический текст, адаптацию для другой аудитории и устную защиту. Зафиксируй инварианты содержания, источники, риски и критерии до начала редактирования."), ("Самооценка по доказательствам", "Не оценивай работу общими словами. Покажи конкретную правку, объясни её эффект, назови оставшееся ограничение и следующий шаг. Итоговый уровень остаётся учебной целью, а не официальной сертификацией.")),
        "grammar": (
            ("Составьте: В итоговой версии я сузил вывод, поскольку один источник не подтверждал причинность.", ["W wersji finalnej zawęziłem wniosek, ponieważ jedno źródło nie potwierdzało przyczynowości.", "Jedno źródło dowodziło wszystkiego, dlatego rozszerzyłem wniosek.", "Wniosek finalny źródłem przyczynowość."], 0, "Ponieważ связывает редакторское решение с доказательным основанием."),
            ("Составьте: Я сохранила метафору, но изменила абзац так, чтобы яснее показать ограничение.", ["Zachowałam metaforę, lecz przebudowałam akapit tak, aby wyraźniej pokazać ograniczenie.", "Usunęłam ograniczenie, żeby metafora była pewna.", "Metafora akapit ograniczeniem zachowała."], 0, "Lecz сохраняет контраст, tak aby вводит функцию правки."),
            ("Które kryterium sukcesu jest sprawdzalne?", ["Odbiorca odróżnia fakt, interpretację i rekomendację.", "Tekst robi dobre wrażenie.", "Projekt jest bardzo ciekawy."], 0, "Критерий описывает наблюдаемое понимание аудитории."),
            ("Jak obronić zmianę gatunku?", ["Wskazać potrzeby odbiorcy, zachowane inwarianty i koszt kompresji.", "Powiedzieć, że krócej zawsze znaczy lepiej.", "Pominąć źródła."], 0, "Защита связывает форму с аудиторией и смысловыми рисками."),
            ("Co jest rzetelną samooceną?", ["Dwa przykłady udanych decyzji, jedno ograniczenie i plan rewizji.", "Stwierdzenie «wszystko jest idealne».", "Sama liczba słów."], 0, "Самооценка опирается на следы работы и допускает улучшение."),
            ("Która nota metodologiczna jest kompletna?", ["Podaje źródła, sposób selekcji, ograniczenia i stopień pewności.", "Zawiera tylko tytuł projektu.", "Ukrywa kryteria wyboru danych."], 0, "Полная записка делает путь к выводу проверяемым."),
        ),
        "paragraphs": (
            "Kamil przygotował projekt o zielonych dachach. Miał stworzyć analizę dla rady miasta, krótką informację dla mieszkańców i pięciominutową obronę decyzji redakcyjnych. W briefie zapisał wspólny cel: wyjaśnić możliwe korzyści bez obiecywania efektów, których lokalne dane jeszcze nie potwierdzają.",
            "Analiza porównywała trzy źródła: eksperyment z innym klimatem, miejskie dane obserwacyjne i wywiady z administratorami budynków. Kamil oddzielił wyniki dotyczące temperatury od opinii o kosztach. Wniosek zawęził do pilotażu, ponieważ żaden materiał nie rozstrzygał długoterminowej opłacalności.",
            "W wersji dla mieszkańców zrezygnował z tabeli, lecz zachował dwie liczby i główne zastrzeżenie. Termin «retencja» wyjaśnił przykładem wody zatrzymanej po ulewie. Nie użył hasła «dachy chłodzą miasto», tylko napisał, że mogą ograniczać nagrzewanie wybranych budynków.",
            "Podczas obrony recenzentka zapytała, dlaczego opis pilotażu pojawia się przed najbardziej efektownym przykładem zagranicznym. Kamil wyjaśnił, że odbiorca najpierw powinien poznać realny zakres decyzji. Po informacji zwrotnej dodał jednak krótkie zdanie łączące przykład z lokalnym pytaniem.",
            "W arkuszu samooceny wskazał mocną hierarchię dowodów i precyzyjną adaptację terminu. Za słabość uznał brak perspektywy osób wynajmujących mieszkania. Projekt zamknął planem kolejnego wywiadu, a nie deklaracją doskonałości. Finalna wersja dokumentowała zarówno rezultat, jak i drogę jego rewizji.",
        ),
        "reading": (
            ("Jaki wspólny cel miał projekt?", ["Wyjaśnić korzyści bez nadmiernych obietnic", "Przekonać wszystkich do budowy", "Skopiować zagraniczny raport"], 0, "Бриф фиксировал информирование с сохранением границ данных."),
            ("Dlaczego Kamil zawęził wniosek do pilotażu?", ["Brakowało danych o długoterminowej opłacalności", "Nie znał terminu retencja", "Rada odrzuciła projekt"], 0, "Источники не позволяли более сильную рекомендацию."),
            ("Jak wyjaśnił termin «retencja»?", ["Przykładem wody zatrzymanej po ulewie", "Definicją bez kontekstu", "Angielskim skrótem"], 0, "Термин адаптирован через понятное последствие."),
            ("Dlaczego pilotaż poprzedzał przykład zagraniczny?", ["Najpierw należało pokazać realny zakres decyzji", "Przykład był niewiarygodny", "Tabela się nie zmieściła"], 0, "Композиция подчинялась задаче адресата."),
            ("Jak Kamil wykorzystał informację zwrotną?", ["Dodał zdanie łączące przykład z lokalnym pytaniem", "Usunął ograniczenia", "Zmienił temat"], 0, "Он переработал связь, не разрушая иерархию."),
            ("Co czyniło samoocenę rzetelną?", ["Mocne strony, konkretna luka i następny krok", "Wyłącznie wysoka ocena", "Brak dalszych pytań"], 0, "Самооценка была доказательной и направленной на ревизию."),
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
        topic, _ = Topic.objects.update_or_create(id=data["id"], defaults={"course": course, "title": data["title"], "description": data["description"], "emoji": data["emoji"], "position": 8 + ti, "is_active": True})
        lessons = {}
        for offset, (suffix, kind, title, count) in enumerate(specs):
            lessons[suffix], _ = Lesson.objects.update_or_create(id=f"{data['prefix']}-{suffix}", defaults={"topic": topic, "kind": kind, "title": f"{title}: {data['title']}" if suffix == "quiz" else title, "plan_title": title, "subtitle": f"{count} заданий · целевой C2", "description": data["description"], "minutes": 14, "emoji": data["emoji"], "theory_title": data["title"] if suffix == "grammar" else "", "theory_sections": list(data["theory"]) if suffix == "grammar" else [], "source_metadata": SOURCE, "position": 332 + ti * 5 + offset, "is_active": True})
        cards = []
        for i, (polish, translation, _pos) in enumerate(data["terms"]):
            card, _ = Flashcard.objects.update_or_create(id=f"{data['prefix']}-{i + 1}", defaults={"polish": polish, "translation": translation, "example": f"W projekcie świadomie stosujemy pojęcie „{polish}”.", "source_metadata": SOURCE, "position": 992 + ti * 15 + i, "is_active": True}); cards.append(card)
        for suffix, subset in (("words", cards[:8]), ("review", cards[8:])):
            Link.objects.filter(lesson=lessons[suffix]).delete()
            for position, card in enumerate(subset): Link.objects.create(lesson=lessons[suffix], flashcard=card, position=position)
        quiz = tuple((f"Co znaczy „{p}”?", [t, data["terms"][(i + 1) % 15][1], data["terms"][(i + 2) % 15][1]], 0, f"„{p}” oznacza: {t}.") for i, (p, t, _pos) in enumerate(data["terms"][:10]))
        for suffix, questions in (("grammar", data["grammar"]), ("quiz", quiz), ("reading-check", data["reading"])):
            Question.objects.filter(lesson=lessons[suffix]).delete()
            for position, (prompt, options, correct, explanation) in enumerate(questions): Question.objects.create(lesson=lessons[suffix], prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
        glossary = {p: {"lemma": p, "translation": t, "part_of_speech": pos} for p, t, pos in data["terms"] + data["extra"]}
        Reading.objects.update_or_create(id=f"{data['prefix']}-tekst", defaults={"topic": topic, "title": data["title"], "description": data["description"], "level": "C2", "minutes": 16, "emoji": data["emoji"], "paragraphs": list(data["paragraphs"]), "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": f"{data['prefix']}-reading-check"}, "position": 65 + ti, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0059_c2_mediation_synthesis")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
