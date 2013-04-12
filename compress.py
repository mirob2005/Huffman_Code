#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/--/2013

# Compresses a test file using Huffman coding algorithm.

import os
import sys
from include.Priority_Queue import PriorityQueue


def compress(inFile,outFile):
    infp = open(inFile,'r')
    text = infp.read()
    outfp = open(outFile,'w')
    
    output = ''
    for char in text:
        if char == 'a':
            output += '1'
    groupings = []    
    while output:
        groupings.append(output[:8])
        output = output[8:]
        
    for group in groupings:
        outfp.write(chr(int(group,2)))
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
    