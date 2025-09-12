from enum import Enum

class ErrorMessages(Enum):
    IRREGULAR_MATRIX = "irregular matrix"


def is_regular(matrix: list[list[int]]) -> bool:
    """ Check whether a matrix is irregular, i.e. all rows have the same number of columns

    Args:
        matrix (list[list[int]]): The matrix to check

    Returns:
        bool: True if the matrix is regular, False otherwise
    """
    try:
        length_of_first_row = len(matrix[0])
    except IndexError:
        return False
    return all(len(row) == length_of_first_row for row in matrix)

def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    """ Find the saddle points in a matrix

    Args:
        matrix (list[list[int]]): The matrix to find the saddle points in

    Raises:
        ValueError: If the matrix is irregular

    Returns:
        list[dict[str, int]]: A list of dictionaries containing the row and column of each saddle point
    """

    if not matrix or not matrix[0]:
        return []
    if not is_regular(matrix):
        raise ValueError(ErrorMessages.IRREGULAR_MATRIX.value)
    points_found: list[dict[str, int]] = []
    max_row_values: list[int] = []
    min_column_values: list[int] = []

    for row_index, row in enumerate(matrix):
        max_row_values.append(max(row))
    for column_index, col in enumerate(zip(*matrix)):
        min_column_values.append(min(col))
    for row_index, row in enumerate(matrix):
        for column_index, value in enumerate(row):
            if value == max_row_values[row_index] and value == min_column_values[column_index]:
                points_found.append({"row": row_index + 1, "column":column_index + 1}) # 1-based indexing for output
    return points_found
