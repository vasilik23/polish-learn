import { config } from './config';

export type TodayTask = { id: string; title: string; description: string; minutes: number; emoji: string; completed: boolean; plan_type: string; reinforcement_reason: string | null };
export type BootstrapData = {
  profile: { display_name: string; level: string; daily_goal_lessons: number };
  progress: { streak_days: number; active_days: number; completed_lesson_count: number };
  today: { date: string; completed_count: number; task_count: number; progress_percent: number; tasks: TodayTask[] };
};

export async function loadBootstrap(accessToken: string): Promise<BootstrapData> {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 12_000);
  try {
    const response = await fetch(`${config.apiBaseUrl}/api/v1/me/bootstrap/`, { headers: { Accept: 'application/json', Authorization: `Bearer ${accessToken}` }, signal: controller.signal });
    if (!response.ok) throw new Error(response.status === 401 ? 'Сессия истекла. Войдите снова.' : 'Не удалось загрузить план.');
    const payload = (await response.json()) as { data: BootstrapData };
    if (!payload?.data?.today?.tasks || !payload.data.profile) throw new Error('Сервер вернул неполный план.');
    return payload.data;
  } finally { clearTimeout(timeout); }
}
