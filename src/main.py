from typing import Optional, List

from src.dates import Date, days_between

welcome = "Days-Between Calculator"

instructions = \
    """
    Enter two dates when prompted between 1/1/1900 and 31/12/2999 in the format
    (DD/MM/YYYY). The program will calculate the days in-between these two days,
    non-inclusive of the dates given.
    """


def parse_date(input_str: str) -> Optional[Date]:
    try:
        tokens: List[int] = [int(token) for token in input_str.split('/')]
    except ValueError:
        return

    day, month, year, *args = tokens

    if len(args) > 0:
        return

    return Date.get_valid_date(year, month, day)


def prompt_for_date(date_name: str) -> Date:
    date: Optional[Date] = None
    while not date:

        input_str = input(f"{date_name} (DD/MM/YYYY) >> ")
        date = parse_date(input_str)
        if not date:
            print("Invalid Date! Please try again.")

    return date


print(welcome)
print(instructions)

date_1 = prompt_for_date("Date #1")
date_2 = prompt_for_date("Date #2")

result = days_between(date_1, date_2)

print(f"Days between dates {date_1} and {date_2}: {result}")
