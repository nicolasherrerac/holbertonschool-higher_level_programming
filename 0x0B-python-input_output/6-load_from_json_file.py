#!/usr/bin/python3
"""Function"""
import json


def load_from_json_file(filename):
    """Create obj with JSON"""
    with open(filename, 'r') as myfile:
        return json.load(myfile)
