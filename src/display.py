from typing import Optional, List

from src.days_between import days_between, Date

welcome = "Days-Between Calculator"

instructions = \
    """
    Enter two dates when prompted between 1/1/1900 and 31/12/2999 in the format
    (DD/MM/YYYY). The program will calculate the days in-between these two days,
    non-inclusive of the dates given.
    """


def parse_date(input_str: str) -> Optional[Date]:
    """
    Attempts to parse an input string into a Date object.
    :param input_str: An input string in the format DD/MM/YYYY
    :return: A Date object, or None if input is invalid
    """
    try:
        tokens: List[int] = [int(token) for token in input_str.split('/')]
    except ValueError:
        return

    if len(tokens) != 3:
        return

    day, month, year = tokens

    return Date.get_valid_date(year, month, day)


def prompt_for_date(date_name: str) -> Date:
    """
    Continuously prompts the user for a date string until a valid
    input is accepted.
    :param date_name: The name of the date to inject into the user prompt.
    :return: The fully-parsed Date object
    """
    date: Optional[Date] = None
    while not date:

        input_str = input(f"{date_name} (DD/MM/YYYY) >> ")
        date = parse_date(input_str)
        if not date:
            print("Invalid Date! Please try again.")

    return date


def run():
    print(welcome)
    print(instructions)

    date_1 = prompt_for_date("Date #1")
    date_2 = prompt_for_date("Date #2")

    result = days_between(date_1, date_2)

    print(f"Days between dates {date_1} and {date_2}: {result}")
