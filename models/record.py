from typing import List, Optional
from .fields import Name, Phone, Birthday


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday: Optional[Birthday] = None

    def __str__(self) -> str:
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return (
            f"Contact name: {self.name.value}, phones: "
            f"{'; '.join(p.value for p in self.phones)}{birthday_str}"
        )

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def find_phone(self, phone: str) -> Optional[str]:
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError("Phone not found.")

    def remove_phone(self, phone: str) -> None:
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone not found.")

    def add_birthday(self, birthday_str: str) -> None:
        if self.birthday:
            raise ValueError("Birthday already set.")
        self.birthday = Birthday(birthday_str)

    def show_birthday(self) -> str:
        return str(self.birthday) if self.birthday else "No birthday set."