#!/usr/bin/python3
"""Module for function that calculates 'n' pascal triangle"""


def pascal_triangle(n):
    """Calulate the 'n' Pascal's pyramid"""
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    pascal = [[1]]
    for row in range(1, n):
        # Append new row
        pascal.append([1, 1])
        #  Calc sum in the middle
        for col in range(1, row):
            prev_row = pascal[row - 1]
            pas_num = prev_row[col] + prev_row[col - 1]
            pascal[row].insert(col, pas_num)
    return pascal
