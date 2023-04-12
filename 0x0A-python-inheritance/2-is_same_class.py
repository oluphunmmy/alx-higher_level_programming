#!/usr/bin/python3

"""This module checks if an object is an instance of a given class"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) == a_class
