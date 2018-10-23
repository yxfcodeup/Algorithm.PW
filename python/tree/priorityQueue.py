import os
import sys
import random


class MaxHeap() :
    def __init__(self , capacity=10) :
        self.capacity = 10
        self.heap = [0] * self.capacity

    def filterdown(start , end) :
        current = start
        left = 2 * current + 1
        tmp = self.heap[current]
        
        while (left <= end) :
            if ((left < end) and (self.heap[left] < self.heap[left+1])) :
                left += 1 
            if (tmp >= self.heap[left]) :
                break
            else :
                self.heap[current] = self.heap[left]
                current = left
                left = 2 * left + 1
        self.heap[current] = tmp

    def remove(rdata) :
        if (0 == len(self.heap)) :
            return -1 
        idx = self.heap.index(rdata) if rdata in self.heap else -1
        if (-1 == idx) :
            return -1

        self.heap[idx] = self.heap[-1]
        self.filterdown(idx , len(self.heap))

    """
        最大堆的向上调整算法(从start开始向上直到0，调整堆)
        注：数组实现的堆中，第N个节点的左孩子的索引值是(2N+1)，右孩子的索引是(2N+2)。
        @param start  --被上调节点的起始位置(一般为数组中最后一个元素的索引)
    """
    def filterup(start) :
        current = start                 # 当前结点的位置
        parent = (current - 1) / 2      # 父结点的位置
        tmp = self.heap[current]        # 当前结点大小

        while (current > 0) :
            if (self.heap[parrent] >= tmp) :
                break
            else :
                self.heap[current] = self.heap[parent]
                current = parent
                parent = (parent - 1) / 2
        self.heap[current] = tmp



