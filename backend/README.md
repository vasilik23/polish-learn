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

Для авторизации Django обращается к Supabase Auth. Настройте только публичные
параметры (service-role/secret key для этого не нужен):

```bash
export SUPABASE_URL=https://PROJECT.supabase.co
export SUPABASE_ANON_KEY=PUBLIC_ANON_KEY
```

Доступны браузерные маршруты `/login/`, `/register/`, `/logout/` и защищённая
страница `/`. Access и refresh tokens сохраняются в `HttpOnly`, `SameSite=Lax`
cookies; истёкший access token автоматически обновляется через Supabase Auth.
В production cookies помечаются `Secure`; локально это управляется переменной
`AUTH_COOKIE_SECURE`.

Минимальные production-переменные Django:

```bash
export DJANGO_DEBUG=false
export DJANGO_SECRET_KEY='long-random-production-secret'
export DJANGO_ALLOWED_HOSTS='your-domain.example'
export AUTH_COOKIE_SECURE=true
export DJANGO_SECURE_SSL_REDIRECT=true
```

HSTS намеренно не включается автоматически: после проверки HTTPS на настоящем
домене задайте `DJANGO_SECURE_HSTS_SECONDS` постепенно, затем при необходимости
включите `DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS` и `DJANGO_SECURE_HSTS_PRELOAD`.
Ошибочная HSTS-конфигурация долго кэшируется браузерами и трудно откатывается.

API-клиент также может передавать access token в `Authorization: Bearer …`.
Защищённый диагностический маршрут `GET /api/auth/me/` возвращает идентификатор
и email проверенного пользователя; отсутствие или отклонение токена даёт `401`.
