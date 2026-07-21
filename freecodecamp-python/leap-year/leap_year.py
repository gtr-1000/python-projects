def is_leap_year(year: int) -> str:
    """Check whether a given year is a leap year.

    A year is a leap year if it's divisible by 4 and not divisible by 100,
    or if it's divisible by 400.

    >>> is_leap_year(2000)
    '2000 is a leap year.'
    >>> is_leap_year(1900)
    '1900 is not a leap year.'
    """
    leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    return f"{year} is a leap year." if leap else f"{year} is not a leap year."


if __name__ == "__main__":
    year = 2023
    result = is_leap_year(year)
    print(result)
