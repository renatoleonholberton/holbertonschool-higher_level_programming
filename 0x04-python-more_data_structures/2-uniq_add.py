#!/usr/bin/python3
def uniq_add(my_list=[]):
    usum = 0
    uniques = set(my_list)
    for val in uniques:
        usum += val

    return usum
