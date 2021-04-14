#!/usr/bin/python3
"""POST email"""
import requests
from sys import argv

if __name__ == '__main__':
    values = {'email': argv[2]}
    r = requests.post(argv[1], values)
    print(r.text)
