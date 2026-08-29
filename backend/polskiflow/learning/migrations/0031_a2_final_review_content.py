from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-29"}
CARDS = (
    ("a2final-opowiedziec", "opowiedzieć o wydarzeniu", "рассказать о событии", "Potrafię opowiedzieć o tym, co wydarzyło się wczoraj."),
    ("a2final-zaplanowac", "zaplanować podróż", "спланировать поездку", "Najpierw zaplanujemy podróż, a potem kupimy bilety."),
    ("a2final-zglosic", "zgłosić problem", "сообщить о проблеме", "Lokator zgłosił właścicielowi problem z ogrzewaniem."),
    ("a2final-porownac", "porównać możliwości", "сравнить варианты", "Przed zakupem warto porównać kilka możliwości."),
    ("a2final-wyjasnic", "wyjaśnić sytuację", "объяснить ситуацию", "Spokojnie wyjaśniła sprzedawcy całą sytuację."),
    ("a2final-poprosic", "poprosić o pomoc", "попросить о помощи", "Czy mogę poprosić panią o pomoc?"),
    ("a2final-doradzic", "doradzić", "посоветовать", "Farmaceutka doradziła mi łagodny syrop."),
    ("a2final-uzasadnic", "uzasadnić opinię", "обосновать мнение", "Uzasadnij swoją opinię jednym przykładem."),
    ("a2final-porozumiec", "porozumieć się", "договориться; понять друг друга", "Po szczerej rozmowie łatwiej było nam się porozumieć."),
    ("a2final-zareagowac", "zareagować", "отреагировать", "Nie wiedziałem, jak zareagować na tę wiadomość."),
    ("a2final-zalatwic", "załatwić sprawę", "уладить дело", "Udało mi się załatwić sprawę w urzędzie."),
    ("a2final-zachowac", "zachować potwierdzenie", "сохранить подтверждение", "Trzeba zachować potwierdzenie płatności."),
    ("a2final-zmienic", "zmienić zdanie", "изменить мнение", "Po filmie zmieniłam zdanie o tym reżyserze."),
    ("a2final-uwzglednic", "uwzględnić pogodę", "учесть погоду", "Planując wycieczkę, trzeba uwzględnić pogodę."),
    ("a2final-polecic", "polecić miejsce", "порекомендовать место", "Czy możesz polecić ciekawe miejsce w Polsce?"),
    ("a2final-podsumowac", "podsumować", "подвести итог", "Na końcu krótko podsumowała swoje doświadczenia."),
)

DIAGNOSIS = (
    ("W sobotę Marta ___ do Krakowa i zwiedziła muzeum.", ["pojechała", "pojedzie", "jechać"], 0, "Завершённое событие в прошлом требует формы pojechała."),
    ("Jutro rano ___ bilety na pociąg.", ["kupimy", "kupiliśmy", "kupować"], 0, "Jutro указывает на будущее: kupimy."),
    ("W mieszkaniu nie ma ___.", ["ciepłej wody", "ciepła woda", "ciepłą wodą"], 0, "После nie ma используется родительный падеж: ciepłej wody."),
    ("Ten plecak jest ___ niż tamten.", ["lżejszy", "najlżejszy", "lekki od"], 0, "При сравнении двух предметов используется сравнительная степень + niż."),
    ("Составьте: Перед поездкой стоит проверить прогноз.", ["Przed podróżą warto sprawdzić prognozę.", "Przed podróż warto sprawdza prognoza.", "Podróżą warto prognozę sprawdził."], 0, "После przed нужен творительный, после warto — инфинитив."),
    ("Ania powiedziała, ___ nie może przyjść, ___ jest chora.", ["że; bo", "bo; że", "dlatego; czy"], 0, "Że вводит содержание сообщения, а bo — его причину."),
    ("Czytałem tę książkę. Polecam ___.", ["ją", "go", "ich"], 0, "Książka — существительное женского рода, поэтому объект заменяется местоимением ją."),
    ("Составьте: Я хотел бы подать заявление завтра.", ["Chciałbym złożyć wniosek jutro.", "Chcę jutro wniosek daj.", "Chciałbym złożyłem wniosek jutro."], 0, "Вежливая просьба строится как chciałbym + инфинитив złożyć."),
)

