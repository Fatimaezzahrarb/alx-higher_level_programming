#!/usr/bin/python3
"""script to find peak in the list of ints, interview prep
"""

"""
    THOUGHT PROCESS
        it's not sorted, so sorting would take n(log(n))
            -> not worth the sorting
        looping through and keep tracking of max (brute force)
            -> O(n)

        possibly by looping from each end reducing to 1/2 run time
            -> still O(n)
"""


def find_peak(list_of_integers):
    """BRUTE force implement for question
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
