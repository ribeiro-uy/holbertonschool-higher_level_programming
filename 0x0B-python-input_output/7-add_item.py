#!/usr/bin/python3
"""
Project: 0x0B. Python - Input/Output
Task: 7
Script that adds all arguments to a Python list, and then save them to a file
"""
import json
create_json = __import__('6-load_from_json_file').load_from_json_file
save_json = __import__('5-save_to_json_file').save_to_json_file
from sys import argv


try:
    new_list = create_json("add_item.json")
except FileNotFoundError:
    new_list = []
for item in range(1, len(argv)):
    new_list.append(argv[item])
save_json(new_list, "add_item.json")
