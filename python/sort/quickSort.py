import os
import sys
import copy
import random
import datetime

def colorString(nums=set()) :
    rstr = ""
    for i in range(10) :
        cf = "{}"
        if i in nums :
            cf = "\033[1;35m{}\033[0m"
        if 9 == i :
            rstr += cf
        else :
            rstr += cf + " , "
    return rstr

def partition(arr , low , high) :
    i = low - 1         # 比基准数小的位置
    pivot = arr[high]   # 基准数
    
    """
    通过遍历数组，以冒泡的方式，将小于基准数的元素交换到位置i
    """
    for j in range(low , high) :
        if (arr[j] <= pivot) :
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]
    """
    因为取位置high的数作为基准数，最后将位置i+1的数与基准数交换，使得左边小于基准数，右边大于基准数
    """
    arr[i+1] , arr[high] = arr[high] , arr[i+1]
    return i+1

"""
快速排序-原地排序
时间复杂度：
    平均：2(n+1)(1/3 + 1/4 + ... +1/(n+1)) ~ 2*n*ln(n)次比较
    最多：n^2/2次比较
"""
def quickSort(arr , low , high) :
    if (low < high) :
        pit = partition(arr , low , high)
        quickSort(arr , low , pit-1)
        quickSort(arr , pit+1 , high)


if "__main__" == __name__ :
    ori_arr = [random.randint(0 , 100) for i in range(10)]
    ori_arr = [59 , 14, 35, 10,15, 41, 64, 22, 55, 40]
    print("ori_arr: " , ori_arr)
    quickSort(ori_arr , 0 , len(ori_arr)-1)
    print("rst_arr: " , ori_arr)
