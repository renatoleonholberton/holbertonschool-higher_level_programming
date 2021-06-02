#!/usr/bin/python3
"""Module that adds args passed to the program
into a list abd then rewrites the list into the file as JSON"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    ls = load_from_json_file(filename)
except:
    ls = []

ls += [arg for arg in argv[1:]]
save_to_json_file(ls, filename)
