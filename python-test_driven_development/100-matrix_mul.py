#!/usr/bin/python3
"""
Module that defines matrix_mul function
with full validation and exact error messages
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices with full validation"""

    # 1. m_a and m_b must be list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. m_a and m_b must be list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. m_a and m_b can't be empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. all elements must be int or float
    for row in m_a:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")

    # 5. all rows same size
    row_len_a = len(m_a[0])
    if any(len(row) != row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    if any(len(row) != row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. matrices must be multipliable
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            s = 0
            for k in range(len(m_b)):
                s += m_a[i][k] * m_b[k][j]
            row_result.append(s)
        result.append(row_result)
    return result
