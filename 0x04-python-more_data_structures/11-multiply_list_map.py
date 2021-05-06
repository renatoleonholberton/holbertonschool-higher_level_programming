#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    fn_mult = mult_by_num(number)
    return list(map(fn_mult, my_list))


def mult_by_num(num):
    return lambda val: val * num
