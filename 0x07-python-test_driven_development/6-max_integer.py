#!/usr/bin/python3
"""Module to find THE max integer in a list
"""


def max_integer(list=[]):
    """Function TO find and return THE max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result