#!/usr/bin/python3
"""Module that contains matrix_mul function"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""

    # 1️⃣ Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2️⃣ Check if they are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3️⃣ Check if empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4️⃣ Check elements are int or float
    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # 5️⃣ Check rectangle shape
    row_length_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_length_a:
            raise TypeError("each row of m_a must be of the same size")

    row_length_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_length_b:
            raise TypeError("each row of m_b must be of the same size")

    # 6️⃣ Check if matrices can be multiplied
    if row_length_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # 7️⃣ Matrix multiplication
    result = []

    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            sum_result = 0
            for k in range(len(m_b)):
                sum_result += m_a[i][k] * m_b[k][j]
            new_row.append(sum_result)
        result.append(new_row)

    return result
