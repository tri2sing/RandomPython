'''
Created on May 20, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    _isdead = 0
    _islive = 1
    _tobelive = 2 # Cell about to become live
    _tobedead = 3 # Cell about to die
    
    def neighbors(self, x, y):
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i < 0 or i > self.rows - 1:
                    continue
                if j < 0 or j > self.cols - 1:
                    continue
                if i == x and j == y:
                    continue
                yield i, j
    
    def nextState(self, board, x, y):
        live_neighbors = 0
        for nx, ny in self.neighbors(x, y):
            if board[nx][ny] == Solution._islive or board[nx][ny] == Solution._tobedead:
                live_neighbors += 1

        curr_state = board[x][y]
        if curr_state == Solution._isdead and live_neighbors == 3:
            board[x][y] = Solution._tobelive
            return
        if curr_state == Solution._islive:
            if live_neighbors < 2:
                board[x][y] = Solution._tobedead
            elif live_neighbors > 3:
                board[x][y] = Solution._tobedead
        return        
                
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        self.rows = len(board)
        self.cols = len(board[0])
        for i in range(self.rows):
            for j in range(self.cols):
                self.nextState(board, i, j)
        
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == Solution._tobelive:
                    board[i][j] = Solution._islive
                if board[i][j] == Solution._tobedead:
                    board[i][j] = Solution._isdead
                    
                                        
if __name__ == '__main__':
    s = Solution()

    board = [[0, 0]]
    print 'Input = ' ,board
    s.gameOfLife(board)
    print 'Output = ', board
    print 128 * '='

    board = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    print 'Input = ' ,board
    s.gameOfLife(board)
    print 'Output = ', board
    print 128 * '='
    
    board = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    print 'Input = ' ,board
    s.gameOfLife(board)
    print 'Output = ', board
    print 128 * '='
    
    