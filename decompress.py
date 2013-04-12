#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/--/2013

#Decompresses a test file compressed by compress.py using Huffman coding
#   algorithm.

import os
import sys
from include.Priority_Queue import PriorityQueue


def decompress(inFile,outFile):
    infp = open(inFile,'r')
    text = infp.read()
    groupings = []
    for char in text:
        groupings.append(ord(char))
    
    code = ''
    outfp = open(outFile,'w')
    for group in groupings:
        code += bin(group)[2:]
    for char in code:
        if char == '1':
            outfp.write('a')
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
    