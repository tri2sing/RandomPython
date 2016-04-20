'''
Created on Apr 19, 2016

@author: Sameer Adhikari
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            # 0 or 1 elements
            return True
            
        # If there are even number of elements,
        # there will be two middle elements.
        mid1 = head  
        mid2 = None
        end = head
        while end.next and end.next.next:
            mid1 = mid1.next
            end = end.next.next
        # If there are even number of elements
        if end.next:
            mid2 = mid1.next
            end = end.next
        else:
            # Insert a duplicate node to make our life easier
            mid2 = ListNode(mid1.val)
            mid2.next = mid1.next
            mid1.next = mid2
        
        # Split the list
        mid1.next = None
        
        print 'about to reverse'
        # Reverse the second list
        p = None # previous
        c = mid2 # current
        n = mid2.next # next
        while c:
            c.next = p
            p = c
            c = n
            if n:
                n = n.next
        
        print 'about to compare'
        # Compare the two string
        ih = head
        ie = end
        while ih and ie:
            if ih.val != ie.val:
                return False
            ih = ih.next
            ie = ie.next
            
        if ih and not ie:
            return False
        if not ih and ie:
            return False
        return True
        
if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode(0)
    s = Solution()
    print s.isPalindrome(head)        