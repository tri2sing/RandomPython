'''
Created on Apr 14, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:
            return []
        
        if n == 3:
            if sum(nums) == 0:
                return [sorted(nums)]
            else:
                return []
        
        # Sort so that the worst case is O(n^2)
        # and that the output is a <= b <= c
        nums = sorted(nums)
        # using a set to prevent duplicates
        result = set()
        for i in range(n - 3):
            j = i + 1
            k = n - 1
            a = nums[i]
            while j < k:
                b = nums[j]
                c = nums[k]
                if a + b + c == 0:
                    result.add((a, b, c))
                    j += 1
                    k -= 1
                elif a + b + c > 0:
                    k -= 1
                else:
                    j += 1
        answer = []
        for t in result:
            answer.append(list(t))
        return answer
    
if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 0]
    print nums
    print s.threeSum(nums)
    print 64 * '='
    nums = [0, 0, 0, 1]
    print nums
    print s.threeSum(nums) 
    print 64 * '='
    nums = [-1, 0, 1, 2, -1, -4]   
    print nums
    print s.threeSum(nums) 
    print 64 * '='
    