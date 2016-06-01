xdim = 4
ydim = 3
zdim = 2

myarray = [[0 for y in range(ydim)] for x in range(xdim)]

v = 0
for i in range(xdim):
    for j in range(ydim):
        myarray[i][j] = v
        v += 1

for row in myarray:
    print row
print '\n'

transpose = [[row[i] for row in myarray] for i in range(ydim)]

for row in transpose:
    print row
print '\n'

my3Darray = [[[0 for z in range(zdim)] for y in range(ydim)] for x in range(xdim)]

v = 0
for i in range(xdim):
    for j in range(ydim):
        for k in range(zdim):
            my3Darray[i][j][k] = v
            v += 1

for i in range(xdim):
    for j in range(ydim):
        for k in range(zdim):
            print '(%d,%d,%d) = %d' % (i, j, k, my3Darray[i][j][k])
