def find(search_list: list[int], value: int) -> int:
    """Find the index of the given value in the sorted list.

    Args:
        search_list: A sorted list of integers.
        value: The value to search for.

    Returns:
        The index of the value in the list.

    Raises:
        ValueError: If the value is not found in the list.
    """
    start = 0
    end = len(search_list) - 1
    while end >= start:
        mid = (start + end) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    # example when value is not found in the array.
    raise ValueError("value not in array")
