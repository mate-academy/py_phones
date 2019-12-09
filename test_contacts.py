import pytest
import contacts


def test_create():
    p = contacts.PhoneBook()
    p.create("Bill", 911)
    assert p.read('Bill') == 911


def test_update():
    p = contacts.PhoneBook()
    p.create("Bill", 911)
    p.update("Bill", 112)
    assert p.read('Bill') == 112


def test_delete():
    p = contacts.PhoneBook()
    p.create("Bill", 911)
    p.delete("Bill")
    with pytest.raises(KeyError):
        p.read('Bill')
