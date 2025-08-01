def square(number):
    """Return the number of grains on a given square of the chessboard.
    param: number: int The square number (1-64).

    Returns: int The number of grains on the square.

    Raises: ValueError If the square number is not between 1 and 64.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")  # noqa: TRY003

    return 1 << (number - 1)


def total():
    """Return the total number of grains on the chessboard.

    Returns:
        int: The total number of grains on the chessboard.
    """
    return (1 << 64) - 1
