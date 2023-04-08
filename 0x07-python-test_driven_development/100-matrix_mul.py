#!/usr/bin/python3
"""

This is a module comprising of  a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: first matrix
        m_b: second matrix


    Raises:
        TypeError: if m_a or m_b are not  a list
        TypeError: if m_a or m_b are not a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b does not have integers or floats
        TypeError: if the rows of m_a or m_b are not of the same size
        ValueError: if m_a and m_b cannot be multiplied
    
    Returns:
        the multiplication result

    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elems in m_a:
        if not isinstance(elems, list):
            raise TypeError("m_a must be a list of lists")

    for elems in m_b:
        if not isinstance(elems, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    length = 0

    for elems in m_a:
        if length != 0 and length != len(elems):
            raise TypeError("each row of m_a must be of the same size")
        length = len(elems)

    length = 0

    for elems in m_b:
        if length != 0 and length != len(elems):
            raise TypeError("each row of m_b must be of the same size")
        length = len(elems)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    x1 = []
    y1 = 0

    for a in m_a:
        x2 = []
        y2 = 0
        number = 0
        while (y2 < len(m_b[0])):
            number += a[y1] * m_b[y1][y2]
            if y1 == len(m_b) - 1:
                y1 = 0
                y2 += 1
                x2.append(num)
                number = 0
            else:
                y1 += 1
        x1.append(x2)

    return x1
