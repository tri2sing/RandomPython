'''
Created on Apr 27, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        if n == 1:
            return [nums]
            
        result = []
        for i in range(n):
            subsets = self.permute(nums[:i] + nums[i + 1:])
            for s in subsets:
                temp = []
                temp.append(nums[i])
                temp.extend(s)
                result.append(temp)
        return result
        
if __name__ == '__main__':
    s = Solution()
    nums = [1, 2]
    result = s.permute(nums)
    print result
    print 128 * '='
    nums = [1, 2, 3]
    result = s.permute(nums)
    print result