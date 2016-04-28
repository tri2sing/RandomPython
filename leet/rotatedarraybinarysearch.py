'''
Created on Apr 28, 2016

@author: Sameer Adhikari
'''
class Solution(object):
    
    def findMinInternal(self, nums, start, end):
        print 'start = {}, end = {}'.format(start, end)
        if start >= end:
            return nums[start]
        mid = (start + end)//2
        if nums[mid] > nums[end]:
            # minimum lies to the right
            return self.findMinInternal(nums, mid + 1, end)
        else:
            # minimum lies to the left
            return self.findMinInternal(nums, start, mid)
    
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.findMinInternal (nums, 0, n - 1)
            

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2]
    print 'min = {}'.format(s.findMin(nums))
    nums = [2, 1]
    print 'min = {}'.format(s.findMin(nums))
    nums = [3, 1, 2]
    print 'min = {}'.format(s.findMin(nums))