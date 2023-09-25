#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x Elements of the lists that are integers.

    Args:
        my_list (list): The list to print Elements from.
        x (int): The_number of elements of my_list to print.

    Returns:
        The number OF elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)

