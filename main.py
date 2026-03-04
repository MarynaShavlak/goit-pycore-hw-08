from models.address_book import AddressBook
from handlers import (
    add_contact,
    edit_phone,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
)
from utils import parse_input


def show_help() -> str:
    return """
Available commands:

General:
- hello
- help
- close / exit

Contacts:
- add [name] [phone]
- change [name] [old_phone] [new_phone]
- phone [name]
- all

Birthdays:
- add-birthday [name] [DD.MM.YYYY]
- show-birthday [name]
- birthdays
"""


def main() -> None:
    book = AddressBook()

    print("Welcome to the assistant bot!")
    print(show_help())

    commands = {
        "hello": lambda args: "How can I help you?",
        "add": lambda args: add_contact(args, book),
        "change": lambda args: edit_phone(args, book),
        "phone": lambda args: show_phone(args, book),
        "all": lambda args: show_all(book),
        "add-birthday": lambda args: add_birthday(args, book),
        "show-birthday": lambda args: show_birthday(args, book),
        "birthdays": lambda args: birthdays(book),
        "help": lambda args: show_help(),
    }

    while True:
        user_input = input("Enter command: ").strip()

        if not user_input:
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command in commands:
            result = commands[command](args)
            print(result)
        else:
            print("Invalid command.")
            print(show_help())


if __name__ == "__main__":
    main()