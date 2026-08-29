from django.db import migrations

SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-29"}
CARDS = (
    ("b1work-stanowisko", "stanowisko", "должность", "Aplikuję na stanowisko specjalisty do spraw sprzedaży."),
    ("b1work-obowiazki", "obowiązki", "обязанности", "Do moich obowiązków należy kontakt z klientami."),
    ("b1work-doswiadczenie", "doświadczenie zawodowe", "профессиональный опыт", "Mam trzyletnie doświadczenie zawodowe."),
    ("b1work-kwalifikacje", "kwalifikacje", "квалификация", "Kandydat powinien mieć odpowiednie kwalifikacje."),
    ("b1work-rekrutacja", "rekrutacja", "подбор персонала", "Rekrutacja składa się z dwóch etapów."),
    ("b1work-rozmowa", "rozmowa kwalifikacyjna", "собеседование", "Jutro mam rozmowę kwalifikacyjną online."),
    ("b1work-zespol", "zespół", "команда", "Nasz zespół pracuje nad nowym projektem."),
    ("b1work-termin", "termin", "срок", "Musimy dotrzymać terminu projektu."),
    ("b1work-awans", "awans", "повышение", "Po dwóch latach otrzymała awans."),
    ("b1work-podwyzka", "podwyżka", "повышение зарплаты", "Chciałbym porozmawiać o podwyżce."),
    ("b1work-szkolenie", "szkolenie", "обучение; тренинг", "Firma organizuje szkolenie z negocjacji."),
    ("b1work-rozwoj", "rozwój zawodowy", "профессиональное развитие", "Zależy mi na rozwoju zawodowym."),
    ("b1work-wdrozyc", "wdrożyć", "внедрить; ввести в курс дела", "Mentorka pomogła wdrożyć nową pracownicę."),
    ("b1work-osiagnac", "osiągnąć cel", "достичь цели", "W tym kwartale osiągnęliśmy cel sprzedażowy."),
    ("b1work-inicjatywa", "wykazać inicjatywę", "проявить инициативу", "Warto wykazać inicjatywę podczas projektu."),
)
GRAMMAR = (
    ("Gdybym miał więcej czasu, ___ kurs zarządzania.", ["ukończyłbym", "ukończę by", "ukończyłem"], 0, "Условное наклонение образуется формой прошедшего времени с частицей by: ukończyłbym."),
    ("Na pani miejscu ___ swoje osiągnięcia w CV.", ["opisałabym", "opisuję by", "opisałam"], 0, "Na pani miejscu + tryb warunkowy служит вежливым советом."),
    ("Составьте: Я хотел бы узнать больше об обязанностях.", ["Chciałbym dowiedzieć się więcej o obowiązkach.", "Chcę się obowiązki więcej dowiedział.", "Dowiedziałbym obowiązkom więcej."], 0, "Chciałbym — вежливая условная форма; dowiedzieć się o требует местного падежа."),
    ("Как официально попросить о встрече?", ["Czy moglibyśmy umówić się na spotkanie?", "Spotkamy się, dobra?", "Musisz dać mi spotkanie."], 0, "Czy moglibyśmy... — нейтральная формальная просьба в условном наклонении."),
    ("Составьте: Если бы компания предложила обучение, я бы принял участие.", ["Gdyby firma zaproponowała szkolenie, wziąłbym w nim udział.", "Jeśli firma proponuje szkolenie, brałem go.", "Gdyby szkolenie firma, wezmę udziałem."], 0, "Gdyby вводит условие, а wziąłbym — его возможный результат; wziąć udział w + miejscownik."),
    ("Uprzejmie ___ o informację na temat wyniku rekrutacji.", ["proszę", "żądam sobie", "pytam tobie"], 0, "Uprzejmie proszę o... — стандартная формула официальной переписки."),
)
QUIZ = (
    ("Что означает stanowisko?", ["должность", "совещание", "зарплата"], 0, "Stanowisko — место или должность в организации."),
    ("Do moich ___ należy przygotowanie raportów.", ["obowiązków", "awansów", "zespołów do"], 0, "Należeć do + dopełniacz: do obowiązków."),
    ("Rekrutacja zwykle zaczyna się od ___.", ["wysłania CV", "wdrożenia terminu", "osiągnięcia zespołu"], 0, "Кандидат начинает процесс с отправки резюме."),
    ("Gdybym dostała tę pracę, ___ się nowych narzędzi.", ["nauczyłabym", "nauczę by", "uczyłam do"], 0, "Gdybym... nauczyłabym — согласованные формы условного наклонения."),
    ("Как вежливо начать просьбу о повышении зарплаты?", ["Chciałbym porozmawiać o możliwości podwyżki.", "Dajcie mi natychmiast podwyżkę.", "Podwyżka należy mnie."], 0, "Chciałbym porozmawiać... звучит профессионально и не категорично."),
    ("Pracownik, który proponuje rozwiązanie bez polecenia, ___.", ["wykazuje inicjatywę", "dotrzymuje stanowiska", "wdraża awans"], 0, "Wykazać inicjatywę — самостоятельно предложить или начать полезное действие."),
    ("Musimy ___ terminu do piątku.", ["dotrzymać", "osiągnąć się", "awansować do"], 0, "Dotrzymać terminu — выполнить работу в установленный срок."),
    ("Szkolenie wspiera nasz ___.", ["rozwój zawodowy", "wynik rekrutacji do", "obowiązek zespołem"], 0, "Обучение развивает профессиональные компетенции."),
    ("Czy ___ przesłać mi szczegóły oferty?", ["mógłby Pan", "Pan może by", "musisz pan"], 0, "Mógłby Pan... — формальная вежливая просьба."),
    ("Po dobrych wynikach Marta otrzymała ___.", ["awans", "rekrutację", "termin"], 0, "Otrzymać awans — получить повышение."),
)
CHECK = (
    ("Dlaczego Lena chciała zmienić pracę?", ["Chciała się rozwijać i mieć większą odpowiedzialność", "Nie lubiła swojego zawodu", "Planowała przestać pracować"], 0, "Ей не хватало возможностей развития и ответственности."),
    ("Co zrobiła przed wysłaniem CV?", ["Opisała wyniki i ukończyła kurs", "Poprosiła o natychmiastowy awans", "Zrezygnowała ze szkolenia"], 0, "Она подготовила конкретные достижения и прошла курс."),
    ("O co zapytał kierownik podczas rozmowy?", ["O reakcję na opóźnienie projektu", "O ulubiony środek transportu", "O cenę mieszkania"], 0, "Руководитель попросил привести пример решения рабочей проблемы."),
    ("Jak Lena odpowiedziała?", ["Opisała plan i rozmowę z klientem", "Obwiniła cały zespół", "Powiedziała, że nie zna rozwiązania"], 0, "Она показала инициативу и спокойную коммуникацию."),
    ("Jakie wsparcie rozwoju oferowała firma?", ["Mentora i budżet szkoleniowy", "Tylko wyższą pensję", "Bezpłatne podróże"], 0, "В предложении были наставник и бюджет на обучение."),
    ("Jaki jest główny wniosek tekstu?", ["Rozwój wymaga przygotowania i świadomych pytań", "Każda zmiana pracy gwarantuje awans", "Na rozmowie nie warto pytać o warunki"], 0, "Лена добилась результата благодаря подготовке и оценке возможностей развития."),
)
READING = {
    "id": "b1work-nowy-krok-leny", "title": "Nowy krok Leny", "description": "Собеседование и осознанный выбор профессионального развития", "level": "B1", "minutes": 8, "emoji": "💼", "position": 26,
    "paragraphs": [
        "Lena od czterech lat pracowała jako specjalistka do spraw obsługi klienta. Lubiła swój zespół i dobrze wykonywała obowiązki, jednak coraz częściej czuła, że stoi w miejscu. Chciała zdobyć nowe kwalifikacje, prowadzić projekty i mieć większy wpływ na decyzje.",
        "Zanim wysłała CV, dokładnie opisała swoje wyniki i ukończyła internetowy kurs zarządzania projektem. Podczas rozmowy kwalifikacyjnej kierownik zapytał, co zrobiłaby, gdyby ważny projekt był opóźniony. Lena odpowiedziała, że najpierw ustaliłaby przyczynę, następnie przygotowałaby plan i spokojnie porozmawiałaby z klientem.",
        "Podała też przykład z poprzedniej pracy. Gdy jej zespół nie mógł dotrzymać terminu, wykazała inicjatywę i podzieliła zadania inaczej. Dzięki temu projekt zakończył się tylko dzień później, a klient wcześniej otrzymał jasną informację. Kierownik docenił jej konkretne odpowiedzi.",
        "Firma zaproponowała Lenie stanowisko koordynatorki, wsparcie mentora i budżet na szkolenia. Zanim przyjęła ofertę, uprzejmie zapytała o zakres obowiązków oraz możliwości awansu. Uznała, że rozwój zawodowy nie polega wyłącznie na zmianie stanowiska: wymaga przygotowania, odwagi i świadomego wyboru miejsca, w którym można się uczyć.",
    ],
    "glossary": {
        "specjalistka": {"lemma": "specjalistka", "translation": "специалистка", "part_of_speech": "существительное"},
        "wykonywała": {"lemma": "wykonywać", "translation": "выполнять", "part_of_speech": "глагол"},
        "wpływ": {"lemma": "wpływ", "translation": "влияние", "part_of_speech": "существительное"},
        "kwalifikacje": {"lemma": "kwalifikacja", "translation": "квалификация", "part_of_speech": "существительное"},
        "wyniki": {"lemma": "wynik", "translation": "результат", "part_of_speech": "существительное"},
        "opóźniony": {"lemma": "opóźniony", "translation": "задержанный", "part_of_speech": "прилагательное"},
        "ustaliłaby": {"lemma": "ustalić", "translation": "установить; определить", "part_of_speech": "глагол"},
        "przyczynę": {"lemma": "przyczyna", "translation": "причина", "part_of_speech": "существительное"},
        "dotrzymać": {"lemma": "dotrzymać", "translation": "соблюсти", "part_of_speech": "глагол"},
        "wykazała": {"lemma": "wykazać", "translation": "проявить", "part_of_speech": "глагол"},
        "docenił": {"lemma": "docenić", "translation": "оценить по достоинству", "part_of_speech": "глагол"},
        "zakres": {"lemma": "zakres", "translation": "объём; круг", "part_of_speech": "существительное"},
        "wyłącznie": {"lemma": "wyłącznie", "translation": "исключительно", "part_of_speech": "наречие"},
        "świadomego": {"lemma": "świadomy", "translation": "осознанный", "part_of_speech": "прилагательное"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(id="b1-work-development", defaults={"course": Course.objects.get(id="b1-independent"), "title": "Работа и развитие", "description": "Обсуждаем опыт, планы и профессиональное развитие в формальном регистре", "emoji": "💼", "position": 2, "is_active": True})
    rows = (("b1work-words", "words", "Nowy krok w pracy", "Работа и обязанности", "8 карточек · B1", "Опиши опыт и условия вакансии", 9, "💼"), ("b1work-grammar", "grammar", "Gdybym dostał tę pracę...", "Условия и вежливость", "6 заданий · B1", "Используй условное наклонение в формальной речи", 12, "✏️"), ("b1work-review", "review", "Plan rozwoju", "Развитие и результаты", "7 карточек · B1", "Обсуди цели, обучение и инициативу", 8, "🔄"), ("b1work-quiz", "quiz", "Quiz: praca i rozwój", "Проверка темы", "10 вопросов · B1", "Проверь лексику и профессиональный регистр", 9, "🎯"), ("b1work-reading-check", "quiz", "Czy rozumiesz historię Leny?", "Понимание текста", "6 вопросов · B1", "Найди мотивацию, действия и вывод", 7, "📖"))
    made = {}
    for position, row in enumerate(rows, 118):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": description, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["b1work-grammar"]
    grammar.theory_title = "Условное наклонение и формальный регистр"
    grammar.theory_sections = [["Условие", "Gdyby + прошедшая форма с частицей by описывает воображаемую ситуацию: Gdybym dostał..., zrobiłbym..."], ["Вежливая просьба", "Chciałbym, mógłby Pan и czy moglibyśmy смягчают просьбу в профессиональной беседе."], ["Официальное письмо", "Uprzejmie proszę o... и Zwracam się z prośbą o... — нейтральные формулы обращения."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS, 392):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": position, "is_active": True, "source_metadata": SOURCE})
        cards.append(card)
    for lesson_id, chosen in (("b1work-words", cards[:8]), ("b1work-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen):
            Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("b1work-grammar", GRAMMAR), ("b1work-quiz", QUIZ), ("b1work-reading-check", CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, question in enumerate(questions):
            Question.objects.create(lesson_id=lesson_id, prompt=question[0], options=question[1], correct=question[2], explanation=question[3], position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": {**SOURCE, "comprehension_lesson_id": "b1work-reading-check"}, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0033_b1_travel_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
