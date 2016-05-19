'''
Created on May 19, 2016

@author: Sameer Adhikari
'''

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    
    def connectInternal(self, current, parent):
        ''' '''
        if not current:
            return
        if current and not parent:
            current.next = None
        # If this node is a left child then the next
        # will be the right child of the same parent
        if parent and current == parent.left:
            current.next = parent.right
        # If this node is a right child then the next
        # node can be either the left child of the next
        # node of its parent, or None if this is the 
        # child of the rightmost node on the parent level
        if parent and current == parent.right:
            if parent.next:
                current.next = parent.next.left
            else:
                current.next = None
        self.connectInternal(current.left, current)
        self.connectInternal(current.right, current)
                
        
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.connectInternal(root, None)
    
    def printTree(self, root):
        if not root:
            return
        self.printTree(root.left)
        print root.val,
        if root.next:
            print root.next.val
        else:
            print None
        self.printTree(root.right)
        
if __name__ == '__main__':
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.left = TreeLinkNode(6)
    root.right.right = TreeLinkNode(7)
    
    s = Solution()
    s.printTree(root)
    print 32 * '='
    s.connect(root)
    s.printTree(root)
    print 32 * '='
