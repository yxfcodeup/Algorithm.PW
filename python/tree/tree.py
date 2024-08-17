# -*- coding: utf-8 -*-

class ParentTreeNode:
    def __init__(self, data: any, parent: int) -> None:
        self.data = data
        self.parent = parent
        
        
class ParentTree:
    def __init__(self) -> None:
        self.pt_nodes = list()
        
    def addNode(self, data: any, parent: int):
        new_node = ParentTreeNode(data, parent)
        self.pt_nodes.append(new_node)
        
    def findParent(self):
        for i in range(len(self.pt_nodes)):
            node = self.pt_nodes[i].data
        


if "__main__" == __name__:
    pass
