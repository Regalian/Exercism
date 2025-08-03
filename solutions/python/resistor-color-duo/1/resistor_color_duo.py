COLOR_MAP = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def value(colors: list[str])-> int:
    """Return the value of a resistor based on its color bands.

    Args:
        colors (list[str]): A list of strings representing the colors of the resistor's bands.

    Returns:
        int: The value of the resistor in ohms.
    """

    if len(colors) < 2:
        raise ValueError("At least two colors are required")

    value = COLOR_MAP[colors[0].lower()] * 10 + COLOR_MAP[colors[1].lower()]
    return value
