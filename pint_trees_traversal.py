class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    print(root, end=' ')
    s = str(root.info) # if we want to return something instead of printing 
    if root.left:
        s += ' ' + preOrder(root.left)
    if root.right:
       s += ' ' + preOrder(root.right)
    
    return s
    
# from io import StringIO
# import sys

# old_stdout = sys.stdout
# sys.stdout = mystdout =  StringIO()

tree = BinarySearchTree()
arr = [1,2,5,3,4,6]
for i in arr:
    tree.create(i)
assert '1 2 5 3 4 6' == preOrder(tree.root)
print()

tree = BinarySearchTree()
arr = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]
for i in arr:
    tree.create(i)
assert '1 14 3 2 7 4 5 6 13 10 8 9 11 12 15' == preOrder(tree.root)
print()

# sys.stdout = old_stdout
# assert '1 14 3 2 7 4 5 6 13 10 8 9 11 12 15 ' == mystdout.getvalue()