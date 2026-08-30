from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}

CARDS = (
    ("doniesienie", "сообщение в СМИ", "Pierwsze doniesienia nie zawierały szczegółów."),
    ("relacja", "репортаж; изложение", "Relacja świadka różniła się od komunikatu."),
    ("nagłówek", "заголовок", "Nagłówek upraszczał treść raportu."),
    ("źródło", "источник", "Redakcja podała źródło danych."),
    ("potwierdzić", "подтвердить", "Rzecznik potwierdził termin otwarcia."),
    ("zaprzeczyć", "опровергнуть", "Ministerstwo zaprzeczyło tej informacji."),
    ("wynikać z", "следовать из", "Z raportu wynika, że emisje spadły."),
    ("rzekomy", "предполагаемый, мнимый", "Rzekomy dokument okazał się fałszywy."),
    ("według", "согласно", "Według ekspertki zmiana potrwa rok."),
    ("jak podaje", "как сообщает", "Jak podaje urząd, prace zakończą się jesienią."),
    ("miał", "якобы; как сообщается", "Pociąg miał odjechać z opóźnieniem."),
    ("podobno", "как говорят", "Podobno decyzja zapadnie jutro."),
    ("ocenić", "оценить", "Komentator ocenił plan jako ryzykowny."),
    ("bezstronny", "беспристрастный", "Bezstronny opis oddziela fakt od opinii."),
    ("sprostowanie", "опровержение, исправление", "Portal opublikował sprostowanie błędnej daty."),
)

GRAMMAR = (
    ("Rzeczniczka powiedziała, że remont ___ trzy miesiące.", ["potrwa", "potrwałby wczoraj", "trwać"], 0, "W mowie zależnej po że zachowujemy osobową formę zgodną z perspektywą czasową."),
    ("Według raportu liczba pasażerów ___.", ["wzrosła", "wzrosnąć", "wzrostem"], 0, "Według + dopełniacz wskazuje źródło, a zdanie przekazuje jego treść."),
    ("Nowa linia ___ zostać otwarta w listopadzie.", ["ma", "miała że", "podaje"], 0, "Ma + bezokolicznik może sygnalizować plan podany przez źródło, bez gwarancji autora."),
    ("Autor nazwał decyzję „przełomową”. To przede wszystkim ___.", ["ocena", "sprawdzalny fakt", "data"], 0, "Przymiotnik wartościujący wyraża ocenę, a nie sam fakt."),
    ("Составьте: По данным управления, мост будет открыт в понедельник.", ["Według urzędu most zostanie otwarty w poniedziałek.", "Urząd podobno most otworzyć poniedziałkiem.", "Jak urząd że most otwarto poniedziałek."], 0, "Według wymaga dopełniacza, a zostanie otwarty jest poprawną formą strony biernej."),
    ("Составьте: Свидетель сообщил, что поезд остановился перед станцией.", ["Świadek przekazał, że pociąg zatrzymał się przed stacją.", "Świadek przekazać pociąg zatrzymuje przed stacji.", "Według świadek że pociągiem zatrzymał."], 0, "Czasownik przekazał wprowadza mowę zależną przez że."),
)

