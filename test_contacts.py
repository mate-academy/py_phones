"""
Test module
"""
import pytest
import contacts


def test_create():
    """
    Test create() option
    :return:
    """
    pbk = contacts.PhoneBook()
    pbk.create("Bill", 911)
    assert pbk.read('Bill') == 911


def test_update():
    """
    Test update() option
    :return:
    """
    pbk = contacts.PhoneBook()
    pbk.create("Bill", 911)
    pbk.update("Bill", 112)
    assert pbk.read('Bill') == 112


def test_delete():
    """
    Test delete option
    :return:
    """
    pbk = contacts.PhoneBook()
    pbk.create("Bill", 911)
    pbk.delete("Bill")
    with pytest.raises(KeyError):
        pbk.read('Bill')
