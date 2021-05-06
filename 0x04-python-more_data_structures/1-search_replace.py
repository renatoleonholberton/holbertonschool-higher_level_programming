#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for val in my_list:
        new_val = replace if val == search else val
        new_list.append(new_val)

    return new_list
