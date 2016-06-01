'''
Created on Apr 12, 2016

@author: Sameer Adhikari
'''


from collections import deque

class Solution(object):
    
    def neighborLocations(self, i, j, rows, cols):
        if i - 1 >= 0: # N
            yield i - 1, j
        #if i - 1 >= 0 and j - 1 >= 0: # NW
        #    yield i - 1, j - 1
        if j - 1 >= 0: # W
            yield i, j - 1
        #if i + 1 < rows and j - 1 >= 0: # SW
        #    yield i + 1, j - 1
        if i + 1 < rows: # S
            yield i + 1, j
        #if i + 1 < rows and j + 1 < cols: # SE
            #yield i + 1, j + 1
        if j + 1 < cols: # E
            yield i, j + 1
        #if i - 1 >= 0 and j + 1 < cols: # NE
            #yield i - 1, j + 1
        return

    def visitIsland(self, i, j, rows, cols, grid, visited):
        # Perform a BFS traversal
        q = deque() # For efficient removal of front element
        q.append((i, j))
        visited[i][j] = True
        while q:
            cx, cy = q.popleft()
            for nx, ny in self.neighborLocations(cx, cy, rows, cols):
                if grid[nx][ny] == '1' and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
        

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        # Number of connected connected components
        components = 0
        rows = len(grid)
        cols = len(grid[0])
        print 'rows = ', rows, ' cols = ', cols
        # Initially none of the cells have been visited
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        print visited
        # Traverse the matrix looking for islands
        for i in range(rows):
            for j in range (cols):
                print 'grid[{}][{}] = {}'.format(i, j, grid[i][j])
                if grid[i][j] == '1' and not visited[i][j]:
                    print 'in island starting at grid[{}][{}] = {}'.format(i, j, grid[i][j])
                    components += 1
                    # Visit all nodes in this island
                    self.visitIsland(i, j, rows, cols, grid, visited)
                    
        return components
        

if __name__ == '__main__':
    s = Solution()
    grid = ["010","101","010"]
    print s.numIslands(grid)
    
    
    
    