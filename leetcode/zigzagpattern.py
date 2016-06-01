'''
Created on Apr 13, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ''
        if numRows == 1:
            return s
        size = len(s)
        if numRows > size:
            return s
            
        # Layout the 0...n-1 indices of input string as desired for zigzag output.
        # You will see that each row consists of terms which have a gap pattern.
        # We works with a list as strings are immutable
        result = []
        for i in range(numRows):
            result.append(s[i])
            gap1 = 2 * (numRows -1 - i)
            gap2 = 2 * i
            j = i
            while j < size:
                if gap1 != 0 and j + gap1 < size:
                    result.append(s[j + gap1])
                if gap2 != 0 and j + gap1 + gap2 < size:
                    result.append(s[j + gap1 + gap2])
                j += gap1 + gap2 # Technically gap1 + gap2 = 2 * (numRows - 1)
        return ''.join(result)        

if __name__ == '__main__':
    s = Solution()
    print s.convert('A', 1)
    print s.convert('AB', 1)
    print s.convert('A', 2)
    print s.convert('helloiamsamandiamnewhere', 4)
