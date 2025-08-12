import re
from collections import Counter


def count_words(sentence: str) -> Counter[str]:
    """Count the occurrences of each word in a sentence.

    Treats words as case-insensitive. Apostrophes within words are preserved
    for contractions (e.g., "don't"), but other punctuation separates words.
    Underscores are treated as word separators.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict[str, int]: A dictionary with words as keys and their counts as values.
    """

    # Extract words: alphanumeric characters, optionally followed by
    # apostrophe + more alphanumeric (handles contractions like "don't")
    words = re.findall(r"\w+(?:\'?\w+)?", sentence.lower().replace("_", " "))

    return Counter(words)
