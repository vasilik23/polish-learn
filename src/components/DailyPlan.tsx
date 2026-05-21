import type { DailyPlanItem } from "@/lib/data/mock";

type DailyPlanProps = {
  items: DailyPlanItem[];
  completedCount: number;
};

export function DailyPlan({ items, completedCount }: DailyPlanProps) {
  const total = items.length;
  const progress = total > 0 ? Math.round((completedCount / total) * 100) : 0;

  return (
    <section className="rounded-2xl bg-[var(--app-surface)] p-4 shadow-sm ring-1 ring-[var(--border)]">
      <div className="mb-4 flex items-end justify-between gap-2">
        <div>
          <p className="text-sm font-medium text-[var(--primary)]">План на день</p>
          <h2 className="text-xl font-bold text-[var(--text)]">
            {completedCount} из {total} заданий
          </h2>
        </div>
        <span className="text-2xl font-bold text-[var(--primary)]">{progress}%</span>
      </div>

      <div className="mb-4 h-2 overflow-hidden rounded-full bg-[var(--app-bg)]">
        <div
          className="h-full rounded-full bg-[var(--primary)] transition-all duration-500"
          style={{ width: `${progress}%` }}
        />
      </div>

      <ul className="space-y-2">
        {items.map((item) => (
          <li
            key={item.id}
            className="flex items-center gap-3 rounded-xl bg-[var(--app-bg)] px-3 py-3"
          >
            <span
              className={`flex h-6 w-6 shrink-0 items-center justify-center rounded-full text-xs font-bold ${
                item.completed
                  ? "bg-[var(--primary)] text-white"
                  : "border-2 border-[var(--border)] text-transparent"
              }`}
              aria-hidden
            >
              ✓
            </span>
            <div className="min-w-0 flex-1">
              <p
                className={`font-medium ${item.completed ? "text-[var(--text-muted)] line-through" : "text-[var(--text)]"}`}
              >
                {item.title}
              </p>
              <p className="text-sm text-[var(--text-muted)]">{item.subtitle}</p>
            </div>
          </li>
        ))}
      </ul>
    </section>
  );
}
