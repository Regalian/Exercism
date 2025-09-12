def triples(triple: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    """Given a primitive Pythagorean Triple it generates the next 3 triples descended from it

    Uses the matrices of F. J. M. Barning to generate the new triples.
    See https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

    Args:
        triple: tuple[int, int, int]: Primitive Pythagorean Triple
    Returns:
        list[tuple[int, int, int]]: List of tuples generated from the primitive triple
    """

    a, b, c = triple

    return [
        (a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c),
        (a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c),
        (-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c),
    ]


def triplets_with_sum(number) -> list[list[int]]:
    """finds all Pythagorean Triplets that sum to number, i.e. a^2 + b^2 = c^2 and a + b + c = number and a < b < c

    Args:
        number: int: The target number
    Returns:
     list[list[int]]: a list of all Pythagorean Triplets that sum to number
    """
    found: list[tuple[int, int, int]] = []

    triplets: list[tuple[int, int, int]] = [(3, 4, 5)]
    while triplets:
        triplet, *triplets = triplets
        total: int = sum(triplet)
        scale, rem = divmod(number, total)  # type: int, int
        if rem == 0:
            a, b, c = triplet  # type: int, int, int
            found.append((scale * a, scale * b, scale * c))
        if total < number:
            triplets.extend(triples(triplet))
    return [sorted(triplet) for triplet in found]
