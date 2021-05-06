#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(calc_row, matrix))


def square(n):
    return n**2


def calc_row(row):
    return list(map(square, row))
