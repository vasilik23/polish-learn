"use client";

import { useState } from "react";

type Card = {
  polish: string;
  translation: string;
  example: string;
};

type FlashcardLessonProps = {
  cards: Card[];
  title: string;
};

export function FlashcardLesson({ cards, title }: FlashcardLessonProps) {
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);

  const card = cards[index];
  const isLast = index >= cards.length - 1;

  function handleKnow() {
    if (isLast) {
      setIndex(0);
      setRevealed(false);
      return;
    }
    setIndex((i) => i + 1);
    setRevealed(false);
  }

  function handleAgain() {
    setRevealed(false);
  }

  if (!card) return null;

  return (
    <div className="space-y-6">
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

      {revealed && (
        <div className="grid grid-cols-2 gap-3">
          <button
            type="button"
            onClick={handleAgain}
            className="rounded-xl border border-[var(--border)] py-3.5 font-semibold text-[var(--text)] transition hover:bg-[var(--app-bg)]"
          >
            Ещё раз
          </button>
          <button
            type="button"
            onClick={handleKnow}
            className="rounded-xl bg-[var(--primary)] py-3.5 font-semibold text-white transition hover:bg-[var(--primary-hover)]"
          >
            {isLast ? "Сначала" : "Знаю →"}
          </button>
        </div>
      )}
    </div>
  );
}
