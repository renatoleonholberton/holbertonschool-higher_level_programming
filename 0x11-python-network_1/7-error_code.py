#!/usr/bin/python3
"""This module makes a request to a URL"""
from sys import argv
import requests as req

if __name__ == '__main__':
    url = argv[1]
    res = req.get(url)
    text = res.text
    status = res.status_code
    if status >= 400:
        text = 'Error code: {}'.format(status)
    print(text)
