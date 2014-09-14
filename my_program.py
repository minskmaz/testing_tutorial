#!/usr/bin/env python

def average(list):

    retval = 0
    for i in list:
        retval += i
    retval /= len(list)

    return retval
