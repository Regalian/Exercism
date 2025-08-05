VALUE_MAP = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9'
}
MULTIPLIER_MAP = {
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 1000,
    'yellow': 10000,
    'green': 100000,
    'blue': 1000000,
    'violet': 10000000,
    'grey': 100000000,
    'white': 1000000000
}
TOLERANCE_MAP = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10
}
def resistor_label(colors:list[str])->str:
    """Return the label of a resistor based on its colors.

    Args:
        colors (list[str]): A list of colors representing the resistor.

    Returns:
        str: The label of the resistor.
    """
    if len(colors) == 1 and colors[0] == 'black':
        return '0 ohms'
    digits, multiplier, tolerance = colors[:-2], colors[-2], colors[-1]
    value = int(''.join(VALUE_MAP[color] for color in digits)) * MULTIPLIER_MAP[multiplier]
    tolerance = TOLERANCE_MAP[tolerance]
    if value < 1000:
        return f'{value} ohms ±{tolerance}%'
    if value < 1000000:
        return f'{value / 1000:g} kiloohms ±{tolerance}%'
    if value < 1000000000:
        return f'{value / 1000000:g} megaohms ±{tolerance}%'
    return f'{value / 1000000000:g} gigaohms ±{tolerance}%'
