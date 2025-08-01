from typing import List

def equilateral(sides: List[int | float]) -> bool:
    """Check if the given sides form an equilateral triangle.

    All sides are equal.

    param:sides: List[int | float] - The sides of the triangle.
    return: bool - True if the triangle is equilateral, False otherwise.
    """

    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: List[int | float]) -> bool:
    """Check if the given sides form an isosceles triangle.

    Two sides are equal.

    param:sides: List[int | float] - The sides of the triangle.
    return: bool - True if the triangle is isosceles, False otherwise.
    """

    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides: List[int | float]) -> bool:
    """Check if the given sides form a scalene triangle.

    All sides are different.

    param:sides: List[int | float] - The sides of the triangle.
    return: bool - True if the triangle is scalene, False otherwise.
    """

    return is_triangle(sides) and len(set(sides)) == 3

def is_triangle(sides: List[int | float]) -> bool:
    """Check if the given sides form a triangle.

    There must be exactly 3 sides and the triangle equality must hold.

    param:sides: List[int | float] - The sides of the triangle.
    return: bool - True if the triangle is valid, False otherwise.
    """

    return len(sides) == 3 and all(sides[i] + sides[(i + 1) % 3] > sides[(i + 2) % 3] for i in range(3))
