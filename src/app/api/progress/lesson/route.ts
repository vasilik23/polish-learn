import { completeLesson } from "@/lib/supabase/progress";
import { createRouteHandlerClient } from "@/lib/supabase/route-handler";
import { ensureProfile } from "@/lib/supabase/profile";
import { taskCards, type TaskType } from "@/lib/data/mock";
import { type NextRequest, NextResponse } from "next/server";

const validLessonIds = new Set(taskCards.map((card) => card.id));

export async function POST(request: NextRequest) {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

  if (!url || !key) {
    return NextResponse.json(
      { error: "Supabase не настроен." },
      { status: 500 },
    );
  }

  let body: {
    lessonId?: string;
    cardsTotal?: number;
    cardsKnown?: number;
  };

  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "Неверный формат запроса" }, { status: 400 });
  }

  const lessonId = body.lessonId;
  const cardsTotal = body.cardsTotal ?? 0;
  const cardsKnown = body.cardsKnown ?? 0;

  if (!lessonId || !validLessonIds.has(lessonId)) {
    return NextResponse.json({ error: "Неизвестный урок" }, { status: 400 });
  }

  const response = NextResponse.json({ ok: true });
  const supabase = createRouteHandlerClient(request, response);

  const {
    data: { user },
    error: authError,
  } = await supabase.auth.getUser();

  if (authError || !user) {
    return NextResponse.json({ error: "Нужно войти в аккаунт" }, { status: 401 });
  }

  try {
    await ensureProfile(supabase, user.id, user.email);
    await completeLesson(supabase, {
      userId: user.id,
      lessonId: lessonId as TaskType,
      cardsTotal,
      cardsKnown,
    });
  } catch (error) {
    const message =
      error instanceof Error ? error.message : "Не удалось сохранить прогресс";
    return NextResponse.json({ error: message }, { status: 500 });
  }

  return response;
}
