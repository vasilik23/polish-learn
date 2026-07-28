import { FlashcardLesson } from "@/components/FlashcardLesson";
import { GrammarLesson } from "@/components/GrammarLesson";
import { MobileShell } from "@/components/MobileShell";
import { QuizLesson } from "@/components/QuizLesson";
import { grammarLesson } from "@/lib/data/grammar-lesson";
import { sampleFlashcards, taskCards, type TaskType } from "@/lib/data/mock";
import { quizQuestions } from "@/lib/data/quiz-lesson";
import { isLessonCompletedToday } from "@/lib/supabase/progress";
import { createClient } from "@/lib/supabase/server";
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

async function getAlreadyCompleted(lessonId: string): Promise<boolean> {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) {
    return false;
  }

  try {
    return await isLessonCompletedToday(supabase, user.id, lessonId as TaskType);
  } catch {
    return false;
  }
}

export default async function LessonPage({ params }: PageProps) {
  const { id } = await params;
  const card = taskCards.find((c) => c.id === id);

  if (!card) {
    notFound();
  }

  const title = lessonTitles[id] ?? card.title;
  const alreadyCompleted = await getAlreadyCompleted(id);

  return (
    <MobileShell title={title} showBack backHref="/">
      {id === "words" || id === "review" ? (
        <FlashcardLesson
          cards={sampleFlashcards}
          title={card.title}
          lessonId={id}
          alreadyCompleted={alreadyCompleted}
        />
      ) : id === "grammar" ? (
        <GrammarLesson
          lesson={grammarLesson}
          lessonId={id}
          alreadyCompleted={alreadyCompleted}
        />
      ) : id === "quiz" ? (
        <QuizLesson
          questions={quizQuestions}
          lessonId={id}
          alreadyCompleted={alreadyCompleted}
        />
      ) : null}
    </MobileShell>
  );
}
