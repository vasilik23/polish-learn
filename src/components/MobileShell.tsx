import Link from "next/link";

type MobileShellProps = {
  children: React.ReactNode;
  title?: string;
  showBack?: boolean;
  backHref?: string;
  headerRight?: React.ReactNode;
};

export function MobileShell({
  children,
  title,
  showBack,
  backHref = "/",
  headerRight,
}: MobileShellProps) {
  return (
    <div className="mx-auto flex min-h-full w-full max-w-md flex-col bg-[var(--app-bg)]">
      {(title || showBack || headerRight) && (
        <header className="sticky top-0 z-10 flex items-center gap-3 border-b border-[var(--border)] bg-[var(--app-surface)]/95 px-4 py-3 backdrop-blur-sm safe-top">
          {showBack ? (
            <Link
              href={backHref}
              className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full text-[var(--text-muted)] transition hover:bg-[var(--app-bg)]"
              aria-label="Назад"
            >
              ←
            </Link>
          ) : (
            <div className="w-10 shrink-0" />
          )}
          {title && (
            <h1 className="flex-1 truncate text-lg font-semibold text-[var(--text)]">
              {title}
            </h1>
          )}
          <div className="ml-auto shrink-0">{headerRight}</div>
        </header>
      )}
      <main className="flex-1 px-4 pb-8 pt-4 safe-bottom">{children}</main>
    </div>
  );
}
