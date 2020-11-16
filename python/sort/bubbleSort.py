import os
import sys
import copy
import random
import datetime


def bubbleSort(arr):
    """
    冒泡排序：
    时间复杂度：
        最快：n*(n-1)/2次比较和0次交换
        最慢：n*(n-1)/2次比较和3*n*(n-1)/2次交换
    """
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubbleSort2(arr):
    """
    优化的冒泡排序：
    时间复杂度：
        最快：n-1次比较和0次交换
        最慢：n*(n-1)/2次比较和3*n*(n-1)/2次交换
    """
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


if "__main__" == __name__:
    ori_arr = [random.randint(0, 100) for i in range(10)]
    print("ori_arr: ", ori_arr)
    bubbleSort2(ori_arr)
    print("rst_arr: ", ori_arr)
