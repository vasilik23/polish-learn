"""Bounded listening content and stateless answer evaluation for native clients."""

from dataclasses import dataclass


class NativeListeningError(ValueError):
    pass


@dataclass(frozen=True)
class NativeListeningExercise:
    id: str
    title: str
    level: str
    delivery: str
    fragments: tuple[dict, ...]
    questions: tuple[dict, ...]


LISTENING_ITEMS = (
    {"id": "tecza", "audio": "polskiflow/audio/tecza.ogg", "options": ("tęcza", "część", "ciężar"), "answer": "tęcza", "hint": "Słychać nosowe ę i połączenie cz: tę-cza."},
    {"id": "wrobel", "audio": "polskiflow/audio/wrobel.ogg", "options": ("wróbel", "wybór", "wrona"), "answer": "wróbel", "hint": "Początkowe wr- i ó /u/ pomagają rozpoznać słowo wróbel."},
    {"id": "mysz", "audio": "polskiflow/audio/mysz.ogg", "options": ("my", "mysz", "miś"), "answer": "mysz", "hint": "Końcowe sz odróżnia mysz od my i miś."},
)

LISTENING_DIALOGUE = {
    "title": "Spotkanie przed podróżą", "level": "A1–A2",
    "lines": (
        "Cześć, Aniu! O której jedziemy jutro do Krakowa?",
        "Pociąg odjeżdża o ósmej piętnaście. Spotkajmy się o ósmej przed kasą numer trzy.",
        "Dobrze. Kupię bilety przez internet i przyniosę kawę.",
        "Świetnie, a ja wezmę kanapki. Do zobaczenia rano!",
    ),
    "questions": (
        {"id": "dialogue_main", "prompt": "O czym umówili się rozmówcy?", "options": ("Spotkać się przed podróżą do Krakowa", "Kupić produkty wieczorem", "Odwiedzić kasę po pracy"), "answer": "Spotkać się przed podróżą do Krakowa", "explanation": "Ustalają pociąg, czas i miejsce spotkania przed podróżą do Krakowa."},
        {"id": "dialogue_detail", "prompt": "Gdzie się spotkają?", "options": ("W pociągu", "Przed kasą numer trzy", "W kawiarni na dworcu"), "answer": "Przed kasą numer trzy", "explanation": "Ania mówi: „Spotkajmy się o ósmej przed kasą numer trzy”."},
    ),
}

LISTENING_B1 = {
    "title": "Zmiana planu sąsiedzkiego spotkania", "level": "B1",
    "lines": (
        "Dzień dobry, tu Marta z rady osiedla. Dzwonię w sprawie sobotniego spotkania mieszkańców.",
        "Ponieważ prognoza zapowiada silny deszcz, nie spotkamy się w parku, lecz w sali biblioteki przy ulicy Lipowej.",
        "Zaczynamy bez zmian o jedenastej. Najpierw porozmawiamy o nowym placu zabaw, a potem podzielimy się zadaniami przy organizacji pikniku.",
        "Proszę przynieść swoje propozycje i, jeśli to możliwe, potwierdzić udział do piątku wieczorem. Dziękuję i do zobaczenia.",
    ),
    "questions": (
        {"id": "b1_listening_reason", "prompt": "Dlaczego zmieniono miejsce spotkania?", "options": ("Z powodu prognozy silnego deszczu", "Z powodu remontu biblioteki", "Z powodu zmiany godziny"), "answer": "Z powodu prognozy silnego deszczu", "explanation": "Marta wiąże przeniesienie spotkania z prognozą silnego deszczu."},
        {"id": "b1_listening_plan", "prompt": "Co uczestnicy omówią najpierw?", "options": ("Nowy plac zabaw", "Podział zadań przy pikniku", "Godziny pracy biblioteki"), "answer": "Nowy plac zabaw", "explanation": "Słowo „najpierw” wprowadza pierwszy temat: nowy plac zabaw."},
        {"id": "b1_listening_action", "prompt": "Co Marta prosi zrobić do piątku wieczorem?", "options": ("Potwierdzić udział", "Przynieść jedzenie", "Zadzwonić do biblioteki"), "answer": "Potwierdzić udział", "explanation": "Zwrot „potwierdzić udział do piątku wieczorem” wskazuje czynność i termin."},
    ),
}

