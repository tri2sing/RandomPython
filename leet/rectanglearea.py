'''
Created on Apr 20, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    
    def checkNoOverlap(self, A, B, C, D, num_edges, F, G, H):
        # If one rectangle is to the left of the other
        if num_edges >= C or A >= G:
            return True
        # If one rectange is above the other
        if F >= D or B >= H:
            return True
        return False
    
    def checkContains(self, A, B, C, D, num_edges, F, G, H):
        if num_edges < A and F < B and C < G and D < H:
            return True
        if A <= num_edges and B <= F and G <= C and H <= D:
            return True
        return False
        
    def computeArea(self, A, B, C, D, num_edges, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type num_edges: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C - A) * (D - B) 
        area2 = (G - num_edges) * (H - F)
        if self.checkContains( A, B, C, D, num_edges, F, G, H):
            print "Found containment"
            if area1 >= area2:
                return area1
            else:
                return area2
        if self.checkNoOverlap(A, B, C, D, num_edges, F, G, H):
            print "Found no overlap"
            return area1 + area2
        # If overlap
    
if __name__ == '__main__':
    s = Solution()
    print s.computeArea(-2, -2, 2, 2, 1, 1, 3, 3)