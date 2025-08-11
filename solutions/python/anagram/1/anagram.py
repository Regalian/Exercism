from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Find anagrams of a word from a list of candidates.

    An anagram is formed by rearranging letters of the original word using
    all letters exactly once. Comparison is case-insensitive but original
    case is preserved in results.

    Args:
        word (str): The word to find anagrams for.
        candidates (list[str]): The list of candidate words to search for anagrams.

    Returns:
        list[str]: A list of anagrams found in the candidates.
    """
    if not word or not candidates:
        return []

    word = word.lower()
    word_counter = Counter(word)

    def _is_anagram(candidate: str) -> bool:
        candidate_lower = candidate.lower()
        return (
            len(word) == len(candidate_lower)
            and word != candidate_lower
            and Counter(candidate_lower) == word_counter
        )

    return [candidate for candidate in candidates if _is_anagram(candidate)]
