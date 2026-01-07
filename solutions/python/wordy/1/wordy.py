import re
SYNTAX_ERROR = "syntax error"
UNKNOWN_OPERATION = "unknown operation"
OPERATORS = {
    'plus': lambda x, y: x + y,
    'minus': lambda x, y: x - y,
    'multiplied_by': lambda x, y: x * y,
    'divided_by': lambda x, y: x / y
}

def answer(question:str)->int:
    """
    Evaluate a simple math word problem.

    Args:
        question (str): The math word problem to be evaluated.

    Returns:
        int: The result of the math word problem.

    Raises:
        ValueError: If the input is invalid.
    """

    equation = re.findall(r'^what is (.+)\?', question.lower().strip().rstrip())
    print(equation)
    if not equation:
        raise ValueError(SYNTAX_ERROR)
    equation = equation[0].replace(' by', '_by')
    tokens = equation.split()
    print(tokens)
    if not tokens:
        raise ValueError(SYNTAX_ERROR)

    try:
        total = int(tokens.pop(0))
    except ValueError:
        raise ValueError(SYNTAX_ERROR)

    token  = None
    while tokens:
        try:
            token = tokens.pop(0)
        except IndexError:
            raise ValueError(SYNTAX_ERROR)
        try:
            operator = OPERATORS[token]
        except KeyError:
            try:
                _ = int(token)
            except ValueError:
                raise ValueError(UNKNOWN_OPERATION)
            raise ValueError(SYNTAX_ERROR)

        try:
            token = tokens.pop(0)
        except IndexError:
            raise ValueError(SYNTAX_ERROR)
        try:
            operand = int(token)
        except ValueError:
            raise ValueError(SYNTAX_ERROR)

        total = operator(total, operand)
    return total
