#!/usr/bin/python3
"""
module containining the class "Student"
"""


class Student:
    """Representation of a class student"""
    def __init__(self, first_name, last_name, age):

        """Initializing  the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This returns a dictionary representation of a Student instance"""
        return self.__dict__
