#!/usr/bin/python3

""" 
A class representing a class basegeometry.
"""


class BaseGeometry:
    """
    A class with public atrribute area.
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message
        area() is not implemented.
        """
        raise Exception("area() is not implemented")
