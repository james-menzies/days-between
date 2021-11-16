import unittest

from src.dates import Date


class TestDate(unittest.TestCase):

    def test_valid_date(self):
        date = Date.get_valid_date(2000, 1, 1)
        self.assertIsNotNone(date)

    def test_invalid_years(self):
        date = Date.get_valid_date(1899, 1, 1)
        self.assertIsNone(date)
        date = Date.get_valid_date(3000, 1, 1)
        self.assertIsNone(date)

    def test_invalid_month(self):
        date = Date.get_valid_date(2000, 0, 1)
        self.assertIsNone(date)
        date = Date.get_valid_date(2000, 13, 1)
        self.assertIsNone(date)

    def test_invalid_day(self):
        date = Date.get_valid_date(2000, 1, 0)
        self.assertIsNone(date)
        date = Date.get_valid_date(2000, 6, 32)
        self.assertIsNone(date)

    def test_uneven_months(self):
        date = Date.get_valid_date(2000, 6, 31)
        self.assertIsNone(date)
        date = Date.get_valid_date(2000, 5, 31)
        self.assertIsNotNone(date)

    def test_leap_years(self):
        date = Date.get_valid_date(1988, 2, 29)
        self.assertIsNotNone(date)
        date = Date.get_valid_date(1989, 2, 29)
        self.assertIsNone(date)
