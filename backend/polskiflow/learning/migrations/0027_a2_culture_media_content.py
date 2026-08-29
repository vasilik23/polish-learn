from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-29"}
CARDS = (
    ("culture-film", "film", "фильм", "Wczoraj obejrzeliśmy ciekawy film."),
    ("culture-serial", "serial", "сериал", "Ten serial ma sześć odcinków."),
    ("culture-powiesc", "powieść", "роман", "Czytam powieść o życiu w Krakowie."),
    ("culture-wystawa", "wystawa", "выставка", "Nowa wystawa opowiada o historii miasta."),
    ("culture-spektakl", "spektakl", "спектакль", "Spektakl trwał prawie dwie godziny."),
    ("culture-rezyser", "reżyser", "режиссёр", "Reżyser spotkał się z publicznością."),
    ("culture-aktor", "aktor", "актёр", "Główny aktor zagrał bardzo naturalnie."),
    ("culture-fabula", "fabuła", "сюжет", "Fabuła była prosta, ale poruszająca."),
    ("culture-bohater", "bohater", "герой произведения", "Bohater wraca do rodzinnego miasta."),
    ("culture-recenzja", "recenzja", "рецензия", "Przeczytałam krótką recenzję filmu."),
    ("culture-odcinek", "odcinek", "серия", "Najnowszy odcinek pojawi się w piątek."),
    ("culture-polecac", "polecać", "рекомендовать", "Polecam ten film całej rodzinie."),
    ("culture-oceniac", "oceniać", "оценивать", "Trudno oceniać książkę po jednym rozdziale."),
    ("culture-wzruszajacy", "wzruszający", "трогательный", "Finał był naprawdę wzruszający."),
    ("culture-nudny", "nudny", "скучный", "Początek był trochę nudny, lecz później akcja przyspieszyła."),
)
GRAMMAR = (
    ("Obejrzałem ten film. Obejrzałem ___ wczoraj.", ["go", "jej", "ich"], 0, "Мужской неодушевлённый объект film заменяется местоимением go."),
    ("Znam tę aktorkę. Widziałem ___ w teatrze.", ["ją", "go", "im"], 0, "Женский объект tę aktorkę заменяется винительным ją."),
    ("Czytasz te recenzje? Czytasz ___ regularnie?", ["je", "go", "nią"], 0, "Во множественном числе неодушевлённые объекты заменяет je."),
    ("Составьте: Я рекомендую его, потому что сюжет интересный.", ["Polecam go, bo fabuła jest ciekawa.", "Polecam jej, że fabuła ciekawy.", "Go polecać dlatego fabuła jest."], 0, "Go относится к фильму, а bo вводит причину рекомендации."),
    ("Anna przeczytała powieść i potem ___ oceniła.", ["ją", "go", "ich"], 0, "Powieść — женский род, поэтому в винительном падеже используется ją."),
)
QUIZ = (
    ("Что означает fabuła?", ["сюжет", "режиссёр", "выставка"], 0, "Fabuła — последовательность событий произведения."),
    ("Ten serial jest świetny. Oglądam ___ co tydzień.", ["go", "ją", "je"], 0, "Serial — мужской род: oglądam go."),
    ("Как сказать «Я рекомендую эту книгу»?", ["Polecam tę książkę.", "Oceniam tego książka.", "Polecam ją książkę jej."], 0, "Polecać + винительный: polecam tę książkę."),
    ("Widzieliśmy aktorów i później spotkaliśmy ___.", ["ich", "je", "go"], 0, "Лично-мужская группа aktorów заменяется местоимением ich."),
    ("Что можно назвать wzruszający?", ["трогательный финал", "цена билета", "время начала"], 0, "Wzruszający описывает сильную эмоциональную реакцию на произведение."),
    ("Film był trochę nudny, ___ zakończenie mi się podobało.", ["ale", "że", "dlatego że"], 0, "Ale противопоставляет две оценки фильма."),
    ("Przeczytałam recenzję. Autor dobrze ___ napisał.", ["ją", "go", "ich"], 0, "Recenzja — женский род, поэтому: napisał ją."),
    ("Кто отвечает за постановку фильма?", ["reżyser", "bohater", "publiczność"], 0, "Reżyser руководит созданием фильма."),
)
CHECK = (
    ("Na jakie wydarzenie poszli Lena i Paweł?", ["Na festiwal krótkich filmów", "Na wystawę fotografii", "Na koncert rockowy"], 0, "Они выбрали фестиваль короткометражных фильмов."),
    ("Który film najbardziej spodobał się Lenie?", ["Historia o starszej sąsiadce", "Komedia o pracy", "Film sportowy"], 0, "Лену тронула история пожилой соседки."),
    ("Dlaczego Paweł inaczej ocenił pierwszy film?", ["Tempo było dla niego zbyt wolne", "Nie rozumiał języka", "Nie widział zakończenia"], 0, "Павлу показался слишком медленным темп."),
    ("Co zrobili po pokazie?", ["Porozmawiali z reżyserką", "Kupili książkę", "Wrócili bez rozmowy"], 0, "После показа они задали режиссёру вопросы."),
    ("Co Lena opublikowała następnego dnia?", ["Krótką recenzję", "Cały film", "Wywiad z aktorem"], 0, "На следующий день Лена опубликовала короткую рецензию."),
)
READING = {
    "id": "wieczor-krotkich-filmow",
    "title": "Wieczór krótkich filmów",
    "description": "Фестиваль, разные мнения и короткая рецензия",
    "level": "A2",
    "minutes": 6,
    "emoji": "🎬",
    "position": 19,
    "paragraphs": [
        "W sobotę Lena i Paweł poszli na festiwal krótkich filmów. W programie były trzy historie młodych polskich reżyserów. Pierwszy film opowiadał o starszej sąsiadce, która codziennie pomagała mieszkańcom swojego domu. Lena uznała go za prosty, ale bardzo wzruszający.",
        "Paweł też docenił główną bohaterkę, jednak tempo filmu było dla niego zbyt wolne. Bardziej spodobała mu się lekka komedia o pierwszym dniu w nowej pracy. Oboje zgodzili się, że aktorzy zagrali naturalnie, a dialogi brzmiały wiarygodnie.",
        "Po pokazie widzowie spotkali się z reżyserką pierwszego filmu. Lena zapytała ją o pomysł na fabułę, a Paweł powiedział, dlaczego inaczej ocenił zakończenie. Następnego dnia Lena opublikowała krótką recenzję. Poleciła w niej cały festiwal, bo różne filmy zachęciły ich do ciekawej rozmowy.",
    ],
    "glossary": {
        "reżyserów": {"lemma": "reżyser", "translation": "режиссёр", "part_of_speech": "существительное"},
        "sąsiadce": {"lemma": "sąsiadka", "translation": "соседка", "part_of_speech": "существительное"},
        "uznała": {"lemma": "uznać", "translation": "счесть", "part_of_speech": "глагол"},
        "wzruszający": {"lemma": "wzruszający", "translation": "трогательный", "part_of_speech": "прилагательное"},
        "docenił": {"lemma": "docenić", "translation": "оценить по достоинству", "part_of_speech": "глагол"},
        "wiarygodnie": {"lemma": "wiarygodnie", "translation": "правдоподобно", "part_of_speech": "наречие"},
        "widzowie": {"lemma": "widz", "translation": "зрители", "part_of_speech": "существительное"},
        "reżyserką": {"lemma": "reżyserka", "translation": "режиссёр (женщина)", "part_of_speech": "существительное"},
        "opublikowała": {"lemma": "opublikować", "translation": "опубликовать", "part_of_speech": "глагол"},
        "zachęciły": {"lemma": "zachęcić", "translation": "побудить", "part_of_speech": "глагол"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(id="culture-media", defaults={"course": Course.objects.get(id="a2-independence"), "title": "Культура и медиа", "description": "Пересказываем произведение и выражаем оценку", "emoji": "🎬", "position": 7, "is_active": True})
    rows = (
        ("culture-words", "words", "Film, książka, wystawa", "Культура и форматы", "8 карточек · A2", "Назови произведение и его создателей", 8, "🎬"),
        ("culture-grammar", "grammar", "Go, ją, je czy ich?", "Объектные местоимения", "5 заданий · A2", "Не повторяй названия людей и произведений", 9, "✏️"),
        ("culture-review", "review", "Moja krótka recenzja", "Оценка произведения", "7 карточек · A2", "Повтори лексику пересказа и рекомендации", 7, "🔄"),
        ("culture-quiz", "quiz", "Quiz: kultura i media", "Проверка темы", "8 вопросов · A2", "Проверь лексику и объектные местоимения", 6, "🎯"),
        ("culture-reading-check", "quiz", "Czy rozumiesz recenzję?", "Понимание текста", "5 вопросов · A2", "Проверь детали фестиваля Лены и Павла", 5, "📖"),
    )
    made = {}
    for position, row in enumerate(rows, 83):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["culture-grammar"]
    grammar.theory_title = "Краткие объектные местоимения"
    grammar.theory_sections = [
        ["Мужской объект", "Film или serial заменяем на go: Obejrzałem go."],
        ["Женский объект", "Książkę, aktorkę или recenzję заменяем на ją: Czytam ją."],
        ["Множественное число", "Неодушевлённые объекты заменяет je, лично-мужскую группу — ich."],
    ]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 286):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("culture-words", cards[:8]), ("culture-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("culture-grammar", GRAMMAR), ("culture-quiz", QUIZ), ("culture-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "culture-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0026_a2_relationships_emotions_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
