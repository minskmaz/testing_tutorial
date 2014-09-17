#!/usr/bin/env python
from __future__ import division

def average(list):
    '''Return average of a list of numbers.

    >>> average([1,2,3,4,5])
    3.0
    '''

    if not list:
        return None
    retval = 0
    for i in list:
        retval += i
    retval /= len(list)

    return retval
