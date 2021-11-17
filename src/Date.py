from __future__ import annotations

from typing import Optional


class Date:
    STANDARD_DAYS_IN_MONTH = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Determine whether the provided year is a leap year.
        """
        if year % 4 > 0:
            return False

        if year % 100 == 0 and year % 400 > 0:
            return False

        return True

    @classmethod
    def get_days_in_month(cls, month: int, year: int) -> int:
        """
        From a given month and year, determine how many days are in
        that month.
        :param month:
        :param year:
        :return: The number of days.
        """
        if cls.is_leap_year(year) and month == 2:
            return 29

        return cls.STANDARD_DAYS_IN_MONTH[month]

    @classmethod
    def get_valid_date(cls, year: int, month: int, day: int) -> Optional[Date]:
        """
        Produce a valid Date given the inputs of day, month and year.
        :return: An instance of Date if the inputs are valid, or None if invalid.
        """

        if year < 1900 or year > 2999:
            return None

        if month < 1 or month > 12:
            return None

        if day < 1 or day > cls.get_days_in_month(month, year):
            return None

        return Date(year, month, day)

    def __eq__(self, other) -> bool:

        if not isinstance(other, Date):
            return False

        return self.day == other.day and self.month == other.month and self.year == other.year

    def __lt__(self, other) -> bool:

        if self.year != other.year:
            return self.year < other.year

        if self.month != other.month:
            return self.month < other.month

        return self.day < other.day

    def __repr__(self):
        return f"{self.day}/{self.month}/{self.year}"
