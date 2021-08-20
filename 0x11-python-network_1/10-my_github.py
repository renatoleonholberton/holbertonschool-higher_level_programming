#!/usr/bin/python3
"""This module makes a request to a URL"""
from sys import argv
import requests as req

if __name__ == '__main__':
    username, password = argv[1:]
    url = 'https://api.github.com/user'
    auth = req.auth.HTTPBasicAuth(username, password)
    res = req.get(url, auth=auth)
    dobj = res.json()
    print(dobj.get('id', None))
