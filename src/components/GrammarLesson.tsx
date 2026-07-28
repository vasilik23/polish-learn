"use client";

import { LessonComplete, saveLessonProgress } from "@/components/LessonComplete";
import { grammarLesson, type GrammarExercise } from "@/lib/data/grammar-lesson";
import { useRouter } from "next/navigation";
import { useState } from "react";

type GrammarLessonProps = {
  lesson: typeof grammarLesson;
  lessonId: string;
  alreadyCompleted?: boolean;
};

type Step = "read" | "exercise" | "done";

export function GrammarLesson({
  lesson,
  lessonId,
  alreadyCompleted = false,
}: GrammarLessonProps) {
  const router = useRouter();
  const [step, setStep] = useState<Step>("read");
  const [exerciseIndex, setExerciseIndex] = useState(0);
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);
  const [correctCount, setCorrectCount] = useState(0);
  const [saving, setSaving] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);

  const exercises = lesson.exercises;
  const exercise = exercises[exerciseIndex];
  const isLastExercise = exerciseIndex >= exercises.length - 1;
  const answered = selectedIndex !== null;

  async function finishLesson(finalCorrectCount: number) {
    setSaving(true);
    setSaveError(null);

    try {
      await saveLessonProgress(lessonId, exercises.length, finalCorrectCount);
      setCorrectCount(finalCorrectCount);
      setStep("done");
      router.refresh();
    } catch (error) {
      setSaveError(
        error instanceof Error ? error.message : "Не удалось сохранить прогресс",
      );
    } finally {
      setSaving(false);
    }
  }

  function handleSelect(optionIndex: number, _current: GrammarExercise) {
    if (answered || saving) return;
    setSelectedIndex(optionIndex);
  }

  function handleNextExercise() {
    const wasCorrect = selectedIndex === exercise.correctIndex;
    const nextCorrect = correctCount + (wasCorrect ? 1 : 0);

    if (isLastExercise) {
      void finishLesson(nextCorrect);
      return;
    }

    setCorrectCount(nextCorrect);
    setExerciseIndex((i) => i + 1);
    setSelectedIndex(null);
  }

  if (step === "done") {
    return (
      <LessonComplete
        alreadyCompleted={alreadyCompleted}
        scoreLabel={`${correctCount} из ${exercises.length} верно`}
      />
    );
  }

  if (step === "read") {
    return (
      <div className="space-y-6">
        {alreadyCompleted && (
          <p className="rounded-lg bg-emerald-50 px-3 py-2 text-sm text-emerald-800">
            Вы уже проходили этот урок сегодня — можно повторить.
          </p>
        )}

        <div className="rounded-2xl bg-[var(--app-surface)] p-6 shadow-sm ring-1 ring-[var(--border)] space-y-5">
          <p className="text-sm font-medium text-[var(--primary)]">{lesson.title}</p>
          {lesson.sections.map((section) => (
            <div key={section.heading}>
              <h2 className="font-semibold text-[var(--text)]">{section.heading}</h2>
              <p className="mt-2 text-sm leading-relaxed text-[var(--text-muted)]">
                {section.body}
              </p>
            </div>
          ))}
        </div>

        <button
          type="button"
          onClick={() => setStep("exercise")}
          className="w-full rounded-xl bg-[var(--primary)] py-3.5 font-semibold text-white transition hover:bg-[var(--primary-hover)]"
        >
          К упражнениям →
        </button>
      </div>
    );
  }

  if (!exercise) return null;

  return (
    <div className="space-y-6">
      <p className="text-center text-sm text-[var(--text-muted)]">
        Упражнение {exerciseIndex + 1} из {exercises.length}
      </p>

      <div className="rounded-2xl bg-[var(--app-surface)] p-6 shadow-sm ring-1 ring-[var(--border)]">
        <p className="text-lg font-semibold text-[var(--text)]">
          {exercise.question}
        </p>
      </div>

      <div className="space-y-3">
        {exercise.options.map((option, optionIndex) => {
          const isSelected = selectedIndex === optionIndex;
          const isCorrect = optionIndex === exercise.correctIndex;
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
              onClick={() => handleSelect(optionIndex, exercise)}
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
          {exercise.explanation}
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
          onClick={handleNextExercise}
          disabled={saving}
          className="w-full rounded-xl bg-[var(--primary)] py-3.5 font-semibold text-white transition hover:bg-[var(--primary-hover)] disabled:opacity-60"
        >
          {saving ? "Сохраняем…" : isLastExercise ? "Завершить" : "Дальше →"}
        </button>
      )}
    </div>
  );
}
