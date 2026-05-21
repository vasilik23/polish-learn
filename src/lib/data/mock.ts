export type TaskType = "words" | "grammar" | "review" | "quiz";

export type DailyPlanItem = {
  id: string;
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
    title: "Новые слова",
    subtitle: "5 слов · A1",
    completed: false,
  },
  {
    id: "2",
    title: "Грамматика",
    subtitle: "Род существительных",
    completed: false,
  },
  {
    id: "3",
    title: "Повторение",
    subtitle: "12 карточек",
    completed: false,
  },
  {
    id: "4",
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

export const sampleFlashcards = [
  { polish: "cześć", translation: "привет", example: "Cześć, jak się masz?" },
  { polish: "dziękuję", translation: "спасибо", example: "Dziękuję bardzo!" },
  { polish: "proszę", translation: "пожалуйста", example: "Proszę bardzo." },
  { polish: "tak", translation: "да", example: "Tak, zgadzam się." },
  { polish: "nie", translation: "нет", example: "Nie, dziękuję." },
];
