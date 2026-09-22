# PolskiFlow Mobile

Первый Expo/React Native vertical slice для iOS и Android: Supabase email/password auth, защищённое хранение сессии и owner-scoped `GET /api/v1/me/bootstrap/` с экраном «Сегодня».

```bash
cp .env.example .env
npm ci
npm run typecheck
npm start
```

В `.env` нужны URL Django API, URL Supabase и только публичный publishable key. `service_role`, database password и другие серверные секреты в Expo добавлять нельзя: `EXPO_PUBLIC_*` встраивается в приложение.

Сессия на iOS/Android хранится через Expo SecureStore. Мобильный поток открывает
уроки из Today, проверяет choice/sentence-builder ответы на сервере и сохраняет
результат идемпотентным событием. Персональные данные offline пока не кэшируются.
Позиция и текущий счёт незавершённого урока сохраняются owner-scoped на сервере,
поэтому урок можно продолжить после перезапуска или на другом устройстве.
