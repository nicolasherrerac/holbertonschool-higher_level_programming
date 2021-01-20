#!/usr/bin/python3
"""Function"""
import json


def load_from_json_file(filename):
    """Create obj with JSON"""
    with open(filename, 'r', encoding="utf-8") as myfile:
        return json.load(myfile)
