export type TaskType = "words" | "grammar" | "review" | "quiz";

export type DailyPlanItem = {
  id: string;
  lessonId: TaskType;
  title: string;
  subtitle: string;
  completed: boolean;
};

export type TaskCard = {
  id: string;
  type: TaskType;
  title: string;
  description: string;
  durationMin: number;
  href: string;
};

export const dailyPlanItems: DailyPlanItem[] = [
  {
    id: "1",
    lessonId: "words",
    title: "Новые слова",
    subtitle: "5 слов · A1",
    completed: false,
  },
  {
    id: "2",
    lessonId: "grammar",
    title: "Грамматика",
    subtitle: "Род существительных",
    completed: false,
  },
  {
    id: "3",
    lessonId: "review",
    title: "Повторение",
    subtitle: "12 карточек",
    completed: false,
  },
  {
    id: "4",
    lessonId: "quiz",
    title: "Мини-тест",
    subtitle: "5 вопросов",
    completed: false,
  },
];

export const taskCards: TaskCard[] = [
  {
    id: "words",
    type: "words",
    title: "Słówka dnia",
    description: "Выучи 5 новых слов с примерами",
    durationMin: 5,
    href: "/lesson/words",
  },
  {
    id: "grammar",
    type: "grammar",
    title: "Gramatyka",
    description: "Короткий урок: rodzajnik nieokreślony",
    durationMin: 8,
    href: "/lesson/grammar",
  },
  {
    id: "review",
    type: "review",
    title: "Powtórka",
    description: "Повтори слова, которые уже знаешь",
    durationMin: 6,
    href: "/lesson/review",
  },
  {
    id: "quiz",
    type: "quiz",
    title: "Quiz",
    description: "Проверь себя: перевод и аудирование",
    durationMin: 4,
    href: "/lesson/quiz",
  },
];

export type Flashcard = {
  id: string;
  polish: string;
  translation: string;
  example: string;
};

export const sampleFlashcards: Flashcard[] = [
  { id: "cześć", polish: "cześć", translation: "привет", example: "Cześć, jak się masz?" },
  { id: "dziękuję", polish: "dziękuję", translation: "спасибо", example: "Dziękuję bardzo!" },
  { id: "proszę", polish: "proszę", translation: "пожалуйста", example: "Proszę bardzo." },
  { id: "tak", polish: "tak", translation: "да", example: "Tak, zgadzam się." },
  { id: "nie", polish: "nie", translation: "нет", example: "Nie, dziękuję." },
];

export function flashcardsByIds(ids: string[]): Flashcard[] {
  const map = new Map(sampleFlashcards.map((card) => [card.id, card]));
  return ids.map((id) => map.get(id)).filter((card): card is Flashcard => Boolean(card));
}
