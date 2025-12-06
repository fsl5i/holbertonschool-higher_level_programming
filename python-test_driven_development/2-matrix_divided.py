#!/usr/bin/python3
"""
This module provides the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): matrix of integers/floats.
        div (int/float): number to divide by.

    Raises:
        TypeError: if matrix is not a list of lists of numbers.
        TypeError: if each row is not the same size.
        TypeError: if div is not a number.
        ZeroDivisionError: if div is 0.

    Returns:
        list: new matrix with values divided by div, rounded to 2 decimals.
    """

    # Validate matrix structure
    if not isinstance(matrix, list) or not matrix or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate matrix elements
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all rows have same length
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new divided matrix
    return [[round(x / div, 2) for x in row] for row in matrix]
