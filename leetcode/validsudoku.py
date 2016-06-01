'''
Created on May 18, 2016

@author: Sameer Adhikari
'''

from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
            
        ref = set((str(i) for i in range(1, 10)))
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        nrows = len(board)
        ncols = len(board[0])
        
        for i in range(nrows):
            for j in range(ncols):
                num = board[i][j]
                if num == '.':
                    continue
                if num not in ref:
                    return False
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)
                if num in cols[j]:
                    return False
                else:
                    cols[j].add(num)
                x, y = i//3, j//3
                if num in boxes[(x, y)]:
                    return False
                else:
                    boxes[(x, y)].add(num)
        
        return True
        
if __name__ == '__main__':
    board = [
            ".87654321",
            "2........",
            "3........",
            "4........",
            "5........",
            "6........",
            "7........",
            "8........",
            "9........"
            ]
    s = Solution()
    print s.isValidSudoku(board)
    
    board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
    print s.isValidSudoku(board)
    
        
        