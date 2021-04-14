#!/usr/bin/python3
"""takes in a letter and sends a POST request"""
import requests
from sys import argv


if __name__ == "__main__":
    """API"""
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
