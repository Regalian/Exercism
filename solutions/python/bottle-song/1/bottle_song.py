from enum import Enum


class ErrorMessages(Enum):
    START_OUT_OF_RANGE = "The start number of bottles must be between 1 and 10."
    TAKE_OUT_OF_RANGE = "The number of verses to take must be greater than 0."
    INVALID_RANGE = "The number of bottles to take exceeds the available bottles from the start number."
    INVALID_TYPE = "start and take must be integers."


MAX_BOTTLES: int = 10
MIN_BOTTLES: int = 1

NUMBERS: dict[int, str] = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
}

INTRO_LINE_MANY: str = "{number} green bottles hanging on the wall,"
INTRO_LINE_ONE: str = "One green bottle hanging on the wall,"
MIDDLE_LINE: str = "And if one green bottle should accidentally fall,"
END_LINE_MANY: str = "There'll be {number} green bottles hanging on the wall."
END_LINE_ONE: str = "There'll be one green bottle hanging on the wall."
END_LINE_NO: str = "There'll be no green bottles hanging on the wall."


def validate_input(start: int, take: int) -> None:
    """
    Validates the input for the Ten Green Bottle song.
    Args:
        start (int): The number of green bottles to start with.
        take (int): The number of verses to take.

        Raises:
        TypeError: If start or take is not an integer.
        ValueError: If start or take is out of range.
        ValueError: If take is greater than start.
    """
    if not isinstance(start, int) or not isinstance(take, int):
        raise TypeError(ErrorMessages.INVALID_TYPE.value)
    if not (MIN_BOTTLES <= take <= MAX_BOTTLES) or not (
        MIN_BOTTLES <= start <= MAX_BOTTLES
    ):
        raise ValueError(ErrorMessages.START_OUT_OF_RANGE.value)
    if take < MIN_BOTTLES:
        raise ValueError(ErrorMessages.TAKE_OUT_OF_RANGE.value)
    if take > start:
        raise ValueError(ErrorMessages.INVALID_RANGE.value)


def build_verse(bottles: int) -> list[str]:
    """
    Builds a verse of the Ten Green Bottle song.

    Args:
        bottles (int): The number of green bottles to start with.

    Returns:
        list[str]: A list of lines that make up the verse.
    """
    verse: list[str] = []
    if bottles > 1:
        verse.append(INTRO_LINE_MANY.format(number=NUMBERS[bottles]))
        verse.append(INTRO_LINE_MANY.format(number=NUMBERS[bottles]))
    elif bottles == 1:
        verse.append(INTRO_LINE_ONE)
        verse.append(INTRO_LINE_ONE)
    verse.append(MIDDLE_LINE)
    if bottles > 2:
        verse.append(END_LINE_MANY.format(number=NUMBERS[bottles - 1].lower()))
    elif bottles == 2:
        verse.append(END_LINE_ONE)
    else:
        verse.append(END_LINE_NO)
    return verse


def recite(start: int, take: int = 1) -> list[str]:
    """
    Recites the Ten Green Bottle song.

    Args:
        start (int): The number of green bottles to start with.
        take (int, optional): The number of verses to take. Defaults to 1.

    Returns:
        list[str]: A list of verses.

    Raises:
        TypeError: If start or take is not an integer.
        ValueError: If start or take is out of range.
        ValueError: If take is greater than start.
    """
    validate_input(start, take)
    verses: list[str] = []
    bottles_left: int = start
    for verses_left in range(take, 0, -1):
        verses.extend(build_verse(bottles_left))
        bottles_left -= 1
        if verses_left - 1:
            verses.append("")
    return verses
