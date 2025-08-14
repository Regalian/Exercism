from typing import Callable
from enum import Enum


class ErrorMessages(Enum):
    STACK_UNDERFLOW = "Insufficient number of items in stack"
    UNDEFINED_OPERATION = "undefined operation"
    DIVISION_BY_ZERO = "divide by zero"
    ILLEGAL_OPERATION = "illegal operation"


class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


OPERATOR_MAP: dict[str, Callable[[int, int], int]] = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}


def _dup(stack: list[int]) -> None:
    """Duplicate the top element of the stack.

    Args:
        stack (list[int]): The stack to duplicate.
    """
    stack.append(stack[-1])


def _swap(stack: list[int]) -> None:
    """Swap the top two elements of the stack.

    Args:
        stack (list[int]): The stack to swap.
    """
    stack[-2:] = stack[-1], stack[-2]


def _drop(stack: list[int]) -> None:
    """Drop the top element of the stack.

    Args:
        stack (list[int]): The stack to drop.
    """
    stack.pop()


def _over(stack: list[int]) -> None:
    """Duplicate the second element of the stack.

    Args:
        stack (list[int]): The stack to duplicate.
    """
    stack.append(stack[-2])


STACK_MANIPULATION_MAP: dict[str, Callable[[list[int]], None]] = {
    "dup": _dup,
    "drop": _drop,
    "swap": _swap,
    "over": _over,
}
START_WORD_DEFINITION: str = ":"
END_WORD_DEFINITION: str = ";"


def apply_operator(stack: list[int], operator: str) -> None:
    """Apply an operator to the top two elements of the stack.

    Args:
        stack (list[int]): The stack to apply the operator to.
        operator (str): The operator to apply.
    Raises:
        StackUnderflowError: If the stack does not have enough elements.
        ZeroDivisionError: If the second element is zero.
    """
    try:
        right = stack.pop()
        left = stack.pop()
        stack.append(OPERATOR_MAP[operator](left, right))
    except IndexError:
        raise StackUnderflowError(ErrorMessages.STACK_UNDERFLOW.value)
    except ZeroDivisionError:
        raise ZeroDivisionError(ErrorMessages.DIVISION_BY_ZERO.value)


def manipulate_stack(stack: list[int], operation: str) -> None:
    """Manipulate the stack according to the given operation.

    Args:
        stack (list[int]): The stack to manipulate.
        operation (str): The operation to perform.
    Raises:
        StackUnderflowError: If the stack does not have enough elements.
    """
    try:
        STACK_MANIPULATION_MAP[operation](stack)
    except IndexError:
        raise StackUnderflowError(ErrorMessages.STACK_UNDERFLOW.value)


def push_to_stack(stack: list[int], value: str) -> None:
    """Push a value to the stack.

    Args:
        stack (list[int]): The stack to push to.
        value (str): The value to push.
    Raises:
        ValueError: If the value is not an integer.
    """
    try:
        stack.append(int(value))
    except ValueError:
        raise ValueError(ErrorMessages.UNDEFINED_OPERATION.value)


def expand_definition(definition: list[str], user_defined_words: dict[str, list[str]]):
    """Expand a definition into a list of words.

    Args:
        definition (list[str]): The definition to expand.
        user_defined_words (dict[str, list[str]]): The user-defined words.
    Returns:
        list[str]: The expanded definition.
    """
    result = []
    for word in definition:
        if word in user_defined_words:
            result.extend(
                expand_definition(user_defined_words[word], user_defined_words)
            )
        else:
            result.append(word)
    return result


def evaluate(input_data: list[str]) -> list[int]:
    """Evaluate a list of Forth commands.

    This function evaluates a list of Forth commands and returns the final stack state.
    It supports basic stack manipulation operations (DUP, DROP, SWAP, OVER)and word definitions :word-name;.
    It also supports basic integer arithmetic operations (+, -, *, /).

    Args:
        input_data: A list of Forth commands.

    Returns:
        The final stack state after evaluating the input data.
    """
    user_defined_words: dict[str, list[str]] = {}
    stack: list[int] = []
    for line in input_data:
        tokens: list[str] = line.lower().split()
        in_word_definition = False
        current_definition = []
        while tokens:
            token, *tokens = tokens
            if token == START_WORD_DEFINITION:
                in_word_definition = True
            elif token == END_WORD_DEFINITION:
                in_word_definition = False
                if current_definition[0].isdigit() or (
                    len(current_definition[0]) > 1
                    and current_definition[0][0] == "-"
                    and current_definition[0][1:].isdigit()
                ):
                    raise ValueError(ErrorMessages.ILLEGAL_OPERATION.value)
                user_defined_words[current_definition[0]] = expand_definition(
                    current_definition[1:], user_defined_words
                )
            elif in_word_definition:
                current_definition.append(token)
            elif token in user_defined_words:
                expanded = expand_definition([token], user_defined_words)
                tokens = expanded + tokens
            elif token in OPERATOR_MAP:
                apply_operator(stack, token)
            elif token in STACK_MANIPULATION_MAP:
                manipulate_stack(stack, token)
            else:
                push_to_stack(stack, token)
    return stack
