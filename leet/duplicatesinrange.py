'''
Created on Apr 20, 2016

@author: Sameer Adhikari
'''

from collections import defaultdict

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tracker = defaultdict(list)
        n = len(nums)
        # track the locations for a number
        for i in range(n):
            tracker[nums[i]].append(i)
        print tracker
        for _, locations in tracker.iteritems():
            numlocs = len(locations)
            if numlocs == 1:
                continue
            # pair-wise comparison of indices
            for i in range(numlocs - 1):
                for j in range(i + 1, numlocs):
                    print 'i = {}, j = {}'.format(i, j)
                    if abs(locations[i] - locations[j]) <= k:
                        return True
        return False  
        
if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1]
    k = 0
    result = s.containsNearbyDuplicate(nums, k)
    print 'result = {}, k = {}, nums = {}'.format(result, k, nums)
    
    nums = [1, 0, 1, 1]
    k = 0
    result = s.containsNearbyDuplicate(nums, k)
    print 'result = {}, k = {}, nums = {}'.format(result, k, nums)
