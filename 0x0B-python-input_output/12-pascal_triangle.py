#!/usr/bin/python3
"""This module defines a function that returns a list of
lists of integers representing Pascal's triangle for a
given number of rows"""


def pascal_triangle(n):
    """Function representing Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle"""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
