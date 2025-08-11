from enum import Enum
from typing import NamedTuple

class RomanNumeral(NamedTuple):
    value: int
    numeral: str

class ErrorMessages(str, Enum):
    NUMBER_OUT_OF_RANGE = "Number out of range (must be between 1-3999)"


NUMERALS = (
    RomanNumeral(1000, "M"),
    RomanNumeral(900, "CM"),
    RomanNumeral(500, "D"),
    RomanNumeral(400, "CD"),
    RomanNumeral(100, "C"),
    RomanNumeral(90, "XC"),
    RomanNumeral(50, "L"),
    RomanNumeral(40, "XL"),
    RomanNumeral(10, "X"),
    RomanNumeral(9, "IX"),
    RomanNumeral(5, "V"),
    RomanNumeral(4, "IV"),
    RomanNumeral(1, "I"),
)
MIN_ROMAN = 1
MAX_ROMAN = 3999

def roman(number: int) -> str:
    """Converts an integer to a Roman numeral.

    Args:
        number (int): The integer to convert.
    Returns:
        str: The Roman numeral representation of the integer.
    Raises:
        ValueError: If the input number is out of range (1-3999).
    """
    if not MIN_ROMAN <= number <= MAX_ROMAN:
        raise ValueError(ErrorMessages.NUMBER_OUT_OF_RANGE)

    result = ""
    for numeral in NUMERALS:
        while number >= numeral.value:
            number -= numeral.value
            result += numeral.numeral
    return result
