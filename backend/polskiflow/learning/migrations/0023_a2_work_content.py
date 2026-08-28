from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-28"}
CARDS = (
    ("a2work-doswiadczenie", "doświadczenie", "опыт", "Mam dwa lata doświadczenia w sprzedaży."),
    ("a2work-obowiazek", "obowiązek", "обязанность", "Moim obowiązkiem jest kontakt z klientami."),
    ("a2work-zadanie", "zadanie", "задача", "Dziś mam trzy ważne zadania."),
    ("a2work-spotkanie", "spotkanie", "встреча", "Spotkanie zespołu zaczyna się o dziewiątej."),
    ("a2work-termin", "termin", "срок", "Termin projektu jest w piątek."),
    ("a2work-zespol", "zespół", "команда", "Pracuję w pięcioosobowym zespole."),
    ("a2work-kierownik", "kierownik", "руководитель", "Kierownik wyjaśnił mi nowe zadanie."),
    ("a2work-zmiana", "zmiana", "смена", "Moja zmiana kończy się o siedemnastej."),
    ("a2work-przygotowywac", "przygotowywać", "подготавливать (процесс)", "Codziennie przygotowuję raporty."),
    ("a2work-przygotowac", "przygotować", "подготовить (результат)", "Przygotuję raport do południa."),
    ("a2work-pisac", "pisać", "писать", "Teraz piszę wiadomość do klienta."),
    ("a2work-napisac", "napisać", "написать", "Napiszę wiadomość przed spotkaniem."),
    ("a2work-rozwiazywac", "rozwiązywać", "решать (процесс)", "Często rozwiązuję problemy klientów."),
    ("a2work-rozwiazac", "rozwiązać", "решить", "Musimy rozwiązać ten problem dzisiaj."),
    ("a2work-awans", "awans", "повышение", "Po roku dostała awans."),
)
GRAMMAR = (
    ("Codziennie ___ raporty.", ["przygotowuję", "przygotuję raz", "przygotował jutro"], 0, "Повторяющийся процесс выражает несовершенный вид: przygotowuję."),
    ("Muszę ___ raport do dwunastej.", ["przygotowywać bez końca", "przygotować", "przygotowałem"], 1, "Важен завершённый результат к сроку: przygotować."),
    ("Wczoraj przez godzinę ___ wiadomość.", ["pisałam", "napiszę", "napisać"], 0, "Длительность процесса в прошлом передаёт несовершенный pisać: pisałam."),
    ("Она решила проблему за десять минут.", ["Rozwiązywała problem codziennie.", "Rozwiązała problem w dziesięć minut.", "Rozwiąże problem wczoraj."], 1, "Завершённый единичный результат: rozwiązała."),
    ("Najpierw ___ dane, a potem wyślę raport.", ["sprawdzę", "sprawdzałem codziennie", "sprawdzać wczoraj"], 0, "Последовательность завершённых будущих действий требует совершенного sprawdzę."),
)
QUIZ = (
    ("Что означает obowiązek?", ["обязанность", "отпуск", "зарплата"], 0, "Obowiązek — обязанность или служебная задача."),
    ("Co tydzień ___ wyniki.", ["analizuję", "przeanalizuję raz", "przeanalizowałem jutro"], 0, "Регулярное действие: несовершенный analizuję."),
    ("Do końca dnia ___ prezentację.", ["robię zawsze", "zrobię", "robiłem jutro"], 1, "Результат к концу дня: совершенный zrobię."),
    ("Как сказать «у меня опыт в продажах»?", ["Mam doświadczenie w sprzedaży.", "Jestem termin sprzedażą.", "Robię awans klientem."], 0, "Mam doświadczenie w sprzedaży — естественная конструкция об опыте."),
    ("Kierownik ___ mi zadanie wczoraj.", ["wyjaśnił", "wyjaśnia jutro", "wyjaśnić"], 0, "Однократное завершённое действие в прошлом: wyjaśnił."),
    ("Teraz ___ problem klienta.", ["rozwiązuję", "rozwiążę wczoraj", "rozwiązałem jutro"], 0, "Teraz указывает на текущий процесс: rozwiązuję."),
    ("Что обозначает termin проекта?", ["команду", "крайний срок", "рабочее место"], 1, "Termin — назначенная дата или крайний срок."),
    ("Najpierw napiszemy ofertę, potem ją ___.", ["wyślemy", "wysyłaliśmy co dzień", "wysłać wczoraj"], 0, "Следующий завершённый этап в будущем: wyślemy."),
)
COMPREHENSION = (
    ("Gdzie zaczęła pracować Maja?", ["W małej firmie informatycznej", "W szkole językowej", "W restauracji"], 0, "Майя начала работу в небольшой IT-компании."),
    ("Co Maja robi codziennie rano?", ["Prowadzi szkolenie", "Sprawdza pocztę i planuje zadania", "Kończy zmianę"], 1, "Каждое утро она проверяет почту и планирует задачи."),
    ("Jakie zadanie dostała od kierownika?", ["Przygotować raport dla klienta", "Zatrudnić nowy zespół", "Zmienić biuro"], 0, "Руководитель поручил подготовить отчёт для клиента."),
    ("Kto pomógł Mai z tabelą?", ["Klient", "Kolega z zespołu", "Kierownik banku"], 1, "Коллега показал ей, как быстрее заполнить таблицу."),
    ("Dlaczego Maja była zadowolona w piątek?", ["Skończyła raport przed terminem", "Dostała urlop na miesiąc", "Nie miała żadnych zadań"], 0, "Она закончила отчёт раньше срока и получила похвалу."),
)
READING = {
    "id": "pierwszy-tydzien-mai", "title": "Pierwszy tydzień Mai", "description": "Новые обязанности и первый результат на работе", "level": "A2", "minutes": 5, "emoji": "💼", "position": 15,
    "paragraphs": [
        "Maja zaczęła pracować w małej firmie informatycznej. Ma już doświadczenie w obsłudze klientów, ale wcześniej nie pracowała w takim zespole. Codziennie rano sprawdza pocztę, planuje zadania i uczestniczy w krótkim spotkaniu z kierownikiem.",
        "We wtorek kierownik poprosił Maję, żeby przygotowała raport dla ważnego klienta. Najpierw analizowała dane, a potem zaczęła pisać podsumowanie. Nie wiedziała, jak szybko uzupełnić jedną tabelę, więc poprosiła kolegę o pomoc. Kolega pokazał jej prostszy sposób.",
        "W czwartek Maja skończyła raport i wysłała go kierownikowi. Następnego dnia dostała odpowiedź: raport był jasny i dokładny. Maja była zadowolona, bo wykonała zadanie przed terminem. W przyszłym tygodniu będzie rozwiązywać podobne problemy samodzielnie i przygotuje pierwszą prezentację dla klienta.",
    ],
    "glossary": {
        "zaczęła": {"lemma": "zacząć", "translation": "начать", "part_of_speech": "глагол"}, "obsłudze": {"lemma": "obsługa", "translation": "обслуживание", "part_of_speech": "существительное"},
        "uczestniczy": {"lemma": "uczestniczyć", "translation": "участвовать", "part_of_speech": "глагол"}, "poprosił": {"lemma": "poprosić", "translation": "попросить", "part_of_speech": "глагол"},
        "analizowała": {"lemma": "analizować", "translation": "анализировать", "part_of_speech": "глагол"}, "podsumowanie": {"lemma": "podsumowanie", "translation": "итог; резюме", "part_of_speech": "существительное"},
        "uzupełnić": {"lemma": "uzupełnić", "translation": "заполнить; дополнить", "part_of_speech": "глагол"}, "skończyła": {"lemma": "skończyć", "translation": "закончить", "part_of_speech": "глагол"},
        "dokładny": {"lemma": "dokładny", "translation": "точный", "part_of_speech": "прилагательное"}, "wykonała": {"lemma": "wykonać", "translation": "выполнить", "part_of_speech": "глагол"},
        "samodzielnie": {"lemma": "samodzielnie", "translation": "самостоятельно", "part_of_speech": "наречие"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite": return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    topic, _ = Topic.objects.update_or_create(id="a2-work", defaults={"course": Course.objects.get(id="a2-independence"), "title": "Работа", "description": "Рассказываем об опыте, обязанностях и результатах", "emoji": "💼", "position": 3, "is_active": True})
    rows = (("a2work-words","words","Praca i obowiązki","Опыт и обязанности","8 карточек · A2","Опиши команду, задачи и график",7,"💼"),("a2work-grammar","grammar","Robię czy zrobię?","Процесс и результат","5 заданий · A2","Различай видовые пары в рабочих ситуациях",9,"✏️"),("a2work-review","review","Zadanie na termin","Рабочий результат","7 карточек · A2","Повтори действия и результаты",7,"🔄"),("a2work-quiz","quiz","Quiz: praca","Проверка темы","8 вопросов · A2","Проверь лексику и вид глагола",6,"🎯"),("a2work-reading-check","quiz","Czy rozumiesz historię?","Понимание текста","5 вопросов · A2","Проверь детали первой недели Майи",5,"📖"))
    made = {}
    for position, row in enumerate(rows, 63):
        id_, kind, title, plan, subtitle, description, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic,"kind":kind,"title":title,"plan_title":plan,"subtitle":subtitle,"description":description,"minutes":minutes,"emoji":emoji,"position":position,"is_active":True,"source_metadata":SOURCE})
    grammar = made["a2work-grammar"]
    grammar.theory_title = "Proces czy gotowy rezultat?"
    grammar.theory_sections = [["Несовершенный вид", "Процесс, повторение и длительность: robić, pisać, przygotowywać, rozwiązywać."], ["Совершенный вид", "Однократный законченный результат: zrobić, napisać, przygotować, rozwiązać."], ["Контекст помогает", "Codziennie и przez godzinę указывают на процесс; do piątku и najpierw… potem часто требуют результата."]]
    grammar.save(update_fields=("theory_title","theory_sections"))
    cards=[]
    for position,(id_,polish,translation,example) in enumerate(CARDS,226):
        card,_=Flashcard.objects.update_or_create(id=id_,defaults={"polish":polish,"translation":translation,"example":example,"position":position,"is_active":True,"source_metadata":SOURCE}); cards.append(card)
    for lesson_id,chosen in (("a2work-words",cards[:8]),("a2work-review",cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position,card in enumerate(chosen): Link.objects.create(lesson_id=lesson_id,flashcard=card,position=position)
    for lesson_id,questions in (("a2work-grammar",GRAMMAR),("a2work-quiz",QUIZ),("a2work-reading-check",COMPREHENSION)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position,(prompt,options,correct,explanation) in enumerate(questions): Question.objects.create(lesson_id=lesson_id,prompt=prompt,options=options,correct=correct,explanation=explanation,position=position)
    ReadingText.objects.update_or_create(id=READING["id"],defaults={**{k:v for k,v in READING.items() if k!="id"},"topic":topic,"source_metadata":{**SOURCE,"comprehension_lesson_id":"a2work-reading-check"},"is_active":True})


class Migration(migrations.Migration):
    dependencies=[("learning","0022_a2_housing_services_content")]
    operations=[migrations.RunPython(seed,migrations.RunPython.noop)]
