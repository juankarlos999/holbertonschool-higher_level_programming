#!/usr/bin/python3
"""Load, add, save to a Python list"""


import sys
from os import path
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


"""script that adds all arguments to a Python list,
and then save them to a file
"""
if path.isfile('add_item.json'):
    args = load_from_json_file('add_item.json')
else:
    args = []
for i in range(1, len(sys.argv)):
    args.append(sys.argv[i])
save_to_json_file(args, 'add_item.json')
