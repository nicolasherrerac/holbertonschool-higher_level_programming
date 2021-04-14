#!/usr/bin/python3
"""HEADER"""
import requests
from sys import argv

if __name__ == "__main__":
    """Header value"""
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
