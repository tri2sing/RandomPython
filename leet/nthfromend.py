'''
Created on Apr 19, 2016

@author: Sameer Adhikari
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tracker = {}
        count = 1
        iterator = head
        while iterator:
            tracker[count] = iterator
            iterator = iterator.next
            count += 1
        # adjust count as it is one more that actual
        count -= 1
        # Calculate element to be removed 
        k = count - n + 1
        
        if k == 1:
            # remove first node list
            temp = head
            head = head.next
            temp.next = None
            return head
            
        # There will always be n entries in the,
        # tracker but not necessarily n + 1.
        if k + 1 in tracker:
            tracker[k - 1].next = tracker[k + 1]
            tracker[k].next = None
        else:
            # we are removing last node.
            tracker[k - 1].next = None
            tracker[k].next = None
        
        return head
        
    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev = None
        slow = head
        fast = head
        
        for _ in range(n):
            fast = fast.next

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        if not prev:
            # We need to remove the head of the list
            temp = head
            head = head.next
            temp.next = None
            return head
       
        if slow:
            # remove element 
            prev.next = slow.next
            slow.next = None
        else:
            # remove last element
            prev.next = None
        return head
    
if __name__ == '__main__':
    head = ListNode(1)
    n = 1
    s = Solution()
    s.removeNthFromEnd2(head, 1)
            
        