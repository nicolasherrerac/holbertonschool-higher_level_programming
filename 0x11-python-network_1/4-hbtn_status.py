#!/usr/bin/python3
"""My Status Request"""
import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    data = r.text
    print("Body response:")
    print("\t - type: {}".format(type(data)))
    print("\t - content: {}".format(data))
