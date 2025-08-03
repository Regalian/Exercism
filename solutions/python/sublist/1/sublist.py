"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one:list, list_two:list)->int:
    """Return the relationship between two lists.

    Args:
        list_one (list): The first list.
        list_two (list): The second list.

    Returns:
        int: The relationship between the two lists.
    """

    def equal(list_one:list, list_two:list)->bool:
        return len(list_one) == len(list_two) and all(a == b for a, b in zip(list_one, list_two))

    if equal(list_one, list_two):
        return EQUAL

    len_one = len(list_one)
    len_two = len(list_two)
    if len_one < len_two:
        if len_one == 0:
            return SUBLIST
        start = 0
        while len_one + start <= len_two:
            try:
                start = list_two.index(list_one[0], start)
                if equal(list_one, list_two[start:start+len_one]):
                    return SUBLIST
                start += 1
            except ValueError:
                return UNEQUAL
    if len_two < len_one:
        if len_two == 0:
            return SUPERLIST
        start = 0
        while len_two + start <= len_one:
            try:
                start = list_one.index(list_two[0], start)
                if equal(list_one[start:start+len_two], list_two):
                    return SUPERLIST
                start += 1
            except ValueError:
                return UNEQUAL
    return UNEQUAL
