import { createClient } from "https://esm.sh/@supabase/supabase-js@2.57.4";

const json = (body: Record<string, unknown>, status: number) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json", "cache-control": "no-store" },
  });

Deno.serve(async (request) => {
  if (request.method !== "POST") return json({ detail: "Method not allowed" }, 405);

  const url = Deno.env.get("SUPABASE_URL") ?? "";
  const anonKey = Deno.env.get("SUPABASE_ANON_KEY") ?? "";
  const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";
  const authorization = request.headers.get("authorization") ?? "";
  if (!url || !anonKey || !serviceKey || !authorization.startsWith("Bearer ")) {
    return json({ detail: "Authentication required" }, 401);
  }

  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return json({ detail: "Invalid JSON" }, 400);
  }
  if (!body || typeof body !== "object" || Array.isArray(body)) {
    return json({ detail: "Invalid payload" }, 400);
  }
  const fields = Object.keys(body as Record<string, unknown>);
  const password = (body as Record<string, unknown>).password;
  if (fields.length !== 1 || fields[0] !== "password" || typeof password !== "string" || !password || password.length > 1024) {
    return json({ detail: "Invalid payload" }, 400);
  }

  const token = authorization.slice("Bearer ".length);
  const userClient = createClient(url, anonKey, {
    auth: { persistSession: false, autoRefreshToken: false },
    global: { headers: { Authorization: authorization } },
  });
  const { data: userData, error: userError } = await userClient.auth.getUser(token);
  const user = userData.user;
  if (userError || !user?.id || !user.email) return json({ detail: "Authentication required" }, 401);

  const reauthClient = createClient(url, anonKey, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
  const { data: reauthData, error: reauthError } = await reauthClient.auth.signInWithPassword({
    email: user.email,
    password,
  });
  if (reauthError || reauthData.user?.id !== user.id) {
    return json({ detail: "Password verification failed" }, 403);
  }

  const admin = createClient(url, serviceKey, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
  const { error: deleteError } = await admin.auth.admin.deleteUser(user.id, false);
  if (deleteError) return json({ detail: "Account deletion failed" }, 503);
  return json({ deleted_user_id: user.id }, 200);
});
