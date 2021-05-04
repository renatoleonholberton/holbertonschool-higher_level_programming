#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = 0, 0
    len_tp_a, len_tp_b = len(tuple_a), len(tuple_b)

    if len_tp_a >= 1:
        a += tuple_a[0]
    if len_tp_b >= 1:
        a += tuple_b[0]

    if len_tp_a >= 2:
        b += tuple_a[1]
    if len_tp_b >= 2:
        b += tuple_b[1]

    return (a, b)
