#!/usr/bin/python3
"""This module fetches makes a request to a URL"""
from sys import argv
from urllib import parse
from urllib import request

if __name__ == '__main__':
    url, email = argv[1:]
    data = {'email': email}

    data = parse.urlencode(data)
    data = data.encode('ascii')
    req = request.Request(url, data)

    with request.urlopen(req) as res:
        _bytes = res.read()
        print(_bytes.decode('utf-8'))