QUIZ = (
    ("Что такое sprostowanie?", ["публичное исправление ошибки", "эмоциональный заголовок", "анонимный комментарий"], 0, "Sprostowanie koryguje wcześniej podaną nieprawdziwą informację."),
    ("Które zdanie wyraźnie wskazuje źródło?", ["Jak podaje urząd, tunel jest już otwarty.", "Wszyscy wiedzą, że tunel działa.", "To na pewno najlepszy tunel."], 0, "Jak podaje urząd przypisuje wiadomość konkretnemu źródłu."),
    ("Słowo „katastrofalny” w nagłówku jest zwykle ___.", ["oceną", "neutralną datą", "nazwą źródła"], 0, "To określenie wartościujące."),
    ("Z komunikatu ___, że lot został odwołany.", ["wynika", "zaprzecza do", "potwierdza się źródłem"], 0, "Wynikać z czego — z komunikatu wynika."),
    ("Jak przekazać niepotwierdzoną informację?", ["Podobno rozmowy zostaną wznowione.", "Rozmowy bez wątpienia wznowiono.", "Potwierdzono, choć nikt tego nie potwierdził."], 0, "Podobno sygnalizuje dystans i brak pełnego potwierdzenia."),
    ("Ministerstwo ___ doniesieniom o rezygnacji.", ["zaprzeczyło", "wyniknęło", "oceniło jako źródłu"], 0, "Zaprzeczyć czemu łączy się z celownikiem."),
    ("Która informacja jest faktem możliwym do sprawdzenia?", ["Głosowanie zakończyło się o 18.00.", "Debata była nudna.", "To skandaliczny wynik."], 0, "Godzinę można zweryfikować niezależnie od oceny."),
    ("Rzecznik powiedział: „Prace zakończą się jutro”. W mowie zależnej:", ["Rzecznik powiedział, że prace zakończą się następnego dnia.", "Rzecznik powiedział prace jutro kończyć.", "Według rzecznik prace zakończenie."], 0, "Że wprowadza treść, a następnego dnia dostosowuje określenie czasu."),
    ("Po co porównujemy kilka relacji?", ["Aby zauważyć różnice, braki i wspólne fakty", "Aby wybrać najgłośniejszy nagłówek", "Aby pominąć źródła"], 0, "Porównanie pomaga oddzielić potwierdzone elementy od interpretacji."),
    ("Który nagłówek jest najbardziej bezstronny?", ["Rada przyjęła budżet 12 głosami do 8", "Wspaniałe zwycięstwo rozsądku!", "Szokująca porażka przeciwników!"], 0, "Pierwszy podaje sprawdzalny wynik bez oceniających epitetów."),
)

CHECK = (
    ("Jakiego wydarzenia dotyczyły trzy publikacje?", ["Awarii systemu biletowego", "Otwarcia stadionu", "Prognozy pogody"], 0, "Wszystkie materiały dotyczyły awarii biletów."),
    ("Co potwierdził operator?", ["Awarię i brak opłat za przejazdy podczas problemu", "Atak hakerski", "Zwolnienie dyrektora"], 0, "Komunikat potwierdził dwa konkretne fakty."),
    ("Czego operator nie potwierdził?", ["Przyczyny awarii", "Godziny publikacji komunikatu", "Istnienia aplikacji"], 0, "Przyczyna miała być ustalona później."),
    ("Jak portal zmienił ton drugiej wersji?", ["Zastąpił oceniający nagłówek neutralnym", "Dodał więcej wykrzykników", "Usunął sprostowanie"], 0, "Redakcja złagodziła język po aktualizacji."),
    ("Co wynikało ze wspólnego porównania źródeł?", ["Fakty były węższe niż pierwsze sugestie", "Wszystkie pogłoski były prawdziwe", "Nie było żadnej awarii"], 0, "Potwierdzono awarię, ale nie sensacyjne przyczyny."),
    ("Jaką zasadę przyjęła grupa?", ["Osobno zapisywać fakt, źródło i ocenę", "Udostępniać pierwszy nagłówek", "Uznawać podobno za potwierdzenie"], 0, "Taki zapis pomaga kontrolować stopień pewności."),
)

PARAGRAPHS = [
    "W poniedziałek rano trzy portale opisały awarię miejskiego systemu biletowego. Pierwszy nagłówek głosił, że doszło do „paraliżu komunikacji”, drugi informował o czasowych trudnościach, a trzeci powoływał się na anonimowego pasażera, według którego problem miał trwać cały dzień.",
    "Komunikat operatora potwierdził awarię aplikacji i podał, że podczas przerwy kontrolerzy nie będą pobierać opłat. Nie wskazał jednak przyczyny. Rzeczniczka przekazała jedynie, że zespół techniczny analizuje dane, a dokładniejsze informacje zostaną opublikowane po zakończeniu prac.",
    "Jeden portal zasugerował rzekomy atak hakerski. Źródłem tej tezy był komentarz bez nazwiska, którego nie potwierdziła ani policja, ani operator. Kilka godzin później redakcja dodała sprostowanie: przyczyna pozostawała nieznana, a wcześniejszy nagłówek zmieniono na bardziej bezstronny.",
    "Na zajęciach grupa porównała relacje zdanie po zdaniu. Z jednej strony wszystkie źródła mówiły o niedziałającej aplikacji. Z drugiej strony tylko oficjalny komunikat precyzował zasady przejazdu, podczas gdy portale dodawały oceny takie jak „chaos” albo „poważny kryzys”.",
    "Z porównania wynikało, że zakres potwierdzonych faktów był znacznie węższy niż sugerowały pierwsze doniesienia. Uczestnicy postanowili odtąd zapisywać osobno: co się wydarzyło, kto to potwierdził oraz które słowa są interpretacją autora. Dzięki temu podobno nie zamienia się niepostrzeżenie w na pewno.",
]

