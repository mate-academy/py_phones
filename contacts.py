"""
Module used to create phone books.

Classes
-------
PhoneBook
"""


class PhoneBook:
    """
    Attributes
    ----------
    phone_book : dict -- storage for all names and numbers

    Methods
    -------
    create()
    read()
    update()
    delete()
    show_all()
    """
    def __init__(self):
        self.phone_book = {}

    def create(self, name, phone):
        """Add new name-number pair to the phone book"""
        if name in self.phone_book:
            raise NameError
        self.phone_book[name] = phone

    def read(self, name):
        """Print number of a person by name"""
        return self.phone_book[name]

    def update(self, name, phone):
        """Update number of a person by name"""
        if name in self.phone_book:
            self.phone_book[name] = phone
        else:
            raise NameError

    def delete(self, name):
        """Delete name-number pair from the phone book"""
        del self.phone_book[name]

    def show_all(self):
        """Print all names in the phone book"""
        return ' | '.join(self.phone_book.keys())
