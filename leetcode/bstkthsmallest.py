'''
Created on Apr 22, 2016

@author: Sameer Adhikari
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def treeCount(self, root):
        """
        Determine the size of tree at root
        """
        if not root:
            return 0
        left = self.treeCount(root.left)
        right = self.treeCount(root.right)
        return left + right + 1
            
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        if k == 0:
            return root.val
        #print 'node: {}, wanted = {}'.format(root.val, k)
        leftcount = self.treeCount(root.left)
        #print 'node: {}, count = {}'.format(root.val, leftcount)
        if leftcount + 1 == k:
            return root.val
        elif leftcount + 1 > k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - leftcount - 1)
        
        
        
if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    s = Solution()
    #print s.kthSmallest(root, 2)        
    #print s.kthSmallest(root, 1)        
    print s.kthSmallest(root, 3)        