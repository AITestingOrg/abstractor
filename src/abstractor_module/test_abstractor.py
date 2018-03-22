'''
Abstractor integration tests
'''
import pytest
from .abstractor import get_abstraction
from .abstractions import ABSTRACTIONS


def test_valid_name_returns_valid_name():
    assert get_abstraction('Jack') == ABSTRACTIONS['FIRST_NAME']


def test_valid_company_returns_valid_company():
    assert get_abstraction('IBM') == ABSTRACTIONS['ORG']


def test_dollar_value_returns_valid_currency():
    assert get_abstraction('$5.00') == ABSTRACTIONS['MONEY']


def test_invalid_input():
    with pytest.raises(Exception):
        get_abstraction({})
