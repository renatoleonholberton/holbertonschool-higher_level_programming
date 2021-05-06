#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_pond = 0
    total_weight = 0
    for (score, weight) in my_list:
        total_pond += score * weight
        total_weight += weight

    return total_pond / total_weight
