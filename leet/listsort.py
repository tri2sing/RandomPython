'''
Created on Apr 25, 2016

@author: Sameer Adhikari
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitList(self, head):
        # Find the middle of the list.
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Split the list
        head1 = head
        head2 = slow
        prev.next = None
        return head1, head2

    def mergeList(self, head1, head2):
        """ head1 and head2 are sorted."""
        head = None
        iter1 = head1
        iter2 = head2

        # Initialize the merge sort
        if iter1.val <= iter2.val:
            head = iter1
            iter1 = iter1.next
        else:
            head = iter2  
            iter2 = iter2.next
        
        iter0 = head  
        while iter1 and iter2:
            if iter1.val <= iter2.val:
                iter0.next = iter1
                iter1 = iter1.next
            else:
                iter0.next = iter2
                iter2 = iter2.next
            iter0 = iter0.next
        
        # At this point one or both of iters is consumed.
        if iter1 and not iter2:
            iter0.next = iter1
        if not iter1 and iter2:
            iter0.next = iter2
            
        return head
        
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # There is no or one node in the list
        if not head or not head.next:
            return head

        # For two or more node, split the list and merge sort.
        left, right = self.splitList(head)
        sortedleft = self.sortList(left)
        sortedright = self.sortList(right)
        head = self.mergeList(sortedleft, sortedright)
        return head

if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    trav = head
    while trav:
        print trav.val,
        trav = trav.next
    print
    s = Solution()
    head = s.sortList(head)
    trav = head
    while trav:
        print trav.val,
        trav = trav.next
    print
    
            