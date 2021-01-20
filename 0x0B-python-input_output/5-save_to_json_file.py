#!/usr/bin/python3
"""Function"""
import json


def save_to_json_file(my_obj, filename):
    """Write object with JSON"""
    with open(filename, "w") as myfile:
        return myfile.write(json.dumps(my_obj))
