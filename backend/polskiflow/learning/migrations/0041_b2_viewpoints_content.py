from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}


CARDS = (
    ("stanowisko", "позиция", "Autorka jasno przedstawia swoje stanowisko."),
    ("założenie", "предпосылка", "To założenie wymaga dodatkowego uzasadnienia."),
    ("uzasadnienie", "обоснование", "Dobre uzasadnienie opiera się na danych."),
    ("dowód", "доказательство", "Jeden przykład nie zawsze stanowi dowód."),
    ("wniosek", "вывод", "Wniosek wynika z przedstawionych argumentów."),
    ("zastrzeżenie", "оговорка", "Mam jedno zastrzeżenie do tej propozycji."),
    ("kontrargument", "контраргумент", "Rozmówca odpowiedział trafnym kontrargumentem."),
    ("przekonujący", "убедительный", "Jej wywód był logiczny i przekonujący."),
    ("z jednej strony", "с одной стороны", "Z jednej strony zmiana ułatwi pracę."),
    ("z drugiej strony", "с другой стороны", "Z drugiej strony zwiększy koszty."),
    ("wprawdzie", "правда, хотя", "Wprawdzie plan jest ambitny, ale wykonalny."),
    ("niemniej jednak", "тем не менее", "Brakuje czasu, niemniej jednak warto spróbować."),
    ("mimo że", "несмотря на то что", "Mimo że się różnimy, możemy współpracować."),
    ("odnieść się do", "ответить на; обратиться к", "Odniosę się do najważniejszego zarzutu."),
    ("podważyć", "поставить под сомнение", "Nowe dane mogą podważyć tę tezę."),
)

GRAMMAR = (
    ("___ rozwiązanie jest wygodne, ale nie uwzględnia potrzeb seniorów.", ["Wprawdzie", "Ponieważ", "Dlatego"], 0, "Wprawdzie zapowiada ustępstwo, po którym zwykle pojawia się ale lub jednak."),
    ("Projekt jest kosztowny. ___ może przynieść oszczędności w przyszłości.", ["Niemniej jednak", "W rezultacie że", "Z powodu"], 0, "Niemniej jednak wprowadza kontrast wobec wcześniejszego zastrzeżenia."),
    ("Mimo że badanie było niewielkie, jego wyniki ___ uwagę.", ["zasługują na", "podważają do", "odnoszą się"], 0, "Mimo że łączy fakt ograniczający z wnioskiem, który pozostaje aktualny."),
    ("Chciałbym odnieść się ___ argumentu dotyczącego kosztów.", ["do", "z", "nad"], 0, "Odnieść się do łączy się z dopełniaczem."),
    ("Составьте: С одной стороны предложение экономит время, с другой — ограничивает выбор.", ["Z jednej strony propozycja oszczędza czas, z drugiej strony ogranicza wybór.", "Wprawdzie propozycja czas, ponieważ wybór ograniczony.", "Z powodu jednej strony propozycję ogranicza wyborem."], 0, "Para z jednej strony… z drugiej strony równoważy dwa aspekty stanowiska."),
    ("Составьте: Хотя я понимаю это возражение, новые данные подтверждают наш вывод.", ["Mimo że rozumiem to zastrzeżenie, nowe dane potwierdzają nasz wniosek.", "Niemniej rozumiem do zastrzeżenia, dane wnioskiem.", "Ponieważ zastrzeżenie, ale dane podważyć wniosek."], 0, "Mimo że wprowadza ustępstwo, a zdanie główne zachowuje właściwy szyk."),
)

