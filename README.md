# Huffman_Code

Implementing the huffman code compression algorithm in Python.

## Usage:

### compress.py
- python compress.py originalFile compressedFile

### decompress.py
- python decompress.py compressedFile decompressedFile

## Implementation:
- The compressed file includes all the information necessary for decompress.py to decompress the file.
- This includes a header portion which includes a representation of the Huffman tree.
- The tree is represented as follows: '0' for each internal node, '1' + ASCII representation for the symbol for each leaf node.
- The tree is traversed in preorder to form the header.
- The header is ended with the second occurrence of 16 '1's (the EOF symbol).
- The first occurrence of 16 '1's is the ASCII representation for the EOF symbol in a tree leaf node.
- The rest of the compressed file is the Huffman tree codes for each character in the original file text.
- The overhead for the header and the extra EOF symbol is listed in the following section.

## Overhead Included in the Algorithm:
- 1 extra bit for each internal node in the Huffman Tree to store in the compressed file.
- 9 extra bits (1 for node, 8 for ASCII representation) for each leaf node.
- 16 extra bits to signify end of the header portion of the compressed file.
- Extra bits for the EOF symbol (17 extra bits: 1 node, 16 ASCII rep. + the Huffman code to represent the symbol)

## Results:

<table>

  <tr>

    <th>File</th><th>Original Size</th><th>Compressed Size</th><th>Ratio</th>

  </tr>

  <tr>

    <td>Test1</td><td>156 bytes</td><td>184 bytes</td><td>+17.95%</td>

  </tr>
  
  <tr>

    <td>Test2</td><td>2850 bytes</td><td>1383 bytes</td><td>-51.47%</td>

  </tr>

  <tr>

    <td>Test3</td><td>830 bytes</td><td>490 bytes</td><td>-40.96%</td>

  </tr>
  
  <tr>

    <td>Test4</td><td>95 bytes</td><td>203 bytes</td><td>+103.68%</td>

  </tr>
  
  <tr>

    <td>Test5</td><td>253309 bytes</td><td>134491 bytes</td><td>-46.95%</td>

  </tr>
  
</table>

### Explaination of Result:
- Test 1 has mostly unique characters with some repeats so the necessary overhead makes the compressed file larger.
- Test 4 has one of each printable ASCII character so there is little possibility for compression.
- Test 2 is a sentence repeated mulitple times allowing for compression.
- Test 3 and 5 include assorted characters resembling more natural written text.
