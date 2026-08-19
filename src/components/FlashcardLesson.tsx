"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import type { Flashcard } from "@/lib/data/mock";

type FlashcardLessonProps = {
  cards: Flashcard[];
  title: string;
  lessonId: string;
  alreadyCompleted?: boolean;
  emptyMessage?: string;
};

async function recordReview(cardId: string, quality: "again" | "know") {
  const res = await fetch("/api/progress/card", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ cardId, quality }),
  });

  const data = (await res.json().catch(() => ({}))) as { error?: string };

  if (!res.ok) {
    throw new Error(data.error ?? "Не удалось сохранить карточку");
  }
}

async function saveLessonProgress(
  lessonId: string,
  total: number,
  known: number,
) {
  const res = await fetch("/api/progress/lesson", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      lessonId,
      cardsTotal: total,
      cardsKnown: known,
    }),
  });

  const data = (await res.json().catch(() => ({}))) as { error?: string };

  if (!res.ok) {
    throw new Error(data.error ?? "Не удалось сохранить прогресс");
  }
}

export function FlashcardLesson({
  cards,
  title,
  lessonId,
  alreadyCompleted = false,
  emptyMessage,
}: FlashcardLessonProps) {
  const router = useRouter();
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [knownCount, setKnownCount] = useState(0);
  const [finished, setFinished] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  if (cards.length === 0 && emptyMessage) {
    return (
      <div className="rounded-2xl bg-[var(--app-surface)] p-8 text-center shadow-sm ring-1 ring-[var(--border)]">
        <p className="text-4xl mb-4">✨</p>
        <p className="font-semibold text-[var(--text)]">Всё повторено!</p>
        <p className="mt-2 text-sm text-[var(--text-muted)]">{emptyMessage}</p>
        <Link
          href="/"
          className="mt-6 inline-block rounded-xl bg-[var(--primary)] px-6 py-3.5 font-semibold text-white transition hover:bg-[var(--primary-hover)]"
        >
          На главную
        </Link>
      </div>
    );
  }

  const card = cards[index];
  const isLast = index >= cards.length - 1;

  async function finishLesson(finalKnown: number) {
    setBusy(true);
    setError(null);

    try {
      await saveLessonProgress(lessonId, cards.length, finalKnown);
      setKnownCount(finalKnown);
      setFinished(true);
      router.refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Не удалось сохранить прогресс");
    } finally {
      setBusy(false);
    }
  }

  async function handleKnow() {
    if (!card || busy) return;

    setBusy(true);
    setError(null);

    try {
      await recordReview(card.id, "know");
      const nextKnown = knownCount + 1;

      if (isLast) {
        await finishLesson(nextKnown);
        return;
      }

      setKnownCount(nextKnown);
      setIndex((i) => i + 1);
      setRevealed(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Ошибка сохранения");
    } finally {
      setBusy(false);
    }
  }

  async function handleAgain() {
    if (!card || busy) return;

    setBusy(true);
    setError(null);

    try {
      await recordReview(card.id, "again");
      setRevealed(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Ошибка сохранения");
    } finally {
      setBusy(false);
    }
  }

  if (finished) {
    return (
      <div className="rounded-2xl bg-[var(--app-surface)] p-8 text-center shadow-sm ring-1 ring-[var(--border)]">
        <p className="text-4xl mb-4">🎉</p>
        <p className="font-semibold text-[var(--text)]">Урок завершён!</p>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          {alreadyCompleted
            ? "Прогресс обновлён. SM-2 запланировал следующие повторения."
            : "Прогресс сохранён — карточки пойдут в повтор по расписанию SM-2."}
        </p>
        <p className="mt-1 text-sm font-medium text-[var(--primary)]">
          {knownCount} из {cards.length} «Знаю»
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
          Вы уже проходили этот урок сегодня — можно повторить.
        </p>
      )}

      <p className="text-center text-sm text-[var(--text-muted)]">
        Карточка {index + 1} из {cards.length}
      </p>

      <button
        type="button"
        onClick={() => setRevealed(true)}
        disabled={busy}
        className="w-full rounded-2xl bg-[var(--app-surface)] p-8 text-center shadow-sm ring-1 ring-[var(--border)] transition active:scale-[0.99] min-h-[220px] flex flex-col items-center justify-center disabled:opacity-60"
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

      {error && (
        <p className="rounded-lg bg-red-50 px-3 py-2 text-sm text-red-700">
          {error}
        </p>
      )}

      {revealed && (
        <div className="grid grid-cols-2 gap-3">
          <button
            type="button"
            onClick={() => void handleAgain()}
            disabled={busy}
            className="rounded-xl border border-[var(--border)] py-3.5 font-semibold text-[var(--text)] transition hover:bg-[var(--app-bg)] disabled:opacity-60"
          >
            Ещё раз
          </button>
          <button
            type="button"
            onClick={() => void handleKnow()}
            disabled={busy}
            className="rounded-xl bg-[var(--primary)] py-3.5 font-semibold text-white transition hover:bg-[var(--primary-hover)] disabled:opacity-60"
          >
            {busy ? "…" : isLast ? "Завершить" : "Знаю →"}
          </button>
        </div>
      )}
    </div>
  );
}
