# Performance baseline

Дата первого замера: 31 августа 2026. Production:
`https://polish-learn.vercel.app`.

## Цели

Для field-данных на 75-м перцентиле:

- LCP ≤ 2,5 с;
- INP ≤ 200 мс;
- CLS ≤ 0,1.

Пока трафика недостаточно для надёжного field-среза, релизный lab baseline
измеряется Lighthouse в мобильном режиме. Lighthouse не измеряет INP без
реального ввода, поэтому в lab используется TBT как диагностический proxy, а
INP должен быть добавлен из real-user monitoring после накопления данных.

Рабочий lab budget для ключевых маршрутов:

- performance score ≥ 90;
- LCP ≤ 2,5 с;
- CLS ≤ 0,1;
- TBT ≤ 200 мс;
- TTFB фиксируется для диагностики, но один холодный serverless-запуск не
  считается регрессией без повторных замеров.

## Первый production-замер

Команда запускается по три раза для каждого маршрута; в таблицу попадает
медиана. Первый диагностический прогон до оптимизации внешнего шрифта:

| Маршрут | Score | LCP | CLS | TBT | TTFB |
| --- | ---: | ---: | ---: | ---: | ---: |
| `/login/` | 61 | 5,53 с | 0,014 | 0 мс | 106 мс |
| `/sources/` | 91 | 2,83 с | 0,016 | 0 мс | 41 мс |

Lighthouse показал до 3,86 с потенциальной экономии на render-blocking
Google Fonts. Поэтому внешний Manrope удалён из критического пути в пользу
нативного системного стека. Итоговую production-медиану нужно зафиксировать
после деплоя этой оптимизации.

## Воспроизводимый запуск

```bash
npx --yes lighthouse https://polish-learn.vercel.app/login/ \
  --only-categories=performance \
  --form-factor=mobile \
  --screenEmulation.mobile=true \
  --throttling-method=simulate \
  --output=json \
  --output-path=/tmp/polskiflow-login-lh.json \
  --chrome-flags='--headless --no-sandbox' \
  --quiet
```

Повторить для `/sources/` и минимум одного авторизованного ключевого маршрута.
Для авторизованной страницы использовать временный Chrome-профиль тестового
аккаунта вне репозитория; cookies, токены и credentials не сохранять в Git.

Перед сравнением результатов фиксировать дату, deployment commit, viewport,
режим throttling и медиану не менее трёх прогонов. Lab-данные не выдавать за
field Core Web Vitals.

Источники методики:

- [Web Vitals](https://web.dev/articles/vitals)
- [Lighthouse performance scoring](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring)
