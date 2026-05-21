import Link from "next/link";
import type { TaskCard as TaskCardType, TaskType } from "@/lib/data/mock";

const typeStyles: Record<
  TaskType,
  { emoji: string; accent: string; bg: string }
> = {
  words: { emoji: "📚", accent: "text-red-700", bg: "bg-red-50" },
  grammar: { emoji: "✏️", accent: "text-amber-700", bg: "bg-amber-50" },
  review: { emoji: "🔄", accent: "text-emerald-700", bg: "bg-emerald-50" },
  quiz: { emoji: "🎯", accent: "text-violet-700", bg: "bg-violet-50" },
};

type TaskCardProps = {
  card: TaskCardType;
};

export function TaskCard({ card }: TaskCardProps) {
  const style = typeStyles[card.type];

  return (
    <Link
      href={card.href}
      className="block rounded-2xl bg-[var(--app-surface)] p-4 shadow-sm ring-1 ring-[var(--border)] transition active:scale-[0.98] hover:ring-[var(--primary)]/30"
    >
      <div className="flex items-start gap-3">
        <span
          className={`flex h-12 w-12 shrink-0 items-center justify-center rounded-xl text-2xl ${style.bg}`}
        >
          {style.emoji}
        </span>
        <div className="min-w-0 flex-1">
          <div className="flex items-center justify-between gap-2">
            <h3 className={`font-semibold ${style.accent}`}>{card.title}</h3>
            <span className="shrink-0 text-xs text-[var(--text-muted)]">
              ~{card.durationMin} мин
            </span>
          </div>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            {card.description}
          </p>
        </div>
        <span className="shrink-0 text-[var(--text-muted)]" aria-hidden>
          →
        </span>
      </div>
    </Link>
  );
}
