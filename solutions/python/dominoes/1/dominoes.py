def flip(domino: tuple[int, int]) -> tuple[int, int]:
    """Flip a domino.

    Args:
        domino: A domino represented as a tuple of integers.
    Returns:
        A tuple representing the flipped domino.
    """
    return (domino[1], domino[0])


def build_chain(
    chain: list[tuple[int, int]], remaining_dominoes: list[tuple[int, int]]
) -> list[tuple[int, int]] | None:
    """Recursively build a chain of dominoes

    Args:
        chain: The current chain of dominoes.
        remaining_dominoes: The remaining dominoes to be added to the chain.
    Returns:
        A list of dominoes representing a chain if possible, otherwise None.
    """
    if not remaining_dominoes:
        return chain
    for index, domino in enumerate(remaining_dominoes):
        new_remaining_dominoes = [
            *remaining_dominoes[:index],
            *remaining_dominoes[index + 1 :],
        ]
        if chain[-1][1] == domino[0]:
            new_chain = build_chain([*chain, domino], new_remaining_dominoes)
            if new_chain:
                return new_chain
        elif chain[-1][1] == domino[1]:
            new_chain = build_chain([*chain, flip(domino)], new_remaining_dominoes)
            if new_chain:
                return new_chain
    return None


def can_chain(dominoes: list[tuple[int, int]]) -> list[tuple[int, int]] | None:
    """Return a chain of dominoes if it is possible to chain them, otherwise return None.

    A chain must include all of the input dominoes.

    Args:
        dominoes: A list of dominoes represented as tuples of integers.
    Returns:
        A list of dominoes representing a chain if possible, otherwise None.
    """
    if dominoes == []:
        return []

    chain = build_chain([dominoes[0]], dominoes[1:])
    return chain if chain and chain[0][0] == chain[-1][1] else None
