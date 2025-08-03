COLORS = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
]

COLOR_MAP = {
    color.lower(): index for index, color in enumerate(COLORS)
}


def color_code(color: str) -> int:
    """Return the numerical value of a resistor color.

    Args:
        color (str): The color of the resistor.

    Returns:
        int: The numerical value of the color.
    """

    return COLOR_MAP[color.lower()]


def colors()->list[str]:
    """Return a list of all resistor colors.

    Returns:
        list[str]: A list of all resistor colors.
    """

    return COLORS
