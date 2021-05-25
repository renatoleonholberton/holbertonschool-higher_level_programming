#!/usr/bin/python3
def magic_string():
    magic_string.c = magic_string.c+1 if magic_string.__dict__.get('c') else 1
    return ('Holberton, ' * magic_string.c)[:-2]
