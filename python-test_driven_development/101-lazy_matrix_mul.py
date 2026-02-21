#!/usr/bin/python3
"""Module that multiplies 2 matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using NumPy.

    Args:
        m_a (list of lists of int/float): first matrix
        m_b (list of lists of int/float): second matrix

    Returns:
        list: result of multiplication as a NumPy array

    Raises:
        TypeError: if m_a or m_b are not lists of lists
        ValueError: if matrices cannot be multiplied due to shape
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0 or len(m_a[0]) == 0 or len(m_b[0]) == 0:
        raise ValueError("matrices can't be empty")

    try:
        return np.matmul(np.array(m_a), np.array(m_b))
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