QUIZ = (
    ("Что означает stanowisko в дискуссии?", ["позиция по вопросу", "случайный пример", "название встречи"], 0, "Stanowisko — jasno określona opinia lub pozycja."),
    ("Który element pokazuje, dlaczego teza ma sens?", ["uzasadnienie", "zastrzeżenie", "powitanie"], 0, "Uzasadnienie łączy tezę z argumentami lub danymi."),
    ("Wprawdzie termin jest krótki, ___ zdążymy przygotować raport.", ["ale", "ponieważ", "z powodu"], 0, "Wprawdzie naturalnie łączy się z ale lub jednak."),
    ("Как вежливо ответить на возражение?", ["Rozumiem to zastrzeżenie, jednak…", "To absurd i koniec.", "Nie będę odpowiadać."], 0, "Pierwsza forma uznaje perspektywę rozmówcy i zapowiada odpowiedź."),
    ("Nowe wyniki mogą ___ wcześniejsze założenie.", ["podważyć", "odnieść", "przekonać do niego dowód"], 0, "Podważyć założenie — wykazać, że może być błędne."),
    ("Który marker wprowadza przeciwny aspekt?", ["z drugiej strony", "w związku z tym", "na przykład"], 0, "Z drugiej strony sygnalizuje kontrastującą perspektywę."),
    ("Mimo że nie mamy pełnych danych, ___.", ["możemy sformułować wstępny wniosek", "ponieważ pełne dane", "z powodu jednak"], 0, "Zdanie główne wyraża rezultat aktualny mimo ograniczenia."),
    ("Co robi kontrargument?", ["odpowiada na argument strony przeciwnej", "powtarza tezę bez podstaw", "zmienia temat"], 0, "Kontrargument odnosi się bezpośrednio do wcześniejszego argumentu."),
    ("Które zdanie zawiera ostrożne zastrzeżenie?", ["Rozwiązanie jest obiecujące, choć wymaga dalszych testów.", "Rozwiązanie jest zawsze idealne.", "Nie ma o czym rozmawiać."], 0, "Choć wskazuje ograniczenie bez odrzucania całej propozycji."),
    ("Jaki porządek buduje przekonujący wywód?", ["stanowisko — uzasadnienie — przykład — wniosek", "wniosek — zmiana tematu — slogan", "przykład bez tezy"], 0, "Taka kolejność pozwala odbiorcy śledzić tok rozumowania."),
)

CHECK = (
    ("Czego dotyczyła debata?", ["Ograniczenia ruchu samochodów w centrum", "Budowy lotniska", "Programu szkolnego"], 0, "Debata dotyczyła strefy z ograniczonym ruchem."),
    ("Jakie stanowisko zajęła Lena?", ["Poparła pilotaż z warunkami", "Odrzuciła każdą zmianę", "Nie zabrała głosu"], 0, "Lena poparła próbę, ale wskazała potrzebne zabezpieczenia."),
    ("Jakie zastrzeżenie zgłosił Marek?", ["Problemy osób dojeżdżających z przedmieść", "Brak miejsc w kinie", "Koszt podręczników"], 0, "Marek mówił o mieszkańcach bez dobrego transportu publicznego."),
    ("Na czym opierał się kontrargument Leny?", ["Na danych z pilotażu w innym mieście", "Na osobistej niechęci", "Na niepotwierdzonej plotce"], 0, "Przywołała porównywalny pilotaż i jego wyniki."),
    ("Co uczestnicy dodali do rekomendacji?", ["Wyjątki i ocenę skutków po pół roku", "Zakaz publikacji wyników", "Natychmiastową stałą zmianę bez testu"], 0, "Rekomendacja uwzględniła wyjątki oraz ewaluację."),
    ("Jaki jest główny wniosek tekstu?", ["Dobra debata może udoskonalić pierwotne stanowisko", "Ustępstwo oznacza porażkę", "Najlepiej ignorować kontrargumenty"], 0, "Rozmowa doprowadziła do bardziej precyzyjnej propozycji."),
)

PARAGRAPHS = [
    "Podczas debaty miejskiej omawiano ograniczenie ruchu samochodów w centrum. Lena poparła pomysł, ponieważ czystsze powietrze i bezpieczniejsze ulice uznała za przekonujące korzyści. Zastrzegła jednak, że sama deklaracja celu nie stanowi jeszcze dowodu skuteczności.",
    "Marek przedstawił kontrargument. Wprawdzie mieszkańcy centrum zyskaliby spokojniejszą przestrzeń, ale osoby dojeżdżające z przedmieść mogłyby mieć trudniejszy dostęp do usług. Jego zdaniem projekt opierał się na założeniu, że każdy ma dogodny transport publiczny.",
    "Lena odniosła się do tego zastrzeżenia, przywołując wyniki podobnego pilotażu. Z jednej strony dane potwierdzały spadek ruchu, z drugiej strony pokazywały większe obciążenie kilku linii autobusowych. Mimo że wyniki nie rozstrzygały wszystkiego, pozwalały podważyć twierdzenie, że zmiana zawsze utrudnia dojazd.",
    "Uczestnicy nie musieli wybierać między bezwarunkowym poparciem a całkowitym sprzeciwem. Dodali do rekomendacji częstsze kursy, wyjątki dla osób z niepełnosprawnościami oraz ocenę skutków po sześciu miesiącach. Niemniej jednak zachowali główny cel projektu.",
    "Końcowy wniosek był bardziej precyzyjny niż początkowe stanowiska. Debata pokazała, że ustępstwo nie osłabia argumentacji, jeśli pomaga dostrzec ograniczenia, odpowiedzieć na kontrargument i zaproponować rozwiązanie możliwe do sprawdzenia.",
]

