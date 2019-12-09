"""
Realisation phone book model.
Classes
-------
PhoneBook
"""
import pickle


class PhoneBook:
    """
    PhoneBook logic realisation
    Attributes
    ----------
    Methods
    -------
    create()
    read()
    update()
    delete()
    """
    def __init__(self):
        self._db_name = "db.pickle"
        try:
            with open(self._db_name, 'rb') as data:
                self._phone_book = pickle.load(data)
        except FileNotFoundError:
            self._phone_book = {}

    def __save(self):
        with open(self._db_name, 'wb') as data:
            pickle.dump(self._phone_book, data)

    def create(self, name, phone):
        """
        Create record in phone book
        """
        if name not in self._phone_book:
            self._phone_book[name] = phone
            self.__save()
            return f"Contact name:{name} phone:{phone} was created"
        return "This name already in phone book"

    def read(self, name):
        """
        Read record from phone book
        """
        if name in self._phone_book:
            return self._phone_book[name]
        raise KeyError

    def update(self, name, phone):
        """
        Update record in phone book
        """
        if name in self._phone_book:
            self._phone_book[name] = phone
            self.__save()
            return f"Contact {name} wos updated"
        return f"Contact with name {name} was not found"

    def delete(self, name):
        """
        Delete record from phone book
        """
        try:
            self._phone_book.pop(name)
            self.__save()
            return f"Contact with name {name} deleted"
        except KeyError:
            return f"Contact with name {name} not found"
