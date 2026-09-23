import { config } from './config';

type BaseScenario = { id: string; level: string; mode: string; title: string; situation: string };
export type ChoiceScenario = BaseScenario & { kind: 'choice'; prompt: string; options: { id: string; text: string }[] };
export type SequenceScenario = BaseScenario & { kind: 'sequence'; prompt: string; blocks: { id: string; text: string }[] };
export type FreeScenario = BaseScenario & { kind: 'free_production'; task: string; checklist: string[]; submission: 'local_only' };
export type InteractionScenario = ChoiceScenario | SequenceScenario | FreeScenario;
export type InteractionAnswer = { scenario_id: string; kind: 'choice' | 'sequence'; correct: boolean; correct_option_id?: string; correct_order?: string[]; explanation: string };

async function request<T>(path: string, accessToken: string, body?: object): Promise<T> {
  const controller = new AbortController(); const timeout = setTimeout(() => controller.abort(), 12_000);
  try {
    const response = await fetch(`${config.apiBaseUrl}${path}`, { method: body ? 'POST' : 'GET', headers: { Accept: 'application/json', Authorization: `Bearer ${accessToken}`, ...(body ? { 'Content-Type': 'application/json' } : {}) }, body: body ? JSON.stringify(body) : undefined, signal: controller.signal });
    if (!response.ok) {
      if (response.status === 401) throw new Error('Сессия истекла. Войдите снова.');
      if (response.status === 429) throw new Error('Слишком много проверок. Попробуйте позже.');
      throw new Error('Не удалось выполнить запрос.');
    }
    const payload = await response.json() as { data?: T };
    if (!payload.data) throw new Error('Сервер вернул неполный ответ.');
    return payload.data;
  } catch (error) {
    if (error instanceof Error && error.name === 'AbortError') throw new Error('Сервер не ответил вовремя.');
    throw error;
  } finally { clearTimeout(timeout); }
}

export async function loadInteraction(accessToken: string): Promise<InteractionScenario[]> {
  const data = await request<{ scenarios: InteractionScenario[] }>('/api/v1/interaction/', accessToken);
  return data.scenarios;
}

export function checkInteraction(scenarioId: string, answer: { option_id: string } | { block_ids: string[] }, accessToken: string) {
  return request<InteractionAnswer>(`/api/v1/interaction/${encodeURIComponent(scenarioId)}/answer/`, accessToken, answer);
}
