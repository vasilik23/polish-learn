from django.db import migrations

SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-27"}
CARDS = (
    ("mieszkanie", "mieszkanie", "квартира", "Moje mieszkanie jest małe, ale jasne."),
    ("dom", "dom", "дом", "Mieszkamy w domu pod Warszawą."),
    ("pokoj", "pokój", "комната", "W pokoju jest duże okno."),
    ("kuchnia", "kuchnia", "кухня", "W kuchni gotujemy obiad."),
    ("lazienka", "łazienka", "ванная", "Łazienka jest obok sypialni."),
    ("sypialnia", "sypialnia", "спальня", "W sypialni stoi łóżko."),
    ("salon", "salon", "гостиная", "W salonie odpoczywamy razem."),
    ("balkon", "balkon", "балкон", "Na balkonie są kwiaty."),
    ("stol", "stół", "стол", "Na stole jest lampa."),
    ("krzeslo", "krzesło", "стул", "Krzesło stoi przy stole."),
    ("lozko", "łóżko", "кровать", "Kot śpi na łóżku."),
    ("szafa", "szafa", "шкаф", "Ubrania są w szafie."),
    ("okno", "okno", "окно", "Przy oknie stoi biurko."),
    ("drzwi", "drzwi", "дверь", "Drzwi do kuchni są otwarte."),
    ("gdzie", "gdzie?", "где?", "Gdzie jest klucz?"),
)
GRAMMAR = (
    ("___ kuchni jest stół.", ["W", "Na", "Do"], 0, "Для положения внутри кухни используем w: w kuchni."),
    ("Książka leży ___ stole.", ["w", "na", "do"], 1, "На поверхности — na + miejscownik: na stole."),
    ("W salonie ___ sofa.", ["jest", "są", "mam"], 0, "С одним предметом употребляется jest."),
    ("W sypialni ___ dwa okna.", ["jest", "są", "to"], 1, "С несколькими предметами употребляется są."),
    ("Как спросить «Где ванная?»", ["Gdzie jest łazienka?", "Co łazienka jest?", "Dokąd łazienkę?"], 0, "О местонахождении спрашиваем Gdzie jest…?"),
)
QUIZ = (
    ("Где обычно готовят?", ["w kuchni", "w sypialni", "na balkonie"], 0, "Kuchnia — кухня."),
    ("Выберите «на балконе».", ["w balkonu", "na balkonie", "do balkon"], 1, "Устойчиво: na balkonie."),
    ("W pokoju ___ trzy krzesła.", ["jest", "są", "ma"], 1, "Три стула — множественное число, поэтому są."),
    ("Что означает szafa?", ["шкаф", "стол", "окно"], 0, "Szafa — шкаф."),
    ("Ubrania są ___ szafie.", ["w", "na", "z"], 0, "Одежда находится внутри шкафа: w szafie."),
    ("Выберите правильное описание.", ["Na stole jest lampa.", "W stole są lampa.", "Do stół jest lampa."], 0, "Предмет на поверхности: na stole."),
    ("Как спросить о ключе?", ["Gdzie jest klucz?", "Jaki jest gdzie klucz?", "Czy gdzie klucza?"], 0, "Gdzie jest…? — где находится…?"),
    ("Где спят?", ["w sypialni", "w kuchni", "na stole"], 0, "Sypialnia — спальня."),
)
READING = {
    "id": "nowe-mieszkanie-marty", "title": "Nowe mieszkanie Marty", "description": "Марта показывает друзьям новую квартиру", "level": "A1", "minutes": 4, "emoji": "🏠", "position": 4,
    "paragraphs": [
        "Marta mieszka teraz w nowym mieszkaniu. Mieszkanie jest na drugim piętrze i ma trzy pokoje. Przy wejściu jest mały przedpokój, a obok niego jasna kuchnia.",
        "W salonie stoją sofa, stół i cztery krzesła. Na stole leżą książki. Przy oknie jest zielona roślina. Z salonu można wyjść na balkon.",
        "Sypialnia Marty jest spokojna. W sypialni stoi łóżko i duża szafa. Naprzeciwko jest łazienka. Marta lubi swoje mieszkanie, bo wszystko ma tutaj swoje miejsce.",
    ],
    "glossary": {
        "nowym": {"lemma": "nowy", "translation": "новый", "part_of_speech": "прилагательное"},
        "piętrze": {"lemma": "piętro", "translation": "этаж", "part_of_speech": "существительное"},
        "wejściu": {"lemma": "wejście", "translation": "вход", "part_of_speech": "существительное"},
        "przedpokój": {"lemma": "przedpokój", "translation": "прихожая", "part_of_speech": "существительное"},
        "stoją": {"lemma": "stać", "translation": "стоять", "part_of_speech": "глагол"},
        "leżą": {"lemma": "leżeć", "translation": "лежать", "part_of_speech": "глагол"},
        "roślina": {"lemma": "roślina", "translation": "растение", "part_of_speech": "существительное"},
        "wyjść": {"lemma": "wyjść", "translation": "выйти", "part_of_speech": "глагол"},
        "spokojna": {"lemma": "spokojny", "translation": "спокойный", "part_of_speech": "прилагательное"},
        "naprzeciwko": {"lemma": "naprzeciwko", "translation": "напротив", "part_of_speech": "наречие"},
        "wszystko": {"lemma": "wszystko", "translation": "всё", "part_of_speech": "местоимение"},
        "miejsce": {"lemma": "miejsce", "translation": "место", "part_of_speech": "существительное"},
    },
}

