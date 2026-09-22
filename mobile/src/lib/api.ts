import { config } from './config';

export type TodayTask = { id: string; title: string; description: string; minutes: number; emoji: string; completed: boolean; plan_type: string; reinforcement_reason: string | null };
export type LessonStep = { position: number; type: 'flashcard' | 'choice' | 'sentence_builder'; polish?: string; translation?: string; example?: string; prompt?: string; options?: string[]; tokens?: string[] };
export type NativeLesson = { lesson: { id: string; kind: string; title: string; description?: string }; theory: { title: string; sections: unknown[] } | null; steps: LessonStep[]; step_count: number };
export type AnswerResult = { correct: boolean; correct_index?: number; correct_sentence?: string; explanation: string };
export type BootstrapData = {
  profile: { display_name: string; level: string; daily_goal_lessons: number };
  progress: { streak_days: number; active_days: number; completed_lesson_count: number };
  today: { date: string; completed_count: number; task_count: number; progress_percent: number; tasks: TodayTask[]; resume: { lesson_id: string; title: string; kind: string; step: number } | null };
};
export type LessonDraft = { lesson_id: string; lesson_kind: string; step_index: number; score: number };

export async function loadBootstrap(accessToken: string): Promise<BootstrapData> {
  return apiRequest('/api/v1/me/bootstrap/', accessToken);
}

export function loadLesson(lessonId: string, accessToken: string): Promise<NativeLesson> {
  return apiRequest(`/api/v1/lessons/${encodeURIComponent(lessonId)}/`, accessToken);
}

export async function loadLatestDraft(accessToken: string): Promise<LessonDraft | null> {
  const result = await apiRequest<{ draft: LessonDraft | null }>('/api/v1/me/lesson-drafts/latest/', accessToken);
  return result.draft;
}

export function saveLessonDraft(lessonId: string, stepIndex: number, score: number, accessToken: string) {
  return apiRequest(`/api/v1/me/lesson-drafts/${encodeURIComponent(lessonId)}/`, accessToken, { step_index: stepIndex, score }, 'PUT');
}

export function deleteLessonDraft(lessonId: string, accessToken: string) {
  return apiRequest(`/api/v1/me/lesson-drafts/${encodeURIComponent(lessonId)}/`, accessToken, undefined, 'DELETE');
}

export function checkAnswer(lessonId: string, position: number, answer: { selected_index: number } | { token_order: number[] }, accessToken: string): Promise<AnswerResult> {
  return apiRequest(`/api/v1/lessons/${encodeURIComponent(lessonId)}/answer/`, accessToken, { position, ...answer }, 'POST');
}

export function saveLessonResult(lessonId: string, cardsTotal: number, cardsKnown: number, eventId: string, accessToken: string) {
  const completedAt = new Date().toISOString();
  return apiRequest('/api/v1/me/lesson-results/', accessToken, {
    event_id: eventId, lesson_id: lessonId, plan_date: completedAt.slice(0, 10), completed_at: completedAt,
    cards_total: cardsTotal, cards_known: cardsKnown, contract_version: '1.0', client_instance_id: 'polskiflow-mobile-v1',
  }, 'POST');
}

async function apiRequest<T>(path: string, accessToken: string, body?: object, method: 'GET' | 'POST' | 'PUT' | 'DELETE' = 'GET'): Promise<T> {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 12_000);
  try {
    const response = await fetch(`${config.apiBaseUrl}${path}`, {
      method,
      headers: { Accept: 'application/json', Authorization: `Bearer ${accessToken}`, ...(body ? { 'Content-Type': 'application/json' } : {}) },
      body: body ? JSON.stringify(body) : undefined,
      signal: controller.signal,
    });
    if (!response.ok) throw new Error(response.status === 401 ? 'Сессия истекла. Войдите снова.' : 'Не удалось загрузить план.');
    const payload = (await response.json()) as { data: T };
    if (!payload || !('data' in payload)) throw new Error('Сервер вернул неполный ответ.');
    return payload.data;
  } finally { clearTimeout(timeout); }
}
