#!/usr/bin/python3
"""
this module defines a name-printing function
"""


def say_my_name(first_name, last_name=""):
    """Print a name.
    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    Returns:
        No return

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
