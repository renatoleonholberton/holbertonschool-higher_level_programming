#!/usr/bin/python3
""" This module defines a funtion to find a peek element in n array """


def find_peak(list_of_integers):
    """ Finds 'a peek' of a given array of integers """
    arr = list_of_integers
    if not arr:
        return None

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return arr[left]
