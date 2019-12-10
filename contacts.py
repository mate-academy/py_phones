"""Module describes phone book"""
import pickle


class PhoneBook:
    """Phone book class"""
    def __init__(self):
        self._contacts = {}
        self._file_name = 'phone_book.pickle'

    def create(self, name, phone):
        """Creating phone book"""
        self._contacts[name] = phone
        self.write_to_file()

    def read(self, name):
        """Read from phone book"""
        self._contacts = self.read_from_file()
        return self._contacts[name]

    def update(self, name, phone):
        """Same as creating (I'd add validation)"""
        self._contacts = self.read_from_file()
        self.create(name, phone)

    def delete(self, name):
        """Delete contact (I'd add validation)"""
        self._contacts = self.read_from_file()
        del self._contacts[name]
        self.write_to_file()

    def write_to_file(self):
        """Write to file"""
        with open(self._file_name, 'wb') as writer:
            pickle.dump(self._contacts, writer)

    def read_from_file(self):
        """Read from file"""
        with open(self._file_name, 'rb') as reader:
            phone_book = pickle.load(reader)
        return phone_book
