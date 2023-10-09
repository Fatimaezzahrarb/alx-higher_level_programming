#!/usr/bin/python3
"""Defines AN inherite list class MyList."""


class MyList(list):
    """Implements sorted printing for THE built-in list class."""

    def print_sorted(self):
        """Print an list in sorted ascending order."""
        print(sorted(self))
