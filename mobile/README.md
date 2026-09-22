# PolskiFlow Mobile

Первый Expo/React Native vertical slice для iOS и Android: Supabase email/password auth, защищённое хранение сессии и owner-scoped `GET /api/v1/me/bootstrap/` с экраном «Сегодня».

```bash
cp .env.example .env
npm ci
npm run verify
npm start
```

В `.env` нужны URL Django API, URL Supabase и только публичный publishable key. `service_role`, database password и другие серверные секреты в Expo добавлять нельзя: `EXPO_PUBLIC_*` встраивается в приложение.

Сессия на iOS/Android хранится через Expo SecureStore. Мобильный поток открывает
уроки из Today, проверяет choice/sentence-builder ответы на сервере и сохраняет
результат идемпотентным событием. Персональные данные offline пока не кэшируются.
Позиция и текущий счёт незавершённого урока сохраняются owner-scoped на сервере,
поэтому урок можно продолжить после перезапуска или на другом устройстве.
Beta-пользователь может отправить категоризированную обратную связь через
существующий owner-scoped API; приложение не прикладывает токены и device data.
Задание словаря в Today открывает только due-карточки личной SM‑2 очереди;
ответ нужно показать до оценки, а расписание обновляется owner-scoped на сервере.
Раздел «Читать» показывает учебные тексты A1–C2, синхронизирует закладки,
добавляет только проверенные glossary-леммы в словарь и открывает comprehension.

Installable closed-beta profiles and the physical-device acceptance gate are
documented in [`docs/mobile-beta.md`](../docs/mobile-beta.md). Running an EAS
build requires a separately authenticated Expo account and signing setup.
