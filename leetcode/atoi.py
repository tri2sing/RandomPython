'''
Created on Apr 10, 2016

@author: Sameer Adhikari
'''

from string import digits, letters, whitespace

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        multiplier = 1
        ans = 0
        n = len(str)
        for i in range(n):
            c = str[i]
            if c in whitespace:
                if i != 0 and str[i - 1] in digits:
                    break;
                else:
                    continue
            if c in letters:
                break
            if c == '+':
                if (i == n - 1) or str[i + 1] not in digits:
                    ans = 0
                    break;
                else:
                    multipler = 1
                    continue
            if c == '-':
                if (i == n - 1) or str[i + 1] not in digits:
                    ans = 0
                    break;
                else:
                    multiplier = -1
                    continue
            ans = 10 * ans + int(c)
        ans *= multiplier
        return ans

if __name__ == '__main__':
    s = Solution()
    # print s.myAtoi('  010   ')
    print s.myAtoi(' +0 123')
    