GLOSSARY = {
    "awarię": ("awaria", "сбой", "существительное"), "głosił": ("głosić", "гласил", "глагол"),
    "paraliżu": ("paraliż", "паралич", "существительное"), "powoływał się": ("powoływać się", "ссылался", "глагол"),
    "pobierać": ("pobierać", "взимать", "глагол"), "wskazał": ("wskazać", "указал", "глагол"),
    "dokładniejsze": ("dokładny", "более подробные", "прилагательное"), "rzekomy": ("rzekomy", "предполагаемый", "прилагательное"),
    "tezy": ("teza", "тезис", "существительное"), "nazwiska": ("nazwisko", "фамилия", "существительное"),
    "pozostawała": ("pozostawać", "оставалась", "глагол"), "bezstronny": ("bezstronny", "беспристрастный", "прилагательное"),
    "precyzował": ("precyzować", "уточнял", "глагол"), "zakres": ("zakres", "объём", "существительное"),
    "doniesienia": ("doniesienie", "сообщения", "существительное"), "interpretacją": ("interpretacja", "интерпретация", "существительное"),
    "odtąd": ("odtąd", "отныне", "наречие"), "niepostrzeżenie": ("niepostrzeżenie", "незаметно", "наречие"),
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    course = Course.objects.get(id="b2-advanced")
    topic, _ = Topic.objects.update_or_create(id="b2-news", defaults={"course": course, "title": "Новости", "description": "Сопоставляем сообщения, отделяем факты от оценок и указываем степень уверенности", "emoji": "📰", "position": 1, "is_active": True})
    rows = (("b2news-words", "words", "Słowa w kontekście", "Новая лексика", "8 карточек · B2", "Лексика новостей и проверки источников", 10, "📰"), ("b2news-grammar", "grammar", "Kto to powiedział?", "Языковой фокус", "6 заданий · B2", "Косвенная речь и модальность источника", 13, "✏️"), ("b2news-review", "review", "Powtórka aktywna", "Активное повторение", "7 карточек · B2", "Закрепи лексику темы", 9, "🔄"), ("b2news-quiz", "quiz", "Quiz: Новости", "Проверка темы", "10 вопросов · B2", "Проверь работу с фактами и источниками", 10, "🎯"), ("b2news-reading-check", "quiz", "Czy rozumiesz tekst?", "Понимание текста", "6 вопросов · B2", "Сопоставь сообщения и степень уверенности", 8, "📖"))
    lessons = {}
    for position, row in enumerate(rows, 173):
        id_, kind, title, plan_title, subtitle, description, minutes, emoji = row
        lessons[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan_title, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = lessons["b2news-grammar"]
    grammar.theory_title = "Источник, факт и оценка"
    grammar.theory_sections = [["Косвенная речь", "Powiedział, że… и przekazała, że… передают содержание без дословной цитаты."], ["Степень уверенности", "Według, jak podaje, ma/miał и podobno показывают, кому принадлежит сообщение и насколько оно подтверждено."], ["Факт или оценка", "Факт можно проверить; слова przełomowy, skandaliczny или katastrofalny требуют пометки как оценка автора."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for offset, card_data in enumerate(CARDS):
        card, _ = Flashcard.objects.update_or_create(id=f"b2news-{offset + 1}", defaults={"polish": card_data[0], "translation": card_data[1], "example": card_data[2], "position": 557 + offset, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, selected in (("b2news-words", cards[:8]), ("b2news-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(selected):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("b2news-grammar", GRAMMAR), ("b2news-quiz", QUIZ), ("b2news-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, question in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=question[0], options=question[1], correct=question[2], explanation=question[3], position=position)
    glossary = {surface: {"lemma": entry[0], "translation": entry[1], "part_of_speech": entry[2]} for surface, entry in GLOSSARY.items()}
    ReadingText.objects.update_or_create(id="b2news-trzy-relacje-o-jednej-awarii", defaults={"topic": topic, "title": "Trzy relacje o jednej awarii", "description": "Как сравнение сообщений отделяет подтверждённые факты от предположений", "level": "B2", "minutes": 11, "emoji": "📰", "paragraphs": PARAGRAPHS, "glossary": glossary, "source_metadata": {**SOURCE, "comprehension_lesson_id": "b2news-reading-check"}, "position": 37, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0041_b2_viewpoints_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