GLOSSARY = {
    "omawiano": ("omawiać", "обсуждали", "глагол"), "ograniczenie": ("ograniczenie", "ограничение", "существительное"),
    "zastrzegła": ("zastrzec", "оговорила", "глагол"), "skuteczności": ("skuteczność", "эффективность", "существительное"),
    "dojeżdżające": ("dojeżdżać", "ездящие издалека", "причастие"), "przedmieść": ("przedmieście", "пригород", "существительное"),
    "dogodny": ("dogodny", "удобный", "прилагательное"), "przywołując": ("przywołać", "приводя", "деепричастие"),
    "pilotażu": ("pilotaż", "пилотный проект", "существительное"), "obciążenie": ("obciążenie", "нагрузка", "существительное"),
    "rozstrzygały": ("rozstrzygać", "решали однозначно", "глагол"), "podważyć": ("podważyć", "поставить под сомнение", "глагол"),
    "bezwarunkowym": ("bezwarunkowy", "безусловный", "прилагательное"), "sprzeciwem": ("sprzeciw", "возражение", "существительное"),
    "niepełnosprawnościami": ("niepełnosprawność", "инвалидность", "существительное"), "skutków": ("skutek", "последствие", "существительное"),
    "ustępstwo": ("ustępstwo", "уступка", "существительное"), "dostrzec": ("dostrzec", "заметить", "глагол"),
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    course, _ = Course.objects.update_or_create(id="b2-advanced", defaults={"title": "Уверенное общение", "description": "Аргументация и работа со сложными сообщениями уровня B2", "level": "B2", "position": 3, "is_active": True})
    topic, _ = Topic.objects.update_or_create(id="b2-viewpoints", defaults={"course": course, "title": "Точки зрения", "description": "Строим аргумент, учитываем ограничения и отвечаем на возражения", "emoji": "⚖️", "position": 0, "is_active": True})
    rows = (("b2view-words", "words", "Słowa w kontekście", "Новая лексика", "8 карточек · B2", "Лексика аргументации", 10, "⚖️"), ("b2view-grammar", "grammar", "Argument i ustępstwo", "Языковой фокус", "6 заданий · B2", "Маркеры аргументации и уступки", 13, "✏️"), ("b2view-review", "review", "Powtórka aktywna", "Активное повторение", "7 карточек · B2", "Закрепи лексику темы", 9, "🔄"), ("b2view-quiz", "quiz", "Quiz: Точки зрения", "Проверка темы", "10 вопросов · B2", "Проверь аргументацию и лексику", 10, "🎯"), ("b2view-reading-check", "quiz", "Czy rozumiesz tekst?", "Понимание текста", "6 вопросов · B2", "Проследи позиции и контраргументы", 8, "📖"))
    lessons = {}
    for position, row in enumerate(rows, 168):
        id_, kind, title, plan_title, subtitle, description, minutes, emoji = row
        lessons[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan_title, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = lessons["b2view-grammar"]
    grammar.theory_title = "Аргумент и уступка"
    grammar.theory_sections = [["Структура", "Обозначь stanowisko, добавь uzasadnienie и dowód, затем сформулируй wniosek."], ["Уступка", "Wprawdzie… ale, mimo że и niemniej jednak признают ограничение, не отменяя основную мысль."], ["Контраргумент", "Сначала точно назови zastrzeżenie, затем odnieś się do niego через данные или пример."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for offset, card_data in enumerate(CARDS):
        card, _ = Flashcard.objects.update_or_create(id=f"b2view-{offset + 1}", defaults={"polish": card_data[0], "translation": card_data[1], "example": card_data[2], "position": 542 + offset, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, selected in (("b2view-words", cards[:8]), ("b2view-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(selected):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("b2view-grammar", GRAMMAR), ("b2view-quiz", QUIZ), ("b2view-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, question in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=question[0], options=question[1], correct=question[2], explanation=question[3], position=position)
    glossary = {surface: {"lemma": entry[0], "translation": entry[1], "part_of_speech": entry[2]} for surface, entry in GLOSSARY.items()}
    ReadingText.objects.update_or_create(id="b2view-debata-o-spokojnym-centrum", defaults={"topic": topic, "title": "Debata o spokojnym centrum", "description": "Как оговорки и контраргументы улучшают городскую рекомендацию", "level": "B2", "minutes": 11, "emoji": "⚖️", "paragraphs": PARAGRAPHS, "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": "b2view-reading-check"}, "position": 36, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0040_complete_b1_curriculum")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
