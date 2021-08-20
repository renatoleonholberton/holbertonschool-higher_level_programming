#!/usr/bin/python3
"""This module fetches makes a request to a URL"""
from sys import argv
from urllib import request
from urllib import error

if __name__ == '__main__':
    url = argv[1]
    try:
        with request.urlopen(url) as res:
            _bytes = res.read()
            print(_bytes.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
