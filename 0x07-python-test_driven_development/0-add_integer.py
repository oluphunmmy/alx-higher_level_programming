#!/usr/bin/python3
"""
This module is made up of  a function that adds two given numbers
"""

def add_integer(a, b=98):
    """ Function that adds two integers or floats a and b

    Returns:
        Returns the integer/float  addition of a and b

    Raises:
        TypeError: If either of a or b is a non-integer and non-float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (int(a) + int(b))
