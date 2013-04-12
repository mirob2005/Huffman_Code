#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/--/2013

# Used in compress.py

class Node:
    def __init__(self, value, key, code=None, left=None, right=None):
        self.value = value
        self.key = key
        self.code = code
        self.left = left
        self.right = right
    def __str__(self):
        return 'Node <%s>: value: %s code: %s\n\tLeft: %s \n\tRight: %s\n'%(self.key,self.value,self.code,self.left,self.right)
    def __contains__(self,key):
        return key == self.key
    def __add__(self,node2):
        self.propagateCode(self,'0')
        node2.propagateCode(node2,'1')
            
        return Node(self.value+node2.value,self.key+node2.key,None,self,node2)
    def propagateCode(self,node,code):
        if node.code == None:
            node.code = code
        else:
            node.code = code + node.code
        if node.left:
            node.propagateCode(node.left,code)
        if node.right:
            node.propagateCode(node.right,code)
        
if __name__ == '__main__':
    c = Node(1,'c')
    #print(c)
    s = Node(2,' ')
    #print(s)
    cs = c + s
    #print(cs)
    
    d = Node(3,'d')
    #print(d)
    csd = cs+d
    print(csd)
    
    b = Node(2,'b')
    #print(b)
    a = Node(3,'a')
    #print(a)
    ba = b+a
    print(ba)
    
    bacsd = ba+csd
    print(bacsd)