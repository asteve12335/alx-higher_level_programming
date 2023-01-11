#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        new_matrix = []
        n = len(matrix)
        for i in range(n):
            sq = list(map(lambda x: x ** 2, matrix[i]))
            new_matrix.append(sq)
        return new_matrix
