#!/usr/bin/python3
# 101-locked_class.py

"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from dynamically creating new instance attributes
    but attributes new instance called  'first_name'.
    """

    __slots__ = "first_name"
