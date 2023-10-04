#!/usr/bin/python3
"""Defines the lock class."""


class LockedClass:
    """
    Prevent  user from instantiating new LockedClass attributes
    for anything BUT attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
