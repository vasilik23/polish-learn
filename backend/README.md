# PolskiFlow Python backend

Здесь находятся независимое доменное ядро и постепенно вводимый Django-проект.
До переключения production текущий Next.js-интерфейс продолжает работать.

Запуск тестов из корня репозитория:

```bash
PYTHONPATH=backend python3 -m unittest discover -s backend/tests -v
```

Проверка Django после установки зависимостей:

```bash
cd backend
python manage.py check
python manage.py test
```

Проверенная версия зависимостей закреплена в `requirements.lock`.

## Supabase

Django-модели отображают существующие таблицы `public.profiles`,
`public.lesson_completions` и `public.flashcard_reviews` как `managed = False`:
Django не создаёт и не изменяет их своими миграциями. SQL сначала проверяется в
preview/staging-проекте Supabase и только после ручной проверки применяется к
production.

Для проверки access token Django обращается к Supabase Auth. Настройте только
публичные параметры (service-role key для этого не нужен):

```bash
export SUPABASE_URL=https://PROJECT.supabase.co
export SUPABASE_ANON_KEY=PUBLIC_ANON_KEY
```

Клиент передаёт текущий access token в `Authorization: Bearer …`. Защищённый
диагностический маршрут `GET /api/auth/me/` возвращает идентификатор и email
проверенного пользователя; отсутствие или отклонение токена даёт `401`.
