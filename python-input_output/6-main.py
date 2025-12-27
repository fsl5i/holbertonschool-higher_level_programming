#!/usr/bin/python3
"""
Test the load_from_json_file function.
"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Load a list
filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

# Load a dict
filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

# Test file does not exist
try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test invalid JSON
try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

