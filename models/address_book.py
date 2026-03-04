from collections import UserDict
from datetime import datetime
from typing import List, Optional
from .record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name not in self.data:
            raise ValueError("Contact not found.")
        del self.data[name]

    def get_upcoming_birthdays(self, days: int = 7) -> List[Record]:
        today = datetime.today().date()
        result = []

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                days_left = (birthday_this_year - today).days
                if 0 <= days_left < days:
                    result.append(record)

        return result

    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.data.values())