"use client";

import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useState } from "react";
import { isSupabaseConfigured } from "@/lib/supabase/client";

type AuthMode = "login" | "register";

type AuthFormProps = {
  mode: AuthMode;
};

export function AuthForm({ mode }: AuthFormProps) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const next = searchParams.get("next") || "/";

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  const isLogin = mode === "login";
  const configured = isSupabaseConfigured();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setMessage(null);

    if (!configured) {
      setError(
        "Supabase не настроен. Добавьте ключи в .env.local (см. README).",
      );
      return;
    }

    setLoading(true);

    try {
      const endpoint = isLogin ? "/api/auth/login" : "/api/auth/signup";
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = (await res.json().catch(() => ({}))) as {
        error?: string;
        ok?: boolean;
      };

      if (!res.ok) {
        throw new Error(data.error ?? "Ошибка авторизации");
      }

      if (isLogin) {
        router.push(next);
        router.refresh();
      } else {
        setMessage(
          "Аккаунт создан. Если включено подтверждение email — проверьте почту, затем войдите.",
        );
      }
    } catch (err) {
      const message =
        err instanceof Error ? err.message : "Ошибка авторизации";
      if (message === "Load failed" || message === "Failed to fetch") {
        setError(
          "Не удалось связаться с сервером. Откройте localhost:3000 на Mac или проверьте Wi‑Fi.",
        );
      } else if (
        message.includes("rate limit") ||
        message.includes("over_email_send_rate_limit")
      ) {
        setError(
          "Лимит писем Supabase (≈3 в час на бесплатном тарифе). Подождите час, отключите Confirm email или создайте пользователя вручную в Supabase → Users → Add user.",
        );
      } else {
        setError(message);
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="mx-auto w-full max-w-md px-4 py-8">
      <div className="mb-8 text-center">
        <p className="text-sm font-semibold uppercase tracking-wider text-[var(--primary)]">
          PolskiFlow
        </p>
        <h1 className="mt-2 text-2xl font-bold text-[var(--text)]">
          {isLogin ? "Вход" : "Регистрация"}
        </h1>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          {isLogin
            ? "Войдите, чтобы открыть материалы"
            : "Бесплатный доступ к урокам"}
        </p>
      </div>

      {!configured && (
        <div className="mb-4 rounded-xl border border-amber-200 bg-amber-50 px-4 py-3 text-sm text-amber-900">
          Скопируйте <code className="text-xs">.env.local.example</code> в{" "}
          <code className="text-xs">.env.local</code> и укажите ключи Supabase.
        </div>
      )}

      <form
        onSubmit={handleSubmit}
        className="space-y-4 rounded-2xl bg-[var(--app-surface)] p-6 shadow-sm ring-1 ring-[var(--border)]"
      >
        <div>
          <label
            htmlFor="email"
            className="mb-1 block text-sm font-medium text-[var(--text)]"
          >
            Email
          </label>
          <input
            id="email"
            type="email"
            autoComplete="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full rounded-xl border border-[var(--border)] bg-[var(--app-bg)] px-4 py-3 text-[var(--text)] outline-none focus:border-[var(--primary)] focus:ring-2 focus:ring-[var(--primary)]/20"
            placeholder="you@example.com"
          />
        </div>

        <div>
          <label
            htmlFor="password"
            className="mb-1 block text-sm font-medium text-[var(--text)]"
          >
            Пароль
          </label>
          <input
            id="password"
            type="password"
            autoComplete={isLogin ? "current-password" : "new-password"}
            required
            minLength={6}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full rounded-xl border border-[var(--border)] bg-[var(--app-bg)] px-4 py-3 text-[var(--text)] outline-none focus:border-[var(--primary)] focus:ring-2 focus:ring-[var(--primary)]/20"
            placeholder="минимум 6 символов"
          />
        </div>

        {error && (
          <p className="rounded-lg bg-red-50 px-3 py-2 text-sm text-red-700">
            {error}
          </p>
        )}
        {message && (
          <p className="rounded-lg bg-emerald-50 px-3 py-2 text-sm text-emerald-800">
            {message}
          </p>
        )}

        <button
          type="submit"
          disabled={loading}
          className="w-full rounded-xl bg-[var(--primary)] py-3.5 font-semibold text-white transition hover:bg-[var(--primary-hover)] disabled:opacity-60"
        >
          {loading ? "Подождите…" : isLogin ? "Войти" : "Создать аккаунт"}
        </button>
      </form>

      <p className="mt-6 text-center text-sm text-[var(--text-muted)]">
        {isLogin ? (
          <>
            Нет аккаунта?{" "}
            <Link href="/register" className="font-medium text-[var(--primary)]">
              Зарегистрироваться
            </Link>
          </>
        ) : (
          <>
            Уже есть аккаунт?{" "}
            <Link href="/login" className="font-medium text-[var(--primary)]">
              Войти
            </Link>
          </>
        )}
      </p>
    </div>
  );
}
