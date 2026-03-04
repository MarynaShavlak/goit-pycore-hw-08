from datetime import datetime


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        if len(value) < 3:
            raise ValueError(
                f"Name '{value}' must be at least 3 characters long."
            )
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError(
                f"Phone number {value} must contain exactly 10 digits."
            )
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str):
        try:
            parsed_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(parsed_date)

    def __str__(self) -> str:
        return self.value.strftime("%d.%m.%Y")