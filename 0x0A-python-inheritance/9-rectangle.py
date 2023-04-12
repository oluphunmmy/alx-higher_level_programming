#!/usr/bin/python3

"""
This module defines a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialization of a new Rectangle.
        Args:
            width: The width int of the new Rectangle.
            height: The height int of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """this returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """this returns the print() and str() representating the  Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
