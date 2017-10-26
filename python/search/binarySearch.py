# -*- coding: utf-8 -*-

"""
 Name:
 Version:
 Author:
    Ployo Wiself
 Language: 
    Python 3.6.0
 Start time:
    2017-10-10 11:00
 Description:
 Input:
    a sequence of n numbers {a1 , a2 , a3 , ... , an}.
 Output:
    a permutation(reordering) {b1 , b2 , b3 , ... , bn} of the input sequence such that b1 <= b2 <= b3 <= ... <= bn.
"""

import os
import sys


def binarySearch(target , box=list()) :
    _len = len(box)
    low = 0
    high = _len - 1
    while low <= high :
        mid = int(low + (high - low) / 2)
        if box[mid] < target :
            low = mid + 1
        elif box[mid] > target :
            high = mid - 1
        else :
            return mid
    return low


def binarySearchRecursion(target , low , high , box=list()) :
    if low > high :
        return low
    mid = int(low + (high - low) / 2)
    if box[mid] > target :
        return binarySearchRecursion(target , low , mid - 1 , box)
    elif box[mid] < target :
        return binarySearchRecursion(target , mid + 1 , high , box)
    else :
        return mid


if "__main__" == __name__ :
    box = [1,2,3,4,5,7,9,12,15,19,21,33,89]
    r1 = binarySearch(89 , box)
    r2 = binarySearchRecursion(89 , 0 , len(box) - 1 , box)
    print(r1 , r2)
