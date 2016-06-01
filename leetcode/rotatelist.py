'''
Created on May 4, 2016

@author: Sameer Adhikari
'''
from pip._vendor.requests.api import head

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        n = 1
        trav = head
        while trav.next:
            n += 1
            trav = trav.next
        # We have the count of nodes and a
        # pointer to the tail of the list
        tail = trav
        
        # If number of rotations is greater than
        # the size of the list we ignore some.
        if k >= n:
            k %= n
        
        if k == 0:
            return head
            
        j = 1
        trav = head
        while j < n - k:
            j += 1
            trav = trav.next
        
        # Break the list
        head1 = trav.next
        trav.next = None
        # Move the list after the break to the front.
        tail.next = head
        head = head1
        
        return head
     
    def printList(self, head):
        n = 1
        trav = head
        while trav:
            print 'n = {}, val = {}'.format(n, trav.val)
            n += 1
            trav = trav.next
        print 64 * '*'     
        
if __name__ == '__main__':
    head = ListNode(5)
    head.next = ListNode(6)
    head.next.next = ListNode(7)
    s = Solution()
    s.printList(head)
    head = s.rotateRight(head, 2)
    s.printList(head)
        
