from enum import Enum


class ErrorMsgs(Enum):
    """
    Error messages for sum_of_multiples.
    """

    LIMIT_ERROR = '"limit" must be > 0'
    MULTIPLE_ERROR = 'all "multiples" must be >= 0'


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """
    Calculates the sum of all unique multiples of the given factors up to (but not including) the limit.


    Args:
        limit (int): The upper bound (exclusive) for finding multiples.
        multiples (list[int]): A list of factors to find multiples for.
    Returns:
        int: The sum of all unique multiples.
    Raises:
        ValueError: If limit is less than 1 or any multiple is negative.
    """
    if limit < 1:
        raise ValueError(ErrorMsgs.LIMIT_ERROR.value)
    if any((i < 0 for i in multiples)):
        raise ValueError(ErrorMsgs.MULTIPLE_ERROR.value)

    # remove duplicates and 0
    multipliers: set[int] = set(multiples) - set([0])
    if multipliers == set():
        return 0

    scores: set[int] = set()
    for multiple in multipliers:
        scores.update(range(multiple, limit, multiple))
    return sum(scores)
