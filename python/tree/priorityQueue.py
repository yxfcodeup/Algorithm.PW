import os
import sys
import random

#External Moduls
from graphviz import Digraph


class MaxHeap :
    def __init__(self , capacity=10) :
        self.capacity = capacity
        self.heap = list()
        self.traversal = list()

    """
    最大堆的向下调整算法
    注：数组实现的堆中，第N个结点的左孩子的索引值是(2N+1)，右孩子的索引值是(2N+2)
    @param start -- 被下调结点的起始位置(一般为0，表示从第1个开始)
    @param end   -- 截至范围(一般为数组中最后一个元素的索引)
    """
    def filterdown(self , start , end) :
        current = start             # 当前结点位置
        left = 2 * current + 1      # 左孩子位置
        tmp = self.heap[current]    # 当前结点值
        
        while left <= end :
            if (left < end) and (self.heap[left] < self.heap[left+1]) :
                left += 1           # 选择左右孩子较大的
            if tmp >= self.heap[left] :
                break               # 调整结束
            else :
                self.heap[current] = self.heap[left]
                current = left
                left = 2 * left + 1
        self.heap[current] = tmp

    """
    删除最大堆中的数据
    @return  -- 0,成功; -1,失败
    """
    def remove(self , rdata) :
        if 0 == len(self.heap) :
            return -1 
        idx = self.heap.index(rdata) if rdata in self.heap else -1
        if -1 == idx :
            return -1

        self.heap[idx] = self.heap.pop()              # 用最后的元素填补
        self.filterdown(idx , len(self.heap)-1)       # 从idx位置开始自上向下调整
        return 0

    """
    最大堆的向上调整算法(从start开始向上直到0，调整堆)
    注：数组实现的堆中，第N个节点的左孩子的索引值是(2N+1)，右孩子的索引是(2N+2)。
    @param start -- 被上调节点的起始位置(一般为数组中最后一个元素的索引)
    """
    def filterup(self , start) :
        current = start                 # 当前结点的位置
        parent = int((current - 1) / 2)      # 父结点的位置
        tmp = self.heap[current]        # 当前结点大小

        while current > 0 :
            if self.heap[parent] >= tmp :
                break
            else :
                self.heap[current] = self.heap[parent]
                current = parent
                parent = int((parent - 1) / 2)
        self.heap[current] = tmp

    """
    插入数据到堆
    @return  -- 0,成功; -1,失败
    """
    def insert(self , idata) :
        if self.capacity == len(self.heap) :
            return -1
        self.heap.append(idata)         # 将数据插在最后
        self.filterup(len(self.heap)-1)   # 向上调整堆
        return 0

    """
    中序遍历
    """
    def inorderTraversal(self , root_node_idx , p_idx) :
        if root_node_idx < len(self.heap) :
            left_idx = 2 * root_node_idx + 1
            right_idx = 2 * root_node_idx + 2
            self.inorderTraversal(left_idx , root_node_idx)
            self.traversal.append((self.heap[p_idx] , self.heap[root_node_idx]))
            self.inorderTraversal(right_idx , root_node_idx)

    def printMaxHeap(self) :
        for v in self.heap :
            print(v)

class MinHeap :
    def __init__(self , capacity=10) :
        self.capacity = capacity
        self.heap = list()
        self.traversal = list()

    """
     最小堆的向下调整算法
     注：数组实现的堆中，第N个节点的左孩子的索引值是(2N+1)，右孩子的索引是(2N+2)
     @param start -- 被下调节点的起始位置(一般为0，表示从第1个开始)
     @param end   -- 截至范围(一般为数组中最后一个元素的索引)
    """
    def filterdown(self , start , end) :
        current = start             # 当前结点位置
        left = 2 * current + 1      # 左孩子结点位置
        tmp = self.heap[current]    # 需要调整的结点值

        while left <= end :
            if (left < end) and (self.heap[left] > self.heap[left+1]) :
                left += 1           # 选择左右孩子较小的
            if tmp <= self.heap[left] :
                break               # 调整结束
            else :
                self.heap[current] = self.heap[left]
                current = left
                left = 2 * left + 1
        self.heap[current] = tmp

    """
    删除最小堆中的数据
    @return  -- 0,成功; -1,失败
    """
    def remove(self , rdata) :
        if 0 == len(self.heap) :
            return -1
        idx = self.heap.index(rdata) if rdata in self.heap else -1
        if -1 == len(self.heap) :
            return -1

        self.heap[idx] = self.heap.pop()              # 用最后的元素填补
        self.filterdown(idx , len(self.heap)-1)       # 从idx位置开始自上向下调整
        return 0

    """
    最小堆的向上调整算法(从start开始向上直到0，调整堆)
    注：数组实现的堆中，第N个节点的左孩子的索引值是(2N+1)，右孩子的索引是(2N+2)。
    @param start -- 被上调节点的起始位置(一般为数组中最后一个元素的索引)
    """
    def filterup(self , start) :
        current = start                 # 当前结点的位置
        parent = int((current - 1) / 2)      # 父结点的位置
        tmp = self.heap[current]        # 当前结点大小

        while current > 0 :
            if self.heap[parent] <= tmp :
                break
            else :
                self.heap[current] = self.heap[parent]
                current = parent
                parent = int((parent-1) / 2)
        self.heap[current] = tmp

    def insert(self , idata) :
        if self.capacity == len(self.heap) :
            return -1
        self.heap.append(idata)         # 将数据插在最后
        self.filterup(len(self.heap)-1)   # 向上调整堆
        return 0

    """
    中序遍历
    """
    def inorderTraversal(self , root_node_idx , p_idx) :
        if root_node_idx < len(self.heap) :
            left_idx = 2 * root_node_idx + 1
            right_idx = 2 * root_node_idx + 2
            self.inorderTraversal(left_idx , root_node_idx)
            self.traversal.append((self.heap[p_idx] , self.heap[root_node_idx]))
            self.inorderTraversal(right_idx , root_node_idx)


if "__main__" == __name__ :
    a = [10, 40, 30, 60, 90, 70, 20, 50, 80]

    max_heap = MaxHeap()
    for val in a :
        max_heap.insert(val)
    max_heap.insert(85)
    max_heap.remove(90)
    max_heap.inorderTraversal(0 , 0)

    """
    使用graphviz生成.gv文件后，执行命令'dot.exe ./max_heap.gv -T png -o max_heap.png'生成图片查看
    """
    #g = Digraph("G" , filename="max_heap.gv")
    #for val in max_heap.traversal :
    #    if val[0] == val[1] :
    #        continue
    #    g.edge(str(val[0]) , str(val[1]))
    #g.save()

    b = [80, 40, 30, 60, 90, 70, 10, 50, 20]
    min_heap = MinHeap()
    for val in b :
        min_heap.insert(val)
    min_heap.insert(15)
    min_heap.remove(10)
    min_heap.inorderTraversal(0 , 0)
    g = Digraph("G" , filename="min_heap.gv")
    for val in min_heap.traversal :
        if val[0] == val[1] :
            continue
        g.edge(str(val[0]) , str(val[1]))
    g.save()
