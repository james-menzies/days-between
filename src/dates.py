from __future__ import annotations

from typing import Optional

standard_days_in_month = {
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


def is_leap_year(year: int) -> bool:
    if year % 4 > 0:
        return False

    if year % 100 == 0 and year % 400 > 0:
        return False

    return True


def get_days_in_month(month: int, year: int) -> int:
    if is_leap_year(year) and month == 2:
        return 29

    return standard_days_in_month[month]


def get_complete_months_in_days_for_year(month_1: int, month_2: int, year: int):
    days = 0

    if month_2 <= month_1:
        return days

    for i in range(month_1, month_2):
        days += get_days_in_month(i, year)

    return days


def get_complete_years_in_days(year_1: int, year_2: int):
    days = 0

    if year_2 <= year_1:
        return days

    for i in range(year_1, year_2):

        days += 366 if is_leap_year(i) else 365

    return days


def days_between(date_1: Date, date_2: Date) -> int:
    # handle equality edge case
    if date_1 == date_2:
        return 0

    # result initialized at -1 to account for exclusive date range calculation.
    result: int = -1

    # Swap dates if they are in reverse order.
    if date_2 < date_1:
        date_1, date_2 = date_2, date_1

    # Handle same year and month scenario
    if date_1.year == date_2.year and date_1.month == date_2.month:
        result += date_2.day - date_1.day
        return result

    if date_1.year == date_2.year:
        result += get_days_in_month(date_1.month, date_1.year) - date_1.day
        result += get_complete_months_in_days_for_year(date_1.month + 1, date_2.month,
                                                       date_1.year)
        result += date_2.day
        return result

    result += get_days_in_month(date_1.month, date_1.year) - date_1.day
    result += get_complete_months_in_days_for_year(date_1.month + 1, 13, date_1.year)
    result += get_complete_years_in_days(date_1.year + 1, date_2.year)
    result += get_complete_months_in_days_for_year(1, date_2.month, date_2.year)
    result += date_2.day
    return result


class Date:

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def get_valid_date(year: int, month: int, day: int) -> Optional[Date]:
        """
        Produce a valid Date given the inputs of day, month and year.
        :return: An instance of Date if the inputs are valid, or None if invalid.
        """

        if year < 1900 or year > 2999:
            return None

        if month < 1 or month > 12:
            return None

        if day < 1 or day > get_days_in_month(month, year):
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
