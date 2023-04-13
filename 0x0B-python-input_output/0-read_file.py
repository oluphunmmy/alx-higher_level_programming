#!/usr/bin/python3

"""
This module defines a text file.
"""


def read_file(filename=""):
    """This function reads a text file (UTF-8) and
    prints its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
