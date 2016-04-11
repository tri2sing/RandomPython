'''
Created on Apr 10, 2016

@author: Sameer Adhikari
'''

from string import uppercase
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        answer = ''
        while n:
            r = (n - 1) % 26
            answer = uppercase[r] + answer
            n = (n - r) / 26
        return answer
        
        
if __name__ == '__main__':
    s = Solution()
    print s.convertToTitle(1)
    print s.convertToTitle(27)
    print s.convertToTitle(5)
    print s.convertToTitle(100)
    print s.convertToTitle(104)
    print s.convertToTitle(26)
    print s.convertToTitle(52)

