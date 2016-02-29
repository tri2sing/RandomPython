'''
Created on Feb 28, 2016

@author: Sameer Adhikari
'''

'''
Given a MxN array in the form of list of lists.
array[x][y] == 1 => can step in the cell.
array[x][y] == 0 => cannot step in the cell.
Starting point is array[0][0].
Ending point is array[M-1][N-1].
Only movement is either right or down.
Find all paths from start to end.
There may not be any path.
'''

array1 = [
         [1, 1, 1],
         [1, 1, 1]
         ]

array2 = [
         [1, 1, 0, 1],
         [0, 1, 1, 0],
         [1, 0, 1, 1]
         ]
array3 = [
          [1, 0],
          [0, 1]
          ]

def traverse(array, xs, ys, xd, yd):
    '''
    xs: x coordinate of source.
    ys: y coordinate of source.
    xd: x coordinate of destination.
    yd: y coordinate of destination.
    '''
    
    # If we cannot step onto this cell
    if array[xs][ys] == 0: 
        return None
     
    # If we are at the destination
    if xs == xd and ys == yd:
        return [[(xs, ys)]]
        
    # If this is the rightpaths-most column, then we can only travel downpaths.
    if ys == yd and xs != xd:
        downpaths = traverse(array, xs + 1, ys, xd, yd)
        rightpaths = None
        
        
    # If this is the bottom row, then we can only travel rightpaths.
    if xs == xd and ys != yd:
        rightpaths = traverse(array, xs, ys + 1, xd, yd)
        downpaths = None
        
    # If this is neither the rightpaths-most columan, nor the bottom Row
    if xs != xd and ys != yd:
        downpaths = traverse(array, xs + 1, ys, xd, yd)
        rightpaths = traverse(array, xs, ys + 1, xd, yd)

    paths = []
    if downpaths:
        for item in downpaths:
            path = []
            path.append((xs, ys))
            path.extend(item)
            paths.append(path)
            
    if rightpaths:
        for item in rightpaths:
            path = []
            path.append((xs, ys))
            path.extend(item)
            paths.append(path)
    
    return paths

if __name__ == '__main__':

    print '=' * 64
    
    print 'Array 1', array1
    paths = traverse(array1, 0, 0, len(array1) - 1, len(array1[0]) - 1)
    print 'Number of paths for array 1 = ', len(paths)
    print 'The paths are: '
    for item in paths:
        print item
    print '=' * 64
    
    print 'Array 2', array2
    paths =  traverse(array2, 0, 0, len(array2) - 1, len(array2[0]) - 1)
    print 'Number of paths for array 2 = ', len(paths)
    print 'The paths are: '
    for item in paths:
        print item
    print '=' * 64
    
    print 'Array 3', array3
    paths =  traverse(array3, 0, 0, len(array3) - 1, len(array3[0]) - 1)
    print 'Number of paths for array 3 = ', len(paths)
    print 'The paths are: '
    for item in paths:
        print item
    print '=' * 64
    
            