#!/usr/bin/python3
"""Define A function that adds attributes to the objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to AN object if possible.

    Args:
        obj (any): object to add an attribute to.
        att (str): name of the attribute to add to obj.
        value (any): value of att.
    Raises:
        TypeError: If the attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
