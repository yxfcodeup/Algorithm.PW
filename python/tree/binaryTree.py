import os
import sys
import random


class BiNode() :
    def __init__(self , val) :
        self.left = None
        self.right = None
        self.element = val

    def getElement(self) :
        return self.element

    def dictFormat(self) :
        return {
                "element": self.element , 
                "left": self.left , 
                "right": self.right ,
                }

    def __str__(self) :
        return str(self.element)

class BinaryTree() :
    def __init__(self , node=None) :
        self.root = node
        self.traversal = list()

    """
    广度遍历的方式添加子结点
    """
    def addNode(self , val) :
        node = BiNode(val)
        if self.root is None :
            self.root = node
        else :
            node_queue = list()
            node_queue.append(self.root)
            while len(node_queue) :
                pop_node = node_queue.pop(0)
                if pop_node.left is None :
                    pop_node.left = node
                    break
                elif pop_node.right is None :
                    pop_node.right = node
                    break
                else :
                    node_queue.append(pop_node.left)
                    node_queue.append(pop_node.right)

    def __inorderTraversal(self , root_node) :
        if not isinstance(root_node , BiNode) :
            return 
        self.traversal.append(root_node)
        left = self.__inorderTraversal(root_node.left)
        right = self.__inorderTraversal(root_node.right)

    """
    前序遍历(DLR)
    """
    def preorderTraversal(self , root_node) :
        if root_node :
            print(root_node.getElement())
            self.preorderTraversal(root_node.left)
            self.preorderTraversal(root_node.right)

    """
    中序遍历(LDR)
    """
    def inorderTraversal(self , root_node) :
        """
        self.traversal = list()
        self.__inorderTraversal(self.root)
        return self.traversal
        """
        if root_node :
            self.preorderTraversal(root_node.left)
            print(root_node.getElement())
            self.preorderTraversal(root_node.right)

    """
    后序遍历(LRD)
    """
    def postorderTraversal(self , root_node) :
        if root_node :
            self.preorderTraversal(root_node.left)
            self.preorderTraversal(root_node.right)
            print(root_node.getElement())

    def morrisTraversal(self , root_node) :
        current = root_node
        while (current is not None) :
            if current.left is None :
                print(current.getElement())
                current = current.right
            else :
                pre = current.left
                while (pre.right is not None and pre.right != current) :
                    pre = pre.right
                if (pre.right is None) :
                    pre.right = current
                    current = current.left
                else :
                    pre.right = None
                    print(current.getElement())
                    current = current.right


if "__main__" == __name__ :
    #node_list = [random.randint(0 , 100) for i in range(10)]
    node_list = [i for i in range(1,11)]
    bt = BinaryTree()
    for v in node_list :
        bt.addNode(v)
    print("preorder")
    bt.preorderTraversal(bt.root)
    print("inorder")
    bt.inorderTraversal(bt.root)
    print("postorder")
    bt.postorderTraversal(bt.root)
