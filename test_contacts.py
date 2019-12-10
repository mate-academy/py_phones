"""
Test module
"""
import pytest
from contacts import PhoneBook


def test_create():
    """
    test
    :return:
    """
    phone_book = PhoneBook()
    phone_book.create_new_record("Bill", 911)
    assert phone_book.get_phone_by_name('Bill') == 911


def test_update():
    """
    test
    :return:
    """
    phone_book = PhoneBook()
    phone_book.create_new_record("Bill", 911)
    phone_book.update_record_by_name("Bill", 112)
    assert phone_book.get_phone_by_name('Bill') == 112


def test_delete():
    """
    test
    :return:
    """
    phone_book = PhoneBook()
    phone_book.create_new_record("Bill", 911)
    phone_book.remove_record_by_name("Bill")
    with pytest.raises(KeyError):
        phone_book.get_phone_by_name('Bill')
