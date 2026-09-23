import { useCallback, useEffect, useState } from 'react';
import { ActivityIndicator, FlatList, Pressable, StyleSheet, Text, View } from 'react-native';
import type { Session } from '@supabase/supabase-js';

import { loadLearningHistory, type HistoryCompletion, type HistoryPage, type HistoryPeriod } from '../lib/history-api';
import type { Colors } from '../theme';

const periods: { id: HistoryPeriod; label: string }[] = [
  { id: '7', label: '7 дней' },
  { id: '30', label: '30 дней' },
  { id: '90', label: '90 дней' },
  { id: 'all', label: 'Всё время' },
];

function lessonTitle(id: string) {
  const title = id.replace(/[-_]+/g, ' ').trim();
  return title ? title.charAt(0).toUpperCase() + title.slice(1) : 'Урок';
}

function displayDate(value: string) {
  const parts = /^(\d{4})-(\d{2})-(\d{2})$/.exec(value);
  return parts ? `${parts[3]}.${parts[2]}.${parts[1]}` : value;
}

export function HistoryScreen({ session, colors, onClose }: { session: Session; colors: Colors; onClose: () => void }) {
  const [period, setPeriod] = useState<HistoryPeriod>('30');
  const [history, setHistory] = useState<HistoryPage | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const load = useCallback(async (nextPeriod: HistoryPeriod, page: number) => {
    setLoading(true);
    setError('');
    try {
      setHistory(await loadLearningHistory(session.access_token, nextPeriod, page));
    } catch (requestError) {
      setError(requestError instanceof Error ? requestError.message : 'Не удалось загрузить историю.');
    } finally {
      setLoading(false);
    }
  }, [session.access_token]);

  useEffect(() => { void load(period, 1); }, [load, period]);

  const renderCompletion = ({ item }: { item: HistoryCompletion }) => {
    const hasScore = item.cards_total > 0;
    const percent = hasScore ? Math.round((item.cards_known / item.cards_total) * 100) : 100;
    return <View accessible accessibilityLabel={`${lessonTitle(item.lesson_id)}, ${displayDate(item.plan_date)}, ${hasScore ? `${item.cards_known} из ${item.cards_total}` : 'завершён'}`} style={[styles.card, { backgroundColor: colors.surface, borderColor: colors.border }]}>
      <View style={styles.cardHeader}>
        <Text style={[styles.lessonTitle, { color: colors.text }]}>{lessonTitle(item.lesson_id)}</Text>
        <Text style={[styles.date, { color: colors.muted }]}>{displayDate(item.plan_date)}</Text>
      </View>
      <View style={styles.scoreRow}>
        <Text style={[styles.score, { color: colors.primary }]}>{hasScore ? `${item.cards_known} / ${item.cards_total}` : 'Завершён'}</Text>
        <Text style={[styles.percent, { color: colors.muted }]}>{percent}%</Text>
      </View>
      <View style={[styles.track, { backgroundColor: colors.border }]}><View style={[styles.fill, { backgroundColor: colors.primary, width: `${Math.max(0, Math.min(100, percent))}%` }]} /></View>
    </View>;
  };

  return <View style={[styles.screen, { backgroundColor: colors.background }]}>
    <FlatList
      data={history?.completions ?? []}
      keyExtractor={(item, index) => `${item.plan_date}-${item.lesson_id}-${index}`}
      renderItem={renderCompletion}
      contentContainerStyle={styles.page}
      refreshing={loading && !!history}
      onRefresh={() => void load(period, history?.page ?? 1)}
      ListHeaderComponent={<View style={styles.header}>
        <Pressable accessibilityRole="button" onPress={onClose} hitSlop={8}><Text style={[styles.back, { color: colors.primary }]}>‹ Сегодня</Text></Pressable>
        <Text accessibilityRole="header" style={[styles.title, { color: colors.text }]}>История обучения</Text>
        <Text style={[styles.subtitle, { color: colors.muted }]}>Завершённые уроки и результаты</Text>
        <View accessibilityRole="radiogroup" style={styles.periods}>{periods.map((option) => <Pressable key={option.id} accessibilityRole="radio" accessibilityState={{ checked: period === option.id }} onPress={() => setPeriod(option.id)} style={[styles.chip, { borderColor: period === option.id ? colors.primary : colors.border, backgroundColor: period === option.id ? colors.surface : 'transparent' }]}><Text style={{ color: period === option.id ? colors.primary : colors.text, fontWeight: '800' }}>{option.label}</Text></Pressable>)}</View>
        {!!error && <View style={[styles.stateCard, { borderColor: colors.danger }]}><Text accessibilityRole="alert" style={{ color: colors.danger }}>{error}</Text><Pressable accessibilityRole="button" onPress={() => void load(period, history?.page ?? 1)}><Text style={[styles.retry, { color: colors.primary }]}>Повторить</Text></Pressable></View>}
        {loading && !history && <View style={styles.loading}><ActivityIndicator color={colors.primary} /><Text style={{ color: colors.muted }}>Загружаем историю…</Text></View>}
      </View>}
      ListEmptyComponent={!loading && !error ? <View style={[styles.stateCard, { borderColor: colors.border }]}><Text style={[styles.emptyTitle, { color: colors.text }]}>Пока нет завершённых уроков</Text><Text style={{ color: colors.muted, lineHeight: 20 }}>Завершите первый урок — результат появится здесь.</Text></View> : null}
      ListFooterComponent={history && history.completions.length ? <View style={styles.pagination}>
        <Pressable accessibilityRole="button" accessibilityState={{ disabled: !history.has_previous || loading }} disabled={!history.has_previous || loading} onPress={() => void load(period, history.page - 1)} style={[styles.pageButton, { borderColor: colors.border, opacity: !history.has_previous || loading ? .45 : 1 }]}><Text style={{ color: colors.text, fontWeight: '800' }}>Назад</Text></Pressable>
        <Text accessibilityLabel={`Страница ${history.page}`} style={{ color: colors.muted }}>Страница {history.page}</Text>
        <Pressable accessibilityRole="button" accessibilityState={{ disabled: !history.has_next || loading }} disabled={!history.has_next || loading} onPress={() => void load(period, history.page + 1)} style={[styles.pageButton, { borderColor: colors.border, opacity: !history.has_next || loading ? .45 : 1 }]}><Text style={{ color: colors.text, fontWeight: '800' }}>Далее</Text></Pressable>
      </View> : null}
    />
  </View>;
}

