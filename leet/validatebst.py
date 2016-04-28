'''
Created on Apr 28, 2016

@author: Sameer Adhikari
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def genInOrder(self, root):
        if not root:
            return []
        
        left = []
        right = []
        if root.left:
            left = self.genInOrder(root.left)
        if root.right:
            right = self.genInOrder(root.right)
            
        return left + [root.val] + right
            
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        inOrder = self.genInOrder(root)
        for i in range(len(inOrder) - 1):
            if inOrder[i] >= inOrder[i + 1]:
                return False
        return True
            
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1) 
    s = Solution()
    print s.isValidBST(root)   
        
            