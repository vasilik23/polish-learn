from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-31", "level_status": "curriculum_target"}

TOPICS = (
    {
        "id": "c2-expert-mediation", "prefix": "c27", "title": "Экспертная медиация", "emoji": "🤝",
        "description": "Согласовываем сложные позиции для аудиторий с разным опытом и интересами",
        "terms": (
            ("mediatorka", "медиатор", "rzeczownik"), ("wspólny mianownik", "общий знаменатель", "wyrażenie rzeczownikowe"),
            ("rozbieżność stanowisk", "расхождение позиций", "wyrażenie rzeczownikowe"), ("interes strony", "интерес стороны", "wyrażenie rzeczownikowe"),
            ("pole porozumienia", "пространство для согласия", "wyrażenie rzeczownikowe"), ("termin specjalistyczny", "специальный термин", "wyrażenie rzeczownikowe"),
            ("asymetria wiedzy", "асимметрия знаний", "wyrażenie rzeczownikowe"), ("warunek brzegowy", "граничное условие", "wyrażenie rzeczownikowe"),
            ("uzgodnić definicję", "согласовать определение", "wyrażenie czasownikowe"), ("przełożyć na język praktyki", "перевести на язык практики", "wyrażenie czasownikowe"),
            ("zneutralizować napięcie", "снять напряжение", "wyrażenie czasownikowe"), ("zachować precyzję", "сохранить точность", "wyrażenie czasownikowe"),
            ("wydobyć potrzebę", "выявить потребность", "wyrażenie czasownikowe"), ("sformułować wariant pośredni", "сформулировать промежуточный вариант", "wyrażenie czasownikowe"),
            ("nie rozstrzygać za strony", "не решать за стороны", "fraza"),
        ),
        "extra": (("mandat negocjacyjny", "переговорный мандат", "wyrażenie rzeczownikowe"), ("język korzyści", "язык пользы", "wyrażenie rzeczownikowe"), ("protokół rozbieżności", "протокол разногласий", "wyrażenie rzeczownikowe")),
        "theory": (("Точность для разных аудиторий", "Медиация не упрощает смысл до лозунга. Она раскрывает термин, сохраняет ограничения и подбирает примеры, понятные конкретной стороне, явно отделяя перевод позиции от собственной оценки."), ("От позиции к интересу", "Фиксируй области согласия и разногласия, проверяй перефразирование у сторон и ищи варианты по интересам. Медиатор организует понимание, но не присваивает себе право решения.")),
        "grammar": (
            ("Составьте: Если обе стороны одинаково понимают риск, можно обсуждать допустимый предел.", ["Jeżeli obie strony tak samo rozumieją ryzyko, można omówić dopuszczalny próg.", "Ryzyko strony rozumieją, więc próg znika.", "Dopuszczalny próg rozumie obie strony."], 0, "Условие jeżeli отделяет согласование понятия от следующего решения."),
            ("Составьте: Иными словами, учёные требуют проверки, а жители — понятного срока.", ["Innymi słowy, naukowcy oczekują weryfikacji, mieszkańcy zaś jasnego terminu.", "Naukowcy mieszkańcy termin weryfikują inaczej słowy.", "Mieszkańcy nie mają żadnych oczekiwań."], 0, "Innymi słowy вводит проверяемую переформулировку, zaś сопоставляет интересы."),
            ("Która parafraza zachowuje warunek brzegowy?", ["Rozwiązanie działa przy małym obciążeniu; przy większym wymaga ponownego testu.", "Rozwiązanie działa zawsze.", "Rozwiązanie nigdy nie działa."], 0, "Первая версия сохраняет область применимости экспертного вывода."),
            ("Jak sprawdzić trafność mediacji?", ["Poprosić każdą stronę o potwierdzenie parafrazy.", "Uznać własne streszczenie za ostateczne.", "Usunąć punkty sporne."], 0, "Подтверждение сторон снижает риск смысловой подмены."),
            ("Co neutralizuje napięcie bez zamiatania sporu?", ["Nazwanie wspólnego celu i dokładnego punktu rozbieżności.", "Stwierdzenie, że konfliktu nie ma.", "Przerwanie rozmowy bez podsumowania."], 0, "Общая цель не отменяет точно названного разногласия."),
            ("Która propozycja nie rozstrzyga za strony?", ["Mogę przedstawić dwa warianty i ich konsekwencje; wybór należy do państwa.", "Zdecydowałam, który wariant musicie przyjąć.", "Nie podam żadnych informacji."], 0, "Медиатор структурирует выбор, сохраняя мандат сторон."),
        ),
        "paragraphs": (
            "W szpitalu spotkali się lekarze, informatycy i przedstawicielki pacjentów, aby omówić system przypominający o badaniach. Lekarze mówili o czułości modelu, pacjenci o liczbie fałszywych alarmów, a informatycy o progu klasyfikacji. Wszyscy używali słowa „bezpieczeństwo”, lecz nadawali mu inny zakres.",
            "Mediatorka zaczęła od uzgodnienia definicji. Poprosiła lekarzy, by przełożyli czułość na praktyczny przykład: ilu chorych system może przeoczyć. Następnie wyjaśniła, że niższy próg zmniejsza to ryzyko, ale zwiększa liczbę powiadomień kierowanych do zdrowych osób.",
            "Przedstawicielka pacjentów potwierdziła parafrazę, lecz dodała, że częste alarmy mogą osłabić zaufanie. Informatycy wskazali warunek brzegowy: wyniki pilotażu dotyczą jednej poradni i nie powinny być automatycznie przenoszone na cały region. Mediatorka zapisała oba ograniczenia bez ich wartościowania.",
            "Wspólnym mianownikiem okazało się wykrycie możliwie wielu przypadków bez przeciążania pacjentów. Powstały dwa warianty: ostrożny pilotaż z częstą kontrolą oraz szersze wdrożenie z możliwością wyłączenia części komunikatów. Przy każdym zapisano korzyści, ryzyka i dane potrzebne do oceny.",
            "Spotkanie nie zakończyło się wyborem. Strony uzgodniły jednak język, kryteria i termin dostarczenia nowych danych. Mediatorka nie rozstrzygnęła za ekspertów ani pacjentów; przekształciła asymetrię wiedzy w wspólną mapę decyzji, na której różnice stały się zrozumiałe i możliwe do negocjowania.",
        ),
        "reading": (
            ("Dlaczego słowo «bezpieczeństwo» nie wystarczało?", ["Strony nadawały mu różny zakres", "Było błędne językowo", "Informatycy go nie znali"], 0, "Общий термин скрывал разные критерии."),
            ("Jak wyjaśniono czułość modelu?", ["Przez liczbę możliwie przeoczonych chorych", "Przez koszt serwera", "Przez długość formularza"], 0, "Термин перевели в практическое последствие."),
            ("Jaki warunek brzegowy wskazali informatycy?", ["Pilotaż obejmował jedną poradnię", "System nie wysyłał komunikatów", "Nie zebrano żadnych danych"], 0, "Ограничение касалось переносимости результатов."),
            ("Co było wspólnym mianownikiem?", ["Wykrywanie przypadków bez przeciążania pacjentów", "Natychmiastowe wdrożenie", "Rezygnacja z modelu"], 0, "Так была сформулирована общая цель."),
            ("Co zapisano przy wariantach?", ["Korzyści, ryzyka i potrzebne dane", "Tylko koszty", "Nazwiska zwolenników"], 0, "Каждый вариант получил прозрачную карту последствий."),
            ("Jaki był rezultat mediacji?", ["Wspólny język i mapa decyzji", "Ostateczny wybór systemu", "Usunięcie rozbieżności"], 0, "Решение не принято, но условия осмысленного выбора созданы."),
        ),
    },
    {
        "id": "c2-research-synthesis", "prefix": "c28", "title": "Исследовательский синтез", "emoji": "🔬",
        "description": "Строим осторожный вывод по нескольким неоднородным источникам",
        "terms": (
            ("synteza źródeł", "синтез источников", "wyrażenie rzeczownikowe"), ("triangulacja danych", "триангуляция данных", "wyrażenie rzeczownikowe"),
            ("jakość dowodu", "качество доказательства", "wyrażenie rzeczownikowe"), ("próba badawcza", "исследовательская выборка", "wyrażenie rzeczownikowe"),
            ("zmienna zakłócająca", "смешивающая переменная", "wyrażenie rzeczownikowe"), ("ograniczenie metodologiczne", "методологическое ограничение", "wyrażenie rzeczownikowe"),
            ("stopień pewności", "степень уверенности", "wyrażenie rzeczownikowe"), ("zbieżność wyników", "сходимость результатов", "wyrażenie rzeczownikowe"),
            ("ważyć dowody", "взвешивать доказательства", "wyrażenie czasownikowe"), ("porównać metodologie", "сравнить методологии", "wyrażenie czasownikowe"),
            ("wyjaśnić rozbieżność", "объяснить расхождение", "wyrażenie czasownikowe"), ("kontrolować zmienną", "контролировать переменную", "wyrażenie czasownikowe"),
            ("zastrzec zakres wniosku", "оговорить область вывода", "wyrażenie czasownikowe"), ("wskazać lukę badawczą", "указать исследовательский пробел", "wyrażenie czasownikowe"),
            ("nie mylić korelacji z przyczynowością", "не путать корреляцию с причинностью", "fraza"),
        ),
        "extra": (("przegląd systematyczny", "систематический обзор", "wyrażenie rzeczownikowe"), ("dane jakościowe", "качественные данные", "wyrażenie rzeczownikowe"), ("replikowalność", "воспроизводимость", "rzeczownik")),
        "theory": (("Не среднее арифметическое", "Синтез учитывает дизайн, выборку и качество каждого источника. Совпадение результатов усиливает вывод лишь тогда, когда одинаковая ошибка или зависимость источников не объясняет это совпадение."), ("Калиброванный вывод", "Разделяй наблюдение, интерпретацию и рекомендацию. Называй степень уверенности, альтернативные объяснения и область применимости, не превращая отсутствие доказательства в доказательство отсутствия.")),
        "grammar": (
            ("Составьте: Результаты совпадают, однако исследования опираются на сходные малые выборки.", ["Wyniki są zbieżne, jednak badania opierają się na podobnych małych próbach.", "Wyniki są pewne, ponieważ próby nie mają znaczenia.", "Podobne wyniki prób badania jednak."], 0, "Jednak вводит методологическое ограничение для внешне согласованных результатов."),
            ("Составьте: Чем слабее контроль переменных, тем осторожнее должен быть причинный вывод.", ["Im słabsza kontrola zmiennych, tym ostrożniejszy powinien być wniosek przyczynowy.", "Kontrola jest słaba, więc przyczyna jest pewna.", "Tym zmienna, im przyczynowy wniosek."], 0, "Im..., tym... калибрует силу вывода по качеству контроля."),
            ("Który wniosek odróżnia korelację od przyczynowości?", ["Związek jest powtarzalny, ale dane obserwacyjne nie rozstrzygają o przyczynie.", "Korelacja zawsze dowodzi przyczyny.", "Skoro istnieje związek, znamy mechanizm."], 0, "Первая версия признаёт наблюдение и ограничивает причинную интерпретацию."),
            ("Jak ważyć sprzeczne źródła?", ["Porównać próby, metody, pomiar i ryzyko błędu.", "Policzyć publikacje bez oceny jakości.", "Wybrać najnowszy tytuł."], 0, "Вес доказательства зависит от метода, а не только от количества источников."),
            ("Co oznacza umiarkowany stopień pewności?", ["Dane wspierają wniosek, lecz istotne alternatywy pozostają otwarte.", "Nie wiadomo absolutnie nic.", "Wniosek jest niepodważalny."], 0, "Средняя уверенность сочетает поддержку и реальные ограничения."),
            ("Gdzie wskazano lukę badawczą?", ["Brakuje badań długoterminowych w grupie osób starszych.", "Badanie ma trzy tabele.", "Autorzy cytują literaturę."], 0, "Фраза точно называет отсутствующий тип данных и популяцию."),
        ),
        "paragraphs": (
            "Zespół analizował, czy krótkie spacery podczas pracy zdalnej poprawiają koncentrację. Pierwsze badanie eksperymentalne obejmowało czterdzieści osób i wykazało niewielką poprawę w teście uwagi. Drugie, obserwacyjne, śledziło tysiąc pracowników i znalazło podobny związek między przerwami a samooceną produktywności.",
            "Pozorna zbieżność nie oznaczała jednak, że dowody są równoważne. Eksperyment lepiej kontrolował porę dnia, lecz trwał tylko tydzień. Badanie obserwacyjne miało większą próbę, ale osoby wybierające spacery mogły różnić się snem, obciążeniem pracą i motywacją.",
            "Wywiady jakościowe dodały trzeci wymiar. Uczestnicy opisywali nie tylko ruch, lecz także chwilowe odcięcie od komunikatorów. Sugerowało to alternatywny mechanizm: korzyść mogła wynikać z przerwy poznawczej, a nie wyłącznie z aktywności fizycznej.",
            "Badacze zważyli źródła zamiast liczyć je jak głosy. Uznali z umiarkowaną pewnością, że regularne krótkie przerwy sprzyjają subiektywnej koncentracji. Nie przesądzili, czy spacer jest lepszy od spokojnego odpoczynku ani czy efekt utrzymuje się przez wiele miesięcy.",
            "Rekomendacja miała więc formę niskiego ryzyka: pracownicy mogą testować krótkie przerwy i obserwować własny rytm, a organizacje nie powinny przedstawiać spaceru jako obowiązkowej terapii wydajności. Luka badawcza dotyczyła porównania rodzajów przerw oraz długoterminowych skutków w różnych zawodach.",
        ),
        "reading": (
            ("Co wykazało pierwsze badanie?", ["Niewielką poprawę w teście uwagi", "Brak jakichkolwiek zmian", "Spadek produktywności"], 0, "Эксперимент дал небольшой эффект в тесте внимания."),
            ("Dlaczego duża próba nie rozstrzygała przyczynowości?", ["Uczestnicy sami wybierali spacery i mogli różnić się innymi cechami", "Badanie trwało zbyt długo", "Nie pytano o produktywność"], 0, "Самоотбор оставлял смешивающие переменные."),
            ("Jaki mechanizm zasugerowały wywiady?", ["Przerwę poznawczą od komunikatorów", "Wyłącznie zmianę pogody", "Rywalizację między pracownikami"], 0, "Качественные данные расширили возможное объяснение."),
            ("Jaki wniosek uznano za umiarkowanie pewny?", ["Krótkie przerwy sprzyjają subiektywnej koncentracji", "Spacer leczy wszystkie problemy", "Każdy rodzaj przerwy działa identycznie"], 0, "Итог был ограничен субъективной концентрацией."),
            ("Dlaczego rekomendacja miała formę testu?", ["Korzyść była prawdopodobna, a ryzyko małe, lecz dowód ograniczony", "Nie istniały żadne dane", "Spacer był obowiązkowy"], 0, "Рекомендация соразмерна качеству доказательства."),
            ("Jaką lukę badawczą wskazano?", ["Porównanie rodzajów przerw i skutków długoterminowych", "Brak definicji pracy", "Brak danych o cenie obuwia"], 0, "Финал точно называет недостающие сравнения."),
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
        topic, _ = Topic.objects.update_or_create(id=data["id"], defaults={"course": course, "title": data["title"], "description": data["description"], "emoji": data["emoji"], "position": 6 + ti, "is_active": True})
        lessons = {}
        for offset, (suffix, kind, title, count) in enumerate(specs):
            lessons[suffix], _ = Lesson.objects.update_or_create(id=f"{data['prefix']}-{suffix}", defaults={"topic": topic, "kind": kind, "title": f"{title}: {data['title']}" if suffix == "quiz" else title, "plan_title": title, "subtitle": f"{count} заданий · целевой C2", "description": data["description"], "minutes": 14, "emoji": data["emoji"], "theory_title": data["title"] if suffix == "grammar" else "", "theory_sections": list(data["theory"]) if suffix == "grammar" else [], "source_metadata": SOURCE, "position": 322 + ti * 5 + offset, "is_active": True})
        cards = []
        for i, (polish, translation, _pos) in enumerate(data["terms"]):
            card, _ = Flashcard.objects.update_or_create(id=f"{data['prefix']}-{i + 1}", defaults={"polish": polish, "translation": translation, "example": f"W analizie świadomie stosujemy pojęcie „{polish}”.", "source_metadata": SOURCE, "position": 962 + ti * 15 + i, "is_active": True}); cards.append(card)
        for suffix, subset in (("words", cards[:8]), ("review", cards[8:])):
            Link.objects.filter(lesson=lessons[suffix]).delete()
            for position, card in enumerate(subset): Link.objects.create(lesson=lessons[suffix], flashcard=card, position=position)
        quiz = tuple((f"Co znaczy „{p}”?", [t, data["terms"][(i + 1) % 15][1], data["terms"][(i + 2) % 15][1]], 0, f"„{p}” oznacza: {t}.") for i, (p, t, _pos) in enumerate(data["terms"][:10]))
        for suffix, questions in (("grammar", data["grammar"]), ("quiz", quiz), ("reading-check", data["reading"])):
            Question.objects.filter(lesson=lessons[suffix]).delete()
            for position, (prompt, options, correct, explanation) in enumerate(questions): Question.objects.create(lesson=lessons[suffix], prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
        glossary = {p: {"lemma": p, "translation": t, "part_of_speech": pos} for p, t, pos in data["terms"] + data["extra"]}
        Reading.objects.update_or_create(id=f"{data['prefix']}-tekst", defaults={"topic": topic, "title": data["title"], "description": data["description"], "level": "C2", "minutes": 16, "emoji": data["emoji"], "paragraphs": list(data["paragraphs"]), "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": f"{data['prefix']}-reading-check"}, "position": 63 + ti, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0058_c2_transformation_culture")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
