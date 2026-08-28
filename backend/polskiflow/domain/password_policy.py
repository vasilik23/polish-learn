"""Application-side password policy for the Supabase Free plan."""

MIN_PASSWORD_LENGTH = 10

COMMON_PASSWORDS = frozenset(
    {
        "1234567890",
        "admin12345",
        "iloveyou123",
        "letmein123",
        "password123",
        "password1234",
        "polskiflow",
        "qwerty1234",
        "qwerty12345",
        "welcome123",
    }
)


def password_error(password: str) -> str | None:
    """Return a user-safe validation error, or ``None`` for an accepted password."""

    if len(password) < MIN_PASSWORD_LENGTH:
        return f"Пароль должен содержать не менее {MIN_PASSWORD_LENGTH} символов"
    if password.casefold() in COMMON_PASSWORDS:
        return "Этот пароль слишком распространён — выберите другой"
    if not any(character.islower() for character in password):
        return "Добавьте в пароль строчную букву"
    if not any(character.isupper() for character in password):
        return "Добавьте в пароль заглавную букву"
    if not any(character.isdigit() for character in password):
        return "Добавьте в пароль цифру"
    return None
