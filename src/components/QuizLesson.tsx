"use client";

import { LessonComplete, saveLessonProgress } from "@/components/LessonComplete";
import type { QuizQuestion } from "@/lib/data/quiz-lesson";
import { useRouter } from "next/navigation";
import { useState } from "react";

type QuizLessonProps = {
  questions: QuizQuestion[];
  lessonId: string;
  alreadyCompleted?: boolean;
};

export function QuizLesson({
  questions,
  lessonId,
  alreadyCompleted = false,
}: QuizLessonProps) {
  const router = useRouter();
  const [index, setIndex] = useState(0);
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);
  const [correctCount, setCorrectCount] = useState(0);
  const [finished, setFinished] = useState(false);
  const [saving, setSaving] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);

  const question = questions[index];
  const isLast = index >= questions.length - 1;
  const answered = selectedIndex !== null;

  async function finishLesson(finalCorrectCount: number) {
    setSaving(true);
    setSaveError(null);

    try {
      await saveLessonProgress(lessonId, questions.length, finalCorrectCount);
      setCorrectCount(finalCorrectCount);
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

  function handleSelect(optionIndex: number) {
    if (answered || saving) return;
    setSelectedIndex(optionIndex);
  }

  function handleNext() {
    const wasCorrect = selectedIndex === question.correctIndex;
    const nextCorrect = correctCount + (wasCorrect ? 1 : 0);

    if (isLast) {
      void finishLesson(nextCorrect);
      return;
    }

    setCorrectCount(nextCorrect);
    setIndex((i) => i + 1);
    setSelectedIndex(null);
  }

  if (finished) {
    return (
      <LessonComplete
        alreadyCompleted={alreadyCompleted}
        scoreLabel={`${correctCount} из ${questions.length} верно`}
      />
    );
  }

  if (!question) return null;

  return (
    <div className="space-y-6">
      {alreadyCompleted && (
        <p className="rounded-lg bg-emerald-50 px-3 py-2 text-sm text-emerald-800">
          Вы уже проходили этот тест сегодня — можно пройти ещё раз.
        </p>
      )}

      <p className="text-center text-sm text-[var(--text-muted)]">
        Вопрос {index + 1} из {questions.length}
      </p>

      <div className="rounded-2xl bg-[var(--app-surface)] p-6 shadow-sm ring-1 ring-[var(--border)]">
        <p className="text-lg font-semibold text-[var(--text)]">{question.prompt}</p>
        {question.hint && (
          <p className="mt-2 text-sm text-[var(--text-muted)]">{question.hint}</p>
        )}
      </div>

      <div className="space-y-3">
        {question.options.map((option, optionIndex) => {
          const isSelected = selectedIndex === optionIndex;
          const isCorrect = optionIndex === question.correctIndex;
          let style =
            "border-[var(--border)] bg-[var(--app-surface)] text-[var(--text)] hover:ring-[var(--primary)]/30";

          if (answered) {
            if (isCorrect) {
              style =
                "border-emerald-500 bg-emerald-50 text-emerald-900 ring-1 ring-emerald-500";
            } else if (isSelected) {
              style = "border-red-400 bg-red-50 text-red-900 ring-1 ring-red-400";
            } else {
              style = "border-[var(--border)] bg-[var(--app-bg)] text-[var(--text-muted)]";
            }
          }

          return (
            <button
              key={option}
              type="button"
              onClick={() => handleSelect(optionIndex)}
              disabled={answered || saving}
              className={`w-full rounded-xl border px-4 py-3.5 text-left font-medium transition ring-1 ring-transparent disabled:cursor-default ${style}`}
            >
              {option}
            </button>
          );
        })}
      </div>

      {answered && (
        <p className="rounded-lg bg-[var(--app-bg)] px-3 py-2 text-sm text-[var(--text-muted)]">
          {question.explanation}
        </p>
      )}

      {saveError && (
        <p className="rounded-lg bg-red-50 px-3 py-2 text-sm text-red-700">
          {saveError}
        </p>
      )}

      {answered && (
        <button
          type="button"
          onClick={handleNext}
          disabled={saving}
          className="w-full rounded-xl bg-[var(--primary)] py-3.5 font-semibold text-white transition hover:bg-[var(--primary-hover)] disabled:opacity-60"
        >
          {saving ? "Сохраняем…" : isLast ? "Завершить" : "Дальше →"}
        </button>
      )}
    </div>
  );
}
