# PolskiFlow

Веб-приложение для изучения польского (mobile-first). MVP: регистрация, главный экран с планом на день, карточки заданий, пример урока со словами.

## Стек

- **Next.js 16** (App Router, TypeScript)
- **Tailwind CSS 4**
- **Supabase** — регистрация и сессии

## Быстрый старт

### 1. Supabase

1. Создайте проект на [supabase.com](https://supabase.com)
2. **Authentication → Providers → Email** — включён по умолчанию
3. Для локальной разработки отключите подтверждение email:  
   **Authentication → Providers → Email → Confirm email** = OFF
4. **Project Settings → API** — скопируйте URL и `anon` key
5. **SQL Editor** — выполните скрипт `supabase/schema.sql` (профили, опционально)

### 2. Переменные окружения

```bash
cp .env.local.example .env.local
# отредактируйте .env.local
```

### 3. Запуск

```bash
npm install
npm run dev
```

Откройте [http://localhost:3000](http://localhost:3000) — вас перенаправит на `/login`.

Для проверки с телефона в той же Wi‑Fi сети:

```bash
npm run dev -- -H 0.0.0.0
```

и откройте `http://<IP-вашего-Mac>:3000`.

## Маршруты

| Путь | Описание |
|------|----------|
| `/login` | Вход |
| `/register` | Регистрация |
| `/` | Главная: план на день + карточки заданий |
| `/lesson/words` | Флеш-карточки (пример) |
| `/lesson/grammar` | Заглушка |
| `/lesson/review` | Флеш-карточки |
| `/lesson/quiz` | Заглушка |

## Структура проекта

```
src/
  app/(auth)/     — login, register
  app/(app)/      — главная, уроки (за middleware)
  components/     — UI
  lib/data/mock.ts — демо-данные плана и карточек
  lib/supabase/   — клиенты и middleware
```

## Дальше

- [ ] Сохранение прогресса плана в Supabase
- [ ] Spaced repetition (SM-2)
- [ ] PWA + Capacitor для магазинов
- [ ] Playwright E2E: register → home → lesson

## Деплой (Vercel)

1. Репозиторий на GitHub
2. [vercel.com](https://vercel.com) → Import → добавьте env `NEXT_PUBLIC_SUPABASE_*`
3. В Supabase **Authentication → URL Configuration** добавьте Site URL и Redirect URLs вашего домена
