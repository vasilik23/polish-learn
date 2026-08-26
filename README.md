# PolskiFlow

Mobile-first приложение для ежедневного изучения польского языка. Основная и
единственная production-версия работает на Python/Django, использует Supabase
для PostgreSQL и авторизации и разворачивается в Vercel.

Production: [polish-learn.vercel.app](https://polish-learn.vercel.app)

## Что уже работает

- регистрация, вход, безопасные пользовательские сессии через Supabase Auth;
- ежедневный план, серия дней и сохранение завершённых уроков;
- уроки слов, грамматики, повторения и мини-тест;
- библиотека адаптированных текстов с интерактивным glossary;
- личный словарь и тренировка сохранённых слов;
- структура контента `Course → Topic → Lesson` и управление через Django Admin;
- адаптивный интерфейс для телефона и desktop;
- базовая реализация алгоритма интервальных повторений SM-2.

## Стек

| Часть | Технологии |
| --- | --- |
| Web | Python 3.12, Django 5.2, Templates, HTMX |
| Данные и Auth | Supabase Postgres, Auth, RLS |
| Доставка | GitHub Actions, Vercel |

Отдельный Next.js-клиент удалён после успешного переноса production. Для сборки
и локальной разработки Node.js не требуется.

## Быстрый запуск

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
cp .env.example .env.local
python manage.py migrate
python manage.py check
python manage.py test
python manage.py runserver
```

По умолчанию используется локальная SQLite. Для Supabase Auth заполните в
локальном окружении публичные `SUPABASE_URL` и `SUPABASE_ANON_KEY`. Для работы
Django Admin с production-подобным PostgreSQL дополнительно задайте
`DATABASE_URL`; секреты нельзя коммитить в Git.

Подробная настройка окружения, базы и Vercel описана в
[`backend/README.md`](backend/README.md).

## Основные маршруты

| Путь | Назначение |
| --- | --- |
| `/login/`, `/register/` | авторизация |
| `/` | ежедневный план |
| `/lesson/words/` | новые слова |
| `/lesson/grammar/` | грамматика |
| `/lesson/review/` | повторение карточек |
| `/lesson/quiz/` | мини-тест |
| `/reading/` | библиотека текстов |
| `/dictionary/` | личный словарь |
| `/dictionary/practice/` | тренировка слов |
| `/admin/` | управление учебным контентом |
| `/health/` | проверка состояния приложения |

## Структура репозитория

```text
backend/                Django-приложение, шаблоны, стили и тесты
supabase/               эталонная схема и последовательные SQL-миграции
docs/python-migration.md история переноса и актуальный план развития
.github/workflows/      Python CI
```

## Проверки

```bash
cd backend
.venv/bin/python manage.py test
.venv/bin/python manage.py check
.venv/bin/python manage.py makemigrations --check --dry-run
```

Эти проверки выполняются GitHub Actions для pull request и `main`. Vercel
автоматически разворачивает Django-проект `polskiflow-python` с корневой
директорией `backend`.

## Supabase

Для новой пустой базы сначала применяется `supabase/schema.sql`, затем миграции
из `supabase/migrations/` в порядке их имён. Пользовательские данные защищены
RLS; приложение обращается к ним с access token пользователя и не использует
`service_role`.

## Следующие этапы

1. Наполнить уровни A1 → A2 по
   [`контент-плану`](docs/content-roadmap.md), соблюдая
   [`реестр источников и лицензий`](docs/content-sources.md).
2. Добавить страницу источников и атрибуции в пользовательский интерфейс.
3. Добавить страницу профиля и пользовательские настройки.
4. Добавить тёмную тему с сохранением выбора.
5. Подключить SM-2 к экрану повторения и расширить типы упражнений.

История завершённых этапов и правила работы с контентом находятся в
[`docs/python-migration.md`](docs/python-migration.md).
