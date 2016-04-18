'''
Created on Apr 14, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        tracker = {}
        n = len(nums)
        for i in range(n):
            # Store the location of the elements in a map
            tracker[nums[i]] = i
        print tracker
        for i in range(n):
            num = nums[i]
            diff = target - num
            print 'num = {} at {}, diff = {} at {}'.format(num, i, diff, tracker[diff])
            if diff in tracker and i != tracker[diff]:
                return [i, tracker[diff]]
        return []
        
if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 4]
    target = 6
    print nums
    print s.twoSum(nums, target)