LISTENING_B2 = {
    "title": "Pilotaż pracy hybrydowej", "level": "B2",
    "lines": (
        "Choć część zespołu proponowała całkowitą pracę zdalną, kierownictwo zdecydowało się na trzymiesięczny pilotaż modelu hybrydowego.",
        "We wtorki wszyscy będą spotykać się w biurze, żeby wspólnie planować projekty, natomiast w pozostałe dni miejsce pracy będzie można wybrać samodzielnie.",
        "Warunkiem udziału jest przestrzeganie zasad bezpieczeństwa danych, zwłaszcza podczas korzystania z sieci poza firmą.",
        "Po zakończeniu pilotażu pracownicy wypełnią anonimową ankietę, a zarząd podejmie ostateczną decyzję na podstawie jej wyników.",
    ),
    "questions": (
        {"id": "b2_listening_model", "prompt": "Jaki model pracy będzie testować firma?", "options": ("Model hybrydowy przez trzy miesiące", "Pełną pracę zdalną bez terminu", "Czterodniowy tydzień pracy"), "answer": "Model hybrydowy przez trzy miesiące", "explanation": "Kierownictwo wybrało trzymiesięczny pilotaż modelu hybrydowego."},
        {"id": "b2_listening_tuesday", "prompt": "Po co zespół spotka się we wtorki w biurze?", "options": ("Na indywidualne rozmowy", "Aby wspólnie planować projekty", "Na szkolenie z bezpieczeństwa"), "answer": "Aby wspólnie planować projekty", "explanation": "Zwrot „żeby wspólnie planować projekty” podaje cel wtorkowych spotkań."},
        {"id": "b2_listening_decision", "prompt": "Na czym będzie oparta ostateczna decyzja?", "options": ("Na wynikach anonimowej ankiety", "Na liczbie dni w biurze", "Na raporcie działu bezpieczeństwa"), "answer": "Na wynikach anonimowej ankiety", "explanation": "Po pilotażu wyniki anonimowej ankiety będą podstawą decyzji."},
    ),
}


def build_native_listening() -> list[dict]:
    exercises = [_word_exercise()]
    exercises.extend(_speech_exercise(identifier, content) for identifier, content in (
        ("travel-dialogue", LISTENING_DIALOGUE), ("neighbourhood-message", LISTENING_B1),
        ("hybrid-work-message", LISTENING_B2),
    ))
    return exercises


def evaluate_native_listening_answer(exercise_id: str, question_id: str, selected_index: int) -> dict:
    exercise = _exercise(exercise_id)
    if exercise is None:
        raise NativeListeningError("exercise_not_found")
    question = next((item for item in exercise.questions if item["id"] == question_id), None)
    if question is None:
        raise NativeListeningError("question_not_found")
    if isinstance(selected_index, bool) or not isinstance(selected_index, int) or not 0 <= selected_index < len(question["options"]):
        raise NativeListeningError("invalid_selected_index")
    correct_index = question["options"].index(question["answer"])
    return {"question_id": question_id, "correct": selected_index == correct_index, "correct_index": correct_index, "explanation": question["explanation"]}


def _exercise(exercise_id: str) -> NativeListeningExercise | None:
    if exercise_id == "sound-words":
        return NativeListeningExercise(
            exercise_id, "Rozpoznaj słowa", "A1", "audio_files",
            tuple({"id": item["id"], "transcript": item["answer"], "audio_path": f"/static/{item['audio']}"} for item in LISTENING_ITEMS),
            tuple({"id": item["id"], "prompt": "Które słowo słyszysz?", **item} for item in LISTENING_ITEMS),
        )
    mapping = {"travel-dialogue": LISTENING_DIALOGUE, "neighbourhood-message": LISTENING_B1, "hybrid-work-message": LISTENING_B2}
    content = mapping.get(exercise_id)
    if content is None:
        return None
    return NativeListeningExercise(exercise_id, content["title"], content["level"], "device_tts", tuple({"id": str(index), "transcript": line} for index, line in enumerate(content["lines"])), content["questions"])


def _word_exercise() -> dict:
    return _public_exercise(_exercise("sound-words"))


def _speech_exercise(identifier: str, _content: dict) -> dict:
    return _public_exercise(_exercise(identifier))


def _public_exercise(exercise: NativeListeningExercise) -> dict:
    return {
        "id": exercise.id, "title": exercise.title, "level": exercise.level,
        "delivery": exercise.delivery, "transcript": " ".join(item["transcript"] for item in exercise.fragments),
        "fragments": list(exercise.fragments),
        "questions": [{"id": item["id"], "prompt": item["prompt"], "options": list(item["options"])} for item in exercise.questions],
    }
