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
    outfp = open(outFile,'wb')
    
    nodes = {}
    
    for char in text:
        if char in nodes:
            nodes[char].value += 1
        else:
            nodes[char] = Node(1,char)

    #for node in nodes.values():
        #print('Node %s has value %s and code %s'%(node.key,node.value,node.code))
            
    q = PriorityQueue()
    for node in nodes.values():
        q.enQueue(node)
    
    min1 = q.deQueue()
    min2 = q.deQueue()
    while min2:
        q.enQueue(min1+min2)
        min1 = q.deQueue()
        min2 = q.deQueue()
   
    root = min1

    output = ''
    for char in text:
        if char in nodes:
            output += nodes[char].code
        else:
            print('Char object not found!')

    bitLength = len(output)
    hexGrp = []    
    while output:
        hexGrp.append(output[:8])
        output = output[8:]
        
    output = bytes([int(group,2) for group in hexGrp])
    
    size = outfp.write(output)
    infp.close()
    outfp.close()
    
    return size

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python compress.py originalFile.txt compressedFile.txt')
        exit()
    if os.path.exists(sys.argv[1]):
        uncompressedSize = os.stat(sys.argv[1]).st_size
        compressedSize = compress(sys.argv[1],sys.argv[2])
        print('Uncompressed Size: %s bytes'%uncompressedSize)
        print('Compressed Size: %s bytes'%compressedSize)
        print('Precent Space Saved: %f'%(1-(compressedSize/uncompressedSize)))
    else:
        print('Path %s does not exist!'%sys.argv[1])
    