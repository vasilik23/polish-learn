import { config } from './config';

export type DiagnosticOption = { value: string; label: string };
export type DiagnosticTaskOption = { id: string; text: string };
export type DiagnosticForm = {
  disclaimer: string;
  self_assessment: Array<{ id: string; title: string; description: string; options: DiagnosticOption[] }>;
  checked_tasks: Array<{ id: string; mode: string; prompt: string; options: DiagnosticTaskOption[] }>;
  persistence: 'none';
};
export type DiagnosticResult = {
  recommended_level: string;
  self_assessment: { level: string; focus_modes: string[]; calculation: string };
  checked_sample: {
    level: string;
    correct: number;
    total: number;
    mode_scores: Array<{ mode: string; correct: number; total: number }>;
    calculation: string;
    feedback: Array<{ task_id: string; correct: boolean; correct_option_id: string; explanation: string }>;
  };
  disclaimer: string;
  persisted: false;
};

async function request<T>(path: string, accessToken: string, init?: RequestInit): Promise<T> {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 12_000);
  try {
    const response = await fetch(`${config.apiBaseUrl}${path}`, {
      ...init,
      headers: { Accept: 'application/json', Authorization: `Bearer ${accessToken}`, ...init?.headers },
      signal: controller.signal,
    });
    if (!response.ok) {
      if (response.status === 401) throw new Error('Сессия истекла. Войдите снова.');
      if (response.status === 429) throw new Error('Слишком много попыток. Подождите немного и повторите.');
      throw new Error('Не удалось обработать диагностику. Попробуйте ещё раз.');
    }
    const payload = (await response.json()) as { data?: T };
    if (!payload.data) throw new Error('Сервер вернул неполный ответ.');
    return payload.data;
  } catch (error) {
    if (error instanceof Error && error.name === 'AbortError') throw new Error('Сервер не ответил вовремя. Проверьте соединение.');
    throw error;
  } finally { clearTimeout(timeout); }
}

export function loadDiagnostic(accessToken: string) {
  return request<DiagnosticForm>('/api/v1/diagnostic/', accessToken);
}

export function evaluateDiagnostic(accessToken: string, selfRatings: Record<string, string>, answers: Record<string, string>) {
  return request<DiagnosticResult>('/api/v1/diagnostic/evaluate/', accessToken, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ self_ratings: selfRatings, answers }),
  });
}
