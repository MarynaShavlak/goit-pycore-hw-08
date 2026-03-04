from typing import Tuple


def parse_input(user_input: str) -> Tuple[str, ...]:
    cmd, *args = user_input.split()
    return cmd.lower(), *args

def validate_phone(phone: str) -> None:
    """
    Raises ValueError if phone is invalid.
    """
    if not phone.isdigit():
        raise ValueError("Wrong phone format. It must contain only digits.")

    if len(phone) != 10:
        raise ValueError("Wrong phone format. It must contain 10 digits.")