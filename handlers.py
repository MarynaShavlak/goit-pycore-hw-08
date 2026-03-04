from typing import List
from models.address_book import AddressBook
from models.record import Record
from decorators import input_error
from utils import validate_phone


@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    if len(args) != 2:
        raise ValueError("Usage: add [name] [phone]")
    name, phone, *_ = args
    validate_phone(phone)

    record = book.find(name)

    if record:
        if record.find_phone(phone):
            return f"Phone {phone} already exists for {name}."

        record.add_phone(phone)
        return f"Phone {phone} added to {name}."

    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)

    return f"Contact {name} added with phone {phone}."

@input_error
def edit_phone(args: List[str], book: AddressBook) -> str:
    """Edit a phone number for a contact."""
    if len(args) != 3:
        raise ValueError("Usage: change [name] [old_phone] [new_phone]")
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    record.edit_phone(old_phone, new_phone)
    return f"Phone number updated for {name}."


@input_error
def show_phone(args: List[str], book: AddressBook) -> str:
    """Show all phone numbers for a contact."""
    if len(args) != 1:
        raise ValueError("Usage: phone [name]")
    name, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    return f"Phones for {name}: " + "; ".join(p.value for p in record.phones)

@input_error
def show_all(book: AddressBook) -> str:
    """
    Returns a formatted string containing all saved contacts.

    Contacts are sorted alphabetically by name.

    Args:
        contacts (Dict[str, str]): Dictionary storing contacts.

    Returns:
        str:
            - A formatted multi-line string of contacts.
            - A message if no contacts are stored.
    """
    if not book:
        return "No contacts found."

    return "\n".join(
        str(record)
        for record in sorted(book.data.values(), key=lambda r: r.name.value)
    )

@input_error
def add_birthday(args: List[str], book: AddressBook) -> str:
    """Add a birthday to a contact."""
    if len(args) != 2:
        raise ValueError("Usage: add-birthday [name] [DD.MM.YYYY]")
    name, birthday_str, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    record.add_birthday(birthday_str)
    return f"Birthday added for {name}."

@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    """Show a contact's birthday."""
    if len(args) != 1:
        raise ValueError("Usage: show-birthday [name]")
    name, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    return record.show_birthday()


@input_error
def birthdays(book: AddressBook) -> str:
    """Show upcoming birthdays within the next 7 days."""
    upcoming_birthdays = book.get_upcoming_birthdays()
    return (
        "\n".join(str(record) for record in upcoming_birthdays)
        if upcoming_birthdays
        else "No upcoming birthdays."
    )