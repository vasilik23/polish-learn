export type GrammarExercise = {
  id: string;
  question: string;
  options: string[];
  correctIndex: number;
  explanation: string;
};

export const grammarLesson = {
  title: "Rodzajnik i ród rzeczownika",
  sections: [
    {
      heading: "Род существительных",
      body: "В польском у каждого существительного есть род: мужской, женский или средний. От рода зависит форма прилагательных и местоимений.",
    },
    {
      heading: "Примеры",
      body: "dom (дом) — мужской · kawa (кофе) — женский · miasto (город) — средний.",
    },
    {
      heading: "Неопределённость",
      body: "В польском нет артиклей «a/an/the», как в английском. «A cat» просто kot, а «the cat» — ten kot.",
    },
  ],
  exercises: [
    {
      id: "1",
      question: "Слово «kawa» (кофе) — это род…",
      options: ["мужской", "женский", "средний"],
      correctIndex: 1,
      explanation: "Kawa оканчивается на -a и относится к женскому роду.",
    },
    {
      id: "2",
      question: "Слово «dom» (дом) — это род…",
      options: ["мужской", "женский", "средний"],
      correctIndex: 0,
      explanation: "Dom — существительное мужского рода.",
    },
    {
      id: "3",
      question: "Слово «miasto» (город) — это род…",
      options: ["мужской", "женский", "средний"],
      correctIndex: 2,
      explanation: "Miasto — существительное среднего рода.",
    },
  ] satisfies GrammarExercise[],
};
