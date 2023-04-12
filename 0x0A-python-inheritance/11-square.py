#!/usr/bin/python3
"""
This module defines a class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """
        Public instance method that validates value:
        * you can assume name is always a string
        * if value is not an integer: raise a TypeError exception, with
        the message <name> must be an integer
        * if value is less or equal to 0: raise a ValueError exception with
        the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Public instance method that returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Prints and returns the following rectangle description:
        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiate with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Prints and returns the following square description:
        [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
