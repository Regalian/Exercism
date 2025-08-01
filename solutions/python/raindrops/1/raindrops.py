def convert(number: int) -> str:
    """Convert a number to a string based on raindrop sounds.

        param: number (int): The number to convert.
        returns: str: The converted string.
    """

    result: str = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    return result or str(number)
