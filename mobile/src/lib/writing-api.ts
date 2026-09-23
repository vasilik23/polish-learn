import { config } from './config';

export type WritingPrompt = {
  id: string;
  level: string;
  title: string;
  task: string;
  hint: string;
  minimum_words: number;
  minimum_paragraphs: number;
  required_markers: string[];
  checklist: string[];
};

export type WritingCatalog = {
  levels: string[];
  prompts: WritingPrompt[];
  prompt_count: number;
  persistence: 'none';
  assessment: 'observable_structure_only';
};

export type WritingCheck =
  | { id: 'minimum_words'; passed: boolean; observed: number; required: number }
  | { id: 'minimum_paragraphs'; passed: boolean; observed: number; required: number }
  | { id: 'required_markers'; passed: boolean; found: string[]; required: string[] };

export type WritingCheckResult = {
  prompt_id: string;
  level: string;
  checks: WritingCheck[];
  all_observable_checks_passed: boolean;
  limitations: string;
  persisted: false;
};

async function writingRequest<T>(path: string, accessToken: string, text?: string): Promise<T> {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 12_000);
  try {
    const response = await fetch(`${config.apiBaseUrl}${path}`, {
      method: text === undefined ? 'GET' : 'POST',
      headers: {
        Accept: 'application/json',
        Authorization: `Bearer ${accessToken}`,
        ...(text === undefined ? {} : { 'Content-Type': 'application/json' }),
      },
      body: text === undefined ? undefined : JSON.stringify({ text }),
      signal: controller.signal,
    });
    if (!response.ok) {
      if (response.status === 401) throw new Error('Сессия истекла. Войдите снова.');
      if (response.status === 429) throw new Error('Слишком много проверок. Попробуйте чуть позже.');
      throw new Error(response.status === 413 ? 'Текст слишком длинный для проверки.' : 'Не удалось выполнить запрос.');
    }
    const payload = (await response.json()) as { data?: T };
    if (!payload.data) throw new Error('Сервер вернул неполный ответ.');
    return payload.data;
  } catch (error) {
    if (error instanceof Error && error.name === 'AbortError') throw new Error('Сервер не ответил вовремя.');
    throw error;
  } finally {
    clearTimeout(timeout);
  }
}

export function loadWritingPrompts(accessToken: string): Promise<WritingCatalog> {
  return writingRequest('/api/v1/writing/', accessToken);
}

export function checkWritingDraft(promptId: string, text: string, accessToken: string): Promise<WritingCheckResult> {
  return writingRequest(`/api/v1/writing/${encodeURIComponent(promptId)}/check/`, accessToken, text);
}
