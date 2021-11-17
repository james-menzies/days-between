from src.Date import Date


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
    # Handle same year but different month scenario
    elif date_1.year == date_2.year:
        result += _calculate_partial_months(date_1, date_2)
        result += _get_complete_months_in_days_for_year(date_1.month + 1, date_2.month,
                                                        date_1.year)
        return result
    # Handle different year scenario
    else:
        result += _calculate_partial_months(date_1, date_2)
        result += _get_complete_months_in_days_for_year(date_1.month + 1, 13, date_1.year)
        result += _get_complete_months_in_days_for_year(1, date_2.month, date_2.year)
        result += _get_complete_years_in_days(date_1.year + 1, date_2.year)
        return result


def _get_complete_months_in_days_for_year(month_1: int, month_2: int, year: int):
    days = 0

    if month_2 <= month_1:
        return days

    for i in range(month_1, month_2):
        days += Date.get_days_in_month(i, year)

    return days


def _get_complete_years_in_days(year_1: int, year_2: int):
    days = 0

    if year_2 <= year_1:
        return days

    for i in range(year_1, year_2):
        days += 366 if Date.is_leap_year(i) else 365

    return days


def _calculate_partial_months(date_1: Date, date_2: Date) -> int:
    result = Date.get_days_in_month(date_1.month, date_1.year) - date_1.day
    result += date_2.day
    return result
