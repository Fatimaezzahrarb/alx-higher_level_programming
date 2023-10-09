#!/usr/bin/python3
"""Defines an object that attribute lookup function."""


def lookup(obj):
    """Return a list OF an objects available attributes."""
    return (dir(obj))
