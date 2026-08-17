import { recordCardReview } from "@/lib/supabase/flashcards";
import { createRouteHandlerClient } from "@/lib/supabase/route-handler";
import { type NextRequest, NextResponse } from "next/server";

const validQualities = new Set(["again", "know"]);

export async function POST(request: NextRequest) {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

  if (!url || !key) {
    return NextResponse.json({ error: "Supabase не настроен." }, { status: 500 });
  }

  let body: { cardId?: string; quality?: string };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "Неверный формат запроса" }, { status: 400 });
  }

  const cardId = body.cardId?.trim();
  const quality = body.quality;

  if (!cardId) {
    return NextResponse.json({ error: "Укажите cardId" }, { status: 400 });
  }

  if (!quality || !validQualities.has(quality)) {
    return NextResponse.json({ error: "quality: again или know" }, { status: 400 });
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
    const review = await recordCardReview(
      supabase,
      user.id,
      cardId,
      quality as "again" | "know",
    );
    return NextResponse.json({ ok: true, review });
  } catch (error) {
    const message =
      error instanceof Error ? error.message : "Не удалось сохранить повторение";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
