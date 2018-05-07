'''
Abstractor integration tests
'''
import pytest
from .abstractor import Abstractor
from .abstractions import ABSTRACTIONS


def test_first_name_returns_valid_first_name():
    assert Abstractor().get_abstraction('First name Joahsna') == ABSTRACTIONS['FIRST_NAME']

def test_last_name_returns_valid_last_name():
    assert Abstractor().get_abstraction('last name Smith') == ABSTRACTIONS['LAST_NAME']

def test_valid_email_returns_valid_email():
    assert Abstractor().get_abstraction('Email Joahsna@gmail.com') == ABSTRACTIONS['EMAIL']

def test_first_name2_returns_valid_first_name():
    assert Abstractor().get_abstraction('First name* William') == ABSTRACTIONS['FIRST_NAME']

def test_last_name2_returns_valid_last_name():
    assert Abstractor().get_abstraction('Sur name Jones') == ABSTRACTIONS['LAST_NAME']

def test_valid_email2_returns_valid_email():
    assert Abstractor().get_abstraction('Email Joahs@gmail.com') == ABSTRACTIONS['EMAIL']

def test_invalid_email_returns_none():
    assert Abstractor().get_abstraction('Email quiet.') == None

def test_invalid_first_name_returns_none():
    assert Abstractor().get_abstraction('First name car') == None

def test_invalid_last_name_returns_none():
    assert Abstractor().get_abstraction('last name promise') == None

def test_invalid_email2_returns_none():
    assert Abstractor().get_abstraction('Email @gmail.com') == None

def test_invalid_email3_returns_none():
    assert Abstractor().get_abstraction('Email quine') == None

def test_invalid_email4_returns_none():
    assert Abstractor().get_abstraction('Email -1.0') == None

def test_invalid_first2_name_returns_none():
    assert Abstractor().get_abstraction('First name 3.3') == None

def test_invalid_last2_name_returns_none():
    assert Abstractor().get_abstraction('Last name NY') == None

def test_invalid_email5_returns_none():
    assert Abstractor().get_abstraction('Email lol.example.com') == None

def test_invalid_email6_returns_none():
    assert Abstractor().get_abstraction('Email: what@e') == None

def test_invalid_input():
    with pytest.raises(Exception):
        Abstractor().get_abstraction({})
