#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/23/2013
#Modified: 4/11/2013 for Huffman Code

from include.Binary_Heap_Array_Structure import BinaryHeap

class PriorityQueue:
    def __init__(self):
        self.order = BinaryHeap()
    def __str__(self):
        temp = self.order.copyHeap()
        front = temp.delete()
        string = ("<Front>")
        while front:
            string+= (" %s"%front)
            front = temp.delete()
        string += " <BACK>"
        return string
    def enQueue(self,value,key):
        self.order.insert(value,key)
    def deQueue(self):
        return self.order.delete()