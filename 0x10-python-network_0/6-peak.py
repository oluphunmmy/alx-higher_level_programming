#!/usr/bin/python3
'''Module:
find a peak in a list of unsorted integers.
'''


def find_peak(list_of_integers):
    '''
    find a peak in a list of unsorted integers.

    args:
        list_of_integers (list): list of integers.
    returns:
        int: peak element.
    '''
    if not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return list_of_integers[start]
