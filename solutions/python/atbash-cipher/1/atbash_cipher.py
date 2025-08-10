ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ATBASH_MAP = {a: b for a, b in zip(ALPHABET, ALPHABET[::-1])}


def _apply_atbash_transform(chars: str) -> str:
    """Process characters in a string using the Atbash cipher.

    Args:
        chars (str): The string to be processed.

    Returns:
        str: The processed string.
    """
    processed_chars: list[str] = []
    for char in chars.lower():
        if char.isalpha():
            processed_chars.append(ATBASH_MAP[char])
        elif char.isdigit():
            processed_chars.append(char)
    return "".join(processed_chars)


def encode(plain_text: str) -> str:
    """Encode a plain text using the Atbash cipher.

    The Atbash cipher is a substitution cipher with a specific key where the letters of the alphabet are reversed.
    Output is grouped into 5-character blocks separated by spaces.

    Args:
        plain_text (str): The plain text to be encoded.

    Returns:
        str: The encoded text.
    """
    processed = decode(plain_text)
    return " ".join(processed[i : i + 5] for i in range(0, len(processed), 5))


def decode(ciphered_text: str) -> str:
    """Decode a ciphered text using the Atbash cipher.

    The Atbash cipher is a substitution cipher with a specific key where the letters of the alphabet are reversed.

    Args:
        ciphered_text (str): The ciphered text to be decoded.

    Returns:
        str: The decoded text.
    """
    processed = _apply_atbash_transform(ciphered_text)
    return "".join(processed)
