'''
Created on Apr 29, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    
    # provided values to represent colors
    RED = 0
    WHITE = 1
    BLUE = 2
    
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if n == 0 or n == 1:
            return
        
        i, red, blue = 0, 0, n - 1
        while i <= blue:
            if nums[i] == Solution.RED:
                temp = nums[red]
                nums[red] = nums[i]
                nums[i] = temp
                red += 1
                i += 1
            elif nums[i] == Solution.BLUE:
                temp = nums[blue]
                nums[blue] = nums[i]
                nums[i] = temp
                blue -= 1
            else:
                i += 1
        return
    
if __name__ == '__main__':
    s = Solution()
#     nums = [2, 2, 2, 0, 0, 0, 1, 1, 1]
#     print 'before = ', nums
#     s.sortColors(nums)
#     print 'after = ', nums
#     nums = [0, 1, 2, 0, 1, 2, 0, 1, 2]
#     print 'before = ', nums
#     s.sortColors(nums)
#     print 'after = ', nums
    nums = [1, 2, 0]
    print 'before = ', nums
    s.sortColors(nums)
    print 'after = ', nums