'''
Created on Apr 8, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = len(nums)
        # Store the product of the terms to left of i
        left = [1] * count
        temp = 1
        for i in range(count):
            left[i] = temp
            temp *= nums[i]
        
        print left
        
        # Store the product of the terms to the right of i
        right = [1] * count
        temp = 1
        for i in range(count - 1, -1, -1):
            right[i] = temp
            temp *= nums[i]
        
        print right
        
        # Calculate the final product of the left and right terms
        product = [1] * count
        for i in range(count):
            product[i] = left[i] * right[i]
        
        return product
    
