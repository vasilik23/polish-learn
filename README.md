# PolskiFlow

Mobile-first приложение для ежедневного изучения польского языка. Проект
работает на Next.js и поэтапно переносится на Python/Django без остановки
production-версии.

## Возможности MVP

- регистрация, вход и сессии через Supabase Auth;
- ежедневный план и серия дней;
- уроки слов, грамматики, повторения и мини-тест;
- сохранение завершённых уроков в Supabase;
- расчёт интервальных повторений SM-2;
- адаптивный интерфейс для телефона.

## Технологии

| Часть | Технологии | Статус |
| --- | --- | --- |
| Web | Next.js 16, React 19, TypeScript, Tailwind CSS 4 | production |
| Backend | Python 3.12, Django 5.2, Templates + HTMX | production-кандидат |
| Данные и Auth | Supabase Postgres, Auth, RLS | production |
| Деплой | GitHub + Vercel | настроен |

## Быстрый запуск Next.js

Требования: Node.js 20+ и npm.

```bash
npm install
cp .env.local.example .env.local
npm run dev
```

Заполните в `.env.local` публичные параметры из Supabase:

```dotenv
NEXT_PUBLIC_SUPABASE_URL=https://YOUR_PROJECT.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=YOUR_PUBLIC_KEY
```

Приложение откроется на [http://localhost:3000](http://localhost:3000) и
перенаправит гостя на `/login`. Для проверки с телефона в той же Wi-Fi сети:

```bash
npm run dev -- -H 0.0.0.0
```

После этого откройте `http://<IP-адрес-компьютера>:3000`.

## Запуск Django

Требования: Python 3.11+.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python manage.py check
python manage.py test
python manage.py runserver
```

Для проверки Supabase access token добавьте публичные параметры:

```bash
export SUPABASE_URL=https://YOUR_PROJECT.supabase.co
export SUPABASE_ANON_KEY=YOUR_PUBLIC_KEY
```

Диагностический endpoint `GET /api/auth/me/` принимает заголовок
`Authorization: Bearer <access-token>`. Модели пользовательского прогресса
отображают существующие таблицы Supabase как `managed = False`; служебные
таблицы Django создаются обычной командой `manage.py migrate`.

## Supabase

Для новой пустой базы сначала выполните `supabase/schema.sql`, затем применяйте
последовательные миграции из `supabase/migrations/` по номеру. Production
приведён к состоянию миграций `002`–`007`: пользовательские данные защищены
RLS, учебный контент доступен в Django Admin, а служебные таблицы Django закрыты
от браузерных ролей Supabase.

## Полезные команды

```bash
# Next.js
npm run lint
npm run build

# Django и доменное ядро
cd backend
.venv/bin/python manage.py check
.venv/bin/python manage.py test
```

## Маршруты

| Путь | Назначение |
| --- | --- |
| `/login` | вход |
| `/register` | регистрация |
| `/` | ежедневный план |
| `/lesson/words` | новые слова |
| `/lesson/grammar` | грамматика |
| `/lesson/review` | повторение карточек |
| `/lesson/quiz` | мини-тест |

## Структура

```text
src/                    текущий Next.js-интерфейс и API
backend/                Django и независимое Python-доменное ядро
supabase/               эталонная схема и последовательные SQL-миграции
docs/python-migration.md подробный контракт и план переноса
```

## План переноса на Python

- [x] Зафиксировать поведение MVP и инфраструктуру.
- [x] Перенести SM-2 и расчёт серии дней в Python с тестами.
- [x] Создать Django-проект и модели Supabase.
- [x] Перенести авторизацию и защищённые маршруты.
- [x] Перенести страницы на Django Templates + HTMX.
- [x] Перенести учебный контент в PostgreSQL и Django Admin.
- [x] Настроить полный CI, preview и production для Python-приложения.
- [ ] Провести E2E-проверку и удалить старую Next.js-реализацию.
- [x] Добавить курсы, темы и привязку слов к урокам.
- [ ] Добавить адаптированные тексты, личный словарь и новые тренировки.

Подробности и критерии совместимости находятся в
[`docs/python-migration.md`](docs/python-migration.md).

## Деплой

- GitHub: ветка `main` запускает production-сборку.
- Vercel: preview создаётся для каждого pull request; Django развёрнут отдельным
  проектом `polskiflow-python` с Root Directory `backend`.
- Для Django в Vercel задаются `SUPABASE_URL`, `SUPABASE_ANON_KEY`,
  `DATABASE_URL`, `DJANGO_SECRET_KEY`, `DJANGO_DEBUG` и `AUTH_COOKIE_SECURE`.
- В Supabase Auth → URL Configuration должны быть добавлены production- и
  preview-адреса приложения.
