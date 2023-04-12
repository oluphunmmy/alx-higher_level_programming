#!/usr/bin/python3

"""
this module contains a classBasegeometry and a subclass Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square."""

    def __init__(self, size):
        """Initialization of  a new square.
        Args:
            size: The size int of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
