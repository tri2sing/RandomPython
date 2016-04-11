'''
Created on Apr 10, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if k == 0:
            return
        n = len(nums)
        if k == n:
            return
        if k > n:
            k %= n
            
        temp = [1] * k
        for i in range(n - k, n):
            temp[i - n + k] = nums[i]
        print temp
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]
        print nums
        for i in range(k):
            nums[i] = temp[i]
        print nums
            
if __name__ == '__main__':
    s = Solution()
    k = 3
    nums = [-1, -100, 3, 99]
    print k, nums
    s.rotate(nums, k)
    print nums
    