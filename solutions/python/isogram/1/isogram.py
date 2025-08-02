from collections import Counter

def is_isogram(string: str)->bool:
    """Check if a string is an isogram.

    An isogram is a word or phrase without a repeating letter,
    ignoring case and spaces.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is an isogram, False otherwise.
    """
    counts = Counter(string.lower().replace(' ', '').replace('-', ''))
    return all(count == 1 for count in counts.values())
