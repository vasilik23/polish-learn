from django.db import migrations


def seed_sqlite(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    Lesson = apps.get_model("learning", "Lesson")
    Flashcard = apps.get_model("learning", "Flashcard")
    Question = apps.get_model("learning", "Question")
    lessons = [
        ("words", "Słówka dnia", "Новые слова", "5 слов · A1", "Выучи 5 новых слов с примерами", 5, "📚"),
        ("grammar", "Gramatyka", "Грамматика", "Род существительных", "Короткий урок о роде существительных", 8, "✏️"),
        ("review", "Powtórka", "Повторение", "5 карточек", "Повтори слова, которые уже знаешь", 6, "🔄"),
        ("quiz", "Quiz", "Мини-тест", "5 вопросов", "Проверь себя: перевод слов", 4, "🎯"),
    ]
    theory = [["Род существительных", "В польском у каждого существительного есть род: мужской, женский или средний."], ["Примеры", "dom — мужской · kawa — женский · miasto — средний."], ["Неопределённость", "В польском нет артиклей a/an/the."]]
    for position, values in enumerate(lessons):
        lesson_id, title, plan_title, subtitle, description, minutes, emoji = values
        Lesson.objects.create(id=lesson_id, title=title, plan_title=plan_title, subtitle=subtitle, description=description, minutes=minutes, emoji=emoji, position=position, theory_title="Rodzajnik i ród rzeczownika" if lesson_id == "grammar" else "", theory_sections=theory if lesson_id == "grammar" else [])
    for position, values in enumerate([("czesc", "cześć", "привет", "Cześć, jak się masz?"), ("dziekuje", "dziękuję", "спасибо", "Dziękuję bardzo!"), ("prosze", "proszę", "пожалуйста", "Proszę bardzo."), ("tak", "tak", "да", "Tak, zgadzam się."), ("nie", "nie", "нет", "Nie, dziękuję.")]):
        card_id, polish, translation, example = values
        Flashcard.objects.create(id=card_id, polish=polish, translation=translation, example=example, position=position)
    questions = {
        "grammar": [("Слово «kawa» (кофе) — это род…", ["мужской", "женский", "средний"], 1, "Kawa оканчивается на -a и относится к женскому роду."), ("Слово «dom» (дом) — это род…", ["мужской", "женский", "средний"], 0, "Dom — существительное мужского рода."), ("Слово «miasto» (город) — это род…", ["мужской", "женский", "средний"], 2, "Miasto — существительное среднего рода.")],
        "quiz": [("Как переводится «cześć»?", ["спасибо", "привет", "пожалуйста", "до свидания"], 1, "Cześć — неформальное «привет»."), ("Что значит «dziękuję»?", ["нет", "да", "спасибо", "извините"], 2, "Dziękuję = спасибо."), ("Выберите перевод «proszę»", ["пожалуйста", "утро", "вечер", "комната"], 0, "Proszę — «пожалуйста» или «прошу»."), ("Как будет «да» по-польски?", ["nie", "tak", "dom", "kawa"], 1, "Tak = да."), ("Как будет «нет» по-польски?", ["tak", "cześć", "nie", "miasto"], 2, "Nie = нет.")],
    }
    for lesson_id, items in questions.items():
        for position, (prompt, options, correct, explanation) in enumerate(items):
            Question.objects.create(lesson_id=lesson_id, prompt=prompt, options=options, correct=correct, explanation=explanation, position=position)


class Migration(migrations.Migration):
    dependencies = [("learning", "0002_content_models")]
    operations = [migrations.RunPython(seed_sqlite, migrations.RunPython.noop)]
