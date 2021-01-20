#!/usr/bin/python3
"""Function"""
import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

try:
    lista = load('add_item.json')
except:
    lista = []

lista.extend(sys.argv[1:])
save(lista, 'add_item.json')
