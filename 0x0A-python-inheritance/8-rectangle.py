#!/usr/bin/python3
"""
this module Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class of Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializing a new instance of Rectangle width and height
        """
        self.__width = self.integer_validator("width", width)

        self.__height = self.integer_validator("height", height)
