def is_valid(isbn: str)->bool:
    """Validate ISBN-10 number

    This function checks if the given string is a valid ISBN-10 number.

    Args:
        isbn (str): The ISBN-10 number to validate.
    Returns:
        bool: True if the ISBN is valid, and False otherwise.
    """

    check = 0
    check_str = isbn[::-1].replace('-','')
    print(f"{isbn} - {check_str}")
    if len(check_str) != 10:
        return False
    for index, char in enumerate(check_str, 1):
        if char.isdigit():
            check += int(char) * index
        elif char in 'xX' and index == 1:
            check += 10
        else:
            return False
    return check % 11 == 0
