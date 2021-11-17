import unittest

from src.Date import Date
from src.days_between import days_between


class TestDaysBetween(unittest.TestCase):

    def test_case_1(self):
        self.run_sample(Date(1983, 6, 2), Date(1983, 6, 22), 19)

    def test_case_2(self):
        self.run_sample(Date(1984, 7, 4), Date(1984, 12, 25), 173)

    def test_case_3(self):
        self.run_sample(Date(1989, 3, 1), Date(1983, 8, 3), 2036)

    def test_case_4(self):
        self.run_sample(Date(2158, 4, 17), Date(2392, 9, 12), 85614)

    def test_case_5(self):
        self.run_sample(Date(2000, 1, 12), Date(2000, 2, 10), 28)

    def test_case_6(self):
        self.run_sample(Date(1985, 6, 6), Date(1986, 11, 12), 523)

    def run_sample(self, date_1: Date, date_2: Date, result: int):
        actual: int = days_between(date_1, date_2)
        self.assertEqual(result, actual)
