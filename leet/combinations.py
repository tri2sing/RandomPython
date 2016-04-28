'''
Created on Apr 28, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def combineInternal(self, lst, k):
        if k == 0:
            return [[]]
        
        result = []    
        for i, x in enumerate(lst):
            subcombs = self.combineInternal(lst[i + 1:], k - 1)
            for comb in subcombs:
                temp = []
                temp.append(x)
                temp.extend(comb)
                result.append(temp)
        return result
            
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combineInternal([i for i in range(1, n + 1)], k)

if __name__ == '__main__':
    s = Solution()
    n, k = 5, 3
    print s.combine(n, k)