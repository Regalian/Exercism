def egg_count(display_value: int)->int:
    """Count the number of eggs in a display value.

    Args:
        display_value (int): Deicmal number where each bit set represents an egg laid

    Returns:
        int: The number of eggs (bits set) in the display value.
    """
    count = 0
    while display_value > 0:
        count +=  1 if display_value % 2 else 0
        display_value //= 2
    return count
