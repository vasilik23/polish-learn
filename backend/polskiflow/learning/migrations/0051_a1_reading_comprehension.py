from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}


SPECS = (
    ("poranek-anny","a1read-poranek",("Co Anna je na śniadanie?",["Chleb z serem","Zupę","Ryż"],0,"Она ест хлеб с сыром."),("Dokąd potem idzie?",["Do pracy","Do szkoły","Na targ"],0,"После завтрака она идёт на работу."),("Kogo spotyka po drodze?",["Sąsiada","Lekarza","Nauczyciela"],0,"По дороге она встречает соседа.")),
    ("pierwszy-dzien-na-kursie","a1read-kurs",("Gdzie jest Anna?",["Na kursie polskiego","W banku","W sklepie"],0,"Это первый день на курсе."),("Skąd pochodzi Anna?",["Z Ukrainy","Z Polski","Z Niemiec"],0,"Анна из Украины."),("Jak ma na imię nowy kolega?",["Marek","Paweł","Thomas"],0,"Нового коллегу зовут Марек.")),
    ("zakupy-na-targu","a1read-targ",("Kiedy Marek idzie na targ?",["W sobotę","W poniedziałek","W nocy"],0,"Он идёт на рынок в субботу."),("Ile kosztuje kilogram pomidorów?",["Cztery złote","Dwanaście złotych","Dwa złote"],0,"Продавец называет четыре злотых."),("Jakie jabłka wybiera?",["Czerwone","Zielone","Żółte"],0,"Он выбирает красные яблоки.")),
    ("rozmowa-w-miedzynarodowej-grupie","a1read-grupa",("Gdzie mieszka Oksana?",["W Krakowie","W Berlinie","W Warszawie"],0,"Оксана живёт в Кракове."),("Jaki jest język ojczysty Thomasa?",["Niemiecki","Polski","Ukraiński"],0,"Томас из Германии."),("Czego uczą się razem?",["Języka polskiego","Matematyki","Historii"],0,"Группа вместе учит польский.")),
    ("niedziela-u-babci","a1read-rodzina",("Kogo odwiedza Maja?",["Babcię i dziadka","Koleżankę","Lekarza"],0,"Мая навещает бабушку и дедушку."),("Kim jest mama Mai?",["Nauczycielką","Lekarką","Sprzedawczynią"],0,"Её мама работает учительницей."),("Czym interesuje się Kuba?",["Sportem","Gotowaniem","Muzyką"],0,"Куба интересуется спортом.")),
    ("zwykly-dzien-oli","a1read-dzien",("O której Ola wstaje?",["O siódmej","O szóstej","O dziewiątej"],0,"Она встаёт в семь."),("Jak wraca z pracy?",["Autobusem","Pociągiem","Rowerem"],0,"Она возвращается автобусом."),("O której kładzie się spać?",["O jedenastej","O ósmej","O północy"],0,"Она ложится в одиннадцать.")),
    ("nowe-mieszkanie-marty","a1read-mieszkanie",("Na którym piętrze mieszka Marta?",["Na drugim","Na pierwszym","Na trzecim"],0,"Квартира на втором этаже."),("Co stoi w salonie?",["Sofa, stół i krzesła","Łóżko i szafa","Biurko i komputer"],0,"Эти предметы находятся в гостиной."),("Co jest naprzeciwko sypialni?",["Łazienka","Kuchnia","Balkon"],0,"Напротив спальни ванная.")),
    ("zakupy-oli","a1read-zakupy",("Co Ola chce przygotować?",["Śniadanie","Obiad dla gości","Kolację w restauracji"],0,"Она покупает продукты на завтрак."),("Jak płaci?",["Kartą","Gotówką","Telefonem"],0,"Оля платит картой."),("Ile jabłek wybiera?",["Cztery","Dwa","Sześć"],0,"Она берёт четыре яблока.")),
    ("droga-do-muzeum","a1read-muzeum",("Skąd wychodzi Anna?",["Z dworca","Z muzeum","Z banku"],0,"Она выходит с вокзала."),("Gdzie skręca na drugim skrzyżowaniu?",["W lewo","W prawo","Nie skręca"],0,"Инструкция велит повернуть налево."),("Co jest naprzeciwko muzeum?",["Kawiarnia","Dworzec","Apteka"],0,"Напротив музея кафе.")),
    ("spotkanie-w-piatek","a1read-spotkanie",("Dlaczego czwartek nie pasuje Pawłowi?",["Ma kurs polskiego","Pracuje w nocy","Jedzie do lekarza"],0,"В четверг у него курс."),("O której się spotykają?",["O szóstej","O piątej","O siódmej"],0,"Они договорились на шесть."),("Gdzie się spotykają?",["W kawiarni obok parku","Na dworcu","W biurze"],0,"Место — кафе возле парка.")),
    ("pierwszy-dzien-w-pracy","a1read-praca",("Gdzie pracuje Kasia?",["W małej firmie","W szkole","W aptece"],0,"У Каси новая работа в небольшой фирме."),("Co pisze pierwszego dnia?",["Pierwszą wiadomość","Długą książkę","Receptę"],0,"Её первая задача — сообщение."),("Jak często uczy się polskiego?",["Dwa razy w tygodniu","Codziennie","Raz w miesiącu"],0,"Она учится дважды в неделю.")),
    ("wolna-sobota-marka","a1read-sobota",("Co Marek robi rano?",["Czyta książkę","Idzie do pracy","Gra w piłkę"],0,"Утром он читает."),("Dlaczego przyjaciele idą do kawiarni?",["Pada deszcz","Jest bardzo gorąco","Park jest zamknięty"],0,"Из-за дождя они меняют план."),("Jaki film wybierają?",["Krótką komedię","Horror","Film historyczny"],0,"Они выбирают короткую комедию.")),
    ("ola-u-lekarza","a1read-lekarz",("Jaką temperaturę ma Ola?",["Trzydzieści osiem stopni","Trzydzieści sześć","Czterdzieści"],0,"У неё 38 градусов."),("Dlaczego nie idzie do pracy?",["Źle się czuje","Ma urlop","Jedzie na kurs"],0,"Она заболела."),("Dokąd idzie po wizycie?",["Do apteki","Do banku","Do muzeum"],0,"После врача она идёт в аптеку.")),
    ("samodzielny-dzien-leny","a1read-final",("Na kiedy Lena umawia lekarza?",["Na czwartek o dziewiątej","Na piątek o szóstej","Na sobotę rano"],0,"Визит назначен на четверг в девять."),("Co kupuje w sklepie?",["Chleb, mleko i jabłka","Lekarstwo i kawę","Ser i pomidory"],0,"Это её покупки."),("O czym rozmawia z koleżanką?",["O rodzinie, pracy i weekendzie","Tylko o pogodzie","O egzaminie z matematyki"],0,"Они обсуждают семью, работу и выходные.")),
)


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite": return
    ReadingText=apps.get_model("learning","ReadingText"); Topic=apps.get_model("learning","Topic"); Lesson=apps.get_model("learning","Lesson"); Question=apps.get_model("learning","Question"); introductions=Topic.objects.get(id="introductions")
    for offset,(reading_id,prefix,*questions) in enumerate(SPECS):
        reading=ReadingText.objects.get(id=reading_id)
        lesson_topic=introductions if reading.topic_id == "first-steps" else reading.topic
        lesson,_=Lesson.objects.update_or_create(id=f"{prefix}-check",defaults={"topic":lesson_topic,"kind":"quiz","title":"Czy rozumiesz tekst?","plan_title":"Понимание текста","subtitle":"3 вопроса · A1","description":f"Проверь понимание текста «{reading.title}»","minutes":5,"emoji":"📖","position":228+offset,"is_active":True,"source_metadata":SOURCE})
        Question.objects.filter(lesson=lesson).delete()
        for position,q in enumerate(questions): Question.objects.create(lesson=lesson,prompt=q[0],options=q[1],correct=q[2],explanation=q[3],position=position)
        metadata=dict(reading.source_metadata or {}); metadata.update(SOURCE); metadata["comprehension_lesson_id"]=lesson.id; reading.source_metadata=metadata; reading.save(update_fields=("source_metadata",))


class Migration(migrations.Migration):
    dependencies=[("learning","0050_complete_b2_curriculum")]
    operations=[migrations.RunPython(seed,migrations.RunPython.noop)]
