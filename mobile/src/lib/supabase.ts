import 'react-native-url-polyfill/auto';
import { createClient } from '@supabase/supabase-js';
import { config } from './config';
import { secureSessionStorage } from './secureSessionStorage';

export const supabase = createClient(config.supabaseUrl, config.supabasePublishableKey, {
  auth: { storage: secureSessionStorage, autoRefreshToken: true, persistSession: true, detectSessionInUrl: false },
});
