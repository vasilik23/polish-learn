from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-29"}
CARDS = (
    ("rel-relacja", "relacja", "отношения", "Mamy dobrą relację i często rozmawiamy."),
    ("rel-przyjazn", "przyjaźń", "дружба", "Nasza przyjaźń jest dla mnie ważna."),
    ("rel-zaufanie", "zaufanie", "доверие", "Zaufanie buduje się przez szczere rozmowy."),
    ("rel-wsparcie", "wsparcie", "поддержка", "Dziękuję ci za wsparcie w trudnym tygodniu."),
    ("rel-szczery", "szczery", "искренний", "Chcę być z tobą szczery."),
    ("rel-dumny", "dumny", "гордый", "Jestem dumny, że zdałeś egzamin."),
    ("rel-zmartwiony", "zmartwiony", "обеспокоенный", "Ola jest zmartwiona, bo przyjaciel nie odpowiada."),
    ("rel-zazdrosny", "zazdrosny", "ревнивый; завистливый", "Nie chcę być zazdrosny o jej sukces."),
    ("rel-klocic", "kłócić się", "ссориться", "Nie warto kłócić się o drobiazgi."),
    ("rel-pogodzic", "pogodzić się", "помириться", "Po rozmowie szybko się pogodzili."),
    ("rel-przeprosic", "przeprosić", "извиниться", "Powinienem przeprosić za swoje słowa."),
    ("rel-wybaczyc", "wybaczyć", "простить", "Trudno wybaczyć bez szczerej rozmowy."),
    ("rel-tesknic", "tęsknić za", "скучать по", "Tęsknię za rodziną, dlatego często dzwonię."),
    ("rel-cieszyc", "cieszyć się", "радоваться", "Cieszę się, że możemy się spotkać."),
    ("rel-rozczarowany", "rozczarowany", "разочарованный", "Byłam rozczarowana, bo zmieniłeś plany."),
)
GRAMMAR = (
    ("Cieszę się, ___ możemy porozmawiać.", ["że", "bo że", "dlatego"], 0, "Że вводит содержание чувства или мнения: cieszę się, że…"),
    ("Ola jest zmartwiona, ___ Marek nie odpowiada.", ["bo", "że dlatego", "ale że"], 0, "Bo вводит причину и соединяет её с главным предложением."),
    ("Я звоню, потому что скучаю.", ["Dzwonię, bo tęsknię.", "Dzwonię, że tęsknię.", "Dlatego że dzwonię tęsknię."], 0, "После действия причину удобно вводить союзом bo."),
    ("Составьте: Я рад, что мы помирились.", ["Cieszę się, że się pogodziliśmy.", "Cieszę, bo my pogodzić się.", "Jestem że pogodziliśmy cieszę."], 0, "После cieszę się содержание эмоции вводится через że."),
    ("Nie miał czasu, ___ napisał krótką wiadomość.", ["dlatego", "dlatego że", "że"], 0, "Dlatego начинает следствие: времени не было, поэтому он написал короткое сообщение."),
)
QUIZ = (
    ("Что означает zaufanie?", ["доверие", "ссора", "встреча"], 0, "Zaufanie — доверие между людьми."),
    ("Jestem dumny, ___ zdałeś egzamin.", ["że", "bo dlatego", "dlatego że"], 0, "Że вводит факт, который вызывает гордость."),
    ("Почему она обеспокоена?", ["Dlaczego ona jest zmartwiona?", "Że ona jest szczera?", "Dlatego ona wybaczyć?"], 0, "Dlaczego задаёт вопрос о причине."),
    ("Nie przyszedł, ___ był chory.", ["bo", "że", "dlatego"], 0, "Bo вводит причину отсутствия."),
    ("Как сказать «Мы помирились»?", ["Pogodziliśmy się.", "Kłócimy ich.", "Wybaczyli nas."], 0, "Pogodzić się — помириться; в прошедшем времени: pogodziliśmy się."),
    ("Tęsknię za rodziną, ___ często dzwonię.", ["dlatego", "że bo", "ponieważ że"], 0, "Dlatego соединяет причину с её следствием."),
    ("Что лучше сказать после обидных слов?", ["Przepraszam, nie chciałem cię zranić.", "Jestem zazdrosny, dlatego milcz.", "Nie wolno mi wybaczyć."], 0, "Конкретное искреннее извинение помогает восстановить разговор."),
    ("Była ___, bo przyjaciółka odwołała spotkanie.", ["rozczarowana", "rozczarowany", "rozczarowane"], 0, "Форма женского рода: rozczarowana."),
)
CHECK = (
    ("Dlaczego Marta była rozczarowana?", ["Ania odwołała spotkanie bez wyjaśnienia", "Marta nie zdała egzaminu", "Telefon Marty się zepsuł"], 0, "Марта ждала встречи, но Аня её отменила без объяснения."),
    ("Co Ania napisała w wiadomości?", ["Że miała trudny dzień i przeprasza", "Że nie chce już rozmawiać", "Że wyjeżdża na rok"], 0, "Аня объяснила ситуацию и извинилась."),
    ("Dlaczego Marta nie odpowiedziała od razu?", ["Potrzebowała czasu, żeby się uspokoić", "Nie znała numeru Ani", "Była w aptece"], 0, "Марте понадобилось время, чтобы успокоиться."),
    ("Co pomogło przyjaciółkom się pogodzić?", ["Szczera rozmowa", "Nowy prezent", "Wspólny egzamin"], 0, "Помириться помогла открытая беседа."),
    ("Czego nauczyły się Marta i Ania?", ["Że warto mówić o emocjach i słuchać", "Że lepiej zawsze milczeć", "Że przyjaźń nie wymaga zaufania"], 0, "Они поняли ценность разговора об эмоциях и внимательного слушания."),
)
READING = {
    "id": "szczera-rozmowa-marty-i-ani",
    "title": "Szczera rozmowa Marty i Ani",
    "description": "Недопонимание, извинение и восстановление дружбы",
    "level": "A2",
    "minutes": 6,
    "emoji": "💬",
    "position": 18,
    "paragraphs": [
        "Marta i Ania przyjaźnią się od kilku lat. W piątek miały spotkać się w kawiarni, ale Ania nagle odwołała spotkanie i niczego nie wyjaśniła. Marta była rozczarowana, bo długo czekała na ten wieczór. Pomyślała też, że przyjaciółka nie szanuje jej czasu.",
        "Następnego dnia Ania napisała, że miała bardzo trudny dzień w pracy. Przeprosiła i przyznała, że powinna była wcześniej wszystko wyjaśnić. Marta nadal była zmartwiona, dlatego nie odpowiedziała od razu. Potrzebowała chwili, żeby się uspokoić.",
        "Wieczorem przyjaciółki spokojnie porozmawiały. Marta powiedziała szczerze, co poczuła, a Ania uważnie jej wysłuchała. Obie zrozumiały, że nie chciały się zranić. Pogodziły się i umówiły na nowy termin. Cieszyły się, że szczera rozmowa odbudowała ich zaufanie.",
    ],
    "glossary": {
        "przyjaźnią": {"lemma": "przyjaźnić się", "translation": "дружить", "part_of_speech": "глагол"},
        "odwołała": {"lemma": "odwołać", "translation": "отменить", "part_of_speech": "глагол"},
        "rozczarowana": {"lemma": "rozczarowany", "translation": "разочарованная", "part_of_speech": "прилагательное"},
        "szanuje": {"lemma": "szanować", "translation": "уважать", "part_of_speech": "глагол"},
        "przyznała": {"lemma": "przyznać", "translation": "признать", "part_of_speech": "глагол"},
        "uspokoić": {"lemma": "uspokoić się", "translation": "успокоиться", "part_of_speech": "глагол"},
        "poczuła": {"lemma": "poczuć", "translation": "почувствовать", "part_of_speech": "глагол"},
        "wysłuchała": {"lemma": "wysłuchać", "translation": "выслушать", "part_of_speech": "глагол"},
        "zranić": {"lemma": "zranić", "translation": "обидеть; ранить", "part_of_speech": "глагол"},
        "odbudowała": {"lemma": "odbudować", "translation": "восстановить", "part_of_speech": "глагол"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course = apps.get_model("learning", "Course")
    Topic = apps.get_model("learning", "Topic")
    Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard")
    Link = apps.get_model("learning", "LessonFlashcard")
    Question = apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(
        id="relationships-emotions",
        defaults={"course": Course.objects.get(id="a2-independence"), "title": "Отношения и эмоции", "description": "Выражаем чувства, объясняем причины и решаем недопонимание", "emoji": "💬", "position": 6, "is_active": True},
    )
    rows = (
        ("rel-words", "words", "Relacje i uczucia", "Отношения и чувства", "8 карточек · A2", "Назови эмоции и важные элементы отношений", 8, "💛"),
        ("rel-grammar", "grammar", "Że, bo czy dlatego?", "Причина, содержание и следствие", "5 заданий · A2", "Связывай мнение, эмоцию и объяснение", 9, "✏️"),
        ("rel-review", "review", "Rozmowa po konflikcie", "Извинение и примирение", "7 карточек · A2", "Повтори фразы для спокойного разговора", 7, "🔄"),
        ("rel-quiz", "quiz", "Quiz: relacje i emocje", "Проверка темы", "8 вопросов · A2", "Проверь лексику и причинные союзы", 6, "🎯"),
        ("rel-reading-check", "quiz", "Czy rozumiesz rozmowę?", "Понимание текста", "5 вопросов · A2", "Проверь детали истории Марты и Ани", 5, "📖"),
    )
    made = {}
    for position, row in enumerate(rows, 78):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["rel-grammar"]
    grammar.theory_title = "Że, bo, dlatego i dlatego że"
    grammar.theory_sections = [
        ["Содержание мысли или чувства", "Że отвечает на вопрос «что?»: Cieszę się, że jesteś tutaj."],
        ["Причина", "Bo и dlatego że отвечают на вопрос «почему?»: Nie przyszedł, bo był chory."],
        ["Следствие", "Dlatego показывает результат: Był chory, dlatego został w domu."],
    ]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 271):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("rel-words", cards[:8]), ("rel-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("rel-grammar", GRAMMAR), ("rel-quiz", QUIZ), ("rel-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "rel-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0025_a2_doctor_pharmacy_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
