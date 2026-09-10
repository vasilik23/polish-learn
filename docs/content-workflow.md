# Редакторский workflow контента

`content_workflow` — безопасный первый этап подготовки вертикальной темы. Он
проверяет JSON manifest и создаёт preview либо план публикации. Команда **не**
подключается к Supabase, не читает секреты, не создаёт миграции и не пишет в БД.

## 1. Черновик

Manifest версии 1 содержит стабильный `id`, уровень A1–C2, `language: "pl"`,
статус, карточку источника, содержимое вертикальной темы и ожидаемые количества.
Минимальная форма:

```json
{
  "schema_version": 1,
  "id": "b1-example-topic",
  "title": "Temat przykładowy",
  "level": "B1",
  "language": "pl",
  "status": "draft",
  "source": {
    "origin": "original",
    "created_for": "PolskiFlow",
    "license": "PolskiFlow original content",
    "verified_at": "2026-09-01"
  },
  "content": {
    "active_units": [{"id": "stable-unit-id"}],
    "card_sets": [[{"id": "card-1", "polish": "forma", "translation": "перевод", "example": "Naturalny przykład."}]],
    "grammar": {"summary": "Объяснение"},
    "exercises": [{"id": "exercise-1", "prompt": "Pytanie", "options": ["A", "B"], "answer": "A", "explanation": "Dlaczego A."}],
    "reading": {
      "paragraphs": ["непустой текст"],
      "glossary": {"форма": {"lemma": "лемма", "translation": "перевод"}}
    },
    "final_quiz": [{"id": "quiz-1", "prompt": "Pytanie", "options": ["A", "B"], "answer": "A", "explanation": "Dlaczego A."}]
  },
  "expected_counts": {
    "active_units": 12,
    "card_sets": 2,
    "flashcards": 10,
    "exercises": 5,
    "reading_paragraphs": 1,
    "glossary": 1,
    "final_quiz": 8
  }
}
```

Все учебные элементы имеют уникальные стабильные `id`; неизвестные поля
отклоняются. У вопроса варианты уникальны, а `answer` должен ровно совпадать с
одним из них. Абзацы должны быть непустыми строками, а каждая glossary-запись —
содержать `lemma` и `translation`; допускается также `part_of_speech`.
На этом этапе проверяются структура и количества, а не качество польского или
соответствие CEFR. Для внешнего материала обязательна полная карточка из
[`content-sources.md`](content-sources.md) со `status: "approved"`; `review` и
`blocked` останавливают workflow.

## 2. Проверка и preview

Из каталога `backend/`:

```bash
.venv/bin/python manage.py content_workflow path/to/draft.json
.venv/bin/python manage.py content_workflow path/to/draft.json --output /tmp/topic-preview.json
```

Preview фиксирует SHA-256 канонического manifest, фактические количества,
источник, предупреждения и флаг `publishable`. Изменение любого поля меняет
checksum, поэтому редактор и разработчик должны проверять один и тот же вариант.

До одобрения редактор вручную проверяет естественность польского, перевод,
однозначность ответов, объяснения, сложность и лицензию. Автоматическая
валидация не заменяет эту проверку и не подтверждает уровень CEFR.

## 3. Явная граница публикации

После проверки выставить `status: "approved"` и добавить:

```json
"review": {
  "language_reviewer": "editor-id",
  "license_reviewer": "rights-reviewer-id",
  "reviewed_at": "2026-09-01"
}
```

Затем создать только план:

```bash
.venv/bin/python manage.py content_workflow path/to/approved.json \
  --prepare-publish --approval-id ED-123 --output /tmp/topic-publish-plan.json
```

Даже этот режим не публикует данные. План задаёт следующую ручную границу:
сгенерировать из точного checksum упорядоченную Django data migration и
соответствующую rerunnable Supabase migration, проверить diff, тесты, drift,
RLS/grants и preview, затем применить только reviewed migration и развернуть
соответствующий commit.

## 4. Безопасный scaffold миграций

После одобрения можно создать **неисполняемые** парные заготовки, передав checksum
ровно того manifest, который проверял редактор:

```bash
.venv/bin/python manage.py content_workflow path/to/approved.json \
  --generate-scaffold \
  --approval-id ED-123 \
  --expected-checksum <полный SHA-256 из preview> \
  --output-directory /tmp/b1-example-topic-scaffold
```

