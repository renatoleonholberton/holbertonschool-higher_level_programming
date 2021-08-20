#!/usr/bin/python3
"""This module fetches makes a request to a URL"""
from sys import argv
import requests as req

if __name__ == '__main__':
    url = argv[1]
    res = req.get(url)
    print(res.headers.get('X-Request-Id'))
