from itertools import zip_longest


def _clean_transposed_row(row: str) -> str:
    return row.rstrip("\u2420").replace("\u2420", " ")


def transpose(text: str) -> str:
    """Transpose an input string

    Rows in the string are separated by '\n'.

    Args:
        text: str: The string to be transposed

    Returns:
        str: The transposed string
    """
    if not text:
        return ""

    # split into rows
    rows: list[str] = text.split("\n")
    # transpose, filling missing values with Unicode NUL (\u0000)
    rows_trans: list[str] = [
        "".join(row) for row in zip_longest(*rows, fillvalue="\u2420")
    ]
    # remove trailing NUL characters and replace ionternal ones by '" "
    rows_final: list[str] = [_clean_transposed_row(row) for row in rows_trans]
    return "\n".join(rows_final)
