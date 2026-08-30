from django.db import migrations


SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-30"}

SPEC = {
    "id": "b2-economy-consumption", "title": "Экономика и потребление",
    "description": "Интерпретируем тенденции, сравниваем данные и принимаем взвешенное решение", "emoji": "📊", "position": 4,
    "prefix": "b2economy", "lesson_start": 188, "card_start": 602,
    "theory": ("Данные, сравнение и степень вероятности", [
        ["Тенденция", "Конструкции wzrosło o / spadło z… do… точно различают изменение на величину и диапазон изменения."],
        ["Сравнение", "Ponad dwa razy więcej, nieco mniej niż и w porównaniu z помогают сопоставлять показатели без потери масштаба."],
        ["Вероятность", "Prawdopodobnie, możliwe, że и istnieje ryzyko, że отделяют прогноз от подтверждённого факта."],
    ]),
    "cards": (
        ("wzrost", "рост", "Wzrost cen był wolniejszy niż rok temu."),
        ("spadek", "снижение", "Firma odnotowała spadek sprzedaży."),
        ("wydatki", "расходы", "Gospodarstwa ograniczyły wydatki na energię."),
        ("dochód", "доход", "Średni dochód wzrósł o sześć procent."),
        ("popyt", "спрос", "Popyt na lokalne produkty nadal rośnie."),
        ("podaż", "предложение", "Mała podaż podniosła ceny mieszkań."),
        ("udział", "доля", "Udział zakupów internetowych wyniósł jedną trzecią."),
        ("tendencja", "тенденция", "Dane potwierdzają długoterminową tendencję."),
        ("opłacalny", "выгодный", "Tańsza oferta nie zawsze jest najbardziej opłacalna."),
        ("siła nabywcza", "покупательная способность", "Inflacja osłabiła siłę nabywczą rodzin."),
        ("porównać dane", "сопоставить данные", "Przed decyzją warto porównać dane z dwóch lat."),
        ("wahać się", "колебаться", "Cena paliwa wahała się przez cały miesiąc."),
        ("prognoza", "прогноз", "Prognoza zakłada stopniową poprawę."),
        ("prawdopodobnie", "вероятно", "Popyt prawdopodobnie pozostanie stabilny."),
        ("podjąć decyzję", "принять решение", "Klienci podjęli decyzję po analizie kosztów."),
    ),
    "grammar": (
        ("Sprzedaż wzrosła ___ dwanaście procent.", ["o", "z", "na"], 0, "Wzrosła o отвечает на вопрос, на сколько изменился показатель."),
        ("Udział zakupów online zwiększył się ___ 28% do 35%.", ["z", "o", "przez"], 0, "Z… do… показывает начальное и конечное значение."),
        ("W tym roku wydatki były nieco mniejsze ___ rok wcześniej.", ["niż", "od", "jak"], 0, "Сравнительная степень с конкретным показателем соединяется через niż."),
        ("Według prognozy ceny ___ ustabilizują się jesienią.", ["prawdopodobnie", "na pewno już", "bez wątpienia wczoraj"], 0, "Prawdopodobnie маркирует прогноз, а не установленный факт."),
        ("Составьте: Спрос вырос на 8%, но предложение почти не изменилось.", ["Popyt wzrósł o 8%, ale podaż prawie się nie zmieniła.", "Popyt wzrósł z 8%, lecz podaż zmienił się prawie.", "Podaż o popyt osiem wzrosła bez zmiany."], 0, "Изменение на величину выражается wzrósł o, а podaż требует формы zmieniła."),
        ("Составьте: Вероятно, этот вариант будет выгоднее по сравнению с предыдущим.", ["Prawdopodobnie ten wariant będzie bardziej opłacalny w porównaniu z poprzednim.", "Ten wariant na pewno opłacalny od poprzedni prawdopodobieństwo.", "W porównaniu poprzednim wariant będzie opłacalność."], 0, "Прогноз вводит prawdopodobnie, сравнение — w porównaniu z + творительный."),
    ),
    "quiz": (
        ("Co oznacza siła nabywcza?", ["ilość dóbr, które można kupić za dochód", "liczbę sklepów", "wysokość podaży jednego produktu"], 0, "Покупательная способность показывает, сколько благ позволяет приобрести доход."),
        ("Ceny spadły z 120 do 108 zł. O ile procent w przybliżeniu?", ["o 10%", "o 12%", "do 10%"], 0, "Разница 12 от исходных 120 составляет 10%."),
        ("Które słowo nazywa zapotrzebowanie klientów?", ["popyt", "podaż", "udział"], 0, "Popyt — спрос покупателей; podaż — предложение продавцов."),
        ("Dochód wzrósł ___ 5%.", ["o", "z", "do"], 0, "O 5% обозначает величину роста."),
        ("Co sygnalizuje ostrożny wniosek?", ["Możliwe, że tendencja się utrzyma.", "Tendencja na pewno trwa od zawsze.", "Nie trzeba sprawdzać danych."], 0, "Możliwe, że отмечает возможность, а не уверенность."),
        ("Który wariant jest najbardziej opłacalny?", ["Ten o najniższym łącznym koszcie i odpowiedniej jakości", "Zawsze ten z najniższą ceną początkową", "Ten bez warunków umowy"], 0, "Выгодность учитывает все расходы и качество, не только ценник."),
        ("Udział wzrósł z 20% do 30%, czyli o ___.", ["10 punktów procentowych", "10 procent wartości", "50 punktów"], 0, "Разница долей равна 10 процентным пунктам."),
        ("Dane wahały się, czyli ___.", ["zmieniały się w górę i w dół", "stale rosły", "pozostały identyczne"], 0, "Wahać się — колебаться между значениями."),
        ("Co należy zrobić przed decyzją konsumencką?", ["porównać całkowite koszty i warunki", "opierać się wyłącznie na reklamie", "pominąć ryzyko"], 0, "Сопоставление условий делает решение обоснованным."),
        ("Które zdanie opisuje prognozę?", ["Popyt prawdopodobnie wzrośnie w kolejnym kwartale.", "Popyt wzrósł wczoraj o 4%.", "Raport podaje wynik za maj."], 0, "Будущее и маркер вероятности создают прогноз."),
    ),
    "reading": {
        "id": "b2economy-subskrypcja-czy-zakup", "title": "Subskrypcja czy zakup? Decyzja oparta na danych",
        "description": "Как числа, скрытые расходы и степень уверенности меняют потребительский выбор", "emoji": "📊", "minutes": 12,
        "paragraphs": [
            "Coraz więcej osób korzysta ze sprzętu domowego w modelu subskrypcyjnym zamiast kupować go na własność. Z raportu miejskiego rzecznika konsumentów wynika, że udział takich umów wzrósł w ciągu dwóch lat z 9% do 14%. To wzrost o pięć punktów procentowych, a nie o pięć procent. Popyt zwiększył się przede wszystkim wśród osób, które często zmieniają miejsce zamieszkania.",
            "Miesięczna opłata wydaje się niska, jednak o opłacalności decyduje łączny koszt. Przy umowie na trzy lata klient może zapłacić ponad dwa razy więcej niż wynosi cena urządzenia. Z drugiej strony abonament obejmuje naprawy, a więc zmniejsza ryzyko nieprzewidzianych wydatków. Korzyść zależy zatem od czasu użytkowania i warunków serwisu.",
            "Analitycy porównali trzy oferty pralek. Cena zakupu wahała się od 1800 do 2400 złotych, natomiast suma opłat abonamentowych wynosiła od 2100 zł po dwóch latach do 3900 zł po czterech. Dochody badanych gospodarstw były podobne, lecz ich priorytety się różniły: jedni cenili przewidywalne wydatki, inni chcieli zachować pełną własność.",
            "Prognoza zakłada, że podaż usług subskrypcyjnych prawdopodobnie wzrośnie, ponieważ firmy szukają stałych przychodów. Nie oznacza to jednak, że taki model zawsze będzie korzystny. Istnieje ryzyko podwyżki opłat, kary za wcześniejsze rozwiązanie umowy oraz ograniczonego wyboru serwisu.",
            "Rozsądna decyzja wymaga więc porównania danych, całkowitego kosztu i własnych potrzeb. Konsument powinien odróżnić potwierdzony wynik od przewidywania, sprawdzić okres umowy i policzyć kilka scenariuszy. Dopiero wtedy niska rata może zostać oceniona jako rzeczywista oszczędność, a nie tylko atrakcyjny komunikat reklamowy.",
        ],
        "glossary": {
            "subskrypcyjnym": ("subskrypcyjny", "подписочный", "прилагательное"), "na własność": ("na własność", "в собственность", "устойчивое выражение"),
            "udział": ("udział", "доля", "существительное"), "rzecznika": ("rzecznik", "уполномоченный, представитель", "существительное"),
            "punktów procentowych": ("punkt procentowy", "процентных пунктов", "словосочетание"), "łączny": ("łączny", "совокупный", "прилагательное"),
            "opłacalności": ("opłacalność", "выгодность", "существительное"), "abonament": ("abonament", "абонентская плата", "существительное"),
            "nieprzewidzianych": ("nieprzewidziany", "непредвиденных", "прилагательное"), "użytkowania": ("użytkowanie", "использование", "существительное"),
            "wahała się": ("wahać się", "колебалась", "глагол"), "przewidywalne": ("przewidywalny", "предсказуемые", "прилагательное"),
            "podaż": ("podaż", "предложение", "существительное"), "przychodów": ("przychód", "выручка, доход", "существительное"),
            "podwyżki": ("podwyżka", "повышение", "существительное"), "rozwiązanie umowy": ("rozwiązanie umowy", "расторжение договора", "словосочетание"),
            "scenariuszy": ("scenariusz", "сценариев", "существительное"), "rata": ("rata", "платёж, взнос", "существительное"),
            "oszczędność": ("oszczędność", "экономия", "существительное"), "przewidywania": ("przewidywanie", "прогноз, предположение", "существительное"),
        },
        "check": (
            ("O ile punktów procentowych wzrósł udział subskrypcji?", ["O pięć", "O czternaście", "O dziewięć"], 0, "Доля изменилась с 9% до 14%, то есть на 5 п.п."),
            ("Co obejmuje abonament poza urządzeniem?", ["Naprawy", "Zakup mieszkania", "Dowolną wymianę bez warunków"], 0, "В тексте прямо упомянут включённый ремонт."),
            ("Ile może wynieść suma opłat po czterech latach?", ["3900 zł", "1800 zł", "2100 zł"], 0, "Максимальная указанная сумма — 3900 zł."),
            ("Dlaczego firmy rozwijają subskrypcje?", ["Szukają stałych przychodów", "Maleje cała podaż", "Zakazano sprzedaży"], 0, "Регулярная выручка названа причиной прогноза."),
            ("Jakie ryzyko wskazuje tekst?", ["Podwyżkę opłat lub karę za wcześniejsze rozwiązanie", "Brak jakichkolwiek kosztów", "Gwarantowany spadek cen"], 0, "Оба риска перечислены в четвёртом абзаце."),
            ("Co jest podstawą rozsądnej decyzji?", ["Porównanie pełnych kosztów, warunków i potrzeb", "Tylko wysokość raty", "Slogan reklamowy"], 0, "Финальный вывод требует анализа нескольких факторов."),
        ),
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite": return
    Course, Topic = apps.get_model("learning", "Course"), apps.get_model("learning", "Topic")
    Lesson, Flashcard = apps.get_model("learning", "Lesson"), apps.get_model("learning", "Flashcard")
    Link, Question = apps.get_model("learning", "LessonFlashcard"), apps.get_model("learning", "Question")
    ReadingText = apps.get_model("learning", "ReadingText"); s = SPEC; course = Course.objects.get(id="b2-advanced")
    topic, _ = Topic.objects.update_or_create(id=s["id"], defaults={"course": course, "title": s["title"], "description": s["description"], "emoji": s["emoji"], "position": s["position"], "is_active": True})
    p=s["prefix"]; rows=((f"{p}-words","words","Słowa w kontekście","Новая лексика","8 карточек · B2",s["description"],10,s["emoji"]),(f"{p}-grammar","grammar","Jak to wyrazić?","Языковой фокус","6 заданий · B2",s["theory"][0],13,"✏️"),(f"{p}-review","review","Powtórka aktywna","Активное повторение","7 карточек · B2","Закрепи лексику темы",9,"🔄"),(f"{p}-quiz","quiz",f"Quiz: {s['title']}","Проверка темы","10 вопросов · B2","Проверь лексику и языковой фокус",10,"🎯"),(f"{p}-reading-check","quiz","Czy rozumiesz tekst?","Понимание текста","6 вопросов · B2","Найди данные, риски и вывод",8,"📖"))
    lessons={}
    for position,row in enumerate(rows,s["lesson_start"]):
        id_,kind,title,plan,subtitle,description,minutes,emoji=row; lessons[id_],_=Lesson.objects.update_or_create(id=id_,defaults={"topic":topic,"kind":kind,"title":title,"plan_title":plan,"subtitle":subtitle,"description":description,"minutes":minutes,"emoji":emoji,"position":position,"is_active":True,"source_metadata":SOURCE})
    grammar=lessons[f"{p}-grammar"]; grammar.theory_title,grammar.theory_sections=s["theory"]; grammar.save(update_fields=("theory_title","theory_sections"))
    cards=[]
    for offset,(polish,translation,example) in enumerate(s["cards"]):
        card,_=Flashcard.objects.update_or_create(id=f"{p}-{offset+1}",defaults={"polish":polish,"translation":translation,"example":example,"position":s["card_start"]+offset,"is_active":True,"source_metadata":SOURCE}); cards.append(card)
    for lesson_id,selected in ((f"{p}-words",cards[:8]),(f"{p}-review",cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position,card in enumerate(selected): Link.objects.create(lesson_id=lesson_id,flashcard=card,position=position)
    for lesson_id,questions in ((f"{p}-grammar",s["grammar"]),(f"{p}-quiz",s["quiz"]),(f"{p}-reading-check",s["reading"]["check"])):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position,q in enumerate(questions): Question.objects.create(lesson_id=lesson_id,prompt=q[0],options=q[1],correct=q[2],explanation=q[3],position=position)
    r=s["reading"]; glossary={surface:{"lemma":e[0],"translation":e[1],"part_of_speech":e[2]} for surface,e in r["glossary"].items()}
    ReadingText.objects.update_or_create(id=r["id"],defaults={"topic":topic,"title":r["title"],"description":r["description"],"level":"B2","minutes":r["minutes"],"emoji":r["emoji"],"position":40,"paragraphs":r["paragraphs"],"glossary":glossary,"source_metadata":{**SOURCE,"comprehension_lesson_id":f"{p}-reading-check"},"is_active":True})


class Migration(migrations.Migration):
    dependencies = [("learning", "0044_b2_science_technology_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
