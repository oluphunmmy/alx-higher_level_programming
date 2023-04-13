#!/usr/bin/python3
"""
This module writess a string to a file.
"""


def write_file(filename="", text=""):
    """This function writes a string to a text file (UTF-8)
    and returns the number of characters written."""
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
