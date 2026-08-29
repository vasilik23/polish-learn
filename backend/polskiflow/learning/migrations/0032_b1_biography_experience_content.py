from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-29"}
CARDS = (
    ("bio-dorastac", "dorastać", "расти; взрослеть", "Dorastałam w małym mieście na południu Polski."),
    ("bio-ukonczyc", "ukończyć studia", "окончить вуз", "Po pięciu latach ukończył studia techniczne."),
    ("bio-zdobyc", "zdobyć doświadczenie", "приобрести опыт", "Pierwszą pracę podjęła, żeby zdobyć doświadczenie."),
    ("bio-podjac", "podjąć decyzję", "принять решение", "Wtedy podjąłem ważną decyzję o przeprowadzce."),
    ("bio-przeprowadzic", "przeprowadzić się", "переехать", "W 2018 roku przeprowadziliśmy się do Poznania."),
    ("bio-rozpoczac", "rozpocząć karierę", "начать карьеру", "Karierę rozpoczęła jako asystentka."),
    ("bio-osiagnac", "osiągnąć cel", "достичь цели", "Po kilku latach osiągnął swój zawodowy cel."),
    ("bio-wydarzenie", "ważne wydarzenie", "важное событие", "To wydarzenie całkowicie zmieniło jej plany."),
    ("bio-poczatkowo", "początkowo", "поначалу", "Początkowo nie znałem w mieście nikogo."),
    ("bio-z-czasem", "z czasem", "со временем", "Z czasem poczuła się pewniej w nowej roli."),
    ("bio-okazac", "okazać się", "оказаться", "Nowe zajęcie okazało się bardzo ciekawe."),
    ("bio-wplynac", "wpłynąć na", "повлиять на", "Ta rozmowa wpłynęła na moją decyzję."),
    ("bio-wspominac", "wspominać", "вспоминать", "Często wspominam pierwszy dzień pracy."),
    ("bio-doswiadczenie", "życiowe doświadczenie", "жизненный опыт", "Podróż była dla niej ważnym doświadczeniem."),
    ("bio-przelom", "punkt zwrotny", "поворотный момент", "Zmiana zawodu stała się punktem zwrotnym."),
)
GRAMMAR = (
    ("Przez trzy lata Marta ___ w banku, a potem zmieniła zawód.", ["pracowała", "przepracowała", "będzie pracować"], 0, "Несовершенный вид pracowała описывает длительный фон прошлого."),
    ("W 2020 roku Marta ___ kurs i dostała certyfikat.", ["kończyła", "ukończyła", "kończy"], 1, "Ukończyła подчёркивает завершённый результат."),
    ("Kiedy ___ studia, przeprowadził się do Gdańska.", ["kończył", "ukończył", "ukończy"], 1, "Одно завершённое событие предшествует другому: ukończył."),
    ("Составьте: Сначала она работала в школе, а потом открыла фирму.", ["Najpierw pracowała w szkole, a potem założyła firmę.", "Najpierw założyła szkołę, bo pracowała firmę.", "Pracuje najpierw, potem firma otwierała."], 0, "Najpierw и potem выстраивают хронологию; założyła передаёт достигнутый результат."),
    ("Co roku Jan ___ za granicę, ale w zeszłym roku ___ w Polsce.", ["jeździł; został", "pojechał; zostawał", "jeździ; zostanie"], 0, "Jeździł описывает повторение, został — единичный завершённый выбор."),
    ("Составьте: Этот опыт сильно повлиял на мою жизнь.", ["To doświadczenie bardzo wpłynęło na moje życie.", "To doświadczenie wpływało moje życie bardzo.", "Moje życie wpłynęło do doświadczenia."], 0, "Wpłynąć требует na + винительный падеж: na moje życie."),
)
QUIZ = (
    ("Что означает dorastać?", ["взрослеть", "переезжать", "увольняться"], 0, "Dorastać — постепенно становиться взрослым."),
    ("Po studiach Anna ___ karierę w mediach.", ["rozpoczęła", "dorastała", "wspominała się"], 0, "Rozpocząć karierę — начать профессиональный путь."),
    ("Как сказать «поворотный момент»?", ["punkt zwrotny", "ważny kierunek", "czas doświadczenia"], 0, "Punkt zwrotny меняет дальнейшее развитие событий."),
    ("Pracował nad projektem rok i wreszcie ___ cel.", ["osiągnął", "osiągał się", "dorósł na"], 0, "Osiągnął обозначает полученный результат."),
    ("Która forma opisuje powtarzające się podróże?", ["jeździłem", "pojechałem", "pojadę raz"], 0, "Jeździłem передаёт повторявшееся действие."),
    ("Ta książka ___ na wybór jej zawodu.", ["wpłynęła", "przeprowadziła", "ukończyła"], 0, "Wpłynąć na — оказать влияние на что-либо."),
    ("___ było trudno, lecz z czasem wszystko się zmieniło.", ["Początkowo", "Na końcu wczoraj", "Osiągnięcie"], 0, "Początkowo вводит начальный этап истории."),
    ("Nowa praca ___ ciekawsza, niż oczekiwał.", ["okazała się", "podjęła się na", "zdobyła się"], 0, "Okazać się сообщает, каким что-либо оказалось."),
    ("Что лучше связывает биографический рассказ?", ["najpierw, następnie, z czasem, w końcu", "bo, albo, czy, lecz że", "wczoraj, jutro, teraz, nigdy"], 0, "Хронологические маркеры делают рассказ связным."),
    ("Как сказать о завершённом образовании?", ["Ukończyłem studia w 2019 roku.", "Kończyłem studia i nie wiadomo kiedy.", "Studia ukończyć w roku."], 0, "Ukończyłem ясно обозначает завершённый этап."),
)
CHECK = (
    ("Gdzie dorastała Joanna?", ["W Białymstoku", "W Krakowie", "Za granicą"], 0, "Йоанна выросла в Белостоке."),
    ("Co studiowała?", ["Architekturę", "Medycynę", "Dziennikarstwo"], 0, "Она изучала архитектуру в Варшаве."),
    ("Dlaczego pierwsza praca była ważna?", ["Zdobyła praktyczne doświadczenie", "Od razu została dyrektorką", "Mogła wrócić do szkoły"], 0, "Первая работа дала ей практический опыт."),
    ("Co było punktem zwrotnym?", ["Projekt biblioteki w małym mieście", "Wyjazd na wakacje", "Zmiana mieszkania w dzieciństwie"], 0, "Работа над библиотекой изменила её профессиональные цели."),
    ("Jak zmieniły się jej plany?", ["Postanowiła projektować miejsca publiczne", "Zrezygnowała z architektury", "Chciała pracować wyłącznie sama"], 0, "Она решила заниматься общественными пространствами."),
    ("Jaki wniosek wyciąga Joanna?", ["Doświadczenia pomagają lepiej rozumieć własne cele", "Każdy plan musi pozostać bez zmian", "Pierwsza praca zawsze jest najważniejsza"], 0, "В финале она связывает опыт с пониманием собственных целей."),
)
READING = {
    "id": "bio-droga-joanny", "title": "Droga Joanny do własnego celu", "description": "Биография, профессиональный выбор и поворотный момент", "level": "B1", "minutes": 8, "emoji": "🧭", "position": 24,
    "paragraphs": [
        "Joanna dorastała w Białymstoku. Już jako dziecko lubiła rysować domy i obserwować, jak zmienia się jej miasto. Po maturze przeprowadziła się do Warszawy, gdzie rozpoczęła studia architektoniczne. Początkowo trudno było jej przyzwyczaić się do szybkiego życia w stolicy, ale z czasem poznała przyjaciół i poczuła się pewniej.",
        "Po ukończeniu studiów Joanna podjęła pracę w niewielkim biurze projektowym. Przez dwa lata przygotowywała rysunki i pomagała bardziej doświadczonym architektom. Nie prowadziła jeszcze własnych projektów, jednak zdobyła praktyczne doświadczenie i nauczyła się rozmawiać z klientami.",
        "Punktem zwrotnym okazał się projekt biblioteki w małym mieście. Joanna odpowiadała za spotkania z mieszkańcami. Zrozumiała wtedy, że dobrze zaprojektowane miejsce może wpłynąć na codzienne życie wielu osób. Po zakończeniu projektu podjęła decyzję, że chce zajmować się przede wszystkim przestrzeniami publicznymi.",
        "Dziś Joanna pracuje w większym zespole i prowadzi własne projekty. Często wspomina pierwsze lata kariery, bo dzięki nim lepiej rozumie swoje cele. Uważa, że nawet trudne doświadczenie może z czasem stać się ważnym etapem rozwoju.",
    ],
    "glossary": {
        "dorastała": {"lemma": "dorastać", "translation": "взрослеть", "part_of_speech": "глагол"}, "maturze": {"lemma": "matura", "translation": "выпускной экзамен", "part_of_speech": "существительное"}, "przyzwyczaić": {"lemma": "przyzwyczaić się", "translation": "привыкнуть", "part_of_speech": "глагол"}, "ukończeniu": {"lemma": "ukończenie", "translation": "окончание", "part_of_speech": "существительное"}, "niewielkim": {"lemma": "niewielki", "translation": "небольшой", "part_of_speech": "прилагательное"}, "zdobyła": {"lemma": "zdobyć", "translation": "приобрести", "part_of_speech": "глагол"}, "punktem": {"lemma": "punkt zwrotny", "translation": "поворотный момент", "part_of_speech": "словосочетание"}, "mieszkańcami": {"lemma": "mieszkaniec", "translation": "житель", "part_of_speech": "существительное"}, "wpłynąć": {"lemma": "wpłynąć na", "translation": "повлиять на", "part_of_speech": "глагол"}, "przestrzeniami": {"lemma": "przestrzeń", "translation": "пространство", "part_of_speech": "существительное"}, "prowadzi": {"lemma": "prowadzić", "translation": "вести; руководить", "part_of_speech": "глагол"}, "rozwoju": {"lemma": "rozwój", "translation": "развитие", "part_of_speech": "существительное"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite": return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText")
    course, _ = Course.objects.update_or_create(id="b1-independent", defaults={"title":"Независимое общение","description":"Связная речь, опыт и мнение в знакомых ситуациях","level":"B1","position":2,"is_active":True})
    topic, _ = Topic.objects.update_or_create(id="b1-biography", defaults={"course":course,"title":"Биография и опыт","description":"Связно рассказываем о прошлом, этапах и важных решениях","emoji":"🧭","position":0,"is_active":True})
    rows = (("bio-words","words","Etapy życia","Биография","8 карточек · B1","Назови этапы, решения и достижения",9,"🧭"),("bio-grammar","grammar","Proces czy rezultat?","Вид в рассказе","6 заданий · B1","Различай фон, повторение и завершённый результат",12,"✏️"),("bio-review","review","Co mnie ukształtowało?","Опыт и перемены","7 карточек · B1","Свяжи опыт с его последствиями",8,"🔄"),("bio-quiz","quiz","Quiz: biografia","Проверка темы","10 вопросов · B1","Проверь лексику и связность рассказа",9,"🎯"),("bio-reading-check","quiz","Czy rozumiesz drogę Joanny?","Понимание текста","6 вопросов · B1","Найди этапы, причины и главный вывод",7,"📖"))
    made={}
    for position,row in enumerate(rows,108):
        id_,kind,title,plan,subtitle,description,minutes,emoji=row; made[id_],_=Lesson.objects.update_or_create(id=id_,defaults={"topic":topic,"kind":kind,"title":title,"plan_title":plan,"subtitle":subtitle,"description":description,"minutes":minutes,"emoji":emoji,"position":position,"is_active":True,"source_metadata":SOURCE})
    grammar=made["bio-grammar"]; grammar.theory_title="Как вид глагола строит рассказ о прошлом"; grammar.theory_sections=[["Фон и процесс","Несовершенный вид описывает длительность, повторение и фон: pracowała, jeździł."],["Результат","Совершенный вид выделяет завершённый этап: ukończyła, podjął, osiągnęli."],["Связная история","Najpierw, następnie, z czasem и w końcu помогают показать развитие событий."]]; grammar.save(update_fields=("theory_title","theory_sections"))
    cards=[]
    for position,(id_,polish,translation,example) in enumerate(CARDS,362): card,_=Flashcard.objects.update_or_create(id=id_,defaults={"polish":polish,"translation":translation,"example":example,"position":position,"is_active":True,"source_metadata":SOURCE}); cards.append(card)
    for lesson_id,chosen in (("bio-words",cards[:8]),("bio-review",cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position,card in enumerate(chosen): Link.objects.create(lesson_id=lesson_id,flashcard=card,position=position)
    for lesson_id,questions in (("bio-grammar",GRAMMAR),("bio-quiz",QUIZ),("bio-reading-check",CHECK)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position,(prompt,options,correct,explanation) in enumerate(questions): Question.objects.create(lesson_id=lesson_id,prompt=prompt,options=options,correct=correct,explanation=explanation,position=position)
    ReadingText.objects.update_or_create(id=READING["id"],defaults={**{k:v for k,v in READING.items() if k!="id"},"topic":topic,"source_metadata":{**SOURCE,"comprehension_lesson_id":"bio-reading-check"},"is_active":True})


class Migration(migrations.Migration):
    dependencies=[("learning","0031_a2_final_review_content")]
    operations=[migrations.RunPython(seed,migrations.RunPython.noop)]
