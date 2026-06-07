import { DailyPlan } from "@/components/DailyPlan";
import { MobileShell } from "@/components/MobileShell";
import { SignOutButton } from "@/components/SignOutButton";
import { TaskCard } from "@/components/TaskCard";
import { dailyPlanItems, taskCards } from "@/lib/data/mock";
import { ensureProfile, formatStreak } from "@/lib/supabase/profile";
import { getTodayCompletions } from "@/lib/supabase/progress";
import { createClient } from "@/lib/supabase/server";

export default async function HomePage() {
  let displayName = "ученик";
  let level = "A1";
  let streakDays = 0;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  let planItems = dailyPlanItems;

  if (user) {
    try {
      const profile = await ensureProfile(supabase, user.id, user.email);
      displayName =
        profile.display_name ?? user.email?.split("@")[0] ?? displayName;
      level = profile.level;
      streakDays = profile.streak_days ?? 0;

      const completions = await getTodayCompletions(supabase, user.id);
      const completedLessonIds = new Set(completions.map((item) => item.lesson_id));

      planItems = dailyPlanItems.map((item) => ({
        ...item,
        completed: completedLessonIds.has(item.lessonId),
      }));
    } catch {
      displayName = user.email?.split("@")[0] ?? displayName;
    }
  }

  const completedCount = planItems.filter((item) => item.completed).length;

  const today = new Intl.DateTimeFormat("ru-RU", {
    weekday: "long",
    day: "numeric",
    month: "long",
  }).format(new Date());

  const streakLabel =
    streakDays > 0 ? formatStreak(streakDays) : "0 дней";

  return (
    <MobileShell headerRight={<SignOutButton />}>
      <section className="mb-6">
        <p className="text-sm capitalize text-[var(--text-muted)]">{today}</p>
        <h1 className="mt-1 text-2xl font-bold text-[var(--text)]">
          Cześć, {displayName}! 👋
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Уровень {level} · серия {streakLabel}
        </p>
      </section>

      <div className="mb-6">
        <DailyPlan items={planItems} completedCount={completedCount} />
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
