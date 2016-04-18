'''
Created on Apr 16, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ugly = set([2, 3, 5])
        divisors = set()
        # Check the different prime numbers starting at 2
        i = 2
        while i <= abs(num//i):
            while num % i == 0:
                divisors.add(i)
                num //= i
            i += 1
        
        # If num itself is prime
        if num != 1:
            divisors.add(num)
        
        if divisors.issubset(ugly):
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    n = 214797179
    print 'n = {}.  Q. Is Ugly? A. {}'.format(n, s.isUgly(n))
    n = -2147483648
    print 'n = {}.  Q. Is Ugly? A. {}'.format(n, s.isUgly(n))
    n = 937351770
    print 'n = {}.  Q. Is Ugly? A. {}'.format(n, s.isUgly(n))
    n = 4
    print 'n = {}.  Q. Is Ugly? A. {}'.format(n, s.isUgly(n))
