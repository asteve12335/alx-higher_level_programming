#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all the elements of a matrix

    Args:
    matrix: A list of lists of ints or floats
    div: The divisor, an int or a float

    Raises:
    TypeError => rows of different sizes
    TypeError => matrix contains non-numbers
    TypeError => div is not an int or a float
    ZeroDivisionError => div equals 0

    Returns:
    A new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")

    for i in range(len(matrix)):
        if matrix[i] == matrix[-1]:
            break
        if len(matrix[i + 1]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            quotient = round(i / div, 2)
            new_row.append(quotient)
        new_matrix.append(new_row)
    return (new_matrix)
