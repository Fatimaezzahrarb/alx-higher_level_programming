#!/usr/bin/python3
# 3-say_my_name.py
"""Defines A name printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): THE first name to print.
        last_name (str): THE last name to print.
    Raises:
        TypeError: If one or other of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
