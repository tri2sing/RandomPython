'''
Created on Apr 25, 2016

@author: Sameer Adhikari
'''

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = deque()
        trav = root
        while trav:
            self.stack.append(trav)
            trav = trav.left
        print 'init done'

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack        

    def next(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        node = self.stack.pop()
        ans = node.val
        trav = node.right
        if node.right:
            trav = node.right
            while trav:
                self.stack.append(trav)
                trav = trav.left
        return ans
        

# Your BSTIterator will be called like this:
if __name__ == '__main__':
    root = None
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())

    