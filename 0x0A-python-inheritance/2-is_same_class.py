#!/usr/bin/python3
"""Define A class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object IS exactly an instance of an given class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Other than that - False.
    """
    if type(obj) == a_class:
        return True
    return False
