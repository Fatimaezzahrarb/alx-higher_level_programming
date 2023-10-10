#!/usr/bin/python3
"""Define A JSON file reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from A JSON file."""
    with open(filename) as f:
        return json.load(f)
