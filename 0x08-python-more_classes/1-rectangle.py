#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """initialises the rectangle"""
        self.width = width
        self.height =height

        @property
        def width(self):
            """getter for the private instance attribute width"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets width attribute"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """retrieves  height attribute"""
                return self.__height

            @height.setter
            def height(self, value):
                """sets height attribute"""
                if type(value) is not int:
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
