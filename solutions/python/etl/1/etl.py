from collections import defaultdict
def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """Transforms legacy data into a new format.

    Legacy data is a dictionary where keys are integers representing scores and values are lists of strings representing letters.
    New data is a dictionary where keys are strings representing letters and values are integers representing scores.

    Args:
        legacy_data (dict[int, list[str]]): The legacy data to be transformed.

    Returns:
        dict[str, int]: The transformed data.
    """
    result = defaultdict(int)
    for score, letters in legacy_data.items():
        for letter in letters:
            result[letter.lower()] = score
    return result
