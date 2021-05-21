#!/usr/bin/python3
"""This module contains add_integer function"""


def matrix_divided(matrix, div):
    """matrix_divided: divides all elemetns of matrix by 'div'

    Args:
        matrix (list): First number
        div (int|float): Number by wich divide the matrix elements
    """
    result_matrix = []

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    prev_len = -1
    row_ind = 0
    for row in matrix:
        result_matrix.append([])
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        row_len = len(row)
        if prev_len != -1 and prev_len != row_len:
            raise TypeError('Each row of the matrix must have the same size')
        prev_len = row_len

        for el in row:
            if type(el) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            
            result_matrix[row_ind].append(round(el / div, 2))
        row_ind += 1

    return result_matrix
