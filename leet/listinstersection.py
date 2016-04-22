'''
Created on Apr 21, 2016

@author: Sameer Adhikari
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        iterA = headA
        numA = 0
        while iterA:
            numA += 1
            iterA = iterA.next
        
        iterB = headB
        numB = 0
        while iterB:
            numB += 1
            iterB = iterB.next
        
        print 'num A = {}, num B = {}'.format(numA, numB)
        iterA = headA
        iterB = headB
        steps = abs(numA - numB)
        if numA > numB:
            while steps > 0:
                iterA = iterA.next
                steps -= 1
        else:
            if numA < numB:
                while steps > 0:
                    iterB = iterB.next
                    steps -= 1
        
        while iterA and iterB:
            print 'A = {}, B = {}'.format(iterA.val, iterB.val)
            if iterA.val == iterB.val:
                return iterA
            iterA = iterA.next
            iterB = iterB.next
        return None
        
                
                
        
if __name__ == '__main__':
    headA = ListNode(3)
    headB = ListNode(2)
    headB.next = ListNode(3)
    s = Solution()
    s.getIntersectionNode(headA, headB)