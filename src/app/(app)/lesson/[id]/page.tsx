import { FlashcardLesson } from "@/components/FlashcardLesson";
import { MobileShell } from "@/components/MobileShell";
import { sampleFlashcards, taskCards } from "@/lib/data/mock";
import { notFound } from "next/navigation";

const lessonTitles: Record<string, string> = {
  words: "Новые слова",
  grammar: "Грамматика",
  review: "Повторение",
  quiz: "Мини-тест",
};

type PageProps = {
  params: Promise<{ id: string }>;
};

export default async function LessonPage({ params }: PageProps) {
  const { id } = await params;
  const card = taskCards.find((c) => c.id === id);

  if (!card) {
    notFound();
  }

  const title = lessonTitles[id] ?? card.title;

  return (
    <MobileShell title={title} showBack backHref="/">
      {id === "words" || id === "review" ? (
        <FlashcardLesson cards={sampleFlashcards} title={card.title} />
      ) : (
        <div className="rounded-2xl bg-[var(--app-surface)] p-6 text-center shadow-sm ring-1 ring-[var(--border)]">
          <p className="text-4xl mb-4">🚧</p>
          <p className="font-semibold text-[var(--text)]">Скоро здесь</p>
          <p className="mt-2 text-sm text-[var(--text-muted)]">
            Тип задания «{card.title}» добавим на следующем шаге. Пока
            попробуйте «Słówka dnia» или «Powtórka».
          </p>
        </div>
      )}
    </MobileShell>
  );
}
