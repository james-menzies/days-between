from src.Date import Date


def days_between(date_1: Date, date_2: Date) -> int:
    """
    Given two dates, calculate the number of days between them.
    The result is non-inclusive of the two dates. For example,
    1/1/1900 and 3/1/1900 yield 1.

    The dates are not required to be in order.
    :param date_1:
    :param date_2:
    :return: The number of days in date range.
    """

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
    # Handle same year but different month scenario
    elif date_1.year == date_2.year:
        result += _get_partial_months(date_1, date_2)
        result += _get_complete_months_in_days_for_year(date_1.month + 1, date_2.month,
                                                        date_1.year)
        return result
    # Handle different year scenario
    else:
        result += _get_partial_months(date_1, date_2)
        result += _get_complete_months_in_days_for_year(date_1.month + 1, 13, date_1.year)
        result += _get_complete_months_in_days_for_year(1, date_2.month, date_2.year)
        result += _get_complete_years_in_days(date_1.year + 1, date_2.year)
        return result


def _get_complete_months_in_days_for_year(month_1: int, month_2: int, year: int) -> int:
    """
    For a given range, determine the number of days in all of those months.
    For example, submitting the values 2 and 5 and 2000 will return the number
    of days in February, March and April in the year 2000 (90).

    :param month_1: Beginning month
    :param month_2: End month (exclusive)
    :param year: Year of range, must be provided to calculate leap years.
    :return: Total number of days.
    """
    days = 0

    if month_2 <= month_1:
        return days

    for i in range(month_1, month_2):
        days += Date.get_days_in_month(i, year)

    return days


def _get_complete_years_in_days(year_1: int, year_2: int) -> int:
    """
    Given a range of years, determine the number of days total
    in those years. For example, providing 2003 and 2006 will
    yield the total number of days in 2003, 2004 and 2005 (1096).
    :param year_1: Start year
    :param year_2: End year (exclusive)
    :return: Total number of days
    """
    days = 0

    if year_2 <= year_1:
        return days

    for i in range(year_1, year_2):
        days += 366 if Date.is_leap_year(i) else 365

    return days


def _get_partial_months(date_1: Date, date_2: Date) -> int:
    """
    Given two dates, figure out the remainder of days in the first
    and last month as part of the total range.

    This is useful when calculating the range of two dates that
    don't occur in the same month.
    :param date_1:
    :param date_2:
    :return: The total number of days.
    """
    result = Date.get_days_in_month(date_1.month, date_1.year) - date_1.day
    result += date_2.day
    return result
