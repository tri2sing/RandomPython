'''
Created on May 9, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def __init__(self, num_nodes):
        # result[i] = j => a queen is placed at row i, column j.
        self.N = num_nodes
        self.result = [-1] * num_nodes
        
    def safePlace(self, row, col):
        '''Check if it is possible to place queen at (row, col) '''
        # for two queens at (x1, y1), and (x2, y2)
        # x1 == x2 => same row, y1 == y2 => same column, 
        # |x1 - x2| == |y1 - y2| => same diagonal.
        for i in range(row):
            if self.result[i] == col or abs(i - row) == abs(self.result[i] - col):
                return False
        return True
    
    def arrangeQueenInRow(self, row):
        if row == self.N:
            # We have found a valid result
            print self.result
            return
        for col in range(self.N):
            if self.safePlace(row, col):
                # Place the queen at this location.
                self.result[row] = col
                # Check the next row.
                self.arrangeQueenInRow(row + 1)
                # Backtrack if at any row later 
                # we did not find a solution, 
                # or if we did find a solution.
                self.result[row] = -1
        
        
if __name__ == '__main__':
    num_nodes = 4
    s = Solution(num_nodes)
    s.arrangeQueenInRow(0)
    print 64 * '*'
    num_nodes = 5
    s = Solution(num_nodes)
    s.arrangeQueenInRow(0)
    print 64 * '*'
    num_nodes = 6
    s = Solution(num_nodes)
    s.arrangeQueenInRow(0)
    print 64 * '*'
    num_nodes = 7
    s = Solution(num_nodes)
    s.arrangeQueenInRow(0)
        