'''
Created on Apr 22, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = len(nums)
        start = 0
        end = n - 1
        mididx = None
        while start <= end:
            mididx = (start + end)//2
            print 'start = {}, end  {}, middle = {}'.format(start, end, mididx)
            midnum = nums[mididx]
            if midnum == target:
                return mididx
            elif midnum > target:
                end = mididx - 1
            else: # midnum < target
                start = mididx + 1
                
        if end < 0:
            return 0
        if start > n - 1:
            return n
        if target > nums[mididx]:
            return mididx + 1
        else:
            return mididx
        
if __name__ == '__main__':
    s = Solution()
    nums = [1,3,5,6]
    #print s.searchInsert(nums, 5)
    print s.searchInsert(nums, 2)
    #print s.searchInsert(nums, 7)
    #print s.searchInsert(nums, 0)
    nums = [1,3]
    print s.searchInsert(nums, 2)
