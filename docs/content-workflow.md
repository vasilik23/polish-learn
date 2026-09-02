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
    "active_units": ["12–20 элементов"],
    "card_sets": [["5–8 карточек"], ["5–8 карточек"]],
    "grammar": {"summary": "Объяснение"},
    "exercises": ["минимум 5 объектов"],
    "reading": {
      "paragraphs": ["непустой текст"],
      "glossary": {"форма": {"lemma": "лемма", "translation": "перевод"}}
    },
    "final_quiz": ["минимум 8 объектов"]
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

Элементы внутри списков могут быть полноценными объектами будущего импортера.
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
создаёт четыре review-артефакта: точный `approved-manifest.json`, метаданные с
checksum и approval ID, Django scaffold и SQL scaffold. Последние содержат
только явные TODO: manifest версии 1 ещё не описывает модели, таблицы, связи и
конфликты достаточно строго, поэтому генератор не придумывает publish data.

Разработчик вручную преобразует заготовки в следующую упорядоченную пару,
сверяет стабильные ID и текущую схему, добавляет обратимое/корректирующее
поведение и тесты. До этого scaffold нельзя копировать в migration-каталоги.

## 5. Откат

Применённые миграции не редактируются и production-строки не удаляются вручную.
Откат выполняется новой forward-only корректирующей парой миграций: записи темы
с её стабильными ID выключаются, заменённые значения восстанавливаются из
предыдущей reviewed migration, после чего сверяются количества и маршруты.
Конкретный `scope_key` и эти шаги включены в publish-plan artifact.
