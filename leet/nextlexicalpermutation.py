'''
Created on Apr 25, 2016

@author: Sameer Adhikari
'''

# https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
# 

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or n == 1:
            return
        # Find the longest non-increasing suffix from end.
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            # The suffix is already the maximal permutation.
            # Do an in place sort to the minimal permutation.
            j = n - 1
            while i < j:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i += 1
                j -= 1
            return
            
        # a[i - 1] is the pivot; it is less than left-most 
        # element of the suffix.
        # Find the right-most element greater than the pivot.
        j = n - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
            
        # Swap the pivot with the greater element
        temp = nums[j]
        nums[j] = nums[i - 1]
        nums[i - 1] = temp
        
        # Reverse the suffix
        j = n - 1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
        
        return
        
if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1]
    print 'Before = {}'.format(nums)
    s.nextPermutation(nums)   
    print 'After = {}'.format(nums)
    
    
    