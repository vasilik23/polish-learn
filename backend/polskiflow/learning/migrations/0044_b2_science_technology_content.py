from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}

SPEC = {
    "id": "b2-science-technology", "title": "Наука и технологии",
    "description": "Доступно объясняем процесс, идею и границы технологического решения", "emoji": "🔬", "position": 3,
    "prefix": "b2tech", "lesson_start": 183, "card_start": 587,
    "theory": ("Определения и безличное описание процесса", [
        ["Определение", "X to urządzenie/proces, który… сначала называет класс, затем отличительный признак."],
        ["Пассив", "Формы jest wykorzystywany / został opracowany выдвигают объект и результат на первый план."],
        ["Безличность", "Конструкции bada się, można zmierzyć и zaobserwowano описывают общий метод без ненужного исполнителя."],
    ]),
    "cards": (
        ("zjawisko", "явление", "Badacze obserwują niezwykłe zjawisko."),
        ("założenie", "предположение, исходная посылка", "Model opiera się na prostym założeniu."),
        ("hipoteza", "гипотеза", "Eksperyment potwierdził hipotezę."),
        ("przeprowadzić badanie", "провести исследование", "Zespół przeprowadził badanie w dwóch szkołach."),
        ("próbka", "образец, выборка", "Próbka była zbyt mała na pewny wniosek."),
        ("wynik", "результат", "Wynik trzeba powtórnie sprawdzić."),
        ("wiarygodny", "достоверный", "Potrzebujemy wiarygodnych danych."),
        ("ograniczenie", "ограничение", "Autorzy opisali ograniczenia metody."),
        ("przetwarzać dane", "обрабатывать данные", "Program przetwarza dane z czujników."),
        ("algorytm", "алгоритм", "Algorytm rozpoznaje powtarzalne wzorce."),
        ("czujnik", "датчик", "Czujnik mierzy temperaturę co minutę."),
        ("zastosowanie", "применение", "Technologia ma zastosowanie w medycynie."),
        ("opracować", "разработать", "Inżynierowie opracowali nową metodę."),
        ("wykrywać", "обнаруживать", "System pomaga wykrywać awarie."),
        ("na podstawie", "на основании", "Decyzję podjęto na podstawie danych."),
    ),
    "grammar": (
        ("Czujnik to urządzenie, ___ mierzy zmiany temperatury.", ["które", "który", "którego"], 0, "Urządzenie — средний род, поэтому które."),
        ("Dane są ___ przez algorytm co kilka sekund.", ["przetwarzane", "przetwarzać", "przetworzyły"], 0, "Пассив: są + причастие, согласованное с dane во множественном числе."),
        ("W laboratorium ___ wpływ światła na rośliny.", ["bada się", "badają siebie", "jest badać"], 0, "Bada się — безличная возвратная конструкция для общего процесса."),
        ("Podczas testu ___ niewielką różnicę między grupami.", ["zaobserwowano", "obserwując się", "został obserwować"], 0, "Форма на -no сообщает наблюдение без указания исследователя."),
        ("Составьте: Алгоритм — это набор правил, который используется для обработки данных.", ["Algorytm to zbiór reguł, który jest wykorzystywany do przetwarzania danych.", "Algorytm jest reguły, które wykorzystuje przetwarzać dane.", "Zbiór algorytmem został danych przetwarzać."], 0, "Определение строится через to, а пассив jest wykorzystywany согласуется с zbiór."),
        ("Составьте: На основании результатов было разработано новое решение.", ["Na podstawie wyników opracowano nowe rozwiązanie.", "Podstawą wyniki opracował się nowe rozwiązaniem.", "Wyniki zostały opracować rozwiązanie."], 0, "Na podstawie требует родительного, opracowano — безличная форма."),
    ),
    "quiz": (
        ("Что означает próbka в исследовании?", ["образец или группа для анализа", "готовый вывод", "название прибора"], 0, "Próbka — часть материала или наблюдений."),
        ("Hipotezę należy ___.", ["sprawdzić", "założyć wynik", "ukryć ograniczenie"], 0, "Гипотеза требует проверки данными."),
        ("Które zdanie zawiera definicję?", ["Czujnik to urządzenie, które rejestruje zmiany.", "Czujnik leży tutaj.", "Lubię czujniki."], 0, "Указан класс и отличительная функция."),
        ("Dane zostały ___ przez niezależny zespół.", ["zweryfikowane", "weryfikować", "weryfikując"], 0, "Пассив требует причастия zweryfikowane."),
        ("Co zwiększa wiarygodność wyniku?", ["powtórzenie badania na większej próbce", "pominięcie danych", "brak opisu metody"], 0, "Повторяемость и выборка укрепляют вывод."),
        ("W tym laboratorium ___ nowe materiały.", ["testuje się", "testuje siebie", "jest testować"], 0, "Безличное się описывает регулярный процесс."),
        ("Algorytm ___ wzorce w danych.", ["wykrywa", "próbkuje się do", "wiarygodni"], 0, "Wykrywać wzorce — естественное сочетание."),
        ("Dlaczego podaje się ograniczenia badania?", ["Чтобы показать границы вывода", "Чтобы скрыть метод", "Чтобы заменить результаты"], 0, "Ограничения помогают правильно интерпретировать данные."),
        ("Na podstawie ___ sformułowano wniosek.", ["wyników", "wyniki", "wynikami"], 0, "Na podstawie требует родительного падежа."),
        ("Która forma skupia uwagę na rezultacie?", ["Rozwiązanie zostało opracowane w maju.", "Inżynierowie lubią maj.", "My coś robimy."], 0, "Пассив выдвигает решение и факт разработки."),
    ),
    "reading": {
        "id": "b2tech-czujniki-ktore-oszczedzaja-wode", "title": "Czujniki, które pomagają oszczędzać wodę",
        "description": "Как объяснить принцип системы и не скрыть ограничения исследования", "emoji": "🔬", "minutes": 11,
        "paragraphs": [
            "Grupa studentów opracowała system, który pomaga ograniczyć zużycie wody w miejskich ogrodach. Jego podstawowym elementem jest czujnik, czyli urządzenie mierzące wilgotność gleby. Dane są przesyłane do programu, gdzie co kilka minut przetwarza je algorytm.",
            "Algorytm to zbiór reguł, na podstawie których podejmowana jest decyzja o podlewaniu. Jeżeli gleba pozostaje wilgotna, zawór nie zostaje otwarty. Gdy czujnik wykrywa dłuższy niedobór wody, system uruchamia podlewanie tylko w wybranej części ogrodu. Dzięki temu nie działa według stałego harmonogramu, lecz reaguje na rzeczywiste warunki.",
            "Przed wdrożeniem przeprowadzono badanie w sześciu ogrodach. Zużycie wody porównywano przez dwa miesiące, a wynik wskazywał na średnią oszczędność wynoszącą osiemnaście procent. Podobne zjawisko zaobserwowano w większości lokalizacji, dlatego wstępna hipoteza została uznana za wiarygodną.",
            "Autorzy podkreślili jednak ograniczenia. Próbka była niewielka, a badanie prowadzono tylko latem. Nie wiadomo więc, czy taki sam wynik uzyska się przy innej glebie albo częstszych opadach. Zanim rozwiązanie znajdzie szersze zastosowanie, należy powtórzyć pomiary w różnych warunkach.",
            "Projekt pokazuje, że technologię można wyjaśnić bez nadmiaru terminów: najpierw definiuje się elementy, potem opisuje proces, wyniki i granice wniosku. Tak przedstawiona informacja pozwala odbiorcy zrozumieć zarówno korzyści, jak i niepewność związaną z nową metodą.",
        ],
        "glossary": {
            "opracowała": ("opracować", "разработала", "глагол"), "zużycie": ("zużycie", "потребление", "существительное"),
            "wilgotność": ("wilgotność", "влажность", "существительное"), "gleby": ("gleba", "почва", "существительное"),
            "przesyłane": ("przesyłać", "передаваемые", "причастие"), "podejmowana": ("podejmować", "принимаемая", "причастие"),
            "podlewaniu": ("podlewanie", "полив", "существительное"), "zawór": ("zawór", "клапан", "существительное"),
            "niedobór": ("niedobór", "недостаток", "существительное"), "uruchamia": ("uruchamiać", "запускает", "глагол"),
            "rzeczywiste": ("rzeczywisty", "фактические", "прилагательное"), "wdrożeniem": ("wdrożenie", "внедрение", "существительное"),
            "oszczędność": ("oszczędność", "экономия", "существительное"), "wstępna": ("wstępny", "предварительная", "прилагательное"),
            "ograniczenia": ("ograniczenie", "ограничения", "существительное"), "opadach": ("opad", "осадки", "существительное"),
            "pomiary": ("pomiar", "измерения", "существительное"), "niepewność": ("niepewność", "неопределённость", "существительное"),
        },
        "check": (
            ("Co mierzy czujnik?", ["Wilgotność gleby", "Liczbę gości", "Cenę wody"], 0, "Датчик измеряет влажность почвы."),
            ("Kiedy system uruchamia podlewanie?", ["Po wykryciu dłuższego niedoboru wody", "Zawsze o tej samej godzinie", "Gdy gleba jest mokra"], 0, "Решение зависит от фактических условий."),
            ("Gdzie przeprowadzono badanie?", ["W sześciu ogrodach", "W jednej fabryce", "W stu mieszkaniach"], 0, "В тексте указаны шесть садов."),
            ("Jaki był średni wynik?", ["Osiemnaście procent oszczędności", "Osiemdziesiąt procent", "Brak zmiany"], 0, "Средняя экономия составила 18%."),
            ("Jakie ograniczenie wskazali autorzy?", ["Małą próbkę i badanie tylko latem", "Brak czujników", "Zbyt wiele zimowych danych"], 0, "Оба ограничения названы прямо."),
            ("Jak należy jasno wyjaśniać technologię?", ["Definicja, proces, wyniki i granice wniosku", "Tylko lista terminów", "Wyłącznie obietnice korzyści"], 0, "Финал текста предлагает эту структуру."),
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
    rows = ((f"{p}-words", "words", "Słowa w kontekście", "Новая лексика", "8 карточек · B2", s["description"], 10, s["emoji"]), (f"{p}-grammar", "grammar", "Jak to wyrazić?", "Языковой фокус", "6 заданий · B2", s["theory"][0], 13, "✏️"), (f"{p}-review", "review", "Powtórka aktywna", "Активное повторение", "7 карточек · B2", "Закрепи лексику темы", 9, "🔄"), (f"{p}-quiz", "quiz", f"Quiz: {s['title']}", "Проверка темы", "10 вопросов · B2", "Проверь лексику и научное объяснение", 10, "🎯"), (f"{p}-reading-check", "quiz", "Czy rozumiesz tekst?", "Понимание текста", "6 вопросов · B2", "Найди метод, результат и ограничения", 8, "📖"))
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
    ReadingText.objects.update_or_create(id=reading["id"], defaults={"topic": topic, "title": reading["title"], "description": reading["description"], "level": "B2", "minutes": reading["minutes"], "emoji": reading["emoji"], "position": 39, "paragraphs": reading["paragraphs"], "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": f"{p}-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0043_b2_professional_communication_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
