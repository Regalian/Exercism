def step(number: int, count: int = 0):
    """Recursive function to calculate the number of steps required to reach 1 from the given number.

    :param number: int  The number to start from.
    :param count: int  The number of steps taken so far.
    :return: int  The number of steps required to reach 1.
    """

    if number == 1:
        return count
    elif number % 2 == 0:
        return step(number // 2, count + 1)
    else:
        return step(number * 3 + 1, count + 1)


def steps(number: int) -> int:
    """Returns the number of steps required to reach 1 from the given number.

    :param number: int  The number to start from.
    :return: int  The number of steps required to reach 1.
    :raises: ValueError If the number is less than or equal to 0.
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")  # noqa: TRY003
    return step(number)
