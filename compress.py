#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/--/2013

# Compresses a test file using Huffman coding algorithm.

import os
import sys
from include.Priority_Queue import PriorityQueue
from include.Node import Node

def compress(inFile,outFile):
    infp = open(inFile,'r')
    text = infp.read()
    outfp = open(outFile,'w')
    
    nodes = []
    
    for char in text:
        found = False
        for node in nodes:
            if node.key == char:
                node.value += 1
                found = True
        if not found:
            nodes.append(Node(1,char))

    for node in nodes:
        print('Node %s has value %s and code %s'%(node.key,node.value,node.code))
            
    q = PriorityQueue()
    for node in nodes:
        q.enQueue(node)
    
    min1 = q.deQueue()
    min2 = q.deQueue()
    while min2:
        q.enQueue(min1+min2)
        min1 = q.deQueue()
        min2 = q.deQueue()
    print(min1)

    #groupings = []    
    #while output:
    #    groupings.append(output[:8])
    #    output = output[8:]
    #    
    #for group in groupings:
    #    outfp.write(chr(int(group,2)))
    infp.close()
    outfp.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python compress.py originalFile.txt compressedFile.txt')
        exit()
    if os.path.exists(sys.argv[1]):
        compress(sys.argv[1],sys.argv[2])
    else:
        print('Path %s does not exist!'%sys.argv[1])
    