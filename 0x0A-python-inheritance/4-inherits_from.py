#!/usr/bin/python3

"""
This module defines the inherited class-checking function
"""


def inherits_from(obj, a_class):

    """returns true if obj is a subclass of a_class, otherwise false"""
    if (issubclass(type(obj), a_class) and type(obj) != a_class)
    return True
return False
