#!/usr/bin/python3
"""This module fetches makes a request to a URL"""


from urllib import request as rq

if __name__ == '__main__':
    with rq.urlopen('https://intranet.hbtn.io/status') as res:
        _bytes = res.read()
        print('\t- type: {}'.format(type(_bytes)))
        print('\t- content: {}'.format(_bytes))
        print('\t- utf8 content: {}'.format(_bytes.decode('utf-8')))
