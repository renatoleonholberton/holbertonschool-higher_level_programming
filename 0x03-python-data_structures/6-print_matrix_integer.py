#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        space = False
        for num in row:
            if space:
                print(end=" ")
            print("{:d}".format(num), end="")
            space = True
        print()
