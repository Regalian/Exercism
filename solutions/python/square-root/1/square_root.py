def square_root(number:int) ->int:
    """Return the integer square root of a number.

    Uses binary search to find the largest integer x such that x * x <= number
    Args:
        number: The number to find the square root of.

    Returns:
        The integer square root of the number.
    """
    above = number
    below = 0
    while above - below > 1:
        mid = (above + below) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            below = mid
        else:
            above = mid
    return above
