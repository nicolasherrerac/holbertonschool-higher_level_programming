#!/usr/bin/python3
"""script that takes in a URL, sends a request to the
    URL and displays the value of the X-Request-Id
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    """Header"""
    direcc = argv[1]
    with urllib.request.urlopen(direcc) as response:
        print(response.headers.get('X-Request-Id'))
