def is_paired(input_string: str) -> bool:
    """Check if the input string has matching brackets.

    Args:
        input_string (str): The string to check for matching brackets.

    Returns:
        bool: True if the input string has matching brackets, False otherwise.
    """

    opening = '([{'
    closing = {')': '(', ']': '[', '}': '{'}

    stack = []

    for char in input_string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != closing[char]:
                return False
    return not stack
