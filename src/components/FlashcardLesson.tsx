"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";

type Card = {
  polish: string;
  translation: string;
  example: string;
};

type FlashcardLessonProps = {
  cards: Card[];
  title: string;
  lessonId: string;
  alreadyCompleted?: boolean;
};

export function FlashcardLesson({
  cards,
  title,
  lessonId,
  alreadyCompleted = false,
}: FlashcardLessonProps) {
  const router = useRouter();
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [knownCount, setKnownCount] = useState(0);
  const [finished, setFinished] = useState(false);
  const [saving, setSaving] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);

  const card = cards[index];
  const isLast = index >= cards.length - 1;

  async function saveProgress(cardsKnown: number) {
    setSaving(true);
    setSaveError(null);

    try {
      const res = await fetch("/api/progress/lesson", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          lessonId,
          cardsTotal: cards.length,
          cardsKnown,
        }),
      });

      const data = (await res.json().catch(() => ({}))) as { error?: string };

      if (!res.ok) {
        throw new Error(data.error ?? "Не удалось сохранить прогресс");
      }

      setFinished(true);
      router.refresh();
    } catch (error) {
      setSaveError(
        error instanceof Error ? error.message : "Не удалось сохранить прогресс",
      );
    } finally {
      setSaving(false);
    }
  }

  function handleKnow() {
    const nextKnownCount = knownCount + 1;

    if (isLast) {
      void saveProgress(nextKnownCount);
      return;
    }

    setKnownCount(nextKnownCount);
    setIndex((i) => i + 1);
    setRevealed(false);
  }

  function handleAgain() {
    setRevealed(false);
  }

  if (finished) {
    return (
      <div className="rounded-2xl bg-[var(--app-surface)] p-8 text-center shadow-sm ring-1 ring-[var(--border)]">
        <p className="text-4xl mb-4">🎉</p>
        <p className="font-semibold text-[var(--text)]">Урок завершён!</p>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          {alreadyCompleted && !saving
            ? "Вы уже проходили этот урок сегодня. Прогресс сохранён."
            : "Прогресс сохранён — пункт плана на главной отмечен."}
        </p>
        <Link
          href="/"
          className="mt-6 inline-block rounded-xl bg-[var(--primary)] px-6 py-3.5 font-semibold text-white transition hover:bg-[var(--primary-hover)]"
        >
          На главную
        </Link>
      </div>
    );
  }

  if (!card) return null;

  return (
    <div className="space-y-6">
      {alreadyCompleted && (
        <p className="rounded-lg bg-emerald-50 px-3 py-2 text-sm text-emerald-800">
          Вы уже прошли этот урок сегодня — можно повторить или вернуться на главную.
        </p>
      )}

      <p className="text-center text-sm text-[var(--text-muted)]">
        Карточка {index + 1} из {cards.length}
      </p>

      <button
        type="button"
        onClick={() => setRevealed(true)}
        className="w-full rounded-2xl bg-[var(--app-surface)] p-8 text-center shadow-sm ring-1 ring-[var(--border)] transition active:scale-[0.99] min-h-[220px] flex flex-col items-center justify-center"
      >
        <p className="text-sm font-medium text-[var(--primary)]">{title}</p>
        <p className="mt-4 text-4xl font-bold text-[var(--text)]">{card.polish}</p>
        {revealed ? (
          <>
            <p className="mt-4 text-xl text-[var(--text-muted)]">
              {card.translation}
            </p>
            <p className="mt-3 text-sm italic text-[var(--text-muted)]">
              {card.example}
            </p>
          </>
        ) : (
          <p className="mt-6 text-sm text-[var(--text-muted)]">
            Нажми, чтобы увидеть перевод
          </p>
        )}
      </button>

      {saveError && (
        <p className="rounded-lg bg-red-50 px-3 py-2 text-sm text-red-700">
          {saveError}
        </p>
      )}

      {revealed && (
        <div className="grid grid-cols-2 gap-3">
          <button
            type="button"
            onClick={handleAgain}
            disabled={saving}
            className="rounded-xl border border-[var(--border)] py-3.5 font-semibold text-[var(--text)] transition hover:bg-[var(--app-bg)] disabled:opacity-60"
          >
            Ещё раз
          </button>
          <button
            type="button"
            onClick={handleKnow}
            disabled={saving}
            className="rounded-xl bg-[var(--primary)] py-3.5 font-semibold text-white transition hover:bg-[var(--primary-hover)] disabled:opacity-60"
          >
            {saving ? "Сохраняем…" : isLast ? "Завершить" : "Знаю →"}
          </button>
        </div>
      )}
    </div>
  );
}
