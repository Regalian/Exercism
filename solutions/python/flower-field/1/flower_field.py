def _is_rectangle(garden: list[str]) -> bool:
    row_length = len(garden[0])
    return all(len(row) == row_length for row in garden)


def _valid_chars(garden: list[str]) -> bool:
    valid_chars = set(" *")
    return all(set(row).issubset(valid_chars) for row in garden)


def _count_neighbours(garden: list[str], row: int, column: int) -> int:
    count = 0
    RADIUS = 1
    for y in range(max(0, row - RADIUS), min(len(garden), row + RADIUS + 1)):
        for x in range(max(0, column - RADIUS), min(len(garden[0]), column + RADIUS + 1)):
            if x == column and y == row:
                continue
            if garden[y][x] == "*":
                count += 1
    return count


def annotate(garden: list[str]) -> list[str]:
    """Annotates the garden with the count of neighboring flowers for each empty space.

    Args:
        garden (list[str]): The garden grid where '*' represents flowers and ' ' represents empty spaces.
    Returns:
        list[str]: The annotated garden with neighbor counts.
    Raises:
        ValueError: If the garden is not rectangular or contains invalid characters.
    """

    error_msg = "The board is invalid with current input."
    if garden == []:
        return []

    if not _is_rectangle(garden):
        raise ValueError(error_msg)
    if not _valid_chars(garden):
        raise ValueError(error_msg)

    annotated_garden = [[""] * len(garden[0]) for _ in range(len(garden))]
    for row in range(len(garden)):
        for column in range(len(garden[0])):
            count = _count_neighbours(garden, row, column)
            if garden[row][column] == " " and count:
                annotated_garden[row][column] = str(count)
            else:
                annotated_garden[row][column] = garden[row][column]

    return ["".join(row) for row in annotated_garden]
