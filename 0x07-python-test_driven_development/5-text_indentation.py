#!/usr/bin/python3

"""
This module contains  a function that prints 2 new lines after ".,?:" characters
"""


def text_indentation(text):
    
    """ Function that prints 2 new lines after ".?:" characters
    Args:
        text (string): input string to print

    Raises:
        TypeError: If text is not a string

    Return:
        No return

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    y = text[:]

    for d in ".?:":
        list_text = y.split(d)
        y = ""
        for i in list_text:
            i = i.strip(" ")
            y = i + d if y == "" else y + "\n\n" + i + d

    print(y[:-3], end="")
