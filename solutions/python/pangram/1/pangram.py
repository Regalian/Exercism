
def is_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram.

    Args:
        sentence (str): The sentence to check.
    Returns True if the sentence contains every letter of the alphabet at least once, False otherwise.
    """

    present = {char: False for char in 'abcdefghijklmnopqrstuvwxyz'}
    for char in sentence.lower():
        if char.isalpha():
            present[char.lower()] = True
    return all(present.values())
