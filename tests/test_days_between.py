import unittest

from src.dates import Date, days_between


class TestDaysBetween(unittest.TestCase):

    def test_case_1(self):
        self.run_sample(Date(1983, 6, 2), Date(1983, 6, 22), 19)

    def test_case_2(self):
        self.run_sample(Date(1984, 7, 4), Date(1984, 12, 25), 173)

    def test_case_3(self):
        self.run_sample(Date(1989, 1, 3), Date(1983, 8, 3), 2036)

    def run_sample(self, date_1: Date, date_2: Date, result: int):
        actual: int = days_between(date_1, date_2)
        self.assertEqual(result, actual)
