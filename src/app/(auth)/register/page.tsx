import { Suspense } from "react";
import { AuthForm } from "@/components/AuthForm";

export default function RegisterPage() {
  return (
    <Suspense fallback={<p className="p-8 text-center">Загрузка…</p>}>
      <AuthForm mode="register" />
    </Suspense>
  );
}
