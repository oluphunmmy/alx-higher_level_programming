#!/usr/bin/python3

"""
Module that contains a  function that multiplies two matrices.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices using the module NumPy.
    Args:
        m_a : The first list of list matrix.
        m_b : The second list of list matrix.

    Return:
        the multiplication of two matrices
    """

    return (np.matmul(m_a, m_b))
