import unittest

from src.Date import Date
from src.display import parse_date


class TestDateParser(unittest.TestCase):

    def test_valid_input(self):

        date = parse_date('1/1/2000')
        self.assertTrue(isinstance(date, Date))

    def test_invalid_extra_tokens(self):

        date = parse_date('1/1/2000/2000')
        self.assertIsNone(date)

    def test_non_integer_chars(self):

        date = parse_date('z/1/2000')
        self.assertIsNone(date)

    def test_insufficient_tokens(self):

        date = parse_date('1/12')
        self.assertIsNone(date)

    def test_invalid_date(self):

        date = parse_date('29/2/1989')
        self.assertIsNone(date)
