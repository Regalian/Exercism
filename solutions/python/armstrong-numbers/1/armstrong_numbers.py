def is_armstrong_number(number: int) -> bool:
    """
    Determine if a number is an Armstrong number.

    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

    For example:

    - 9 is an Armstrong number, because `9 = 9^1 = 9`
    - 10 is _not_ an Armstrong number, because `10 != 1^2 + 0^2 = 1`
    - 153 is an Armstrong number, because: `153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`
    - 154 is _not_ an Armstrong number, because: `154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190`
    :param number: The number to check.
    :return: True if the number is an Armstrong number, False otherwise.
    """

    digits: tuple[int] = tuple(int(digit) for digit in str(number))
    n_digits = len(digits)
    total: int = sum(digit**n_digits for digit in digits)
    return total == number
