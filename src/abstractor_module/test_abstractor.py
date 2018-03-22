'''
Abstractor integration tests
'''
import pytest
from .abstractor import Abstractor
from .abstractions import ABSTRACTIONS


def test_valid_name_returns_valid_name():
    assert Abstractor().get_abstraction('Jack') == ABSTRACTIONS['FIRST_NAME']


def test_valid_company_returns_valid_company():
    assert Abstractor().get_abstraction('Striker') == ABSTRACTIONS['LAST_NAME']


def test_invalid_input():
    with pytest.raises(Exception):
        Abstractor().get_abstraction({})
