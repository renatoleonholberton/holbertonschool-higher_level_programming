#!/usr/bin/python3
"""This module contains text_indentation function"""


def text_indentation(text):
    """text_indentation: Prints 2 new lines after each of
                         these chars: '.', '?', ':'

    Args:
        size (str): Text to be printed
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    p_str = ''
    for i in range(len(text)):
        p_str += text[i]
        if text[i] in ['.', '?', ':']:
            print(p_str.strip(), end="")
            print("\n")
            p_str = ''
    # empty buffer last chars
    if p_str:
        print(p_str.strip(), end="")
