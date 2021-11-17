
# Days Between

## Premise

This CLI program will accept two dates and calculate the number in between them and display it to the user. The total will not include the provided dates. The program guides the user interactively through the process.

It will rely solely on built-in functions and primitives and not use modules such as `datetime`.

### Leap Years

A key consideration when making these calculations are leap years. This will add extra day to February of that year bringing the total number of days in the month to 29. In order to determine which year is a leap year:
* The year must be divisible by 4. *e.g. 1988*
* If the year is also divisible by 100, it must then be divisible by 400. For example, 2000 is a leap year and 1900 is not.

## How to Run

This program requires Python 3.6+ to run. Simply clone the repository, navigate to the source directory and run `python days_between.py` (`python3 days_between.py` on some platforms). No external dependencies are required.

To run the test suite run `python[3] -m unittest discover tests`.

## Components

### User Flow

The program will ask the user for 2 dates in sequence by looping through a prompt/input cycle and then attempt to parse a `Date` object from it. On invalid input, it re-prompts the user.

Once the 2 date objects are obtained, it will call the `days_between` module to provide the actual calculation. It then returns the result and the program terminates.

### Date Object

This date structure will represent a date in the program, containing `day`, `month` and `year` attributes. It will be responsible for:

* Ensuring that dates are between 1/1/1900 and 31/12/2999.
* Ensuring that months are between 1 and 12.
* Ensuring that the day is valid given the month and year.
* Providing a static method that can provide the days in a month, given a month and year.

### Days Between Method

The underlying algorithm used by the application. It will dispatch one of three functions based on the following scenarios:
* Both dates are in the same month and year.
* Both dates are in the same year but different month.
* Both dates are in a different year.

However, before dispatching the appropriate function, it will first determine which of the two dates is the earliest, and swap them around if needed.

> All subroutines will subtract 1 from the final total to ensure that it does not include the day of the end date as part of the calculation.

### Month and Year the Same

The simplest scenario, function returns the difference between the two day values.

###  Year the Same

Calculate the remaining days from the month in the start date. Then add the complete months in-between, then finally add the day value of the end date.

### Different Year

Calculate the remaining days from the month in the start date. Then add all the days of the month for the rest of the year. Then calculate the whole years between the dates. Then the whole months from the start of the year to the month of the end date, and then finally the day value of the end date.

## Testing

### Days Between Method

The following test cases are used to ensure accuracy:

1) 2/6/1983 to 22/6/1983 = 19 days 
2) 4/7/1984 to 25/12/1984 = 173 days
3) 1/3/1989 to 3/8/1983 = 2036 days
4) 17/4/2158 to 12/9/2392 = 85614 days
5) 12/1/2000 to 10/2/2000 = 28 days
6) 6/6/1985 to 12/11/1986 = 523 days


### Dates Module

* The MIN and MAX dates should be enforced.
* Dates should be valid in respect to their day and month variables.

### Dates Parsing

* Test valid / invalid inputs from the user.
