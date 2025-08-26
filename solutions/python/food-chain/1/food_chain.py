from enum import Enum


MIN_VERSE: int = 1
MAX_VERSE: int = 8


class ErrorMessages(Enum):
    OUT_OF_RANGE = f"Verse must be between {MIN_VERSE} and {MAX_VERSE}"
    BEGIN_BEFORE_END = "End verse must be after start verse"
    INVALID_TYPE = "Verse must be an integer"


INTRO_TEMPLATE: str = "I know an old lady who swallowed a {}."
MIDDLE_LINE_TEMPLATE: str = "She swallowed the {} to catch the {}."
MIDDLE_LINE_TEMPLATE_SPIDER: str = "She swallowed the {} to catch the {} that wriggled and jiggled and tickled inside her."
LAST_LINE: str = "I don't know why she swallowed the fly. Perhaps she'll die."
ANIMALS: dict[int, tuple[str, str]] = {
    1: ("fly", ""),
    2: ("spider", "It wriggled and jiggled and tickled inside her."),
    3: ("bird", "How absurd to swallow a bird!"),
    4: ("cat", "Imagine that, to swallow a cat!"),
    5: ("dog", "What a hog, to swallow a dog!"),
    6: ("goat", "Just opened her throat and swallowed a goat!"),
    7: ("cow", "I don't know how she swallowed a cow!"),
    8: ("horse", "She's dead, of course!"),
}

middle_lines_cache: dict[tuple[str, str], str] = {}
intro_cache: dict[str, list[str]] = {}


def build_verse(verse: int):
    """Build a verse of the song.

    Args:
        verse (int): The verse number.

    Returns:
        list[str]: The verse of the song.
    """
    verse_lines: list[str] = []
    current_animal, action = ANIMALS[verse]
    verse_lines.extend(build_intro(current_animal, action))
    if verse == MAX_VERSE:
        return verse_lines
    for line_index in range(verse, MIN_VERSE, -1):
        previous_animal = ANIMALS[line_index - 1][0]
        if is_middle_line(line_index):
            verse_lines.append(build_middle_line(current_animal, previous_animal))
        current_animal = previous_animal
    verse_lines.append(LAST_LINE)
    return verse_lines


def build_middle_line(current_animal: str, previous_animal: str) -> str:
    """Build a middle line of a verse.

    Args:
        current_animal (str): The current animal in the line.
        previous_animal (str): The previous animal in the line.

    Returns:
        str: The middle line of the song.
    """
    if middle_lines_cache.get((current_animal, previous_animal), False):
        return middle_lines_cache[(current_animal, previous_animal)]
    if previous_animal != "spider":
        middle_lines_cache[(current_animal, previous_animal)] = (
            MIDDLE_LINE_TEMPLATE.format(current_animal, previous_animal)
        )
    else:
        middle_lines_cache[(current_animal, previous_animal)] = (
            MIDDLE_LINE_TEMPLATE_SPIDER.format(current_animal, previous_animal)
        )
    return middle_lines_cache[(current_animal, previous_animal)]


def build_intro(animal: str, action: str) -> list[str]:
    """Build the intro line(s) of a verse

    Args:
        animal (str): The animal in the line.
        action (str): The action of the animal.

    Returns:
        list[str]: The intro line(s) of the verse.
    """
    if intro_cache.get(animal, False):
        return intro_cache[animal]

    first_line = INTRO_TEMPLATE.format(animal)
    if action:
        intro_cache[animal] = [first_line, action]
    else:
        intro_cache[animal] = [first_line]
    return intro_cache[animal]


def in_range(verse: int) -> bool:
    """Check if the verse is within the valid range.

    Args:
        verse (int): The verse number.

    Returns:
        bool: True if the verse is within the valid range, False otherwise.
    """
    return MIN_VERSE <= verse <= MAX_VERSE


def in_order(start_verse: int, end_verse: int) -> bool:
    """Check if the start and end verses are in order.

    Args:
        start_verse (int): The starting verse of the song.
        end_verse (int): The ending verse of the song.

    Returns:
        bool: True if the start and end verses are in order, False otherwise.
    """
    return start_verse <= end_verse


def is_middle_line(verse: int) -> bool:
    """Check if the verse is a middle verse.

    Args:
        verse (int): The verse number.

    Returns:
        bool: True if the verse is a middle verse, False otherwise.
    """
    return MIN_VERSE < verse < MAX_VERSE


def validate(start_verse: int, end_verse: int) -> None:
    """Validate the start and end verses of the food chain song.

    Args:
        start_verse (int): The starting verse of the song.
        end_verse (int): The ending verse of the song.

    Raises:
        ValueError: If the start or end verse is out of range or if the start verse is greater than the end verse.
    """
    if not isinstance(start_verse, int) or not isinstance(end_verse, int):
        raise TypeError(ErrorMessages.INVALID_TYPE.value)
    if not in_range(start_verse):
        raise ValueError(ErrorMessages.OUT_OF_RANGE.value)
    if not in_range(end_verse):
        raise ValueError(ErrorMessages.OUT_OF_RANGE.value)
    if not in_order(start_verse, end_verse):
        raise ValueError(ErrorMessages.BEGIN_BEFORE_END.value)


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the food chain song from start_verse to end_verse.

    Args:
        start_verse (int): The starting verse of the song.
        end_verse (int): The ending verse of the song.

    Returns:
        list[str]: The recited food chain song.
    """
    validate(start_verse, end_verse)
    complete_song: list[str] = []
    for verse in range(start_verse, end_verse + 1):
        complete_song.extend(build_verse(verse))
        if verse != end_verse:
            complete_song.append("")
    return complete_song
