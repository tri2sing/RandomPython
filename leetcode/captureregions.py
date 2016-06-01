'''
Created on Apr 13, 2016

@author: Sameer Adhikari
'''

from collections import deque

class Solution(object):
    
    def on_boundary(self, x, y, numrows, numcols):
        if x == 0 or y == 0 or x == numrows - 1 or y == numcols - 1:
            return True
        else:
            return False

    def get_neighbors(self, x, y, numrows, numcols):
        if x > 0: # N
            yield x - 1, y
        if y > 0: # W
            yield x, y - 1
        if x < numrows - 1: # S
            yield x + 1, y
        if y < numcols - 1: #E
            yield x, y + 1
            
    def explore_region(self, regionid, startx, starty, numrows, numcols, board, visited, captureset, capturemap):
        # Start with assumption that reqion can be captured
        cancapture = True
        tempset = set()
        queue = deque()
        tempset.add((startx, starty))
        if self.on_boundary(startx, starty, numrows, numcols):
            cancapture = False
        queue.append((startx, starty))
        visited[startx][starty] = True
        while queue:
            currx, curry = queue.popleft()
            for nx, ny in self.get_neighbors(currx, curry, numrows, numcols):
                if not visited[nx][ny] and board[nx][ny] == 'O':
                    tempset.add((nx, ny))
                    if self.on_boundary(nx, ny, numrows, numcols):
                        cancapture = False
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        if cancapture:
            captureset.add(regionid)
            capturemap[regionid] = tempset
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        
        rows = len(board) # Number of items in the external list
        cols = len(board[0]) # Number of items in an internal list
        # Intialize all locations to not visited 
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        # The number of regions with Os
        numregions = 0
        # Set to store ids of regions that can be captured
        captureset = set()
        # Map to store members of regions that can be captured
        capturemap = {}

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and board[i][j] == 'O':
                    # This is a region we are interested in exploring
                    self.explore_region(numregions, i, j, rows, cols, board, visited, captureset, capturemap)
                    numregions += 1
        
        for regid in captureset:
            for x, y in capturemap[regid]:
                # Leetcode requires: 
                # board[x] = board[x][:y] + ['X'] + board[x][y + 1:]
                # My Python 2.7 requires:
                board[x] = board[x][:y] + 'X' + board[x][y + 1:]
        
        return
        
if __name__ == '__main__':
    s = Solution()
    board = ['X']
    print board
    s.solve(board)
    print board        
    board = ["XXX","XOX","XXX"]
    print board        
    s.solve(board)
    print board        
    board = ['XXXX', 'XOOX', 'XXOX', 'XOXX']
    print board        
    s.solve(board)
    print board        
    
    