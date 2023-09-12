#!/usr/bin/python3
import doctest


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: first int.
        b: second int, default value is 98.

    Raises:
          TypeError: if a, b are neither int nor float.

    Returns:
           int: sum of a and b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, float) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)
        
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
