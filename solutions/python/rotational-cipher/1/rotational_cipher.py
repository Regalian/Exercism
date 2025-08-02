def rotate(text: str, key: int) -> str:
    """Rotate text by key

    Args:
        text (str): The text to be rotated.
        key (int): The number of positions to rotate the text.

    Returns:
        str: The rotated text.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[key:] + alphabet[:key]
    rotated_text = ''
    for char in text:
        if char in alphabet:
            rotated_text += rotated_alphabet[alphabet.index(char.lower())]
        elif char in alphabet.upper():
            rotated_text += rotated_alphabet[alphabet.upper().index(char)].upper()
        else:
            rotated_text += char
    return rotated_text
