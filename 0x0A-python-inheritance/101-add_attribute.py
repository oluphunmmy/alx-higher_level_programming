#!/usr/bin/python3

"""
This module defines the function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(obj, attr, value):
    """
    it adds a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute to add.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not isinstance(obj, object):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