FINAL_QUIZ = (
    ("Co powiesz o zakończonym weekendzie?", ["W sobotę spotkałem się z przyjaciółmi.", "W sobotę spotkam się wczoraj.", "W sobotę spotykać przyjaciele."], 0, "Для законченного события используем прошедшее время."),
    ("Pociąg odjeżdża ___ Warszawy o siódmej.", ["do", "w", "na"], 0, "Направление к городу передаётся конструкцией do + родительный падеж."),
    ("Hydraulik zajmuje się ___.", ["naprawą kranu", "naprawę kranu", "naprawa kran"], 0, "Zajmować się требует творительного падежа: naprawą."),
    ("Najpierw ___ raport, a potem wysłałem go kierownikowi.", ["napisałem", "pisałem do końca", "będę pisał"], 0, "Napisałem подчёркивает завершённый результат действия."),
    ("Który produkt kosztuje najmniej?", ["najtańszy", "tańszy niż", "bardziej drogi"], 0, "Najtańszy — превосходная степень от tani."),
    ("Mam gorączkę. Co powinienem zrobić?", ["Powinieneś odpocząć i skontaktować się z lekarzem.", "Nie wolno zawsze lekarz.", "Odpoczywałeś jutro."], 0, "Powinieneś + инфинитив выражает рекомендацию."),
    ("Ola była smutna, ___ nie dostała tej pracy.", ["bo", "że", "dlatego"], 0, "Bo вводит причину эмоционального состояния."),
    ("Film był ciekawy, więc poleciłem ___ znajomym.", ["go", "ją", "je"], 0, "Film — мужской род, объект заменяется местоимением go."),
    ("Jak grzecznie poprosić o informację w urzędzie?", ["Czy może mi pani powiedzieć, gdzie mam podpisać?", "Powiedz mi teraz, gdzie podpis!", "Gdzie ja podpisuje pani?"], 0, "Czy może mi pani powiedzieć…? — нейтральная официальная просьба."),
    ("Jeśli jutro będzie burza, ___.", ["zostaniemy w domu", "zostaliśmy w domu wczoraj", "zostać dom"], 0, "Реальное условие относится к будущему: jeśli będzie…, zostaniemy…."),
    ("Najpierw zwiedziliśmy zamek, ___ poszliśmy na rynek.", ["następnie", "ponieważ", "chociaż że"], 0, "Następnie связывает последовательные события рассказа."),
    ("Что лучше всего завершает связный рассказ?", ["Na koniec podsumowałem, czego się nauczyłem.", "Bo na koniec i dlatego.", "Podsumować ja nauczył."], 0, "Финальный маркер na koniec и правильное прошедшее время создают ясное завершение."),
)

READING_CHECK = (
    ("Dlaczego Lena pojechała do Torunia?", ["Na weekend i spotkanie z kuzynką", "Żeby złożyć reklamację", "Na wizytę u lekarza"], 0, "Лена планировала выходные и встречу с двоюродной сестрой."),
    ("Jaki problem pojawił się po przyjeździe?", ["W pokoju nie działało ogrzewanie", "Lena zgubiła paszport", "Muzeum było zamknięte"], 0, "В комнате было холодно, потому что не работало отопление."),
    ("Jak rozwiązano problem w hostelu?", ["Recepcjonistka dała Lenie inny pokój", "Lena kupiła nowy grzejnik", "Kuzynka naprawiła okno"], 0, "После спокойного объяснения Лена получила другую комнату."),
    ("Dlaczego Lena i Zosia zmieniły plan spaceru?", ["Zaczął padać deszcz", "Nie miały biletów", "Pokłóciły się"], 0, "Из-за дождя они выбрали музей вместо долгой прогулки."),
    ("Co Lena zrobiła przed powrotem?", ["Kupiła syrop i zachowała paragon", "Złożyła wniosek o paszport", "Oddała bilet kolejowy"], 0, "В аптеке она купила сироп и сохранила чек."),
    ("Jaki jest główny wniosek Leny?", ["Spokój i jasne wyjaśnienie pomagają rozwiązać problem", "Każdą podróż trzeba odwołać", "W mieście nie warto pytać o pomoc"], 0, "В конце Лена подводит итог: спокойствие и ясная просьба помогают."),
)

