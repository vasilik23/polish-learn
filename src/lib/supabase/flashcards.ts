import type { SupabaseClient } from "@supabase/supabase-js";
import { DEFAULT_SM2_STATE, sm2Next, type ReviewQuality } from "@/lib/sm2";
import { todayUtcDate } from "@/lib/supabase/progress";

export type FlashcardReviewRow = {
  card_id: string;
  ease_factor: number;
  interval_days: number;
  repetitions: number;
  next_review_date: string;
};

export async function recordCardReview(
  supabase: SupabaseClient,
  userId: string,
  cardId: string,
  quality: ReviewQuality,
): Promise<FlashcardReviewRow> {
  const today = todayUtcDate();

  const { data: existing, error: readError } = await supabase
    .from("flashcard_reviews")
    .select("ease_factor, interval_days, repetitions")
    .eq("user_id", userId)
    .eq("card_id", cardId)
    .maybeSingle();

  if (readError) {
    throw readError;
  }

  const current = existing
    ? {
        easeFactor: existing.ease_factor,
        intervalDays: existing.interval_days,
        repetitions: existing.repetitions,
      }
    : DEFAULT_SM2_STATE;

  const next = sm2Next(current, quality, today);

  const row = {
    user_id: userId,
    card_id: cardId,
    ease_factor: next.easeFactor,
    interval_days: next.intervalDays,
    repetitions: next.repetitions,
    next_review_date: next.nextReviewDate,
    last_reviewed_at: new Date().toISOString(),
  };

  const { data, error } = await supabase
    .from("flashcard_reviews")
    .upsert(row, { onConflict: "user_id,card_id" })
    .select("card_id, ease_factor, interval_days, repetitions, next_review_date")
    .single();

  if (error) {
    throw error;
  }

  return data as FlashcardReviewRow;
}

export async function getDueCardIds(
  supabase: SupabaseClient,
  userId: string,
): Promise<string[]> {
  const today = todayUtcDate();

  const { data, error } = await supabase
    .from("flashcard_reviews")
    .select("card_id")
    .eq("user_id", userId)
    .lte("next_review_date", today)
    .order("next_review_date", { ascending: true });

  if (error) {
    throw error;
  }

  return (data ?? []).map((row) => row.card_id);
}

export async function countDueCards(
  supabase: SupabaseClient,
  userId: string,
): Promise<number> {
  const ids = await getDueCardIds(supabase, userId);
  return ids.length;
}
