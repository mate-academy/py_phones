"""
main - module containing user interface of a phone book
console-based application

Functions
---------
create()
read()
update()
delete()
show_all()
"""


import pickle
import contacts


PHONE_BOOK = None
try:
    with open("saved_book.pickle", 'rb') as book:
        PHONE_BOOK = pickle.load(book)
except FileNotFoundError:
    pass

PH_BOOK = PHONE_BOOK if PHONE_BOOK else contacts.PhoneBook()
GO_ON = "To continue press Enter"


def create():
    """Add new name-number pair to the phone book"""

    name = input("Name of a person you want to add: ").title()
    number = input("Number of a person: ")
    try:
        PH_BOOK.create(name, number)
        print(f'New name added. {GO_ON}')
        input()
    except NameError:
        print(f"Used name already exists in the phone book. {GO_ON}")
        input()


def read():
    """Print number of a person by name"""

    name = input("Name of a person: ").title()
    try:
        print(PH_BOOK.read(name))
        print(GO_ON)
        input()
    except KeyError:
        print(f'{name} not found! To try again press Enter')
        input()


def update():
    """Update number of a person by name"""

    name = input("Name of a person whose number you want to update: ").title()
    number = input("New number: ")
    try:
        PH_BOOK.update(name, number)
        print(f"{name}'s number updated. {GO_ON}")
        input()
    except NameError:
        print(f"There is no such name in the phone book. {GO_ON}")
        input()


def delete():
    """Delete name-number pair from the phone book"""

    name = input("Name of a person who you want to delete: ").title()
    try:
        PH_BOOK.delete(name)
        print(f"{name} was deleted. {GO_ON}")
        input()
    except KeyError:
        print(f'There is no {name} in the phone book. {GO_ON}')
        input()


def show_all():
    """Print all names in the phone book"""

    print(PH_BOOK.show_all())
    print(GO_ON)
    input()


def break_():
    """Doing nothing (to satisfy mypy test)"""
    print("Don't call me")


OPTIONS = {'c': create, 'r': read, 'u': update,
           'd': delete, 'q': break_, 'a': show_all}
while True:
    print("""What do you want to do?
c - create
r - read
u - update
d - delete
q - quit
a - show all names
""")
    ACTION = input("Choose option: ").lower()
    if ACTION not in OPTIONS:
        print('Incorrect option. Press Enter to try again.')
        input()
        continue

    if ACTION == 'q':
        break

    OPTIONS[ACTION]()

with open("saved_book.pickle", 'wb') as book:
    pickle.dump(PH_BOOK, book)