Каталог должен быть новым или пустым. Команда отказывается писать в настоящие
`backend/polskiflow/learning/migrations/` и `supabase/migrations/`, не
перезаписывает файлы, не подключается к сети или БД и не выполняет SQL. Она
создаёт пять review-артефактов: точный `approved-manifest.json`, метаданные с
checksum и approval ID, `model-mapping.json`, Django scaffold и SQL scaffold.

`model-mapping.json` детерминированно фиксирует соответствие текущим Django
моделям и Supabase-таблицам: тема → `Topic/topics`, карточки →
`Flashcard/flashcards`, порядок наборов → `LessonFlashcard/lesson_flashcards`,
грамматика → `Lesson/lessons`, задания → `Question/questions`, чтение →
`ReadingText/reading_texts`. Для ответа вопроса документирует преобразование
`options.index(answer) → correct`, а для источника — перенос карточки в
`source_metadata`. Отдельно перечислены обязательные решения, которых нет в
manifest v1: course и lesson IDs, оформление уроков, ID и метаданные чтения,
позиции темы. `active_units` пока остаются редакторским инвентарём: одних ID
недостаточно для без потерь сопоставления текущей модели.

Mapping является только контрактом проверки: он не импортирует модели, не
читает БД, не генерирует ORM/SQL и не выбирает отсутствующие значения. Django и
SQL scaffolds по-прежнему содержат только явные TODO, поэтому генератор не
придумывает publish data.

### Проверка явных model resolutions

Перед будущей генерацией разработчик может вынести недостающие решения в
отдельный JSON и проверить их без обращения к моделям или БД:

```bash
.venv/bin/python manage.py content_workflow path/to/approved.json \
  --check-resolutions path/to/model-resolutions.json \
  --approval-id ED-123 \
  --expected-checksum <полный SHA-256 из preview> \
  --output /tmp/model-resolution-check.json
```

Файл resolutions версии 1 привязан к `manifest_checksum` и явно задаёт
`course_id`, оформление темы, по одному lesson ID на каждый набор карточек,
полное оформление урока грамматики, lesson IDs для упражнений и финального
теста, а также ID и оформление чтения. Команда отклоняет неизвестные,
пропущенные, некорректные или относящиеся к другому manifest значения и создаёт
детерминированный отчёт с отдельным checksum resolutions.

Успешный отчёт означает только структурную полноту. Существование ID, конфликты
позиций и ограничения схемы будут проверяться позже на ручной границе. Режим не
импортирует ORM, не читает БД и сеть, не генерирует и не выполняет миграции.

### Исполняемый preview после полной резолюции

Из неизменившихся manifest и resolutions можно сгенерировать детерминированные
кандидаты `RunPython` и rerunnable Supabase SQL для code review:

```bash
.venv/bin/python manage.py content_workflow path/to/approved.json \
  --generate-migration-preview \
  --model-resolutions path/to/model-resolutions.json \
  --approval-id ED-123 \
  --expected-checksum <SHA-256 manifest> \
  --expected-resolutions-checksum <SHA-256 resolutions из отчёта> \
  --output-directory /tmp/b1-example-topic-migration-preview
```

Команда принимает только полностью проверенную карту и оба точных checksum.
Она пишет три review-файла только в новый или пустой внешний каталог и
отказывается от настоящих Django/Supabase migration-каталогов, обхода пути и
перезаписи. Кандидаты содержат операции, но команда их не импортирует и не
исполняет, не читает БД и не использует сеть.

Ручная граница остаётся обязательной: разработчик сверяет существование lookup
ID и ограничения актуальной схемы, переносит код в новые упорядоченные миграции,
задаёт Django dependency и имя Supabase migration, добавляет тесты, проверяет
RLS/grants и только затем отдельно применяет reviewed пару. Preview-файлы сами
по себе не являются миграциями и не должны копироваться без этой проверки.

Разработчик вручную преобразует заготовки в следующую упорядоченную пару,
сверяет стабильные ID и текущую схему, добавляет обратимое/корректирующее
поведение и тесты. До этого scaffold нельзя копировать в migration-каталоги.

## 5. Откат

Применённые миграции не редактируются и production-строки не удаляются вручную.
Откат выполняется новой forward-only корректирующей парой миграций: записи темы
с её стабильными ID выключаются, заменённые значения восстанавливаются из
предыдущей reviewed migration, после чего сверяются количества и маршруты.
Конкретный `scope_key` и эти шаги включены в publish-plan artifact.
