#!/usr/bin/python3


def safe_print_integer(value):
    """Print AN integer with "{:d}".format().

    Args:
        value (int): The Integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Other than that - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
