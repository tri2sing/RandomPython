'''
Created on May 17, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        n1 = x
        n2 = 0
        while n1 > 0:
            n2 = (n2 * 10) + (n1 % 10)
            n1 = n1 // 10
            print 'n1 = {}, n2 = {}'.format(n1, n2)
        
        if x == n2:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(1)
    