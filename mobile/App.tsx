import { useEffect, useState } from 'react';
import { AppState, SafeAreaView, StyleSheet, useColorScheme } from 'react-native';
import type { Session } from '@supabase/supabase-js';
import { StatusBar } from 'expo-status-bar';

import { LoginScreen } from './src/components/LoginScreen';
import { TodayScreen } from './src/components/TodayScreen';
import { LessonScreen } from './src/components/LessonScreen';
import { supabase } from './src/lib/supabase';
import { palette } from './src/theme';

export default function App() {
  const dark = useColorScheme() === 'dark';
  const colors = palette(dark);
  const [session, setSession] = useState<Session | null>(null);
  const [loading, setLoading] = useState(true);
  const [lessonId, setLessonId] = useState<string | null>(null);

  useEffect(() => {
    let mounted = true;
    void supabase.auth.getSession().then(({ data }) => {
      if (mounted) { setSession(data.session); setLoading(false); }
    });
    const { data: listener } = supabase.auth.onAuthStateChange((_event, next) => {
      setSession(next); setLoading(false);
    });
    const appState = AppState.addEventListener('change', (state) => {
      if (state === 'active') supabase.auth.startAutoRefresh();
      else supabase.auth.stopAutoRefresh();
    });
    supabase.auth.startAutoRefresh();
    return () => {
      mounted = false; listener.subscription.unsubscribe(); appState.remove(); supabase.auth.stopAutoRefresh();
    };
  }, []);

  return (
    <SafeAreaView style={[styles.shell, { backgroundColor: colors.background }]}>
      <StatusBar style={dark ? 'light' : 'dark'} />
      {session ? (lessonId
        ? <LessonScreen lessonId={lessonId} session={session} colors={colors} onClose={() => setLessonId(null)} />
        : <TodayScreen session={session} colors={colors} onOpenLesson={setLessonId} />
      ) : <LoginScreen colors={colors} booting={loading} />}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({ shell: { flex: 1 } });
