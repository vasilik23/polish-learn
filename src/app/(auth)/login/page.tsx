import { Suspense } from "react";
import { AuthForm } from "@/components/AuthForm";

export default function LoginPage() {
  return (
    <Suspense fallback={<p className="p-8 text-center">Загрузка…</p>}>
      <AuthForm mode="login" />
    </Suspense>
  );
}
