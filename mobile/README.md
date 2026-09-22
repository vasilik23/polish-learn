# PolskiFlow Mobile

Первый Expo/React Native vertical slice для iOS и Android: Supabase email/password auth, защищённое хранение сессии и owner-scoped `GET /api/v1/me/bootstrap/` с экраном «Сегодня».

```bash
cp .env.example .env
npm ci
npm run typecheck
npm start
```

В `.env` нужны URL Django API, URL Supabase и только публичный publishable key. `service_role`, database password и другие серверные секреты в Expo добавлять нельзя: `EXPO_PUBLIC_*` встраивается в приложение.

Сессия на iOS/Android хранится через Expo SecureStore. MVP пока не выполняет уроки и не кэширует персональные данные offline; эти границы явно показаны в UI.
