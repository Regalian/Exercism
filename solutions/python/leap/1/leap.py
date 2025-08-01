import re
def leap_year(year: int) -> bool:
    """Check if a year is a leap year.

    A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

    param year: The year to check.
    return: True if the year is a leap year, False otherwise.
    """

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
