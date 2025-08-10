def rows(letter: str) -> list[str]:
    """Generate a diamond pattern for a given letter.

    Creates a diamond where 'A' appears at the tips and the specified
    letter appears at the widest point.

    Args:
        letter (str): A single alphabetic character.

    Returns:
        list[str]: A list of strings representing the diamond pattern.

    Raises:
        ValueError: If input is not a single alphabetic character.

    Examples:
        >>> rows('A')
        ['A']
        >>> rows('B')
        [' A ', 'B B', ' A ']
    """

    if not letter or len(letter) != 1 or not letter.isalpha():
        raise ValueError("Input must be a single letter")

    # Calculate diamond size: A=1x1, B=3x3, C=5x5, etc.
    size = (ord(letter.upper()) - ord('A')) * 2 + 1

    matrix = [[' '] * size for _ in range(size)]

    middle = size // 2
    for index in range((size + 1) // 2):
        current_letter = chr(ord('A') + index)
        # Top half
        matrix[index][middle + index] = current_letter
        matrix[index][middle - index] = current_letter

        # Bottom half
        matrix[size - index - 1][middle + index] = current_letter
        matrix[size - index - 1][middle - index] = current_letter
    return [''.join(row) for row in matrix]
