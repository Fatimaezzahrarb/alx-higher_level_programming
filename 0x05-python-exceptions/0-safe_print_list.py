#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x Elememts of a list.

    Args:
        my_list (list): The list TO print elements from.
        x (int): The number of the elements of my_list to print.

    Returns:
        The number of the elements are printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
