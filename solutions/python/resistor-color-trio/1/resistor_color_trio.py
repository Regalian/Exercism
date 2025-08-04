COLOR_MAP = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def label(colors: list[str]) -> str:
    """Returns the label of a resistor based on its color bands.

    Args:
        colors: A list of strings representing the colors of the resistor bands.

    Returns:
        A string representing the label of the resistor.
    """
    digit = (COLOR_MAP[colors[0]] * 10 + COLOR_MAP[colors[1]]) * (10 ** COLOR_MAP[colors[2]])
    if digit < 1000:
        return f"{digit} ohms"
    if digit < 1000000:
        return f"{digit // 1000} kiloohms"
    if digit < 1000000000:
        return f"{digit // 1000000} megaohms"
    return f"{digit // 1000000000} gigaohms"
