"use client";

import Link from "next/link";

type LessonCompleteProps = {
  scoreLabel?: string;
  alreadyCompleted?: boolean;
};

export function LessonComplete({
  scoreLabel,
  alreadyCompleted = false,
}: LessonCompleteProps) {
  return (
    <div className="rounded-2xl bg-[var(--app-surface)] p-8 text-center shadow-sm ring-1 ring-[var(--border)]">
      <p className="text-4xl mb-4">🎉</p>
      <p className="font-semibold text-[var(--text)]">Урок завершён!</p>
      {scoreLabel && (
        <p className="mt-2 text-lg font-medium text-[var(--primary)]">
          {scoreLabel}
        </p>
      )}
      <p className="mt-2 text-sm text-[var(--text-muted)]">
        {alreadyCompleted
          ? "Вы уже проходили этот урок сегодня. Прогресс обновлён."
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

export async function saveLessonProgress(
  lessonId: string,
  total: number,
  correct: number,
): Promise<void> {
  const res = await fetch("/api/progress/lesson", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      lessonId,
      cardsTotal: total,
      cardsKnown: correct,
    }),
  });

  const data = (await res.json().catch(() => ({}))) as { error?: string };

  if (!res.ok) {
    throw new Error(data.error ?? "Не удалось сохранить прогресс");
  }
}
