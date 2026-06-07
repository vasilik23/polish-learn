import type { SupabaseClient } from "@supabase/supabase-js";

export type Profile = {
  id: string;
  display_name: string | null;
  level: string;
  streak_days: number;
  last_active_date: string | null;
};

export async function ensureProfile(
  supabase: SupabaseClient,
  userId: string,
  email?: string | null,
): Promise<Profile> {
  const { data: existing } = await supabase
    .from("profiles")
    .select("id, display_name, level, streak_days, last_active_date")
    .eq("id", userId)
    .maybeSingle();

  if (existing) {
    return existing as Profile;
  }

  const displayName = email?.split("@")[0] ?? "ученик";
  const { data: created, error } = await supabase
    .from("profiles")
    .insert({ id: userId, display_name: displayName })
    .select("id, display_name, level, streak_days, last_active_date")
    .single();

  if (error) {
    throw error;
  }

  return created as Profile;
}

export function formatStreak(streakDays: number): string {
  const n = streakDays % 100;
  const n10 = n % 10;

  if (n10 === 1 && n !== 11) return `${streakDays} день`;
  if (n10 >= 2 && n10 <= 4 && (n < 10 || n >= 20)) return `${streakDays} дня`;
  return `${streakDays} дней`;
}
