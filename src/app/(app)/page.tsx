import { DailyPlan } from "@/components/DailyPlan";
import { MobileShell } from "@/components/MobileShell";
import { SignOutButton } from "@/components/SignOutButton";
import { TaskCard } from "@/components/TaskCard";
import { dailyPlanItems, taskCards } from "@/lib/data/mock";
import { createClient } from "@/lib/supabase/server";

export default async function HomePage() {
  let email = "ученик";

  if (
    process.env.NEXT_PUBLIC_SUPABASE_URL &&
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
  ) {
    const supabase = await createClient();
    const {
      data: { user },
    } = await supabase.auth.getUser();
    if (user?.email) email = user.email;
  }
  const displayName = email.split("@")[0];
  const completedCount = dailyPlanItems.filter((i) => i.completed).length;

  const today = new Intl.DateTimeFormat("ru-RU", {
    weekday: "long",
    day: "numeric",
    month: "long",
  }).format(new Date());

  return (
    <MobileShell headerRight={<SignOutButton />}>
      <section className="mb-6">
        <p className="text-sm capitalize text-[var(--text-muted)]">{today}</p>
        <h1 className="mt-1 text-2xl font-bold text-[var(--text)]">
          Cześć, {displayName}! 👋
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Уровень A1 · серия 0 дней
        </p>
      </section>

      <div className="mb-6">
        <DailyPlan items={dailyPlanItems} completedCount={completedCount} />
      </div>

      <section>
        <h2 className="mb-3 text-lg font-semibold text-[var(--text)]">
          Задания
        </h2>
        <div className="space-y-3">
          {taskCards.map((card) => (
            <TaskCard key={card.id} card={card} />
          ))}
        </div>
      </section>
    </MobileShell>
  );
}
