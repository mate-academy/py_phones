"""
Model
"""
from pickle import dump


class PhoneBook:
    """
    Class represents phone book.
    """

    def __init__(self):
        self._phone_book = {}
        self._filename = "phone_book.pickle"

    def __str__(self) -> str:
        return f"{self._phone_book}"

    def __repr__(self) -> str:
        return f"PhoneBook:{self._phone_book}"

    def save_data(self):
        """
        Save record to dump file.
        :return: None
        """
        with open(self._filename, 'wb') as file:
            dump(self._filename, file)

    def get_all_data(self):
        """
        Get phone book dictionary.
        :return: dict
        """
        return self._phone_book

    def get_phone_by_name(self, contact_name):
        """
        Get phone information by contact name.
        :param contact_name: str
        :return: int
        """
        return self._phone_book[contact_name]

    def check_name_exist(self, contact_name):
        """
        Check if name exist in phone book dict.
        :param contact_name: str
        :return: bool
        """
        return contact_name in self._phone_book

    def create_new_record(self, new_contact_name: str, new_contact_phone: int):
        """
        Add a new record to the phone book that avoids to add duplicates.
        :param new_contact_name: str
        :param new_contact_phone: int
        :return: None
        """
        try:
            if not self.check_name_exist(new_contact_name):
                self._phone_book[new_contact_name] = new_contact_phone
                self.save_data()
        except ValueError as error:
            print(error)

    def remove_record_by_name(self, contact_name):
        """
        Remove record from phone book by contact name.
        :param contact_name: str
        :return: None
        """
        self._phone_book.pop(contact_name)

    def update_record_by_name(self, contact_name, new_phone_number):
        """
        Update record in phone book by contact name.
        :param contact_name: str
        :param new_phone_number: int
        :return: None
        """
        try:
            self._phone_book[contact_name] = new_phone_number
            self.save_data()
        except ValueError as error:
            print(error)
