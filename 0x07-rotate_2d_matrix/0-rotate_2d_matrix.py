#!/usr/bin/python3
"""0-rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix"""
    n = len(matrix)

    # Transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
