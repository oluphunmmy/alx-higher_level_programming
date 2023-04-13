#!/usr/bin/python3
"""This module defines a student class"""


class Student:
    """This is Representing a student"""

    def __init__(self, first_name, last_name, age):

        """Initializing a new Student instance
        with the given name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """Returning a dictionary representation
        of the Student instance"""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr
                in attrs if hasattr(self, attr)}
