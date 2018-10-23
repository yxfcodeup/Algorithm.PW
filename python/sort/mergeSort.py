import os
import sys
import copy
import random

"""
原地归并
"""
def merge(arr , low , mid , high) :
    n1 = mid - low + 1
    n2 = high - mid
    left = [0] * n1         # 左半辅助数组
    right = [0] * n2        # 右半辅助数组

    for m in range(0 , n1) :
        left[m] = arr[low + m]
    for n in range(0 , n2) :
        right[n] = arr[mid + n + 1]

    i = 0       # index of first subarray
    j = 0       # index of second subarray
    k = low     # index of merged subarray
    # 合并两个数组
    while i < n1 and j < n2 :
        if left[i] <= right[j] :
            arr[k] = left[i]
            i += 1
        else :
            arr[k] = right[j]
            j += 1
        k += 1
    # 复制最后剩余的
    while i < n1 :
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2 :
        arr[k] = right[j]
        j += 1
        k += 1

"""
自顶向下的归并排序
时间复杂度：n*log(n)/2 至 n*log(n)次比较
"""
def mergeSort(arr , low , high) :
    assert(isinstance(ori_arr , list))
    if 1 == len(arr) :
        return arr
    if low < high :
        mid = int((low + (high - 1)) / 2)
        mergeSort(arr , low , mid)
        mergeSort(arr , mid+1 , high)
        merge(arr , low , mid , high)

"""
自底向上的归并排序
时间复杂度：n*log(n)/2 至 n*log(n)次比较
"""
def mergeSort2(arr) :
    assert(isinstance(ori_arr , list))
    if 1 == len(arr) :
        return arr
    arr_len = len(arr)
    rst = list()
    sub_len = 1   # 子数组大小
    while sub_len < arr_len :
        sub_idx = 0     # 子数组索引
        while sub_idx < arr_len - sub_len :
            merge(arr , sub_idx , sub_idx + sub_len - 1 , min(sub_idx + sub_len * 2 -1 , arr_len -1))
            sub_idx += sub_len * 2
        sub_len *= 2


if "__main__" == __name__ :
    ori_arr = [random.randint(0 , 100) for i in range(10)]
    print("ori_arr: " , ori_arr)
    #mergeSort(ori_arr , 0 , len(ori_arr)-1)
    mergeSort2(ori_arr)
    print("mrg_arr: " , ori_arr)
