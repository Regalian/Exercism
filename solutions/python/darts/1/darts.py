import math

def radius(x:int | float, y:int | float) -> float:
    """Calculate the radius of a point from the origin.

    Args:
        x (int | float): The x-coordinate of the point.
        y (int | float): The y-coordinate of the point.

    Returns:
        float: The radius of the point from the origin.
    """
    return math.sqrt(x**2 + y**2)

def score(x: int | float, y: int | float) ->  int:
    """Calculate the score of a dart throw.

    Args:
        x (int | float): The x-coordinate of the point.
        y (int | float): The y-coordinate of the point.

    Returns:
        int: The score of the dart throw.
    """


    r: float  = radius(x, y)
    if r <=1:
        return 10
    if r <=5:
        return 5
    if r <=10:
        return 1
    return 0
