"""modules for working with data."""
import pickle


class PhoneBook:
    """Class to represent phone book"""
    def __init__(self):
        with open("pb.pickle", "rb") as _file:
            self._phone_book = pickle.load(_file)

    def create(self, name, phone):
        """
        Create new contact in phone book.
        :param name: name of contact
        :param phone: phone number of contact
        :return: string report to user
        :raise KeyError if contact already in phone book
        """
        if name in self._phone_book:
            raise KeyError
        if not name or not phone:
            return "Invalid name or number"
        self._phone_book[name] = phone
        return "Added"

    def read(self, name):
        """
        Read contact in phone book
        :param name: name of contact
        :return: phone of specified contact or string report to user
        :raise KeyError if contact doesnt exist
        """
        if name in self._phone_book:
            return self._phone_book[name]
        if not self._phone_book:
            return "Book is empty"
        raise KeyError

    def update(self, name, phone):
        """
        Update contact in phone book
        :param name: name to update
        :param phone: phone number to update
        :return: updated contact or string report to user
        :raise: KeyError if contact doesnt exist
        """
        if name in self._phone_book:
            self._phone_book[name] = phone
            return f"Updated. {name}: {self._phone_book[name]}"
        if not self._phone_book:
            return "Book is empty"
        raise KeyError

    def delete(self, name):
        """
        Delete contact from phone book
        :param name: name of contact
        :return: string report to user
        :raise: KeyError if contact doesnt exist
        """
        if not self._phone_book or name not in self._phone_book:
            raise KeyError
        del self._phone_book[name]
        return "Deleted"

    def write(self):
        """
        Write phone book to file after user finish work with phone book
        :return: None
        """
        with open("pb.pickle", "wb") as phone_book:
            pickle.dump(self._phone_book, phone_book)

    def _clear(self):
        """
        Clear phone book or create
        :return: None
        """
        self._phone_book = {}
