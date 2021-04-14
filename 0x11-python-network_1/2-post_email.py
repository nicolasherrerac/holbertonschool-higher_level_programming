#!/usr/bin/python3
"""POST email"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    """URL and email send POST"""
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
