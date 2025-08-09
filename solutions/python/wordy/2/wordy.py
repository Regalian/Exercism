import re
from collections.abc import Callable
from enum import Enum

class ErrorMessages(str, Enum):
    SYNTAX_ERROR = "syntax error"
    UNKNOWN_OPERATION = "unknown operation"

OPERATORS: dict[str, Callable[[int | float, int | float], int | float]] = {
    'plus': lambda x, y: x + y,
    'minus': lambda x, y: x - y,
    'multiplied_by': lambda x, y: x * y,
    'divided_by': lambda x, y: x / y
}

def _parse_int(token: str) -> int:
    try:
        return int(token)
    except ValueError:
        raise ValueError(ErrorMessages.SYNTAX_ERROR)

def _extract_tokens(question: str) -> list[str]:
    equation = re.findall(r'^what is (.+)\?', question.lower().strip().rstrip())
    try:
        equation = equation[0].replace(' by', '_by')
        tokens = equation.split()
    except IndexError:
        raise ValueError(ErrorMessages.SYNTAX_ERROR)
    if not tokens:
        raise ValueError(ErrorMessages.SYNTAX_ERROR)
    return tokens

def _parse_operator(token: str) -> Callable[[int | float, int | float], int | float]:
    if token in OPERATORS:
        return OPERATORS[token]

    # If it's a number where we expected an operator, that's a syntax error
    try:
        _parse_int(token)
    except ValueError:
        raise ValueError(ErrorMessages.UNKNOWN_OPERATION)
    raise ValueError(ErrorMessages.SYNTAX_ERROR)


def _get_next_token(tokens: list[str]) -> str:
    try:
        return tokens.pop(0)
    except IndexError:
        raise ValueError(ErrorMessages.SYNTAX_ERROR)

def answer(question: str) -> int | float:
    """
    Evaluate a simple math word problem.

    Args:
        question (str): The math word problem to be evaluated.
                        Example: "What is 5 plus 13?"

    Returns:
        int | float: The result of the math word problem.

    Raises:
        ValueError: If the input has invalid syntax or unknown operations.

    Examples:
        >>> answer("What is 5 plus 13?")
        18
        >>> answer("What is 7 minus 5?")
        2
    """

    tokens = _extract_tokens(question)

    total: int | float = _parse_int(tokens.pop(0))

    while tokens:
        token = _get_next_token(tokens)
        operator = _parse_operator(token)
        token = _get_next_token(tokens)
        operand = _parse_int(token)
        total = operator(total, operand)
    return total
