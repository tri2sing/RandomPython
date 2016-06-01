'''
Created on Apr 10, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if not version1 and not version2:
            return 0
        
        if version1 and not version2:
            return 1
        
        if not version1 and version2:
            return -1
            
        # If we are here means both strings are non-empty
        v1 = [int(i) for i in version1.split('.')]
        n1 = len(v1)
        # Remove meaningless zeroes at the end
        while n1 > 0 and v1[n1 - 1] == 0:
            v1.pop()
            n1 -= 1 
        v2 = [int(i) for i in version2.split('.')]
        n2 = len(v2)
        while n2 > 0 and v2[n2 - 1] == 0:
            v2.pop()
            n2 -= 1 
        
        i = 0
        while i < n1 and i < n2:
            if v1[i] > v2[i]:
                return 1
            if v1[i] < v2[i]:
                return -1
            i += 1
        
        # If we are here mean we have exhauseted one string 
        # and both of them have been equal so far.
        if i < n1 and i == n2:
            return 1
            
        if i == n1 and i < n2:
            return -1
        
        return 0
        
if __name__ == '__main__':
    s = Solution()
    print s.compareVersion('1.0', '1')
    print s.compareVersion('0', '1')
    print s.compareVersion('1', '0')
        
        
