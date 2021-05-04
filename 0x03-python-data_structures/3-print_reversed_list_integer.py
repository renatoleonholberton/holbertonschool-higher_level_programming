#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return

    last_idx = len(my_list) - 1
    rang = range(last_idx, -1, -1)
    for i in rang:
        print("{:d}".format(my_list[i]))
