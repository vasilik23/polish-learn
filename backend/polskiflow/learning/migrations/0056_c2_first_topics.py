from django.db import migrations


SOURCE = {
    "origin": "original",
    "created_for": "PolskiFlow",
    "verified_at": "2026-08-31",
    "level_status": "curriculum_target",
}

TOPICS = (
    {
        "id": "c2-semantic-precision",
        "title": "Смысловая точность",
        "description": "Различаем пресуппозицию, импликатуру и намеренную недосказанность",
        "emoji": "🧠",
        "prefix": "c21",
        "terms": (
            ("presupozycja", "пресуппозиция", "rzeczownik"),
            ("implikatura", "импликатура, подразумеваемый смысл", "rzeczownik"),
            ("niedopowiedzenie", "недосказанность", "rzeczownik"),
            ("wieloznaczność", "многозначность", "rzeczownik"),
            ("dosłowność", "буквальность", "rzeczownik"),
            ("odczytanie intencji", "считывание намерения", "wyrażenie rzeczownikowe"),
            ("sens naddany", "добавочный смысл", "wyrażenie rzeczownikowe"),
            ("wynikać z kontekstu", "следовать из контекста", "wyrażenie czasownikowe"),
            ("uchylić się od odpowiedzi", "уклониться от ответа", "wyrażenie czasownikowe"),
            ("zasugerować mimochodem", "намекнуть вскользь", "wyrażenie czasownikowe"),
            ("doprecyzować zakres", "уточнить границы", "wyrażenie czasownikowe"),
            ("rozbroić dwuznaczność", "устранить двусмысленность", "wyrażenie czasownikowe"),
            ("pozostawić pole do interpretacji", "оставить пространство для интерпретации", "fraza"),
            ("czytać między wierszami", "читать между строк", "frazeologizm"),
            ("nie bez znaczenia", "не без значения", "fraza modalna"),
        ),
        "extra_glossary": (
            ("pragmatyka", "прагматика", "rzeczownik"),
            ("adresat zbiorowy", "коллективный адресат", "wyrażenie rzeczownikowe"),
            ("warstwa deklaratywna", "декларативный слой", "wyrażenie rzeczownikowe"),
        ),
        "theory": (
            ("Смысл за пределами слов", "Пресуппозиция считается уже принятой предпосылкой, а импликатура выводится из контекста и принципов сотрудничества. Проверяй, что именно сказано, что предполагается и что лишь вероятно подразумевается."),
            ("Точная переформулировка", "При медиации отмечай степень уверенности: autor stwierdza, sugeruje, zdaje się zakładać. Не превращай намёк в утверждение и сохраняй продуктивную неоднозначность, если она существенна."),
        ),
        "grammar": (
            ("Составьте: Автор лишь намекает, что решение было принято раньше.", ["Autor jedynie sugeruje, że decyzję podjęto wcześniej.", "Autor potwierdza decyzję bez żadnych zastrzeżeń.", "Decyzja wcześniej autora jedynie sugeruje."], 0, "Jedynie sugeruje точно маркирует вывод, а не подтверждённый факт."),
            ("Составьте: Из контекста следует, что адресат знал об изменении.", ["Z kontekstu wynika, że adresat wiedział o zmianie.", "Adresat zmianę z kontekstu wiedzieć powinien.", "Kontekst zaprzecza wiedzy adresata o zmianie."], 0, "Конструкция wynikać z + dopełniacz вводит контекстуальный вывод."),
            ("Które zdanie oddziela treść dosłowną od wniosku?", ["Dosłownie autor mówi o kosztach; pośrednio podważa sens reformy.", "Autor na pewno odrzuca reformę.", "Koszty są reformą."], 0, "Первая формулировка отдельно называет буквальный и выводимый уровни смысла."),
            ("Jak ostrożnie przypisać autorowi ukryte założenie?", ["Autor zdaje się zakładać, że odbiorcy znają wcześniejszy spór.", "Autor bezsprzecznie kłamie.", "Wszyscy odbiorcy wszystko wiedzą."], 0, "Zdaje się zakładać сохраняет эпистемическую осторожность."),
            ("Która korekta rozbraja dwuznaczność zdania «Rozmawiała z siostrą Anny»?", ["Rozmawiała z Anną, która ma siostrę.", "Rozmawiała z nią.", "Rozmawiała z siostrą."], 0, "Переформулировка прямо указывает референта и устраняет конкурирующее прочтение."),
            ("Jak zachować niedopowiedzenie bez dopisywania faktu?", ["Wypowiedź pozostawia otwarte pytanie o motywy rozmówcy.", "Rozmówca kierował się wyłącznie zazdrością.", "Motyw nie ma żadnego znaczenia."], 0, "Открытый вопрос описывает недосказанность, не выдавая интерпретацию за факт."),
        ),
        "paragraphs": (
            "Podczas posiedzenia komisji przewodnicząca powiedziała, że projekt „nie jest pozbawiony zalet”. Część słuchaczy uznała to za ostrożną pochwałę, inni — za elegancki sposób okazania rezerwy. Sama warstwa dosłowna nie rozstrzygała sporu.",
            "Językoznawczyni zaproponowała więc rozdzielenie trzech poziomów. Zdanie stwierdzało istnienie zalet, presuponowało wspólną znajomość projektu, a przez nietypowo powściągliwą formę mogło implikować, że zastrzeżenia przeważają nad aprobatą.",
            "Nagranie ujawniło dodatkowy szczegół: chwilę wcześniej rozmówcy dyskutowali o wysokich kosztach. Ten kontekst wzmacniał krytyczne odczytanie, lecz nadal go nie dowodził. Badaczka zaznaczyła różnicę między wnioskiem dobrze uzasadnionym a jedyną możliwą interpretacją.",
            "W protokole zapisano zatem, że przewodnicząca dostrzegła zalety projektu, a jej ogólna ocena pozostała niejednoznaczna. Nie przypisano jej ani poparcia, ani sprzeciwu. Dopiero prośba o doprecyzowanie mogłaby zamknąć pole interpretacji.",
            "Przykład pokazał, że zaawansowana kompetencja nie polega na odgadywaniu ukrytej prawdy. Polega raczej na ważeniu sygnałów, nazywaniu stopnia pewności i powstrzymaniu się od twierdzenia mocniejszego niż dostępne dane.",
        ),
        "reading_questions": (
            ("Które dwa odczytania wypowiedzi pojawiły się wśród słuchaczy?", ["Ostrożna pochwała i elegancka rezerwa", "Zgoda i odmowa głosowania", "Opis kosztów i harmonogramu"], 0, "Оба прочтения прямо названы в первом абзаце."),
            ("Co presuponowała wypowiedź według językoznawczyni?", ["Wspólną znajomość projektu", "Jednomyślność komisji", "Brak kosztów"], 0, "Пресуппозицией была общая осведомлённость о проекте."),
            ("Jak wcześniejsza rozmowa o kosztach wpłynęła na interpretację?", ["Wzmocniła krytyczne odczytanie, ale go nie dowiodła", "Całkowicie je obaliła", "Nie miała żadnego związku"], 0, "Контекст повысил правдоподобие, но не сделал вывод доказанным."),
            ("Dlaczego protokół nie przypisał poparcia ani sprzeciwu?", ["Ogólna ocena pozostała niejednoznaczna", "Nagranie zaginęło", "Projekt wycofano"], 0, "Текст подчёркивает сохранённую неоднозначность оценки."),
            ("Co mogłoby zamknąć pole interpretacji?", ["Prośba o doprecyzowanie", "Kolejne domysły", "Usunięcie protokołu"], 0, "Автор прямо указывает на запрос уточнения."),
            ("Jaka zasada podsumowuje tekst?", ["Nie formułować twierdzenia mocniejszego niż dane", "Zawsze wybierać najbardziej krytyczne odczytanie", "Ignorować kontekst"], 0, "Финальный абзац формулирует именно этот принцип."),
        ),
    },
    {
        "id": "c2-rhetorical-strategy",
        "title": "Риторическая стратегия",
        "description": "Управляем перспективой, темпом и силой аргумента без манипуляции",
        "emoji": "🎙️",
        "prefix": "c22",
        "terms": (
            ("figura retoryczna", "риторическая фигура", "wyrażenie rzeczownikowe"),
            ("punkt ciężkości", "смысловой центр", "wyrażenie rzeczownikowe"),
            ("gradacja", "градация", "rzeczownik"),
            ("antyteza", "антитеза", "rzeczownik"),
            ("paralelizm składniowy", "синтаксический параллелизм", "wyrażenie rzeczownikowe"),
            ("pytanie retoryczne", "риторический вопрос", "wyrażenie rzeczownikowe"),
            ("puenta", "пуанте, заключительный акцент", "rzeczownik"),
            ("wyprzedzić kontrargument", "предвосхитить контраргумент", "wyrażenie czasownikowe"),
            ("stopniować napięcie", "наращивать напряжение", "wyrażenie czasownikowe"),
            ("przesunąć akcent", "сместить акцент", "wyrażenie czasownikowe"),
            ("zawęzić tezę", "сузить тезис", "wyrażenie czasownikowe"),
            ("odwrócić perspektywę", "изменить перспективу", "wyrażenie czasownikowe"),
            ("pozorny dylemat", "ложная дилемма", "wyrażenie rzeczownikowe"),
            ("chwyt erystyczny", "эристический приём", "wyrażenie rzeczownikowe"),
            ("uczciwość argumentacyjna", "честность аргументации", "wyrażenie rzeczownikowe"),
        ),
        "extra_glossary": (
            ("rytm wypowiedzi", "ритм высказывания", "wyrażenie rzeczownikowe"),
            ("hierarchia racji", "иерархия доводов", "wyrażenie rzeczownikowe"),
            ("odporność argumentu", "устойчивость аргумента", "wyrażenie rzeczownikowe"),
        ),
        "theory": (
            ("Композиция как аргумент", "Порядок доводов, повтор и синтаксический параллелизм направляют внимание. Сильная композиция делает логику видимой; она не должна подменять доказательство эмоциональным эффектом."),
            ("Риторика без манипуляции", "Предвосхищай сильнейший контраргумент, называй ограничения и проверяй ложные дилеммы. Этическая стратегия усиливает тезис прозрачностью, а не сокрытием неудобных данных."),
        ),
        "grammar": (
            ("Составьте: Мы меняем не цель, а способ её достижения.", ["Nie zmieniamy celu, lecz sposób jego osiągnięcia.", "Zmieniamy cel i pomijamy sposób.", "Sposób celu nie zmieniamy osiągnięcia."], 0, "Конструкция nie..., lecz... создаёт точную антитезу."),
            ("Составьте: Даже если возражение верно, оно не опровергает главного вывода.", ["Nawet jeśli zarzut jest trafny, nie obala głównego wniosku.", "Zarzut trafny obala zawsze każdy wniosek.", "Główny wniosek nawet zarzut jeśli."], 0, "Nawet jeśli вводит уступку без отказа от основного вывода."),
            ("Które zdanie stosuje paralelizm bez pustego patosu?", ["Potrzebujemy danych, potrzebujemy czasu, potrzebujemy odpowiedzialności.", "Potrzebujemy wszystkiego i natychmiast.", "Dane są, jakie są."], 0, "Повтор одной структуры создаёт параллелизм и сохраняет содержательные опоры."),
            ("Jak wyprzedzić mocny kontrargument?", ["Można zarzucić tej propozycji wysoki koszt; dlatego porównajmy go z kosztem zaniechania.", "Kto się nie zgadza, ten nie rozumie problemu.", "Koszt nie istnieje."], 0, "Первая версия признаёт возражение и предлагает критерий сравнения."),
            ("Która puenta wynika z argumentu, zamiast tylko brzmieć efektownie?", ["Skoro pilotaż zmniejszył liczbę błędów, rozszerzenie wymaga teraz niezależnej ewaluacji.", "Przyszłość należy do odważnych.", "Nie ma innej drogi."], 0, "Вывод связан с данными и одновременно обозначает следующий критерий проверки."),
            ("Gdzie pojawia się pozorny dylemat?", ["Albo przyjmiemy projekt dziś, albo miasto nigdy się nie rozwinie.", "Możemy wdrożyć projekt, zmienić go albo odrzucić.", "Decyzja wymaga danych o kosztach."], 0, "Первая реплика искусственно сводит множество возможностей к двум крайностям."),
        ),
        "paragraphs": (
            "Zespół rzeczniczki przygotował wystąpienie o ograniczeniu ruchu w centrum. Pierwsza wersja zaczynała się od alarmujących danych, po których natychmiast padało pytanie retoryczne: „Czy naprawdę stać nas na bezczynność?”. Tekst był dynamiczny, lecz dzielił odbiorców na zwolenników działania i rzekomych obrońców chaosu.",
            "Redaktorka rozpoznała w tej konstrukcji pozorny dylemat. Zaproponowała odwrócenie perspektywy: zamiast przeciwstawiać działanie bezczynności, należało porównać trzy warianty zmian, ich koszty i skutki dla różnych grup mieszkańców.",
            "Nowa wersja zachowała rytm dzięki paralelizmowi: „sprawdźmy dane, sprawdźmy koszty, sprawdźmy konsekwencje”. Potem wyprzedzała kontrargument przedsiębiorców, przyznając, że reorganizacja dostaw będzie kosztowna, i wskazując fundusz przejściowy jako częściową odpowiedź.",
            "Najważniejsza zmiana dotyczyła puenty. Zamiast hasła o odwadze pojawił się wniosek o półrocznym pilotażu z publicznymi kryteriami oceny. Retoryczny punkt ciężkości przesunął się z moralnej presji na możliwość wspólnego sprawdzenia rozwiązania.",
            "Wystąpienie stało się mniej widowiskowe, ale bardziej odporne na krytykę. Rzeczniczka nie zrezygnowała z perswazji: użyła kompozycji, gradacji i antytezy. Podporządkowała je jednak uczciwości argumentacyjnej, dzięki czemu odbiorcy mogli ocenić nie tylko siłę słów, lecz także jakość racji.",
        ),
        "reading_questions": (
            ("Dlaczego pierwsza wersja wystąpienia była problematyczna?", ["Tworzyła pozorny dylemat", "Nie zawierała żadnych danych", "Dotyczyła innego miasta"], 0, "Она сводила аудиторию к сторонникам действия и мнимым защитникам хаоса."),
            ("Jak redaktorka odwróciła perspektywę?", ["Porównała trzy warianty, koszty i skutki", "Usunęła wszystkie argumenty", "Zastąpiła wystąpienie reklamą"], 0, "Вместо бинарного выбора предложено сравнение вариантов."),
            ("Czemu służył paralelizm w nowej wersji?", ["Zachowaniu rytmu przy jasnej strukturze kontroli", "Ukryciu kosztów", "Ośmieszeniu przedsiębiorców"], 0, "Повтор организовал три проверяемых шага."),
            ("Jak potraktowano kontrargument przedsiębiorców?", ["Uznano koszt i wskazano częściową odpowiedź", "Przemilczano go", "Nazwano go kłamstwem"], 0, "Возражение признано и связано с переходным фондом."),
            ("Na czym polegała nowa puenta?", ["Na propozycji pilotażu z kryteriami oceny", "Na wezwaniu do natychmiastowej decyzji", "Na pytaniu bez odpowiedzi"], 0, "Финал стал проверяемым предложением."),
            ("Co oznacza w tekście uczciwość argumentacyjna?", ["Podporządkowanie środków retorycznych jakości racji", "Rezygnację z perswazji", "Unikanie wszelkich figur stylistycznych"], 0, "Риторические средства сохранены, но подчинены прозрачному доводу."),
        ),
    },
)


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course = apps.get_model("learning", "Course")
    Topic = apps.get_model("learning", "Topic")
    Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard")
    LessonFlashcard = apps.get_model("learning", "LessonFlashcard")
    Question = apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")

    course, _ = Course.objects.update_or_create(
        id="c2-mastery",
        defaults={
            "title": "C2 · Мастерство смысла",
            "description": "Целевая программа: точная интерпретация и ответственная риторика",
            "level": "C2",
            "position": 5,
            "is_active": True,
        },
    )
    for topic_position, data in enumerate(TOPICS):
        topic, _ = Topic.objects.update_or_create(
            id=data["id"],
            defaults={
                "course": course,
                "title": data["title"],
                "description": data["description"],
                "emoji": data["emoji"],
                "position": topic_position,
                "is_active": True,
            },
        )
        lesson_specs = (
            ("words", "words", "Лексика в точном контексте", 8),
            ("grammar", "grammar", "Точность конструкции", 6),
            ("review", "review", "Активное повторение", 7),
            ("quiz", "quiz", f"Итог: {data['title']}", 10),
            ("reading-check", "quiz", "Аналитическая проверка текста", 6),
        )
        lessons = {}
        for offset, (suffix, kind, title, count) in enumerate(lesson_specs):
            lessons[suffix], _ = Lesson.objects.update_or_create(
                id=f"{data['prefix']}-{suffix}",
                defaults={
                    "topic": topic,
                    "kind": kind,
                    "title": title,
                    "plan_title": title,
                    "subtitle": f"{count} заданий · целевой C2",
                    "description": data["description"],
                    "minutes": 14,
                    "emoji": data["emoji"],
                    "theory_title": data["title"] if suffix == "grammar" else "",
                    "theory_sections": list(data["theory"]) if suffix == "grammar" else [],
                    "source_metadata": SOURCE,
                    "position": 292 + topic_position * 5 + offset,
                    "is_active": True,
                },
            )

        cards = []
        for index, (polish, translation, _part_of_speech) in enumerate(data["terms"]):
            card, _ = Flashcard.objects.update_or_create(
                id=f"{data['prefix']}-{index + 1}",
                defaults={
                    "polish": polish,
                    "translation": translation,
                    "example": f"W analizie świadomie stosujemy pojęcie „{polish}” i sprawdzamy jego funkcję.",
                    "source_metadata": SOURCE,
                    "position": 872 + topic_position * 15 + index,
                    "is_active": True,
                },
            )
            cards.append(card)
        for suffix, subset in (("words", cards[:8]), ("review", cards[8:])):
            LessonFlashcard.objects.filter(lesson=lessons[suffix]).delete()
            for position, card in enumerate(subset):
                LessonFlashcard.objects.create(lesson=lessons[suffix], flashcard=card, position=position)

        quiz = tuple(
            (
                f"Co w tym kontekście znaczy „{polish}”?",
                [translation, data["terms"][(index + 1) % 15][1], data["terms"][(index + 2) % 15][1]],
                0,
                f"„{polish}” oznacza tutaj: {translation}.",
            )
            for index, (polish, translation, _part_of_speech) in enumerate(data["terms"][:10])
        )
        for suffix, questions in (("grammar", data["grammar"]), ("quiz", quiz), ("reading-check", data["reading_questions"])):
            Question.objects.filter(lesson=lessons[suffix]).delete()
            for position, (prompt, options, correct, explanation) in enumerate(questions):
                Question.objects.create(
                    lesson=lessons[suffix], prompt=prompt, options=options,
                    correct=correct, explanation=explanation, position=position,
                )

        glossary = {
            polish: {"lemma": polish, "translation": translation, "part_of_speech": part_of_speech}
            for polish, translation, part_of_speech in data["terms"] + data["extra_glossary"]
        }
        ReadingText.objects.update_or_create(
            id=f"{data['prefix']}-tekst",
            defaults={
                "topic": topic,
                "title": data["title"],
                "description": data["description"],
                "level": "C2",
                "minutes": 16,
                "emoji": data["emoji"],
                "paragraphs": list(data["paragraphs"]),
                "glossary": glossary,
                "source_metadata": {**SOURCE, "comprehension_lesson_id": f"{data['prefix']}-reading-check"},
                "position": 57 + topic_position,
                "is_active": True,
            },
        )


class Migration(migrations.Migration):
    dependencies = [("learning", "0055_complete_c1_curriculum")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
