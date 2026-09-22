import { useCallback, useEffect, useState } from 'react';
import { ActivityIndicator, Pressable, RefreshControl, ScrollView, StyleSheet, Text, View } from 'react-native';
import type { Session } from '@supabase/supabase-js';
import { loadBootstrap, loadLatestDraft, type BootstrapData } from '../lib/api';
import { supabase } from '../lib/supabase';
import type { Colors } from '../theme';

export function TodayScreen({ session, colors, onOpenLesson, onResumeLesson }: { session: Session; colors: Colors; onOpenLesson: (lessonId: string) => void; onResumeLesson: (launch: { lessonId: string; stepIndex: number; score: number }) => void }) {
  const [data, setData] = useState<BootstrapData | null>(null); const [loading, setLoading] = useState(true); const [error, setError] = useState('');
  const refresh = useCallback(async () => {
    setLoading(true); setError('');
    try { setData(await loadBootstrap(session.access_token)); } catch (reason) { setError(reason instanceof Error ? reason.message : 'Не удалось загрузить план.'); } finally { setLoading(false); }
  }, [session.access_token]);
  useEffect(() => { void refresh(); }, [refresh]);
  if (!data && loading) return <View style={styles.center}><ActivityIndicator size="large" color={colors.primary} /><Text style={{ color: colors.muted }}>Загружаем план…</Text></View>;
  return <ScrollView contentContainerStyle={styles.page} refreshControl={<RefreshControl refreshing={loading} onRefresh={refresh} tintColor={colors.primary} />}>
    <View style={styles.header}><View><Text style={[styles.eyebrow, { color: colors.primary }]}>МОБИЛЬНАЯ БЕТА</Text><Text style={[styles.title, { color: colors.text }]}>Сегодня</Text></View><Pressable accessibilityRole="button" onPress={() => supabase.auth.signOut()}><Text style={[styles.link, { color: colors.primary }]}>Выйти</Text></Pressable></View>
    {!!error && <View style={[styles.alert, { borderColor: colors.danger }]}><Text accessibilityRole="alert" style={{ color: colors.danger }}>{error}</Text><Pressable onPress={refresh}><Text style={[styles.link, { color: colors.primary }]}>Повторить</Text></Pressable></View>}
    {data && <><Text style={[styles.greeting, { color: colors.text }]}>Привет, {data.profile.display_name}</Text><Text style={[styles.sub, { color: colors.muted }]}>Уровень {data.profile.level} · серия {data.progress.streak_days} дн.</Text>
      <View style={[styles.goal, { backgroundColor: colors.primary }]}><Text style={styles.goalLabel}>Цель на сегодня</Text><Text style={styles.goalValue}>{data.today.completed_count} / {data.today.task_count}</Text><View style={styles.track}><View style={[styles.fill, { width: `${data.today.progress_percent}%` }]} /></View></View>
      {data.today.resume && <Pressable accessibilityRole="button" onPress={async () => { setError(''); try { const draft = await loadLatestDraft(session.access_token); if (draft) onResumeLesson({ lessonId: draft.lesson_id, stepIndex: draft.step_index, score: draft.score }); } catch { setError('Не удалось загрузить сохранённую позицию.'); } }} style={[styles.resume, { backgroundColor: colors.surface, borderColor: colors.primary }]}><Text style={[styles.taskTitle, { color: colors.text }]}>Продолжить: {data.today.resume.title}</Text><Text style={[styles.taskCopy, { color: colors.muted }]}>С шага {data.today.resume.step}</Text><Text style={[styles.meta, { color: colors.primary }]}>Вернуться к уроку →</Text></Pressable>}
      <Text style={[styles.sectionTitle, { color: colors.text }]}>План</Text>
      {data.today.tasks.map((task) => <Pressable accessibilityRole="button" disabled={task.plan_type === 'dictionary-review'} onPress={() => onOpenLesson(task.id)} key={`${task.plan_type}:${task.id}`} style={({ pressed }) => [styles.task, { backgroundColor: colors.surface, borderColor: colors.border, opacity: pressed ? .7 : 1 }]}><Text style={styles.emoji}>{task.emoji || '📘'}</Text><View style={styles.taskBody}><Text style={[styles.taskTitle, { color: colors.text }]}>{task.completed ? '✓ ' : ''}{task.title}</Text><Text style={[styles.taskCopy, { color: colors.muted }]}>{task.reinforcement_reason || task.description}</Text><Text style={[styles.meta, { color: colors.primary }]}>{task.plan_type === 'dictionary-review' ? 'Словарь — в следующем срезе' : `${task.minutes} мин. · Открыть`}</Text></View></Pressable>)}
      <Text style={[styles.boundary, { color: colors.muted }]}>Сейчас доступны просмотр плана и обновление. Выполнение уроков и offline-режим появятся в следующих мобильных итерациях.</Text></>}
  </ScrollView>;
}
const styles = StyleSheet.create({
  center: { flex: 1, justifyContent: 'center', alignItems: 'center', gap: 12 }, page: { padding: 20, paddingBottom: 40, gap: 12 }, header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }, eyebrow: { fontSize: 12, fontWeight: '900', letterSpacing: 1 }, title: { fontSize: 36, fontWeight: '900' }, link: { fontWeight: '800', paddingVertical: 10 }, greeting: { fontSize: 22, fontWeight: '800', marginTop: 10 }, sub: { fontSize: 15 },
  goal: { borderRadius: 22, padding: 20, marginVertical: 8 }, goalLabel: { color: '#fff', fontWeight: '700' }, goalValue: { color: '#fff', fontSize: 34, fontWeight: '900', marginVertical: 4 }, track: { height: 7, backgroundColor: 'rgba(255,255,255,.35)', borderRadius: 10 }, fill: { height: 7, backgroundColor: '#fff', borderRadius: 10 }, sectionTitle: { fontSize: 20, fontWeight: '800', marginTop: 6 },
  task: { flexDirection: 'row', borderWidth: 1, borderRadius: 18, padding: 16, gap: 12 }, resume: { borderWidth: 2, borderRadius: 18, padding: 16, gap: 5 }, emoji: { fontSize: 25 }, taskBody: { flex: 1, gap: 4 }, taskTitle: { fontSize: 17, fontWeight: '800' }, taskCopy: { fontSize: 14, lineHeight: 20 }, meta: { fontSize: 13, fontWeight: '800' }, alert: { borderWidth: 1, borderRadius: 14, padding: 14 }, boundary: { fontSize: 12, lineHeight: 18, marginTop: 8 },
});
