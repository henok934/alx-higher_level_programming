#!/usr/bin/python3
"""returns json representation of an object(string)"""
from json import dumps as d


def to_json_string(my_obj):
    """returns the json representation of an object"""
    return d(my_obj)