def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite": return
    Course=apps.get_model("learning","Course"); Topic=apps.get_model("learning","Topic"); Lesson=apps.get_model("learning","Lesson")
    Flashcard=apps.get_model("learning","Flashcard"); Link=apps.get_model("learning","LessonFlashcard"); Question=apps.get_model("learning","Question"); ReadingText=apps.get_model("learning","ReadingText")
    course=Course.objects.get(id="a1-foundations")
    Topic.objects.filter(course=course,position__gte=4).update(position=5)
    topic,_=Topic.objects.update_or_create(id="home",defaults={"course":course,"title":"Дом","description":"Называем комнаты и описываем расположение предметов","emoji":"🏠","position":4,"is_active":True})
    rows=(("home-words","words","Mój dom","Комнаты и дом","8 карточек · A1","Назови помещения в доме",7,"🏠"),("home-grammar","grammar","Gdzie to jest?","Где находится?","5 заданий · A1","Используй jest/są и w/na",8,"✏️"),("home-review","review","W pokoju","Мебель и предметы","7 карточек · A1","Закрепи предметы и их расположение",6,"🔄"),("home-quiz","quiz","Quiz: dom","Проверка темы","8 вопросов · A1","Проверь комнаты, мебель и местонахождение",5,"🎯"))
    made={}
    for position,row in enumerate(rows,16):
        id_,kind,title,plan,subtitle,desc,minutes,emoji=row
        made[id_],_=Lesson.objects.update_or_create(id=id_,defaults={"topic":topic,"kind":kind,"title":title,"plan_title":plan,"subtitle":subtitle,"description":desc,"minutes":minutes,"emoji":emoji,"position":position,"is_active":True,"source_metadata":SOURCE})
    grammar=made["home-grammar"]; grammar.theory_title="Gdzie? — w domu, na stole"
    grammar.theory_sections=[["Jest или są","Jest użyваем с одним предметом: W pokoju jest stół. Są — с несколькими: W pokoju są krzesła."],["Внутри: w","На вопрос gdzie? говорим: w domu, w pokoju, w kuchni, w łazience, w szafie."],["На поверхности: na","Na stole, na łóżku, na balkonie. После w/na форма существительного меняется."]]; grammar.save(update_fields=("theory_title","theory_sections"))
    cards=[]
    for position,(id_,polish,translation,example) in enumerate(CARDS):
        card,_=Flashcard.objects.update_or_create(id=id_,defaults={"polish":polish,"translation":translation,"example":example,"position":60+position,"is_active":True,"source_metadata":SOURCE}); cards.append(card)
    for lesson_id,chosen in (("home-words",cards[:8]),("home-review",cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position,card in enumerate(chosen): Link.objects.create(lesson_id=lesson_id,flashcard=card,position=position)
    for lesson_id,questions in (("home-grammar",GRAMMAR),("home-quiz",QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position,(prompt,options,correct,explanation) in enumerate(questions): Question.objects.create(lesson_id=lesson_id,prompt=prompt,options=options,correct=correct,explanation=explanation,position=position)
    ReadingText.objects.update_or_create(id=READING["id"],defaults={**{k:v for k,v in READING.items() if k!="id"},"topic":topic,"source_metadata":SOURCE})

class Migration(migrations.Migration):
    dependencies=[("learning","0009_a1_daily_routine_content")]
    operations=[migrations.RunPython(seed,migrations.RunPython.noop)]
