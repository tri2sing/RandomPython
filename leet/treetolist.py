'''
Created on Apr 27, 2016

@author: Sameer Adhikari
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        if not root.left:
            return
        
        if root.left:
            self.flatten (root.left)

        if root.right:
            self.flatten (root.right)

        trav = root.left
        while trav.right:
            trav = trav.right
        trav.right = root.right
        root.right = root.left
        root.left = None
        
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    s = Solution()
    s.flatten(root)