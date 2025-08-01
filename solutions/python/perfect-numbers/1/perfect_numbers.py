def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if type(number) is not int or number <= 0:
        # if a number to be classified is less than 1.
        raise ValueError("Classification is only possible for positive integers.")  # noqa: TRY003

    factors = tuple(i for i in range(1, number) if number % i == 0)
    aliquot_sum = sum(factors)
    print(number, factors, aliquot_sum)
    if len(factors) == 1:
        return "deficient"
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"
