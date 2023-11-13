#!/usr/bin/python3
"""rotate_2d_matrix template"""


def rotate_2d_matrix(matrix):
    # sourcery skip: use-itertools-product
    if not matrix:
        return None
    # ensure matrix is a square matrix
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")
    # ensure matrix contains only integers or floats
    for row in matrix:
        for col in row:
            if not isinstance(col, (int, float)):
                raise ValueError("matrix must contain only integers or floats")
    N = len(matrix)
    # transpose the matrix
    for row in range(N):
        for col in range(row, N):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]  # noqa: E501
    # reverse the matrix
    for row in range((N // 2)):
        for col in range(N):
            matrix[col][row], matrix[col][N - 1 - row] = matrix[col][N - 1 - row], matrix[col][row]  # noqa: E501
