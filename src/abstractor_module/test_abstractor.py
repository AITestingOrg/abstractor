'''
Abstractor integration tests
'''
import pytest
from .abstractor import Abstractor
from .abstractions import ABSTRACTIONS


def test_first_name_returns_valid_first_name():
    assert Abstractor().get_abstraction('First name Joahsna') == ABSTRACTIONS['FIRST_NAME']

def test_last_name_returns_valid_last_name():
    assert Abstractor().get_abstraction('last name smith') == ABSTRACTIONS['LAST_NAME']

def test_valid_email_returns_valid_email():
    assert Abstractor().get_abstraction('email Joahsna@gmail.com') == ABSTRACTIONS['EMAIL']

def test_invalid_email_returns_none():
    assert Abstractor().get_abstraction('email qq') == None

def test_invalid_input():
    with pytest.raises(Exception):
        Abstractor().get_abstraction({})
