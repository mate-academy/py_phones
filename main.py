"""
In this assignment you must write a phone book. This should be a
console-based application. The user can create a new contact by
name and phone number, find the contact by name, update the contact
by name and delete it by name. Data must be saved in a pickle file.
Divide your application into two modules, one for working with data and
one for the user interface. Please note that the data module
must not contain print () / input () functions.
"""

import contacts


def interface():
    """Phone interface"""
    phone_book = contacts.PhoneBook()

    while True:
        print("""What do you want to do?
    c - create
    r - read
    u - update
    d - delete
    q - quit
    """)
        funcs = {'c': create, 'r': read, 'u': update}
        action = input("?").lower()

        if action == 'q':
            break

        funcs.get(action, 'You enter wrong command')(phone_book)


def create(phone_book):
    """Create new name"""
    name = input('Please enter new name: ')
    phone = input('Please enter phone number: ')
    phone_book.create(name, phone)


def read(phone_book):
    """Read phone number """
    name = input('Please enter name: ')
    phone_book.read(name)


def update(phone_book):
    """Update phone number"""
    name = input('Please enter name (update): ')
    phone = input('Please enter phone number: ')
    phone_book.update(name, phone)
