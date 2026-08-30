from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}

SPEC = {
    "id": "b2-psychology-relationships", "title": "Психология и отношения",
    "description": "Точно описываем эмоции, мотивы и неоднозначные ситуации в отношениях", "emoji": "🧠", "position": 6,
    "prefix": "b2psych", "lesson_start": 198, "card_start": 632,
    "theory": ("Оттенки модальности и оценки", [
        ["Степень уверенности", "Наверняка: z pewnością / niewątpliwie; вероятно: prawdopodobnie / przypuszczalnie; осторожная гипотеза: być może / możliwe, że."],
        ["Оценка поведения", "Wydaje mi się rozsądne, że… оценивает решение мягче, чем To było nierozsądne. Конструкция mógł / mogła + infinitiv показывает упущенную возможность без прямого обвинения."],
        ["Мотив и потребность", "Zależało mu na…, obawiała się, że… и potrzebowała, żeby… связывают поступок с внутренней причиной, не выдавая догадку за факт."],
    ]),
    "cards": (
        ("odczuwać napięcie", "чувствовать напряжение", "Przed rozmową oboje odczuwali napięcie."),
        ("poczucie bezpieczeństwa", "чувство безопасности", "Szczerość buduje poczucie bezpieczeństwa."),
        ("potrzeba bliskości", "потребность в близости", "Każdy inaczej wyraża potrzebę bliskości."),
        ("wycofać się", "отстраниться, выйти из ситуации", "Paweł wycofał się z rozmowy, gdy emocje wzrosły."),
        ("okazać zrozumienie", "проявить понимание", "Warto najpierw okazać zrozumienie."),
        ("przypisywać komuś intencje", "приписывать кому-то намерения", "Nie należy przypisywać komuś intencji bez pytania."),
        ("reagować impulsywnie", "реагировать импульсивно", "Pod presją łatwiej reagować impulsywnie."),
        ("stawiać granice", "устанавливать границы", "Można stawiać granice bez odrzucania drugiej osoby."),
        ("mieć żal", "обижаться, испытывать досаду", "Miała żal, że nikt jej nie wysłuchał."),
        ("czuć się pominiętym", "чувствовать себя обойдённым вниманием", "Czuł się pominięty podczas podejmowania decyzji."),
        ("unikać konfrontacji", "избегать конфронтации", "Unikanie konfrontacji nie zawsze rozwiązuje problem."),
        ("wziąć odpowiedzialność", "взять ответственность", "Oboje wzięli odpowiedzialność za swoje słowa."),
        ("dojść do porozumienia", "прийти к согласию", "Po spokojnej rozmowie doszli do porozumienia."),
        ("prawdopodobnie", "вероятно", "Prawdopodobnie potrzebował czasu, żeby odpowiedzieć."),
        ("z perspektywy", "с точки зрения", "Z jej perspektywy cisza oznaczała brak zainteresowania."),
    ),
    "grammar": (
        ("Ola ___ poczuła się pominięta, ale nie znamy wszystkich okoliczności.", ["prawdopodobnie", "niewątpliwie na pewno", "bez wątpienia zawsze"], 0, "Prawdopodobnie обозначает обоснованную, но не абсолютную уверенность."),
        ("Z jego perspektywy rozsądne ___ odłożenie rozmowy do rana.", ["wydawało się", "dowiodło się", "musiało zawsze"], 0, "Wydawało się передаёт субъективную оценку, а не установленный факт."),
        ("Marta mogła ___ wcześniej, że potrzebuje chwili spokoju.", ["powiedzieć", "powiedziała", "mówiąc"], 0, "Mogła + infinitiv показывает возможное, но не реализованное действие."),
        ("Nie przypisuj mu intencji; ___ obawiał się reakcji grupy.", ["być może", "bezsprzecznie", "na pewno zawsze"], 0, "Być może вводит осторожную гипотезу о мотиве."),
        ("Составьте: Вероятно, она отстранилась, потому что боялась очередного конфликта.", ["Prawdopodobnie wycofała się, ponieważ obawiała się kolejnego konfliktu.", "Pewna wycofać, bo konflikt ją zawsze.", "Wycofała prawdopodobny obawiając konfliktowi."], 0, "Prawdopodobnie смягчает вывод, а obawiać się требует родительного падежа."),
        ("Составьте: С его точки зрения она могла проявить больше понимания.", ["Z jego perspektywy mogła okazać więcej zrozumienia.", "Jego perspektywa mogła okazała rozumienie więcej.", "Według jego ona więcej zrozumieć mogła okazała."], 0, "Z perspektywy + родительный задаёт точку зрения; mogła + infinitiv — упущенную возможность."),
    ),
    "quiz": (
        ("Co znaczy stawiać granice?", ["ясно обозначать допустимое в отношениях", "полностью прекращать общение", "скрывать свои потребности"], 0, "Границы защищают потребности и не равны отвержению."),
        ("Które słowo sygnalizuje ostrożną hipotezę?", ["być może", "niewątpliwie", "bezsprzecznie"], 0, "Być może оставляет место неопределённости."),
        ("Nie chcę ci ___ złych intencji.", ["przypisywać", "wycofywać", "odczuwać się"], 0, "Естественное сочетание: przypisywać komuś intencje."),
        ("Co pomaga uniknąć impulsywnej reakcji?", ["nazwanie emocji i krótka przerwa", "natychmiastowy zarzut", "udawanie, że problemu nie ma"], 0, "Пауза и называние эмоции снижают напряжение."),
        ("Kasia mogła powiedzieć to łagodniej oznacza, że…", ["существовала другая возможность поведения", "она точно ничего не сказала", "говорить мягче было запрещено"], 0, "Mogła + infinitiv здесь оценивает упущенную возможность."),
        ("Które zdanie nie przedstawia domysłu jako faktu?", ["Prawdopodobnie zależało mu na uznaniu.", "Na pewno chciał wszystkich zranić.", "Jego motyw jest oczywisty."], 0, "Prawdopodobnie явно маркирует степень уверенности."),
        ("Po szczerej rozmowie łatwiej ___.", ["dojść do porozumienia", "przypisać ciszę", "odczuwać granicę"], 0, "Dojść do porozumienia — прийти к согласию."),
        ("Czuła żal, ponieważ…", ["jej potrzeba nie została zauważona", "zawsze była spokojna", "porozumienie już istniało"], 0, "Żal часто возникает из-за пережитой несправедливости или недостатка внимания."),
        ("Jak brzmi najbardziej empatyczna reakcja?", ["Rozumiem, że mogłeś poczuć się pominięty.", "Przesadzasz jak zawsze.", "Wiem lepiej, co naprawdę czujesz."], 0, "Первая реплика называет возможное чувство без навязывания интерпретации."),
        ("Z jej perspektywy oznacza…", ["с её точки зрения", "по доказанному правилу", "против её воли"], 0, "Выражение отделяет субъективное восприятие от общего факта."),
    ),
    "reading": {
        "id": "b2psych-rozmowa-po-nieudanym-wyjezdzie", "title": "Rozmowa po nieudanym wyjeździe",
        "description": "Как отличить наблюдение от догадки о мотивах и восстановить диалог", "emoji": "🧠", "minutes": 12,
        "paragraphs": [
            "Po wspólnym wyjeździe Lena i Michał przez kilka dni rozmawiali wyłącznie o sprawach praktycznych. Lena miała żal, że podczas planowania większość decyzji zapadła bez niej. Michał natomiast odczuwał napięcie, ponieważ każdą próbę wyjaśnienia odbierał jako zapowiedź kolejnego konfliktu. Oboje potrzebowali bliskości, lecz każde z nich inaczej interpretowało ciszę drugiej osoby.",
            "Lena początkowo przypisywała Michałowi obojętność. Z jej perspektywy wycofał się właśnie wtedy, gdy najbardziej potrzebowała wsparcia. Później uznała jednak, że była to tylko jedna z możliwych interpretacji. Michał prawdopodobnie unikał konfrontacji, bo obawiał się, że zareaguje impulsywnie. Nie oznaczało to, że jej uczucia były dla niego nieważne.",
            "Podczas rozmowy ustalili zasadę: najpierw opisują to, co zauważyli, a dopiero potem mówią o emocjach i potrzebach. Lena powiedziała: «Kiedy wybraliście trasę beze mnie, poczułam się pominięta». Nie stwierdziła, że Michał celowo ją lekceważył. On odpowiedział: «Mogłem wcześniej zapytać o twoje zdanie. Potrzebowałem chwili spokoju, ale nie umiałem tego jasno powiedzieć».",
            "Ta zmiana języka obniżyła napięcie. Michał okazał zrozumienie, a Lena postawiła granicę: chciała uczestniczyć w decyzjach, które dotyczą ich obojga. Jednocześnie wzięła odpowiedzialność za to, że wcześniej wypowiadała swoje przypuszczenia jak pewniki. Zamiast rozstrzygać, kto miał rację, próbowali zrozumieć, jakie potrzeby stały za ich reakcjami.",
            "Nie doszli do porozumienia w każdej sprawie, lecz odzyskali poczucie bezpieczeństwa. Ich rozmowa pokazała, że ostrożna modalność nie służy unikaniu odpowiedzialności. Pozwala oddzielić fakty od interpretacji, dokładniej nazwać motywy i dać drugiej osobie przestrzeń na własne wyjaśnienie.",
        ],
        "glossary": {
            "zapadła": ("zapaść", "была принята", "глагол"), "odczuwał": ("odczuwać", "чувствовал", "глагол"),
            "napięcie": ("napięcie", "напряжение", "существительное"), "odbierał": ("odbierać", "воспринимал", "глагол"),
            "zapowiedź": ("zapowiedź", "предвестие", "существительное"), "przypisywała": ("przypisywać", "приписывала", "глагол"),
            "obojętność": ("obojętność", "равнодушие", "существительное"), "wycofał": ("wycofać się", "отстранился", "глагол"),
            "unikał": ("unikać", "избегал", "глагол"), "konfrontacji": ("konfrontacja", "конфронтации", "существительное"),
            "obawiał": ("obawiać się", "опасался", "глагол"), "zauważyli": ("zauważyć", "заметили", "глагол"),
            "pominięta": ("pominąć", "обойдённая вниманием", "причастие"), "lekceważył": ("lekceważyć", "пренебрегал", "глагол"),
            "obniżyła": ("obniżyć", "снизила", "глагол"), "przypuszczenia": ("przypuszczenie", "предположения", "существительное"),
            "pewniki": ("pewnik", "неоспоримые факты", "существительное"), "rozstrzygać": ("rozstrzygać", "решать однозначно", "глагол"),
            "odzyskali": ("odzyskać", "вернули", "глагол"), "modalność": ("modalność", "модальность", "существительное"),
        },
        "check": (
            ("Dlaczego Lena miała żal?", ["Decyzje o wyjeździe zapadły bez niej", "Michał odwołał wyjazd", "Nie znała trasy powrotnej"], 0, "Она чувствовала себя исключённой из принятия решений."),
            ("Dlaczego Michał prawdopodobnie unikał konfrontacji?", ["Obawiał się impulsywnej reakcji", "Nie pamiętał wyjazdu", "Nie zależało mu na Lenie"], 0, "Текст предлагает осторожную гипотезу о его страхе эскалации."),
            ("Jaką zasadę przyjęli?", ["Najpierw obserwacja, potem emocje i potrzeby", "Najpierw oskarżenie, potem cisza", "Rozmowa tylko o faktach"], 0, "Их структура отделяет наблюдение от интерпретации."),
            ("Za co Michał wziął odpowiedzialność?", ["Nie zapytał wcześniej o zdanie Leny", "Sam wybrał cały wyjazd", "Przerwał rozmowę na zawsze"], 0, "Он признал, что мог раньше включить Лену в решение."),
            ("Jaką granicę postawiła Lena?", ["Chce uczestniczyć we wspólnych decyzjach", "Nie będzie więcej podróżować", "Nie chce słuchać wyjaśnień"], 0, "Граница касается совместных решений."),
            ("Po co używać ostrożnej modalności?", ["Aby oddzielić fakty od interpretacji", "Aby uniknąć odpowiedzialności", "Aby ukryć wszystkie emocje"], 0, "Финал текста прямо формулирует эту функцию."),
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
    ReadingText.objects.update_or_create(id=reading["id"], defaults={"topic": topic, "title": reading["title"], "description": reading["description"], "level": "B2", "minutes": reading["minutes"], "emoji": reading["emoji"], "position": 42, "paragraphs": reading["paragraphs"], "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": f"{p}-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0046_b2_law_civic_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
