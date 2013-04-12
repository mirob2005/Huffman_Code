#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/23/2013
#Modified: 4/12/2013 for Huffman Code

from include.Binary_Heap_Array_Structure import BinaryHeap
from include.Node import Node

class PriorityQueue:
    def __init__(self):
        self.order = BinaryHeap()
    def __str__(self):
        temp = self.order.copyHeap()
        front = temp.delete()
        string = ("<Front>\n")
        while front:
            string+= (" %s"%front)
            front = temp.delete()
        string += "<BACK>"
        return string
    def enQueue(self,Node):
        self.order.insert(Node)
    def deQueue(self):
        return self.order.delete()