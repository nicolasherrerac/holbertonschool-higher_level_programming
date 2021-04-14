#!/usr/bin/python3
"""ERROR code"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    """Display error"""
    data = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(data) as reponse:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
