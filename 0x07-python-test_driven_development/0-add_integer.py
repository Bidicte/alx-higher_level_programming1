#!/usr/bin/python3
def add_integer(a, b=98):
    """ A function that adds 2 integers

    Args:
        a: must be an integer
        b: must be an integer
    Raises:
         TypeError if a or b is not an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
