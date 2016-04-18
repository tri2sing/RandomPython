'''
Created on Apr 17, 2016

@author: Sameer Adhikari
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __repr__(self):
        return 'TreeNode(%s)' % repr(self.val)
   
    __str__ = __repr__

from collections import defaultdict, deque

class Solution(object):
    '''Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).'''
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        # Track all the nodes in a level
        levelmap = defaultdict(list)
        level = 0
        queue = deque()
        queue.append(root)
        queue.append(None)
        while queue:
            # breadth first traversal
            node = queue.popleft()
            if not node and not queue:
                # Finished will all nodes
                break
            if not node and queue:
                # Finished will all nodes of this level
                level += 1
                queue.append(None)
                continue
            levelmap[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result = []
        print levelmap
        for i in range(level, -1, -1):
            result.append(levelmap[i])
        return result
    

if __name__ == '__main__':
    root = TreeNode(1)
    s = Solution()
    res = s.levelOrderBottom(root)
    print res
