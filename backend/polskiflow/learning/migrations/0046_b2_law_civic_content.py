from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}

SPEC = {
    "id": "b2-law-civic", "title": "Право и гражданские вопросы",
    "description": "Понимаем правила, проверяем процедуру и формулируем официальное обращение", "emoji": "⚖️", "position": 5,
    "prefix": "b2law", "lesson_start": 193, "card_start": 617,
    "theory": ("Официальное обращение и сложное управление", [
        ["Цель письма", "Zwracam się z prośbą o… и wnoszę o… называют просьбу или требование нейтрально и точно."],
        ["Управление", "Odwołać się od decyzji, ubiegać się o świadczenie и zobowiązać kogoś do działania требуют фиксированных предлогов и падежей."],
        ["Основание", "Zgodnie z, na podstawie и w związku z связывают обращение с правилом, документом или обстоятельством."],
    ]),
    "cards": (
        ("przepis", "правовая норма, положение", "Przepis określa termin złożenia wniosku."),
        ("uprawnienie", "право, полномочие", "Mieszkańcowi przysługuje takie uprawnienie."),
        ("obowiązek", "обязанность", "Urząd ma obowiązek udzielić odpowiedzi."),
        ("wniosek", "заявление, ходатайство", "Wniosek można złożyć elektronicznie."),
        ("załącznik", "приложение к документу", "Do pisma dołączono wymagany załącznik."),
        ("termin", "срок", "Termin upływa trzydziestego września."),
        ("decyzja administracyjna", "административное решение", "Decyzja administracyjna zawiera uzasadnienie."),
        ("uzasadnienie", "обоснование", "W uzasadnieniu wskazano podstawę prawną."),
        ("zwrócić się z prośbą", "обратиться с просьбой", "Zwracam się z prośbą o wyjaśnienie sprawy."),
        ("wnieść odwołanie", "подать апелляцию", "Strona może wnieść odwołanie w ciągu czternastu dni."),
        ("odwołać się od", "обжаловать", "Mieszkaniec odwołał się od decyzji."),
        ("ubiegać się o", "ходатайствовать, претендовать на", "Rodzina ubiega się o świadczenie."),
        ("zgodnie z", "в соответствии с", "Zgodnie z regulaminem potrzebny jest podpis."),
        ("na podstawie", "на основании", "Urząd działa na podstawie ustawy."),
        ("rozpatrzyć sprawę", "рассмотреть дело", "Proszę o ponowne rozpatrzenie sprawy."),
    ),
    "grammar": (
        ("Zwracam się z prośbą ___ przesłanie kopii decyzji.", ["o", "od", "do"], 0, "Prośba o + винительный называет предмет просьбы."),
        ("Wnioskodawca odwołał się ___ decyzji urzędu.", ["od", "o", "z"], 0, "Odwołać się od требует родительного падежа."),
        ("Rodzina ubiega się ___ świadczenie mieszkaniowe.", ["o", "na", "do"], 0, "Ubiegamy się o что-либо — устойчивое управление."),
        ("___ z regulaminem odpowiedź powinna zostać wysłana w ciągu 30 dni.", ["Zgodnie", "Zgodny", "Zgodność"], 0, "Официальная связка zgodnie z вводит основание правила."),
        ("Составьте: Прошу повторно рассмотреть дело на основании приложенных документов.", ["Proszę o ponowne rozpatrzenie sprawy na podstawie załączonych dokumentów.", "Proszę ponownie sprawę rozpatrzyć na podstawa załączniki.", "Wnoszę od dokumentów dla sprawa ponowna."], 0, "Proszę o требует отглагольного существительного, na podstawie — родительного."),
        ("Составьте: В связи с отсутствием ответа я подаю жалобу на бездействие органа.", ["W związku z brakiem odpowiedzi składam skargę na bezczynność organu.", "W związku brak odpowiedź skargę od organ składa.", "Bez odpowiedzi organu odwołuję skargą do bezczynność."], 0, "W związku z требует творительного, skarga na — винительного."),
    ),
    "quiz": (
        ("Co należy dołączyć do pisma, jeśli wymaga tego procedura?", ["załącznik", "ustną obietnicę", "reklamę"], 0, "Załącznik — документ, приложенный к обращению."),
        ("Od decyzji można się ___.", ["odwołać", "ubiegać", "załączać o"], 0, "Нормативное сочетание — odwołać się od decyzji."),
        ("Która forma jest odpowiednia w oficjalnym piśmie?", ["Zwracam się z prośbą o wyjaśnienie.", "Hej, ogarnijcie to.", "No i co z tym?"], 0, "Первая формула нейтральна, точна и вежлива."),
        ("Urząd działa ___ ustawy.", ["na podstawie", "na podstawę", "podstawą od"], 0, "Na podstawie + родительный вводит правовое основание."),
        ("Co zawiera uzasadnienie decyzji?", ["powody i podstawę rozstrzygnięcia", "wyłącznie adres urzędu", "reklamę usługi"], 0, "Обоснование объясняет фактические и правовые причины."),
        ("Ubiegam się ___ wydanie zaświadczenia.", ["o", "od", "w"], 0, "Ubiegam się o + винительный."),
        ("Termin upływa, czyli ___.", ["kończy się czas na wykonanie czynności", "sprawa jest zawsze wygrana", "przepis znika"], 0, "Upływ terminu означает окончание установленного срока."),
        ("Co pomaga skutecznie sformułować wniosek?", ["konkretne żądanie, podstawa i załączniki", "emocjonalne oskarżenia", "brak danych kontaktowych"], 0, "Структурированное обращение позволяет органу проверить требование."),
        ("W związku ___ zmianą adresu proszę o aktualizację danych.", ["ze", "od", "dla"], 0, "Перед сочетанием согласных употребляется w związku ze + творительный."),
        ("Kto rozpatruje sprawę?", ["właściwy organ lub instytucja", "dowolny sklep", "wyłącznie sąsiad"], 0, "Дело рассматривает компетентный орган."),
    ),
    "reading": {
        "id": "b2law-odwolanie-od-decyzji", "title": "Odwołanie, które można było rozpatrzyć",
        "description": "Как жительница проверила срок, основание и структуру официального обращения", "emoji": "⚖️", "minutes": 12,
        "paragraphs": [
            "Marta złożyła wniosek o świadczenie mieszkaniowe, lecz po miesiącu otrzymała decyzję odmowną. Dokument zawierał pouczenie, że może wnieść odwołanie w ciągu czternastu dni od doręczenia. Kobieta najpierw sprawdziła datę odbioru, ponieważ przekroczenie terminu mogłoby utrudnić dalsze postępowanie.",
            "W uzasadnieniu urząd wskazał brak jednego załącznika potwierdzającego dochód. Marta miała jednak elektroniczne potwierdzenie, że dokument został przesłany razem z wnioskiem. Zgodnie z regulaminem platformy takie potwierdzenie stanowi dowód złożenia pliku, dlatego postanowiła odwołać się od decyzji.",
            "Pismo rozpoczęła od danych swoich i właściwego organu. Następnie napisała: „Wnoszę o ponowne rozpatrzenie sprawy oraz zmianę decyzji”. W związku z rozbieżnością między uzasadnieniem a potwierdzeniem wysyłki opisała kolejność zdarzeń, podała numer sprawy i powołała się na załączony dowód. Unikała ocen pracownika, bo celem było wyjaśnienie faktów.",
            "Do odwołania ponownie dołączyła dokument o dochodzie, kopię decyzji i potwierdzenie wysyłki. Urząd miał obowiązek przekazać pismo do właściwej jednostki albo samodzielnie zmienić rozstrzygnięcie. Po dziesięciu dniach Marta otrzymała informację, że jej uprawnienie do świadczenia zostanie ponownie ocenione.",
            "Ta sytuacja pokazuje, że oficjalny styl nie musi być skomplikowany. Skuteczne pismo jasno określa żądanie, wskazuje podstawę, porządkuje fakty i wymienia załączniki. Przed wysłaniem warto też sprawdzić właściwość organu, termin oraz sposób doręczenia. Dzięki temu instytucja może rozpatrzyć sprawę, zamiast prosić o uzupełnienie podstawowych danych.",
        ],
        "glossary": {
            "świadczenie": ("świadczenie", "пособие, выплата", "существительное"), "odmowną": ("odmowny", "отказную", "прилагательное"),
            "pouczenie": ("pouczenie", "разъяснение порядка обжалования", "существительное"), "wnieść odwołanie": ("wnieść odwołanie", "подать апелляцию", "устойчивое выражение"),
            "doręczenia": ("doręczenie", "вручения", "существительное"), "przekroczenie": ("przekroczenie", "пропуск, превышение", "существительное"),
            "postępowanie": ("postępowanie", "производство, процедура", "существительное"), "uzasadnieniu": ("uzasadnienie", "обосновании", "существительное"),
            "załącznika": ("załącznik", "приложения", "существительное"), "stanowi": ("stanowić", "представляет собой", "глагол"),
            "rozbieżnością": ("rozbieżność", "расхождением", "существительное"), "powołała się": ("powołać się", "сослалась", "глагол"),
            "kolejność zdarzeń": ("kolejność zdarzeń", "последовательность событий", "словосочетание"), "rozstrzygnięcie": ("rozstrzygnięcie", "решение по существу", "существительное"),
            "uprawnienie": ("uprawnienie", "право", "существительное"), "żądanie": ("żądanie", "требование", "существительное"),
            "właściwość organu": ("właściwość organu", "компетенция органа", "словосочетание"), "doręczenia": ("doręczenie", "вручения", "существительное"),
            "uzupełnienie": ("uzupełnienie", "дополнение", "существительное"), "obowiązek": ("obowiązek", "обязанность", "существительное"),
        },
        "check": (
            ("Ile dni miała Marta na odwołanie?", ["Czternaście", "Trzydzieści", "Dziesięć"], 0, "Срок в разъяснении составлял 14 дней."),
            ("Dlaczego decyzja była odmowna?", ["Urząd uznał, że brakowało załącznika", "Marta przekroczyła termin wniosku", "Nie podała adresu"], 0, "В обосновании указали отсутствие документа о доходе."),
            ("Jaki dowód miała Marta?", ["Elektroniczne potwierdzenie wysłania pliku", "Nagranie rozmowy sąsiada", "Paragon ze sklepu"], 0, "Платформа сохранила подтверждение отправки."),
            ("Czego zażądała w odwołaniu?", ["Ponownego rozpatrzenia i zmiany decyzji", "Zmiany pracownika", "Usunięcia regulaminu"], 0, "Просьба сформулирована прямо в третьем абзаце."),
            ("Dlaczego unikała ocen pracownika?", ["Chciała skupić pismo na faktach", "Nie znała numeru sprawy", "Nie mogła dodać załączników"], 0, "Официальное письмо должно помогать проверить факты."),
            ("Co warto sprawdzić przed wysłaniem pisma?", ["Organ, termin i sposób doręczenia", "Tylko kolor dokumentu", "Popularność instytucji"], 0, "Эти три элемента перечислены в выводе."),
        ),
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite": return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic"); Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question"); ReadingText = apps.get_model("learning", "ReadingText")
    s=SPEC; course=Course.objects.get(id="b2-advanced"); topic,_=Topic.objects.update_or_create(id=s["id"],defaults={"course":course,"title":s["title"],"description":s["description"],"emoji":s["emoji"],"position":s["position"],"is_active":True})
    p=s["prefix"]; rows=((f"{p}-words","words","Słowa w kontekście","Новая лексика","8 карточек · B2",s["description"],10,s["emoji"]),(f"{p}-grammar","grammar","Jak to wyrazić?","Языковой фокус","6 заданий · B2",s["theory"][0],13,"✏️"),(f"{p}-review","review","Powtórka aktywna","Активное повторение","7 карточек · B2","Закрепи лексику темы",9,"🔄"),(f"{p}-quiz","quiz",f"Quiz: {s['title']}","Проверка темы","10 вопросов · B2","Проверь лексику и официальный регистр",10,"🎯"),(f"{p}-reading-check","quiz","Czy rozumiesz tekst?","Понимание текста","6 вопросов · B2","Найди процедуру, основание и вывод",8,"📖"))
    lessons={}
    for position,row in enumerate(rows,s["lesson_start"]):
        id_,kind,title,plan,subtitle,description,minutes,emoji=row; lessons[id_],_=Lesson.objects.update_or_create(id=id_,defaults={"topic":topic,"kind":kind,"title":title,"plan_title":plan,"subtitle":subtitle,"description":description,"minutes":minutes,"emoji":emoji,"position":position,"is_active":True,"source_metadata":SOURCE})
    grammar=lessons[f"{p}-grammar"]; grammar.theory_title,grammar.theory_sections=s["theory"]; grammar.save(update_fields=("theory_title","theory_sections")); cards=[]
    for offset,(polish,translation,example) in enumerate(s["cards"]):
        card,_=Flashcard.objects.update_or_create(id=f"{p}-{offset+1}",defaults={"polish":polish,"translation":translation,"example":example,"position":s["card_start"]+offset,"is_active":True,"source_metadata":SOURCE}); cards.append(card)
    for lesson_id,selected in ((f"{p}-words",cards[:8]),(f"{p}-review",cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position,card in enumerate(selected): Link.objects.create(lesson_id=lesson_id,flashcard=card,position=position)
    for lesson_id,questions in ((f"{p}-grammar",s["grammar"]),(f"{p}-quiz",s["quiz"]),(f"{p}-reading-check",s["reading"]["check"])):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position,q in enumerate(questions): Question.objects.create(lesson_id=lesson_id,prompt=q[0],options=q[1],correct=q[2],explanation=q[3],position=position)
    r=s["reading"]; glossary={surface:{"lemma":e[0],"translation":e[1],"part_of_speech":e[2]} for surface,e in r["glossary"].items()}; ReadingText.objects.update_or_create(id=r["id"],defaults={"topic":topic,"title":r["title"],"description":r["description"],"level":"B2","minutes":r["minutes"],"emoji":r["emoji"],"position":41,"paragraphs":r["paragraphs"],"glossary":glossary,"source_metadata":{**SOURCE,"comprehension_lesson_id":f"{p}-reading-check"},"is_active":True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0045_b2_economy_consumption_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
