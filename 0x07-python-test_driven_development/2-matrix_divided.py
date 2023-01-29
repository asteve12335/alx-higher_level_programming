#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for i in range(len(matrix)):
        if matrix[i + 1] == matrix[-1]:
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
