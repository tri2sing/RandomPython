'''
Created on Apr 17, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num > 1:
            r = num % 4
            print 'working on {}, remainder = {}'.format(num, r)
            if r != 0:
                return False
            num //= 4
        if num == 1:
            return True
        return False
    
if __name__ == '__main__':
    s = Solution()
    num = 16
    print '{} is power of 4 = {}'.format(num, s.isPowerOfFour(num))