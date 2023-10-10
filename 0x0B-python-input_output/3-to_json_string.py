#!/usr/bin/python3
"""Define A string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an string object."""
    return json.dumps(my_obj)
