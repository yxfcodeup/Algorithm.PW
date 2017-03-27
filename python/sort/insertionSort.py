# -*- coding: utf-8 -*-

"""
 Name:
 Version:
 Author:
    Ployo Wiself
 Language: 
    Python 3.6.0
 Start time:
    2016-10-19 14:00
 Description:
    一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
        1. 从第一个元素开始，该元素可以认为已经被排序
        2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
        3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
        4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
        5. 将新元素插入到该位置后
        6. 重复步骤2~5
    如果比较操作的代价比交换操作大的话，可以采用二分查找法来减少比较操作的数目。该算法可以认为是插入排序的一个变种，称为二分查找插入排序。
 Input:
    a sequence of n numbers {a1 , a2 , a3 , ... , an}.
 Output:
    a permutation(reordering) {b1 , b2 , b3 , ... , bn} of the input sequence such that b1 <= b2 <= b3 <= ... <= bn.
"""

import os



def insertionSort(target) :
    _len = len(target)
    if 1 == _len :
        return target
    for i in range(1 , _len) :
        tmp = target[i]
        j = i - 1
        while j >= 0 and target[j]  > tmp :
            target[j+1] = target[j]
            j = j - 1
        target[j + 1] = tmp
    return target


def insertionSort2(target) :
    _len = len(target)
    if 1 == _len :
        return target
    for i in range(1 , _len) :
        for j in range(i , 0 , -1) :
            if target[j] < target[j-1] :
                target[j] , target[j - 1] = target[j - 1] , target[j]
    return target


if __name__ == "__main__" :
    a = [12,31,4134,1,3,524]
    print(a)
    b = insertionSort2(a)
    print(b)
