#!/usr/bin/python3
"""This module fetches makes a request to a URL"""
import requests as req

if __name__ == '__main__':
    res = req.get('https://intranet.hbtn.io/status')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))
