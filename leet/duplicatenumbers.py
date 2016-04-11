'''
Created on Apr 10, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tracker = 0
        for num in nums:
            mask = 2 ** (num - 1)
            if not (mask & tracker):
                # First time we are seeing the number
                tracker |= mask
            else:
                return num
        return None
    

if __name__ == '__main__':
    s = Solution()
    print s.findDuplicate([1, 2, 3, 4, 5, 1])
    print s.findDuplicate([1, 2, 2, 3, 4, 5])
    print s.findDuplicate([1, 2, 3, 4, 5, 3])
    print s.findDuplicate([1, 4, 2, 3, 4, 5])
    print s.findDuplicate([5, 4, 2, 3, 1, 5])
