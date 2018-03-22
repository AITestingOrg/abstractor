'''
Abstractor integration tests
'''
import pytest
from .abstractor import get_abstraction
from .abstractions import ABSTRACTIONS


def test_valid_name_returns_valid_name():
    assert get_abstraction('Jack') == ABSTRACTIONS['FIRST_NAME']


def test_valid_company_returns_valid_company():
    assert get_abstraction('Striker') == ABSTRACTIONS['LAST_NAME']


def test_invalid_input():
    with pytest.raises(Exception):
        get_abstraction({})
