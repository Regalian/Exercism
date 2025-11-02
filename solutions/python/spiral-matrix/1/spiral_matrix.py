from enum import Enum


class ErrorMessages(Enum):
    INVALID_SIZE = "Size cannot be negative"


class Direction(Enum):
    LEFT = -1, 0
    RIGHT = 1, 0
    UP = 0, -1
    DOWN = 0, 1


def spiral_matrix(size: int) -> list[list[int]] | list:
    """Print a spiral matrix of the given size.

    Args:
        size (int): The size of the matrix.

    Returns:
        list[list[int]] | list: The spiral matrix.

    Raises:
        ValueError: If the size is negative.
    """
    if size < 0:
        raise ValueError(ErrorMessages.INVALID_SIZE.value)

    if size == 0:
        return []

    matrix = [[0 for _ in range(size)] for _ in range(size)]

    x_min, x_max = 0, size - 1
    y_min, y_max = 0, size - 1
    x_pos, y_pos = 0, 0
    direction = Direction.RIGHT

    for number in range(1, size * size + 1):
        matrix[y_pos][x_pos] = number
        x_pos, y_pos = x_pos + direction.value[0], y_pos + direction.value[1]
        match (direction, x_pos, y_pos):
            case (Direction.RIGHT, x, y) if x == x_max:
                direction = Direction.DOWN
                y_min += 1
            case (Direction.DOWN, x, y) if y == y_max:
                direction = Direction.LEFT
                x_max -= 1
            case (Direction.LEFT, x, y) if x == x_min:
                direction = Direction.UP
                y_max -= 1
            case (Direction.UP, x, y) if y == y_min:
                direction = Direction.RIGHT
                x_min += 1
    return matrix
