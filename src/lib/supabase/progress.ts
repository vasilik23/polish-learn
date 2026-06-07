import type { SupabaseClient } from "@supabase/supabase-js";
import type { TaskType } from "@/lib/data/mock";

export type LessonCompletion = {
  lesson_id: TaskType;
  cards_total: number;
  cards_known: number;
  completed_at: string;
};

export function todayUtcDate(): string {
  return new Date().toISOString().slice(0, 10);
}

export function yesterdayUtcDate(): string {
  const date = new Date();
  date.setUTCDate(date.getUTCDate() - 1);
  return date.toISOString().slice(0, 10);
}

export async function getTodayCompletions(
  supabase: SupabaseClient,
  userId: string,
): Promise<LessonCompletion[]> {
  const { data, error } = await supabase
    .from("lesson_completions")
    .select("lesson_id, cards_total, cards_known, completed_at")
    .eq("user_id", userId)
    .eq("plan_date", todayUtcDate());

  if (error) {
    throw error;
  }

  return (data ?? []) as LessonCompletion[];
}

export async function isLessonCompletedToday(
  supabase: SupabaseClient,
  userId: string,
  lessonId: TaskType,
): Promise<boolean> {
  const { data, error } = await supabase
    .from("lesson_completions")
    .select("id")
    .eq("user_id", userId)
    .eq("lesson_id", lessonId)
    .eq("plan_date", todayUtcDate())
    .maybeSingle();

  if (error) {
    throw error;
  }

  return Boolean(data);
}

type CompleteLessonInput = {
  userId: string;
  lessonId: TaskType;
  cardsTotal: number;
  cardsKnown: number;
};

export async function completeLesson(
  supabase: SupabaseClient,
  input: CompleteLessonInput,
): Promise<void> {
  const today = todayUtcDate();
  const yesterday = yesterdayUtcDate();

  const { error: completionError } = await supabase.from("lesson_completions").upsert(
    {
      user_id: input.userId,
      lesson_id: input.lessonId,
      plan_date: today,
      cards_total: input.cardsTotal,
      cards_known: input.cardsKnown,
      completed_at: new Date().toISOString(),
    },
    { onConflict: "user_id,lesson_id,plan_date" },
  );

  if (completionError) {
    throw completionError;
  }

  const { data: profile, error: profileReadError } = await supabase
    .from("profiles")
    .select("streak_days, last_active_date")
    .eq("id", input.userId)
    .single();

  if (profileReadError) {
    throw profileReadError;
  }

  if (profile.last_active_date === today) {
    return;
  }

  let streakDays = 1;
  if (profile.last_active_date === yesterday) {
    streakDays = (profile.streak_days ?? 0) + 1;
  }

  const { error: profileUpdateError } = await supabase
    .from("profiles")
    .update({
      streak_days: streakDays,
      last_active_date: today,
    })
    .eq("id", input.userId);

  if (profileUpdateError) {
    throw profileUpdateError;
  }
}
