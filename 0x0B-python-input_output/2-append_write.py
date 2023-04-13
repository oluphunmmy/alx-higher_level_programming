#!/usr/bin/python3
"""
This modules appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """This function appends a string to the end of a text file (UTF-8)
    and returns the number of characters added"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
