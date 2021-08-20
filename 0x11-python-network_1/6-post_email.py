#!/usr/bin/python3
"""This module fetches makes a request to a URL"""
from sys import argv
import requests as req

if __name__ == '__main__':
    url, email = argv[1:]
    data = {'email': email}
    res = req.post(url, data=data)
    print(res.text)
