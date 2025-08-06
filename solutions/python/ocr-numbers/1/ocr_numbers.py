DIGITS = {
'     |  |   ': '1',
' _  _||_    ': '2',
' _  _| _|   ': '3',
'   |_|  |   ': '4',
' _ |_  _|   ': '5',
' _ |_ |_|   ': '6',
' _   |  |   ': '7',
' _ |_||_|   ': '8',
' _ |_| _|   ': '9',
' _ | ||_|   ': '0'
}

CHAR_HEIGHT = 4
CHAR_WIDTH = 3


def convert(input_grid) -> str:
    """Converts a grid of ocr numbers into a string of digits.

    OCR numbers represented as a grid of characters.
        _  _     _  _  _  _  _  _  #
      | _| _||_||_ |_   ||_||_|| | # decimal numbers.
      ||_  _|  | _||_|  ||_| _||_| #
                                   # fourth line is always blank
    Multiple input lines are returned returned with digits on a line separated by ','
    e.g.
      _  _
    | _| _|
    ||_  _|

        _  _
    |_||_ |_
      | _||_|

     _  _  _
      ||_||_|
      ||_| _|

    is returned as "123,456,789"

    Args:
        input_grid (List[str]): A grid of ocr numbers.
    Returns:
        str: A string of digits.
    Raises:
        ValueError: If the number of input lines is not a multiple of four.
        ValueError: If the number of input columns is not a multiple of three.
    """
    # when the rows aren't multiples of 4
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    # when the columns aren't multiples of 3
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    result = []
    for y_offset in range(len(input_grid) // CHAR_HEIGHT):
        line = ''
        for x_offset in range(len(input_grid[0]) // CHAR_WIDTH):
            digit = ''.join(input_grid[i][x_offset*CHAR_WIDTH:(x_offset+1)*CHAR_WIDTH] for i in range(y_offset*CHAR_HEIGHT, (y_offset+1)*CHAR_HEIGHT))
            print(f"::{digit}::")
            line += DIGITS.get(digit, '?')
        result.append(line)
    return ','.join(result)
