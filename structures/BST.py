'''
Created on Mar 15, 2015

@author: Sameer Adhikari
'''

class BSTNode(object):
    
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        
        

class BST(object):
    
    def __init__(self):   
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def put(self, key, val):
        if self.root:
            self._put(self.root, key, val)
        else:
            self.root = BSTNode(key, val)
        self.size = self.size + 1
        
    def _put(self, current, key, val):
        if key == current.key:  # overwrite existing value for current node
            current.val = val
        elif key < current.key: # case to go left in the subtree
            if current.left:    # current node has left child
                self._put(current.left, key, val)
            else:               # current node does not have a left child
                current.left = BSTNode(key, val, parent = current)
        else:                   # case to go right in the subtree
            if current.right:
                self._put(current.right, key, val)
            else:
                current.right = BSTNode(key, val, parent = current)
            