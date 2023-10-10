#!/usr/bin/python3
"""Define A Python class TO JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
