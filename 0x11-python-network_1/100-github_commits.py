#!/usr/bin/python3
"""This module makes a request to a URL"""
from sys import argv
import requests as req

if __name__ == '__main__':
    repo, owner = argv[1:]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    res = req.get(url)
    objlist = res.json()

    for obj in objlist[:10]:
        sha = obj.get('sha')
        commit = obj.get('commit')
        author = commit and commit.get('author')
        name = author and author.get('name')
        print('{}: {}'.format(sha, name))
