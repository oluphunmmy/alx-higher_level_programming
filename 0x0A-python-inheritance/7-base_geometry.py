#!/usr/bin/python3
"""
Module that defines a class BaseGeometry
"""


class BaseGeometry:
    """
    A class BaseGeometry that is an empty class
    """

    def area(self):
        """
        Public instance method that raises an Exception with
        the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name: The str of the parameter.
            value: The int parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
