import unittest
from .abstractor import get_abstraction
from .abstractions import ABSTRACTIONS

class AbstractorIntegrationTests(unittest.TestCase):

    def test_valid_name_returns_valid_name(self):
        self.assertEqual(get_abstraction('Jack'), ABSTRACTIONS['PERSON'])

    def test_valid_company_returns_valid_company(self):
        self.assertEqual(get_abstraction('IBM'), ABSTRACTIONS['ORG'])

    def test_dollar_value_returns_valid_currency(self):
        self.assertEqual(get_abstraction('$5.00'), ABSTRACTIONS['MONEY'])

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            get_abstraction({})

if __name__ == '__main__':
    unittest.main()