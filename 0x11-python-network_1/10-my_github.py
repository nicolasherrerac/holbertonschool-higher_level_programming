#!/usr/bin/python3
"""My Github"""
import requests
from sys import argv


if __name__ == "__main__":
    """Credentials"""
    user = argv[1]
    passwd = argv[2]
    req = requests.get('https://api.github.com/user',
                       auth=(user, passwd)).json()
    try:
        print(req['id'])
    except:
        print("None")
