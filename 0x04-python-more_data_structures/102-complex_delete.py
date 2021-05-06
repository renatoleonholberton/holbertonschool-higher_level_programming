#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary

    keys = list(a_dictionary.keys())
    for key in keys:
        if key in a_dictionary and a_dictionary[key] == value:
            del a_dictionary[key]

    return a_dictionary
