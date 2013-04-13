#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/--/2013

#Decompresses a test file compressed by compress.py using Huffman coding
#   algorithm.

import os
import sys
from include.Priority_Queue import PriorityQueue
from include.Node import Node

def decompress(inFile,outFile):
    infp = open(inFile,'rb')
    text = infp.read()
    outfp = open(outFile,'w')
    
    hexGrp = []
    for char in text:
        hexGrp.append(bin(char)[2:])
    
    code = ''
    for group in hexGrp[:-1]:
        while len(group) != 8:
            group = '0'+group
        code += group
    code += hexGrp[-1]

    print(code)    

    infp.close()
    outfp.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python decompress.py compressedFile.txt originalFile.txt')
        exit()
    if os.path.exists(sys.argv[1]):
        decompress(sys.argv[1],sys.argv[2])
    else:
        print('Path %s does not exist!'%sys.argv[1])
    