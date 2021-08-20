#!/usr/bin/python3
"""This module makes a request to a URL"""
from sys import argv
import requests as req

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] if len(argv) > 1 else ""
    data = {'q': letter}

    try:
        res = req.post(url, data)
        dobj = res.json()
        text = 'No result'
        if dobj != {}:
            text = '[{}] {}'.format(dobj.get('id'), dobj.get('name'))
        print(text)
    except ValueError:
        print('Not a valid JSON')
