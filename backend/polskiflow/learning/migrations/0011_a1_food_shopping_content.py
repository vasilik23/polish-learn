from django.db import migrations

SOURCE = {"origin": "original", "created_for": "PolskiFlow", "verified_at": "2026-08-27"}
CARDS = (
    ("jedzenie", "jedzenie", "еда", "Kupuję jedzenie na kolację."),
    ("chleb", "chleb", "хлеб", "Proszę jeden chleb."),
    ("bulka", "bułka", "булочка", "Kupuję świeżą bułkę."),
    ("mleko", "mleko", "молоко", "Proszę litr mleka."),
    ("woda", "woda", "вода", "Piję wodę mineralną."),
    ("kawa", "kawa", "кофе", "Poproszę kawę bez cukru."),
    ("ser", "ser", "сыр", "Czy macie żółty ser?"),
    ("jablko", "jabłko", "яблоко", "Biorę dwa jabłka."),
    ("warzywa", "warzywa", "овощи", "Kupujemy świeże warzywa."),
    ("owoce", "owoce", "фрукты", "Lubię polskie owoce."),
    ("sklep", "sklep", "магазин", "Sklep jest obok domu."),
    ("kupowac", "kupować", "покупать", "Często kupuję tutaj chleb."),
    ("prosze", "proszę", "пожалуйста; прошу", "Proszę wodę i kawę."),
    ("ile-kosztuje", "ile kosztuje?", "сколько стоит?", "Ile kosztuje ta bułka?"),
    ("kilogram", "kilogram", "килограмм", "Proszę kilogram jabłek."),
)
GRAMMAR = (
    ("Proszę ___ wodę.", ["zimna", "zimną", "zimnej"], 1, "После proszę предмет — в винительном падеже: zimną wodę."),
    ("Kupuję ___.", ["kawa", "kawę", "kawy"], 1, "Женские существительные на -a обычно получают -ę: kawę."),
    ("Poproszę ___.", ["chleb", "chleba", "chlebem"], 0, "У неодушевлённых существительных мужского рода форма часто не меняется: chleb."),
    ("Proszę litr ___.", ["mleko", "mleka", "mlekiem"], 1, "После единицы количества употребляем родительный: litr mleka."),
    ("Как вежливо спросить цену?", ["Ile kosztuje?", "Jaki koszt?", "Gdzie płaci?"], 0, "Ile kosztuje? — нейтральный вопрос «Сколько стоит?»."),
)
QUIZ = (
    ("Выберите «булочка».", ["bułka", "butelka", "woda"], 0, "Bułka — булочка."),
    ("Kupuję ___.", ["kawę", "kawa", "kawie"], 0, "После kupuję нужна форма kawę."),
    ("Как заказать воду?", ["Proszę wodę.", "Proszę woda.", "Jest wodą."], 0, "В заказе естественно: Proszę wodę."),
    ("Ile ___ ta kawa?", ["kosztuje", "kupuje", "proszę"], 0, "О цене спрашиваем Ile kosztuje…?"),
    ("Что означает owoce?", ["фрукты", "овощи", "напитки"], 0, "Owoce — фрукты."),
    ("Proszę kilogram ___.", ["jabłka", "jabłek", "jabłko"], 1, "После kilogram нужна форма jabłek."),
    ("Где покупают продукты?", ["w sklepie", "w sypialni", "na balkonie"], 0, "Sklep — магазин."),
    ("Выберите естественный заказ.", ["Poproszę kawę bez cukru.", "Poproszę kawa bez cukier.", "Kawę jest proszę."], 0, "Poproszę + винительный падеж — вежливая формула заказа."),
)
READING = {
    "id": "zakupy-oli", "title": "Zakupy Oli", "description": "Оля покупает продукты к завтраку", "level": "A1", "minutes": 4, "emoji": "🛒", "position": 5,
    "paragraphs": [
        "W sobotę rano Ola idzie do małego sklepu obok domu. Chce kupić jedzenie na śniadanie. Ma krótką listę: chleb, mleko, ser, jabłka i kawa.",
        "W sklepie Ola mówi: „Dzień dobry. Proszę jeden chleb, litr mleka i dwieście gramów sera”. Potem wybiera cztery czerwone jabłka. Pyta też: „Ile kosztuje kawa?”.",
        "Sprzedawczyni podaje cenę. Ola płaci kartą i pakuje zakupy do torby. Na koniec mówi: „Dziękuję, do widzenia”. W domu robi kawę i kanapki ze świeżym serem.",
    ],
    "glossary": {
        "idzie": {"lemma": "iść", "translation": "идти", "part_of_speech": "глагол"},
        "chce": {"lemma": "chcieć", "translation": "хотеть", "part_of_speech": "глагол"},
        "kupić": {"lemma": "kupić", "translation": "купить", "part_of_speech": "глагол"},
        "krótką": {"lemma": "krótki", "translation": "короткий", "part_of_speech": "прилагательное"},
        "dwieście": {"lemma": "dwieście", "translation": "двести", "part_of_speech": "числительное"},
        "gramów": {"lemma": "gram", "translation": "грамм", "part_of_speech": "существительное"},
        "wybiera": {"lemma": "wybierać", "translation": "выбирать", "part_of_speech": "глагол"},
        "pyta": {"lemma": "pytać", "translation": "спрашивать", "part_of_speech": "глагол"},
        "sprzedawczyni": {"lemma": "sprzedawczyni", "translation": "продавщица", "part_of_speech": "существительное"},
        "podaje": {"lemma": "podawać", "translation": "сообщать; подавать", "part_of_speech": "глагол"},
        "płaci": {"lemma": "płacić", "translation": "платить", "part_of_speech": "глагол"},
        "pakuje": {"lemma": "pakować", "translation": "упаковывать", "part_of_speech": "глагол"},
        "zakupy": {"lemma": "zakupy", "translation": "покупки", "part_of_speech": "существительное"},
        "torby": {"lemma": "torba", "translation": "сумка", "part_of_speech": "существительное"},
        "świeżym": {"lemma": "świeży", "translation": "свежий", "part_of_speech": "прилагательное"},
    },
}


