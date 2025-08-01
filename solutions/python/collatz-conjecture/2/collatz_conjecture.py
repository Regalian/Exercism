def steps(number: int) -> int:
    """Returns the number of steps required to reach 1 from the given number.

    :param number: int  The number to start from.
    :return: int  The number of steps required to reach 1.
    :raises: ValueError If the number is less than or equal to 0.
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")  # noqa: TRY003

    count: int = 0
    while number > 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        count += 1
    return count
