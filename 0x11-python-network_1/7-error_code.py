#!/usr/bin/python3
"""Error code"""
import requests
from sys import argv

if __name__ == '__main__':
    dirrec = argv[1]
    req = requests.get(dirrec)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
