export type ReviewQuality = "again" | "know";

export type Sm2State = {
  easeFactor: number;
  intervalDays: number;
  repetitions: number;
};

const MIN_EASE = 1.3;

/** SM-2 quality: again = 1, know = 5 */
function toQuality(quality: ReviewQuality): number {
  return quality === "know" ? 5 : 1;
}

export function sm2Next(
  state: Sm2State,
  quality: ReviewQuality,
  today: string,
): Sm2State & { nextReviewDate: string } {
  const q = toQuality(quality);
  let { easeFactor, intervalDays, repetitions } = state;

  if (q < 3) {
    repetitions = 0;
    intervalDays = 1;
  } else {
    if (repetitions === 0) {
      intervalDays = 1;
    } else if (repetitions === 1) {
      intervalDays = 6;
    } else {
      intervalDays = Math.max(1, Math.round(intervalDays * easeFactor));
    }
    repetitions += 1;
  }

  easeFactor = Math.max(
    MIN_EASE,
    easeFactor + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)),
  );

  const next = new Date(`${today}T00:00:00.000Z`);
  next.setUTCDate(next.getUTCDate() + intervalDays);

  return {
    easeFactor,
    intervalDays,
    repetitions,
    nextReviewDate: next.toISOString().slice(0, 10),
  };
}

export const DEFAULT_SM2_STATE: Sm2State = {
  easeFactor: 2.5,
  intervalDays: 0,
  repetitions: 0,
};