READING = {
    "id": "a2final-weekend-leny",
    "title": "Weekend, który sprawdził plan Leny",
    "description": "Поездка, неожиданности и спокойное решение проблем",
    "level": "A2",
    "minutes": 8,
    "emoji": "🧭",
    "position": 23,
    "paragraphs": [
        "Lena zaplanowała weekend w Toruniu, gdzie miała spotkać się z kuzynką Zosią. W piątek kupiła bilet, sprawdziła prognozę pogody i zarezerwowała niedrogi pokój. Pociąg przyjechał zgodnie z planem, więc wieczorem obie zdążyły jeszcze zjeść kolację na Starym Mieście.",
        "Po powrocie do hostelu Lena zauważyła, że w jej pokoju nie działa ogrzewanie. Najpierw zadzwoniła do recepcji, a potem spokojnie wyjaśniła sytuację. Recepcjonistka przeprosiła i zaproponowała cieplejszy pokój. Lena przyjęła propozycję, ponieważ nie chciała zaczynać weekendu od kłótni.",
        "Następnego dnia zaczął padać deszcz, dlatego Lena i Zosia zmieniły plan. Zamiast długiego spaceru wybrały muzeum, które poleciła im recepcjonistka. Wystawa bardzo im się spodobała. Po południu Lena poczuła ból gardła, więc w aptece poprosiła o poradę, kupiła syrop i zachowała paragon.",
        "W niedzielę pogoda się poprawiła i kuzynki krótko spacerowały nad Wisłą. Przed odjazdem Lena podsumowała weekend: nie wszystko wydarzyło się zgodnie z planem, ale każdy problem udało się rozwiązać. Zrozumiała, że warto zachować spokój, jasno prosić o pomoc i umieć zmienić plan.",
    ],
    "glossary": {
        "zarezerwowała": {"lemma": "zarezerwować", "translation": "забронировать", "part_of_speech": "глагол"},
        "zgodnie": {"lemma": "zgodnie", "translation": "согласно; как было запланировано", "part_of_speech": "наречие"},
        "zauważyła": {"lemma": "zauważyć", "translation": "заметить", "part_of_speech": "глагол"},
        "ogrzewanie": {"lemma": "ogrzewanie", "translation": "отопление", "part_of_speech": "существительное"},
        "wyjaśniła": {"lemma": "wyjaśnić", "translation": "объяснить", "part_of_speech": "глагол"},
        "zaproponowała": {"lemma": "zaproponować", "translation": "предложить", "part_of_speech": "глагол"},
        "kłótni": {"lemma": "kłótnia", "translation": "ссора", "part_of_speech": "существительное"},
        "wystawa": {"lemma": "wystawa", "translation": "выставка", "part_of_speech": "существительное"},
        "poradę": {"lemma": "porada", "translation": "совет", "part_of_speech": "существительное"},
        "zachowała": {"lemma": "zachować", "translation": "сохранить", "part_of_speech": "глагол"},
        "odjazdem": {"lemma": "odjazd", "translation": "отъезд", "part_of_speech": "существительное"},
        "podsumowała": {"lemma": "podsumować", "translation": "подвести итог", "part_of_speech": "глагол"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(id="a2final-review", defaults={"course": Course.objects.get(id="a2-independence"), "title": "Итоговое повторение A2", "description": "Интеграционная практика и диагностика навыков уровня A2", "emoji": "🏁", "position": 11, "is_active": True})
    rows = (
        ("a2final-words", "words", "Potrafię to powiedzieć", "Активные умения A2", "8 карточек · A2", "Повтори действия для типичных повседневных ситуаций", 8, "🧩"),
        ("a2final-diagnosis", "grammar", "Diagnoza gramatyczna A2", "Грамматика A2", "8 заданий · A2", "Проверь времена, падежи, союзы и порядок слов", 12, "✏️"),
        ("a2final-review", "review", "Rozwiązuję problemy", "Стратегии общения", "8 карточек · A2", "Повтори фразы для объяснения, совета и итога", 8, "🔄"),
        ("a2final-quiz", "quiz", "Finałowy quiz A2", "Итоговая диагностика", "12 вопросов · A2", "Проверь ключевые навыки всех тем A2", 12, "🎯"),
        ("a2final-reading-check", "quiz", "Czy rozumiesz historię Leny?", "Понимание текста", "6 вопросов · A2", "Найди детали и главный вывод связного рассказа", 7, "📖"),
    )
    made = {}
    for position, row in enumerate(rows, 103):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["a2final-diagnosis"]
    grammar.theory_title = "Как связать знания A2 в самостоятельную речь"
    grammar.theory_sections = [
        ["Время и результат", "Выбирай прошедшее или будущее по ситуации, а вид глагола — по процессу или завершённому результату."],
        ["Форма зависит от связи", "Предлоги и глаголы управляют падежом; niż вводит сравнение, а местоимение заменяет уже названный объект."],
        ["Связный ответ", "Że передаёт содержание, bo — причину, następnie — последовательность. В просьбе используй czy może… или chciałbym/chciałabym…."],
    ]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 346):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("a2final-words", cards[:8]), ("a2final-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("a2final-diagnosis", DIAGNOSIS), ("a2final-quiz", FINAL_QUIZ), ("a2final-reading-check", READING_CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "a2final-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0030_a2_poland_around_us_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
