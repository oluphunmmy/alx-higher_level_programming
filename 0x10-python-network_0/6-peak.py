#!usr/bin/python3
"""
Technical interview preparation
"""


def find_peak(list_of_integers):
    """
    a function that finds a peak in a list of unsorted integers.
    """
    if len(list_of_integers) == 0:
        return None

    L = list_of_integers
    beg = 0
    end = len(L) - 1

    if L[beg] > L[beg + 1]:
        return L[beg]
    if L[end] > L[end - 1]:
        return L[end]

    mid = (beg + end) // 2
    if L[mid-1] < L[mid] and L[mid+1] < L[mid]:
        return L[mid]
    if L[mid] < L[mid + 1]:
        return find_peak(L[mid:end+1])
    elif L[mid] < L[mid - 1]:
        return find_peak(L[beg:mid+1])
    else:
        if beg == end:
            return L[end]
        return L[beg]
