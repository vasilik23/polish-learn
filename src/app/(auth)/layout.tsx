export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="mx-auto min-h-full w-full max-w-md bg-[var(--app-bg)]">
      {children}
    </div>
  );
}
