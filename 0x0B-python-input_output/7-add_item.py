#!/usr/bin/python3
"""Function"""
import sys
import os.path as path

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

lista = []
arg = sys.argv[1:]

if path.exists("add_item.json"):
    lista = load('add_item.json')
save(lista + arg, 'add_item.json')
