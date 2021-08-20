#!/usr/bin/python3
"""This module fetches makes a request to a URL"""
from sys import argv
from urllib import request as req

if __name__ == '__main__':
    url = argv[1]
    with req.urlopen(url) as res:
        print(res.headers.get('X-Request-Id'))
