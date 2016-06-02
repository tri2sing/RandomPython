'''
Created on Jun 2, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def __init__(self, N, B):
        self.num = N
        self.array = B
    
    def distribute(self, start, end, total):
        if start == end - 1:
            if self.array[start]%2 == 0 and self.array[end]%2 == 0:
                return total
            elif self.array[start]%2 != 0 and self.array[end]%2 != 0:
                return total + 2
            elif self.array[start]%2 == 0 and self.array[end]%2 != 0:
                return -1
            elif self.array[start]%2 != 0 and self.array[end]%2 == 0:
                return -1
            else:
                print 'case e'
                return -1
        else:    
            if self.array[start]%2 == 0:
                return self.distribute(start + 1, end, total)
            else:
                self.array[start] += 1
                self.array[start + 1] += 1
                return self.distribute(start + 1, end, total + 2)


if __name__ == '__main__':
    N = 5
    B = [2, 3, 4, 5, 6]
    s = Solution(N, B)
    result = s.distribute(0, N - 1, 0)
    if result == -1:
        print 'NO'
    else:
        print result
    
    N = 2
    B = [1, 2]
    s = Solution(N, B)
    result = s.distribute(0, N - 1, 0)
    if result == -1:
        print 'NO'
    else:
        print result


