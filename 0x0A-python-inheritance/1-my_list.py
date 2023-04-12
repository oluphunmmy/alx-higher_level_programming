#!/usr/bin/python3

"""
This module defines a class MyList that inherits from list
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        Public instance method that prints the sorted list,
        (ascending sort)
        """
        print(sorted(self))