def seed(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Course = apps.get_model("learning", "Course"); Topic = apps.get_model("learning", "Topic"); Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard"); Link = apps.get_model("learning", "LessonFlashcard"); Question = apps.get_model("learning", "Question"); ReadingText = apps.get_model("learning", "ReadingText")
    course = Course.objects.get(id="a1-foundations")
    Topic.objects.filter(course=course, position__gte=5).update(position=6)
    topic, _ = Topic.objects.update_or_create(id="food-shopping", defaults={"course": course, "title": "Еда и магазин", "description": "Покупаем продукты, спрашиваем цену и делаем простой заказ", "emoji": "🛒", "position": 5, "is_active": True})
    rows = (("food-words", "words", "Jedzenie", "Еда и напитки", "8 карточек · A1", "Назови базовые продукты", 7, "🍎"), ("food-grammar", "grammar", "Poproszę…", "Заказ и покупка", "5 заданий · A1", "Используй винительный падеж и количества", 8, "✏️"), ("food-review", "review", "W sklepie", "В магазине", "7 карточек · A1", "Спроси цену и собери покупки", 6, "🔄"), ("food-quiz", "quiz", "Quiz: zakupy", "Проверка темы", "8 вопросов · A1", "Проверь продукты, заказ и цены", 5, "🎯"))
    made = {}
    for position, row in enumerate(rows, 20):
        id_, kind, title, plan, subtitle, desc, minutes, emoji = row
        made[id_], _ = Lesson.objects.update_or_create(id=id_, defaults={"topic": topic, "kind": kind, "title": title, "plan_title": plan, "subtitle": subtitle, "description": desc, "minutes": minutes, "emoji": emoji, "position": position, "is_active": True, "source_metadata": SOURCE})
    grammar = made["food-grammar"]
    grammar.theory_title = "Poproszę kawę — kupuję chleb"
    grammar.theory_sections = [["Вежливый заказ", "Proszę или poproszę + предмет: Proszę wodę. Poproszę kawę."], ["Винительный падеж", "После kupuję/proszę женское -a обычно меняется на -ę: kawa → kawę, woda → wodę. Мужской неодушевлённый часто не меняется: chleb."], ["Количество", "После litr, kilogram и gram форма меняется: litr mleka, kilogram jabłek, dwieście gramów sera."]]
    grammar.save(update_fields=("theory_title", "theory_sections"))
    cards = []
    for position, (id_, polish, translation, example) in enumerate(CARDS):
        card, _ = Flashcard.objects.update_or_create(id=id_, defaults={"polish": polish, "translation": translation, "example": example, "position": 75 + position, "is_active": True, "source_metadata": SOURCE}); cards.append(card)
    for lesson_id, chosen in (("food-words", cards[:8]), ("food-review", cards[8:])):
        Link.objects.filter(lesson_id=lesson_id).delete()
        for position, card in enumerate(chosen): Link.objects.create(lesson_id=lesson_id, flashcard=card, position=position)
    for lesson_id, questions in (("food-grammar", GRAMMAR), ("food-quiz", QUIZ)):
        Question.objects.filter(lesson_id=lesson_id).delete()
        for position, (prompt, options, correct, explanation) in enumerate(questions): Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)
    ReadingText.objects.update_or_create(id=READING["id"], defaults={**{key: value for key, value in READING.items() if key != "id"}, "topic": topic, "source_metadata": SOURCE})


class Migration(migrations.Migration):
    dependencies = [("learning", "0010_a1_home_content")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
