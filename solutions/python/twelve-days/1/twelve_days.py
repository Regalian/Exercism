from enum import Enum
from typing import NamedTuple


class DayInfo(NamedTuple):
    ordinal: str
    gift: str


class ErrorMessages(str, Enum):
    INVALID_START_VERSE = "Invalid start verse"
    INVALID_END_VERSE = "Invalid end verse"
    INVALID_RANGE = (
        "Invalid range (start verse must be less than or equal to end verse)"
    )


FIRST_DAY_GIFT = "a Partridge in a Pear Tree."
TWELVE_DAYS = {
    1: DayInfo("first", f"and {FIRST_DAY_GIFT}"),
    2: DayInfo("second", "two Turtle Doves"),
    3: DayInfo("third", "three French Hens"),
    4: DayInfo("fourth", "four Calling Birds"),
    5: DayInfo("fifth", "five Gold Rings"),
    6: DayInfo("sixth", "six Geese-a-Laying"),
    7: DayInfo("seventh", "seven Swans-a-Swimming"),
    8: DayInfo("eighth", "eight Maids-a-Milking"),
    9: DayInfo("ninth", "nine Ladies Dancing"),
    10: DayInfo("tenth", "ten Lords-a-Leaping"),
    11: DayInfo("eleventh", "eleven Pipers Piping"),
    12: DayInfo("twelfth", "twelve Drummers Drumming"),
}


def _build_gifts(verse: int) -> str:
    if verse == 1:
        return FIRST_DAY_GIFT

    gifts = []
    for i in range(verse, 0, -1):
        gifts.append(TWELVE_DAYS[i].gift)
    return ", ".join(gifts)


def _build_line(verse: int) -> str:
    gifts = _build_gifts(verse)
    return f"On the {TWELVE_DAYS[verse].ordinal} day of Christmas my true love gave to me: {gifts}"


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the Twelve Days of Christmas song.

    Args:
        start_verse (int): The starting verse of the song.
        end_verse (int): The ending verse of the song.

    Returns:
        list[str]: A list of strings representing the verses of the song.

    Raises:
        ValueError: If the start or end verse is invalid.
    """
    if not 1 <= start_verse <= 12:
        raise ValueError(ErrorMessages.INVALID_START_VERSE)
    if not 1 <= end_verse <= 12:
        raise ValueError(ErrorMessages.INVALID_END_VERSE)
    if not start_verse <= end_verse:
        raise ValueError(ErrorMessages.INVALID_RANGE)

    lines = []
    for verse in range(start_verse, end_verse + 1):
        lines.append(_build_line(verse))
    return lines
