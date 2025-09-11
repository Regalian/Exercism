from math import floor, sqrt

MIN_PRIME: int = 2

def to_index(number: int) -> int:
    """Helper function to convert a number into an index.
    
    we want to map numbers 3, 5, 7, 9, ... to indices 0, 1, 2, 3, ... This is a linear mapping index = (number - 3) // 2
    Args:
        number (int): number to convert

    Returns:
        int: index
    """
    return (number - 3) // 2


def primes(limit: int) -> list[int]:
    """Find all primes up to and including limit

    Uses Sieve of Eratosthenes algorithm

    Args:
        limit (int): Maximum number to consider

    Returns:
        list[int]: List of primes. An empty list is returned if limit < 2.
    """

    # return an empty list for limits below 2
    if limit < MIN_PRIME:
        return []
    
    # Treat 2 as a special case and return early
    if limit == 2:
        return [2]

    # Two is prime and all other even numbers are not, so we only need to store the status for odd numbers from 3
    # Initially assume all numbers are prime. Mark them false as we find prime factors for them.
    # At the point of return only prime numbers will be left marked True
    is_prime: list[bool] = [True] * (to_index(limit + 1) + 1)
    candidate: int = MIN_PRIME + 1

    # only need to check for numbers up to sqrt(limit) as one factor must be >= sqrt(limit) and the other <= sqrt(limit)
    max_to_check: int = floor(sqrt(limit))
    while candidate <= max_to_check:
        # mark off all multiples of the prime upto the limit. We will have already marked smaller multiples so start at prime * prime
        # a step of prime in indices is equivalent to a step of 2 * prime in numbers. 
        for i in range(to_index(candidate * candidate), to_index(limit + 1), candidate):
            is_prime[i] = False

        # find the next prime, skipping over even numbers
        candidate += 2
        while candidate <= limit and not is_prime[to_index(candidate)]:
            candidate += 2

    result: list[int] =  [2] + [i for i in range(MIN_PRIME + 1, limit + 1, 2) if is_prime[to_index(i)]]
    return result