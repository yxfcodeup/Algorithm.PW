# -*- coding: utf-8 -*-
import random

def colorString(nums=set()):
    rstr = ""
    for i in range(10):
        cf = "{}"
        if i in nums:
            cf = "\033[1;35m{}\033[0m"
        if 9 == i:
            rstr += cf
        else:
            rstr += cf + " , "
    return rstr

def partition(arr , low , high):
    """
    选择一个基准数，将数列分隔为两部分，小于基准数的在前面，大于基准数的在后面
    """
    i = low - 1         # 比基准数小的位置
    pivot = arr[high]   # 基准数
    
    # 遍历数组，以冒泡的方式，将小于基准数的元素交换到位置i
    for j in range(low , high):
        if (arr[j] <= pivot):
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]

    # 因为取位置high的数作为基准数，最后将位置i+1的数与基准数交换，使得左边小于基准数，右边大于基准数
    arr[i+1] , arr[high] = arr[high] , arr[i+1]
    return i+1

def quickSort(arr , low , high):
    """
    快速排序-原地排序
    :param arr: 待排序数列
    :param low: 需要排序范围的最低位置
    :param high: 需要排序范围的最高位置
    :return: 无
    """
    if (low < high):
        # pit = partition(arr , low , high)
        # 选择一个基准数，将数列分隔为两部分，小于基准数的在前面，大于基准数的在后面
        i = low - 1         # 比基准数小的位置，即i+1比基准数大
        pivot = arr[high]   # 基准数
        
        # 遍历数组，以冒泡的方式，将小于基准数的元素交换到位置i+1
        for j in range(low , high):
            if (arr[j] <= pivot):
                i += 1
                arr[i] , arr[j] = arr[j] , arr[i]
                print(f"exchange: {arr} -> {pivot}, {j}..{arr[j]}, {i}..{arr[i]}")
            else:
                print(f"nochange: {arr} -> {pivot}, {j}..{arr[j]}, {i}..{arr[i]}")

        # 因为取位置high的数作为基准数，最后将位置i+1的数与基准数交换，使得数组左边小于基准数，右边大于基准数
        arr[i+1] , arr[high] = arr[high] , arr[i+1]

        pit = i + 1
        quickSort(arr , low , pit-1)
        quickSort(arr , pit+1 , high)


if "__main__" == __name__:
    ori_arr = [random.randint(0 , 100) for i in range(10)]
    ori_arr = [59 , 14, 35, 10,15, 41, 64, 22, 55, 40]
    ori_arr = [10, 14, 15, 22, 35, 40, 41, 55, 59, 64]
    print(f"ori_arr: {ori_arr}")
    quickSort(ori_arr , 0 , len(ori_arr)-1)
    print(f"rst_arr: {ori_arr}")
