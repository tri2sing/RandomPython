'''
Created on May 11, 2016

@author: Sameer Adhikari
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __next__(self):
        return self.next
    
        
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
            
        
class Solution(object):
    def sortedListToBSTInternal(self, head, start, end):
        """ we use a list to contain the head of the list to allow mutability"""
        if start > end:
            return None
        mid = (start + end)/2
        left = self.sortedListToBSTInternal(head, start, mid - 1)
        root = TreeNode(head[0].val) # This has to be after completing the left subtree
        head[0] = head[0].next  # The reason for using list to hold the head
        right = self.sortedListToBSTInternal(head, mid + 1, end)
        root.left = left
        root.right = right
        return root
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: 
            return None
        n = 0
        trav = head
        while trav:
            n += 1
            trav = trav.next
        return self.sortedListToBSTInternal([head], 0, n - 1)
        
    def inorderInternal(self, root):
        if not root:
            return
        if root.left:
            self.inorder(root.left)
        print root.val
        if root.right:
            self.inorder(root.right)

    def inorder(self, root=None):
        if not root:
            return
        self.inorderInternal(root)

if __name__ == '__main__':
    head = ListNode(1)
    trav = head
    trav.next = ListNode(2)
    trav = trav.next
    trav.next = ListNode(3)
    trav = trav.next
    trav.next = ListNode(4)
    trav = trav.next
    trav.next = ListNode(5)
    trav = trav.next
    trav.next = ListNode(6)
    trav = trav.next
    trav.next = ListNode(7)
    trav = trav.next
    trav.next = ListNode(8)
    
    trav = head
    while trav:
        print trav.val,
        trav = trav.next
    print
    
    s = Solution()
    r = s.sortedListToBST(head)
    s.inorder(r)
    
    
    