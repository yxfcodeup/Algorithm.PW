# -*- coding: utf-8 -*-
import copy
import random

def selectionSort(ori_arr=list()) :
    """
    选择排序：
    时间复杂度：(n-1) + (n-2) + ... + 2 + 1 = n(n-1)/2 ~ n^2/2 --> O(n^2)
    :param ori_arr: 待排序数列
    :return: 排序好的结果数列
    """
    arr = list(copy.deepcopy(ori_arr))
    if 1 == len(arr) :
        return arr
    for i in range(len(arr)) :
        min_idx = i
        for j in range(i+1 , len(arr)) :
            if arr[min_idx] > arr[j] :
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]
    return arr

"""
希尔排序：
"""
def shellSort(ori_arr=list()) :
    arr = list(copy.deepcopy(ori_arr))
    if 1 == len(arr) :
        return arr
    arr_len = len(arr)
    gap = int(arr_len / 2)
    while gap > 0 :
        for i in range(gap , arr_len) :
            tmp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > tmp :
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = tmp
        gap = int(gap/2)
    return arr


if "__main__" == __name__ :
    ori_arr = [random.randint(0 , 100) for i in range(10)]
    ori_arr = [59 , 14, 35, 10,15, 41, 64, 22, 55, 40]
    # ori_arr = [10, 14, 15, 22, 35, 40, 41, 55, 59, 64]
    print("ori_arr: " , ori_arr)
    rst = selectionSort(ori_arr)
    # shell_rst = shellSort(ori_arr)
    print("sel_arr: " , rst)