const styles = StyleSheet.create({
  screen: { flex: 1 }, page: { padding: 20, paddingBottom: 44, gap: 12 }, header: { gap: 10, marginBottom: 4 }, back: { fontSize: 16, fontWeight: '800', paddingVertical: 8 }, title: { fontSize: 30, fontWeight: '900' }, subtitle: { fontSize: 15 }, periods: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, marginTop: 6 }, chip: { borderWidth: 1, borderRadius: 999, paddingHorizontal: 13, paddingVertical: 10 }, card: { borderWidth: 1, borderRadius: 18, padding: 16, gap: 12 }, cardHeader: { flexDirection: 'row', gap: 12, alignItems: 'flex-start' }, lessonTitle: { flex: 1, fontSize: 17, fontWeight: '900' }, date: { fontSize: 13 }, scoreRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }, score: { fontSize: 15, fontWeight: '900' }, percent: { fontSize: 13, fontWeight: '700' }, track: { height: 7, borderRadius: 999, overflow: 'hidden' }, fill: { height: '100%', borderRadius: 999 }, loading: { minHeight: 120, alignItems: 'center', justifyContent: 'center', gap: 10 }, stateCard: { borderWidth: 1, borderRadius: 16, padding: 16, gap: 10, marginTop: 4 }, emptyTitle: { fontSize: 17, fontWeight: '900' }, retry: { fontWeight: '900', paddingVertical: 4 }, pagination: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', marginTop: 8 }, pageButton: { minWidth: 92, minHeight: 44, borderWidth: 1, borderRadius: 12, alignItems: 'center', justifyContent: 'center', paddingHorizontal: 12 },
});
