#!/usr/bin/env python

def average(list):
    '''Return average of a list of numbers.

    >>> average([1,2,3,4,5])
    3.0
    '''

    retval = 0
    for i in list:
        retval += i
    retval /= len(list)

    return retval
