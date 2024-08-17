# -*- coding: utf-8 -*-
import random


def bubbleSort(arr):
    """
    冒泡排序-无特殊优化，直接对比并交换位置
    时间复杂度：
    - 最快：n*(n-1)/2次比较和0次交换
    - 最慢：n*(n-1)/2次比较和3*n*(n-1)/2次交换
    :param arr: 待排序数列
    :return: 无
    """
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubbleSort2(arr):
    """
    优化的冒泡排序-加入了is_swapped，目的是将算法的最佳时间复杂度优化为O(n)，即当原输入序列就是排序好的情况下，该算法的时间复杂度就是O(n)
    时间复杂度：
    - 最快：n-1次比较和0次交换
    - 最慢：n*(n-1)/2次比较和3*n*(n-1)/2次交换
    :param arr: 待排序数列
    :return: 无
    """
    arr_len = len(arr)
    for i in range(arr_len):
        is_swapped = False
        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True
        if not is_swapped:
            print("[INFO] original arr is sorted")
            break
        print(f"[INFO] sort from index[0] to index[{arr_len-i-1}], result is {arr}")


if "__main__" == __name__:
    ori_arr = [random.randint(0, 100) for i in range(10)]
    ori_arr = [59 , 14, 35, 10,15, 41, 64, 22, 55, 40]
    ori_arr = [10, 14, 15, 22, 35, 40, 41, 55, 59, 64]
    print("ori_arr: ", ori_arr)
    bubbleSort2(ori_arr)
    print("rst_arr: ", ori_arr)
