#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/25/2013

#Modified: 4/12/2013 for Huffman Code
#Now has a Node Object, heap based off the value and if ties, then key
#Is now a Min-heap

# Binary Heap implemented using an array instead of a binary tree data structure
# Children are at a[2i+1] and a[2i+2]
# Parent is at a[floor((i-1)/2)]
# where the array goes from 0 to n-1 and the root is at index 0

from include.Node import Node

class BinaryHeap:
    def __init__(self):
        self.nodes = []
    
    def returnBFS(self):
        return self.nodes
    
    def insert(self,Node):
        self.nodes.append(Node)
        self.heapifyUp()
        return True
    
    def delete(self):
        if self.isEmpty():
            return None
        returnValue = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()
        self.heapifyDown(0, self.getLeftChildIndex(0), self.getRightChildIndex(0))
        return returnValue
    
    def peek(self):
        return self.nodes[0] if not self.isEmpty() else None
    
    def heapifyUp(self):
        child = len(self.nodes)-1
        parent = self.getParentIndex(child)
        while(self.nodes[child].value < self.nodes[parent].value or (self.nodes[child].value == self.nodes[parent].value and self.nodes[child].key < self.nodes[parent].key)):
            temp = self.nodes[child]
            self.nodes[child] = self.nodes[parent]
            self.nodes[parent] = temp
            child = parent
            parent = self.getParentIndex(child)
            
    def heapifyDown(self,parent,left,right):
        if not self.validChild(left) and not self.validChild(right):
            return
        if not self.validChild(right) or self.nodes[left].value < self.nodes[right].value or (self.nodes[left].value == self.nodes[right].value and self.nodes[left].key < self.nodes[right].key):
            if(self.nodes[left].value < self.nodes[parent].value or (self.nodes[left].value == self.nodes[parent].value and self.nodes[left].key < self.nodes[parent].key)):
                temp = self.nodes[parent]
                self.nodes[parent] = self.nodes[left]
                self.nodes[left] = temp
                parent = self.getLeftChildIndex(parent)
            else:
                return
        else:
            if(self.nodes[right].value < self.nodes[parent].value or (self.nodes[right].value == self.nodes[parent].value and self.nodes[right].key < self.nodes[parent].key)):
                temp = self.nodes[parent]
                self.nodes[parent] = self.nodes[right]
                self.nodes[right] = temp
                parent = self.getRightChildIndex(parent)
            else:
                return
        self.heapifyDown(parent, self.getLeftChildIndex(parent), self.getRightChildIndex(parent))
            
    def validChild(self,index):
        return True if index < len(self.nodes) else False
            
    def getLeftChildIndex(self,index):
        return ((2*index)+1)
    
    def getLeftChild(self,index):
        child = self.getLeftChildIndex(index)
        return self.nodes[child] if self.validChild(child) else None
    
    def getRightChildIndex(self,index):
        return ((2*index)+2)
    
    def getRightChild(self,index):
        child = self.getRightChildIndex(index)
        return self.nodes[child] if self.validChild(child) else None
    
    def getParentIndex(self,index):
        return int((index-1)/2)
    
    def getParent(self,index):
        return self.nodes[self.getParentIndex(index)] if index > 0 else None
    
    def isEmpty(self):
        return len(self.nodes)==0
    
    def copyHeap(self):
        copy  = BinaryHeap()
        for node in self.nodes:
            copy.insert(node)
        return copy