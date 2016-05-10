'''
Created on May 9, 2016

@author: Sameer Adhikari
'''

from collections import defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type key: int
        :rtype: List[int]
        """
        
        # Frequency count for each object
        histogram = defaultdict(int)
        for item in nums:
            histogram[item] += 1
        heapinput = [(val, key) for key, val in histogram.iteritems()]
        topk = heapq.nlargest(k, heapinput, key=lambda x: x[0])
        return [x[1] for x in topk]
        
if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    key = 2
    s = Solution()
    print s.topKFrequent(nums, key)
        
            
        
