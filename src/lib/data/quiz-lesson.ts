export type QuizQuestion = {
  id: string;
  prompt: string;
  hint?: string;
  options: string[];
  correctIndex: number;
  explanation: string;
};

export const quizQuestions: QuizQuestion[] = [
  {
    id: "1",
    prompt: "Как переводится «cześć»?",
    options: ["спасибо", "привет", "пожалуйста", "до свидания"],
    correctIndex: 1,
    explanation: "Cześć — неформальное «привет».",
  },
  {
    id: "2",
    prompt: "Что значит «dziękuję»?",
    options: ["нет", "да", "спасибо", "извините"],
    correctIndex: 2,
    explanation: "Dziękuję = спасибо.",
  },
  {
    id: "3",
    prompt: "Выберите перевод «proszę»",
    options: ["пожалуйста", "утро", "вечер", "комната"],
    correctIndex: 0,
    explanation: "Proszę — «пожалуйста» или «прошу».",
  },
  {
    id: "4",
    prompt: "Как будет «да» по-польски?",
    options: ["nie", "tak", "dom", "kawa"],
    correctIndex: 1,
    explanation: "Tak = да.",
  },
  {
    id: "5",
    prompt: "Как будет «нет» по-польски?",
    options: ["tak", "cześć", "nie", "miasto"],
    correctIndex: 2,
    explanation: "Nie = нет.",
  },
];
