import { config } from './config';

export type HistoryPeriod = '7' | '30' | '90' | 'all';

export type HistoryCompletion = {
  lesson_id: string;
  plan_date: string;
  cards_total: number;
  cards_known: number;
};

export type HistoryPage = {
  period: HistoryPeriod;
  page: number;
  page_size: number;
  has_previous: boolean;
  has_next: boolean;
  completions: HistoryCompletion[];
};

export async function loadLearningHistory(
  accessToken: string,
  period: HistoryPeriod = '30',
  page = 1,
): Promise<HistoryPage> {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 12_000);
  try {
    const query = new URLSearchParams({ period, page: String(page) });
    const response = await fetch(`${config.apiBaseUrl}/api/v1/me/history/?${query}`, {
      headers: { Accept: 'application/json', Authorization: `Bearer ${accessToken}` },
      signal: controller.signal,
    });
    if (!response.ok) {
      throw new Error(response.status === 401 ? 'Сессия истекла. Войдите снова.' : 'Не удалось загрузить историю.');
    }
    const payload = (await response.json()) as { data?: HistoryPage };
    if (!payload.data || !Array.isArray(payload.data.completions)) {
      throw new Error('Сервер вернул неполный ответ.');
    }
    return payload.data;
  } finally {
    clearTimeout(timeout);
  }
}
