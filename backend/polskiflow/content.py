"""Temporary code-backed lesson content until it moves to Django Admin."""

TASKS = [
    {"id": "words", "title": "Słówka dnia", "plan_title": "Новые слова", "subtitle": "5 слов · A1", "description": "Выучи 5 новых слов с примерами", "minutes": 5, "emoji": "📚"},
    {"id": "grammar", "title": "Gramatyka", "plan_title": "Грамматика", "subtitle": "Род существительных", "description": "Короткий урок о роде существительных", "minutes": 8, "emoji": "✏️"},
    {"id": "review", "title": "Powtórka", "plan_title": "Повторение", "subtitle": "5 карточек", "description": "Повтори слова, которые уже знаешь", "minutes": 6, "emoji": "🔄"},
    {"id": "quiz", "title": "Quiz", "plan_title": "Мини-тест", "subtitle": "5 вопросов", "description": "Проверь себя: перевод слов", "minutes": 4, "emoji": "🎯"},
]

FLASHCARDS = [
    {"id": "cześć", "polish": "cześć", "translation": "привет", "example": "Cześć, jak się masz?"},
    {"id": "dziękuję", "polish": "dziękuję", "translation": "спасибо", "example": "Dziękuję bardzo!"},
    {"id": "proszę", "polish": "proszę", "translation": "пожалуйста", "example": "Proszę bardzo."},
    {"id": "tak", "polish": "tak", "translation": "да", "example": "Tak, zgadzam się."},
    {"id": "nie", "polish": "nie", "translation": "нет", "example": "Nie, dziękuję."},
]

GRAMMAR = {
    "title": "Rodzajnik i ród rzeczownika",
    "sections": [
        ("Род существительных", "В польском у каждого существительного есть род: мужской, женский или средний. От рода зависит форма прилагательных и местоимений."),
        ("Примеры", "dom (дом) — мужской · kawa (кофе) — женский · miasto (город) — средний."),
        ("Неопределённость", "В польском нет артиклей «a/an/the». «A cat» — просто kot, а «the cat» — ten kot."),
    ],
    "questions": [
        {"prompt": "Слово «kawa» (кофе) — это род…", "options": ["мужской", "женский", "средний"], "correct": 1, "explanation": "Kawa оканчивается на -a и относится к женскому роду."},
        {"prompt": "Слово «dom» (дом) — это род…", "options": ["мужской", "женский", "средний"], "correct": 0, "explanation": "Dom — существительное мужского рода."},
        {"prompt": "Слово «miasto» (город) — это род…", "options": ["мужской", "женский", "средний"], "correct": 2, "explanation": "Miasto — существительное среднего рода."},
    ],
}

QUIZ = [
    {"prompt": "Как переводится «cześć»?", "options": ["спасибо", "привет", "пожалуйста", "до свидания"], "correct": 1, "explanation": "Cześć — неформальное «привет»."},
    {"prompt": "Что значит «dziękuję»?", "options": ["нет", "да", "спасибо", "извините"], "correct": 2, "explanation": "Dziękuję = спасибо."},
    {"prompt": "Выберите перевод «proszę»", "options": ["пожалуйста", "утро", "вечер", "комната"], "correct": 0, "explanation": "Proszę — «пожалуйста» или «прошу»."},
    {"prompt": "Как будет «да» по-польски?", "options": ["nie", "tak", "dom", "kawa"], "correct": 1, "explanation": "Tak = да."},
    {"prompt": "Как будет «нет» по-польски?", "options": ["tak", "cześć", "nie", "miasto"], "correct": 2, "explanation": "Nie = нет."},
]

TASKS_BY_ID = {task["id"]: task for task in TASKS}
