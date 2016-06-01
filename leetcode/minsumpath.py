'''
Created on May 10, 2016

@author: Sameer Adhikari
'''
class Solution(object):
    
    def __init__(self):
        self.minsumpath = float('inf')
    
    def minPathSumRecursiveInternal(self, startx, starty, endx, endy, currsum):
        currsum += self.grid[startx][starty]
        
        if currsum > self.minsumpath:
            # Optimization to not pursue a path that is already longer
            currsum -= self.grid[startx][starty]
            return
        
        if startx == endx and starty == endy:
            if currsum < self.minsumpath:
                self.minsumpath = currsum
            return
        
        if startx != endx and starty == endy:
            # If we are on the right most column, only go down
            self.minPathSumRecursiveInternal(startx + 1, starty, endx, endy, currsum)
        elif startx == endx and starty != endy:        
            # If we are on the bottom row, only go right
            self.minPathSumRecursiveInternal(startx, starty + 1, endx, endy, currsum)
        else:
            # Else go down and go right
            self.minPathSumRecursiveInternal(startx + 1, starty, endx, endy, currsum)
            self.minPathSumRecursiveInternal(startx, starty + 1, endx, endy, currsum)
        
        # Backtrack from the path below as we have explored it
        currsum -= self.grid[startx][starty]
        
        
    def minPathSumRecursive(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        self.grid = grid
        self.minPathSumRecursiveInternal(0, 0, rows - 1, cols - 1, 0)
        temp = self.minsumpath
        # reset before this function gets called again
        self.minsumpath = float('inf')
        return temp

    def minPathSumDynamic(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        minsums = [[0 for _ in range(cols)] for _ in range(rows)]
        minsums[0][0] = grid[0][0]
        # Only one path exists to any cell along the top row and left col
        for j in range(1, cols):
            minsums[0][j] = minsums[0][j - 1] + grid[0][j] # Top row
        for i in range(1, rows):
            minsums[i][0] = minsums[i - 1][0] + grid[i][0] # Left col

        # fill up the rest of the matrix
        for i in range(1, rows):
            for j in range(1, cols):
                minsums[i][j] = grid[i][j] + min(minsums[i][j - 1], minsums[i - 1][j])
        return minsums[rows - 1][cols - 1]  
          
if __name__ == '__main__':
    s = Solution()
#     grid = [[0]]
#     print s.minPathSumRecursive(grid)
    print 64 * '='
    grid = [[1,2],[1,1]]
    print s.minPathSumRecursive(grid)
    print s.minPathSumDynamic(grid)

    print 64 * '='
    grid =  [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
    print s.minPathSumRecursive(grid)
    print s.minPathSumDynamic(grid)
    print 64 * '='
    
    grid =  [
            [7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
            [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
            [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
            [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
            [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
            [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
            [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
            [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
            [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
            [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
            [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
            [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]
            ]
    