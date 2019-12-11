"""This script operates phonebook data operations"""
import pickle


def check_absence(func):
    """Check if contact requested exists"""
    def wrapper(self, name, *others):
        if name not in self.contacts:
            raise KeyError
        return func(self, name, *others)
    return wrapper


class PhoneBook:
    """This class represents object with standard crud features"""
    def __init__(self):
        """Initiate the contacts container"""
        self.contacts = {}
        self.filename = "phonebook.pickle"

    def read_contacts_from_file(self):
        """Open the pickle file that contains contacts inputs"""
        try:
            with open(self.filename, 'rb') as func:
                self.contacts = pickle.load(func)
        except FileNotFoundError:
            self.contacts = {}

    def write_to_file(self):
        """Save the contacts data into the pickles file"""
        with open(self.filename, 'wb') as func:
            pickle.dump(self.contacts, func)

    def create(self, name, phone):
        """Add new contact key-value into contacts"""
        self.contacts[name] = phone

    def read(self, name):
        """Find the contact requested and provide it"""
        return self.contacts[name]

    @check_absence
    def update(self, name, phone):
        """Check if contact requested exists and set new value for it"""
        self.contacts[name] = phone

    @check_absence
    def delete(self, name):
        """Delete required contact from the contacts"""
        self.contacts.pop(name)
