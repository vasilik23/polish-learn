from django.db import migrations

SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}
CARDS = (
    ("b1culture-powiesc", "powieść", "роман", "Ta powieść opowiada o przyjaźni w trudnych czasach."),
    ("b1culture-ekranizacja", "ekranizacja", "экранизация", "Ekranizacja różni się od książkowego oryginału."),
    ("b1culture-fabula", "fabuła", "сюжет", "Fabuła rozwija się powoli, ale logicznie."),
    ("b1culture-bohater", "bohater", "герой; персонаж", "Główny bohater podejmuje trudną decyzję."),
    ("b1culture-przedstawienie", "przedstawienie", "спектакль", "Przedstawienie trwało prawie dwie godziny."),
    ("b1culture-wystawa", "wystawa", "выставка", "Wystawa pokazuje fotografie współczesnego miasta."),
    ("b1culture-recenzja", "recenzja", "рецензия", "Po seansie przeczytałam krótką recenzję."),
    ("b1culture-tworca", "twórca", "создатель; автор", "Twórca filmu rozmawiał z publicznością."),
    ("b1culture-poruszajacy", "poruszający", "трогательный", "Najbardziej poruszająca była ostatnia scena."),
    ("b1culture-przekonujacy", "przekonujący", "убедительный", "Aktor stworzył przekonującą postać."),
    ("b1culture-wielowatkowy", "wielowątkowy", "многосюжетный", "Wielowątkowa opowieść wymaga uwagi."),
    ("b1culture-scenografia", "scenografia", "сценография", "Prosta scenografia dobrze budowała nastrój."),
    ("b1culture-publicznosc", "publiczność", "публика", "Publiczność długo rozmawiała po spotkaniu."),
    ("b1culture-wywierac-wrazenie", "wywierać wrażenie", "производить впечатление", "Muzyka wywiera mocne wrażenie."),
    ("b1culture-skłaniac", "skłaniać do refleksji", "побуждать к размышлению", "Zakończenie skłania do refleksji nad odpowiedzialnością."),
)
GRAMMAR = (
    ("To film, ___ bohater wraca po latach do rodzinnego miasta.", ["w którym", "którego", "któremu"], 0, "После w filmie относительное местоимение принимает форму w którym."),
    ("Poznałam reżyserkę, ___ film zdobył nagrodę.", ["której", "którą", "któremu"], 0, "Форма której выражает принадлежность: фильм этой режиссёрки."),
    ("Aktor, ___ publiczność nagrodziła brawami, zagrał bardzo naturalnie.", ["którego", "który", "któremu"], 0, "Глагол nagrodzić требует винительного падежа; для лица мужского рода — którego."),
    ("Książka była ___: długo myślałem o decyzji bohatera.", ["poruszająca", "poruszona", "poruszająco"], 0, "Poruszająca согласуется с существительным książka и оценивает произведение."),
    ("Составьте: Это выставка, которая побуждает публику к размышлению.", ["To wystawa, która skłania publiczność do refleksji.", "To wystawa, której skłania publicznością refleksję.", "To wystawa, który publiczność skłania do refleksją."], 0, "Która согласуется с wystawa; skłaniać kogoś do czegoś требует винительного и родительного падежей."),
    ("Составьте: Мне понравился фильм, в котором музыка создавала тревожное настроение.", ["Spodobał mi się film, w którym muzyka budowała niepokojący nastrój.", "Podobałem film, którego muzyka budowała niepokojącego nastrój.", "Spodobał mnie się film, który muzyką budował nastrój."], 0, "Безличное spodobał mi się требует дательного; место действия выражено w którym."),
)
QUIZ = (
    ("Что означает ekranizacja?", ["фильм по мотивам литературного произведения", "театральная декорация", "критическая статья"], 0, "Ekranizacja переносит литературное произведение на экран."),
    ("Które słowo opisuje wydarzenia utworu?", ["fabuła", "publiczność", "scenografia"], 0, "Fabuła — последовательность событий произведения."),
    ("To autorka, ___ powieść właśnie przeczytałem.", ["której", "którą", "która"], 0, "Której выражает принадлежность: роман этой авторки."),
    ("Spektakl, ___ widzieliśmy wczoraj, był bardzo poruszający.", ["który", "którego", "któremu"], 0, "Неодушевлённое существительное мужского рода в винительном имеет форму który."),
    ("Jak pozytywnie ocenić grę aktora?", ["Stworzył przekonującą i naturalną postać.", "Fabuła siedziała na widowni.", "Recenzja zagrała bohatera."], 0, "Первый вариант естественно оценивает актёрскую работу."),
    ("Prosta ___ pomogła zbudować nastrój przedstawienia.", ["scenografia", "publiczność", "powieść"], 0, "Scenografia — визуальное оформление сцены."),
    ("Выберите естественное сочетание.", ["skłaniać do refleksji", "wywierać publicznością", "oglądać wrażeniem"], 0, "Skłaniać do refleksji — побуждать к размышлению."),
    ("Film był wielowątkowy, czyli ___.", ["rozwijał kilka powiązanych historii", "trwał tylko minutę", "nie miał bohaterów"], 0, "Wielowątkowy значит состоящий из нескольких сюжетных линий."),
    ("Muzeum, ___ odbywa się wystawa, mieści się w centrum.", ["w którym", "którego", "któremu"], 0, "Место выражается конструкцией w którym."),
    ("Która opinia jest uzasadniona?", ["Film wywarł na mnie wrażenie, ponieważ obraz i muzyka tworzyły spójną całość.", "Film był dobry, bo tak.", "Każda ekranizacja jest lepsza od książki."], 0, "Первый вариант содержит конкретную оценку и её обоснование."),
)
CHECK = (
    ("Dlaczego Ola wybrała się na wydarzenie?", ["Chciała porównać książkę z ekranizacją", "Musiała napisać szkolny egzamin", "Szukała nowego mieszkania"], 0, "Она прочитала роман и хотела увидеть его экранизацию."),
    ("Co pokazano przed filmem?", ["Wystawę szkiców i zdjęć ze scenografii", "Koncert muzyki ludowej", "Kurs fotografii"], 0, "Перед сеансом можно было увидеть материалы о создании сценографии."),
    ("Co Ola oceniła pozytywnie?", ["Przekonującą grę głównej aktorki", "Brak związku z książką", "Puste spotkanie bez twórców"], 0, "Ей особенно понравилась убедительная игра актрисы."),
    ("Czym film różnił się od powieści?", ["Łączył kilka postaci i skracał wątki", "Dodawał wszystkie szczegóły książki", "Nie miał muzyki ani obrazu"], 0, "Экранизация объединила персонажей и сократила некоторые линии."),
    ("Co wydarzyło się po seansie?", ["Publiczność rozmawiała z reżyserką", "Kino zostało natychmiast zamknięte", "Ola oddała książkę autorowi"], 0, "После фильма состоялась встреча с режиссёркой."),
    ("Jaki wniosek wyciągnęła Ola?", ["Książka i film mogą inaczej opowiadać tę samą historię", "Ekranizacja zawsze powinna kopiować każde zdanie", "Recenzje są ważniejsze niż własna opinia"], 0, "Главный вывод касается разных средств литературы и кино."),
)
READING = {"id": "b1culture-wieczor-z-ksiazka-i-filmem", "title": "Wieczór z książką i filmem", "description": "Как сравнить роман, экранизацию и культурное событие", "level": "B1", "minutes": 9, "emoji": "🎭", "position": 31, "paragraphs": [
    "Ola niedawno przeczytała powieść o rodzeństwie, które po latach wraca do rodzinnego domu. Kiedy lokalne kino zapowiedziało pokaz ekranizacji i spotkanie z reżyserką, od razu kupiła bilet. Chciała sprawdzić, czy film zachował spokojny nastrój i wielowątkową fabułę książki.",
    "Przed seansem publiczność mogła obejrzeć małą wystawę szkiców kostiumów oraz zdjęć miejsc, w których powstawał film. Olę zainteresowała zwłaszcza prosta scenografia domu. Dzięki światłu i starym przedmiotom wywierała mocne wrażenie, chociaż nie kopiowała dokładnie opisów z powieści.",
    "Film skracał niektóre wątki i łączył kilka drugoplanowych postaci. Mimo to główna aktorka, której grę Ola uznała za przekonującą, dobrze pokazała zmianę bohaterki. Szczególnie poruszająca była scena bez dialogu, w której muzyka i obraz zastąpiły długi książkowy opis.",
    "Po seansie reżyserka odpowiadała na pytania publiczności. Wyjaśniła, że ekranizacja nie musi powtarzać każdego zdania, lecz powinna zachować najważniejszy konflikt i emocje. Spotkanie skłoniło Olę do refleksji: książka i film opowiadają tę samą historię innymi środkami, dlatego warto oceniać każde dzieło osobno.",
], "glossary": {
    "rodzeństwie": {"lemma": "rodzeństwo", "translation": "братья и сёстры", "part_of_speech": "существительное"}, "zapowiedziało": {"lemma": "zapowiedzieć", "translation": "объявить", "part_of_speech": "глагол"}, "zachował": {"lemma": "zachować", "translation": "сохранить", "part_of_speech": "глагол"}, "seansem": {"lemma": "seans", "translation": "сеанс", "part_of_speech": "существительное"}, "szkiców": {"lemma": "szkic", "translation": "эскиз", "part_of_speech": "существительное"}, "kostiumów": {"lemma": "kostium", "translation": "костюм", "part_of_speech": "существительное"}, "powstawał": {"lemma": "powstawać", "translation": "создаваться", "part_of_speech": "глагол"}, "zwłaszcza": {"lemma": "zwłaszcza", "translation": "особенно", "part_of_speech": "наречие"}, "wywierała": {"lemma": "wywierać", "translation": "производить", "part_of_speech": "глагол"}, "drugoplanowych": {"lemma": "drugoplanowy", "translation": "второстепенный", "part_of_speech": "прилагательное"}, "uznała": {"lemma": "uznać", "translation": "счесть", "part_of_speech": "глагол"}, "zastąpiły": {"lemma": "zastąpić", "translation": "заменить", "part_of_speech": "глагол"}, "powtarzać": {"lemma": "powtarzać", "translation": "повторять", "part_of_speech": "глагол"}, "konflikt": {"lemma": "konflikt", "translation": "конфликт", "part_of_speech": "существительное"}, "środkami": {"lemma": "środek", "translation": "средство", "part_of_speech": "существительное"}, "dzieło": {"lemma": "dzieło", "translation": "произведение", "part_of_speech": "существительное"},
}}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(id="b1-culture", defaults={"course": Course.objects.get(id="b1-independent"), "title": "Культура", "description": "Рассказываем о книге, фильме и событии и обосновываем оценку", "emoji": "🎭", "position": 7, "is_active": True})
    rows = (("b1culture-words", "words", "Książka, film i scena", "Произведение и событие", "8 карточек · B1", "Назови элементы книги, фильма и культурного события", 9, "🎭"), ("b1culture-grammar", "grammar", "Dzieło, które porusza", "Оценка и описание", "6 заданий · B1", "Соединяй оценочную лексику с относительными местоимениями", 12, "✏️"), ("b1culture-review", "review", "Moja opinia", "Аргументированная оценка", "7 карточек · B1", "Опиши впечатление и объясни свою оценку", 8, "🔄"), ("b1culture-quiz", "quiz", "Quiz: kultura", "Проверка темы", "10 вопросов · B1", "Проверь лексику и формы относительных местоимений", 9, "🎯"), ("b1culture-reading-check", "quiz", "Książka czy ekranizacja?", "Понимание текста", "6 вопросов · B1", "Сравни произведения и найди вывод героини", 7, "📖"))
    made = {}
    for position, row in enumerate(rows, 143):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["b1culture-grammar"]
    grammar.theory_title = "Оценочная лексика и относительные местоимения"
    grammar.theory_sections = [["Оценка", "Poruszający, przekonujący и wielowątkowy называют конкретное качество; оценку лучше подкреплять примером."], ["Który", "Местоимение который согласуется с существительным в роде и числе, но падеж зависит от его роли в придаточном."], ["Формы", "Który/która — подлежащее, którego/której — принадлежность или дополнение, w którym/w której — место."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 467):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("b1culture-words", cards[:8]), ("b1culture-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("b1culture-grammar", GRAMMAR), ("b1culture-quiz", QUIZ), ("b1culture-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, question in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=question[0], options=question[1], correct=question[2], explanation=question[3], position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "b1culture-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0038_b1_media_internet_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
