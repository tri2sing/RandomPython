
def insertionsort(a):
    for i in range(1, len(a)):
        v = a[i]
        for j in range(i-1, -1, -1):
            if a[j] <= v:
                a[j + 1] = v
                break
            a[j + 1] = a[j]
        else:
            a[0] = v
    return a


def insertionsortreverse(a):
    end = len(a)-1
    for i in range(end-1, -1, -1):
        v = a[i]
        for j in range(i+1, end+1):
            if v > a[j]:
                a[j-1] = v
                break
            a[j-1] = a[j]
        else:
            a[end] = v
    return a

def reversesortedlist (sortedlist):
    return sortedlist.reverse()

def insertionsortreverse2 (a):
    insertionsort(a)
    reversesortedlist(a)
    return a
    
if __name__ == "__main__":

    print "in-order sort"
    a = [5, 2, 4, 6, 1, 9]
    print a
    insertionsort(a)
    print a
    
    print 'reverse sort'
    a = [10, 11, 12, 13, 14, 15]
    print a
    insertionsortreverse(a)
    print a
    
    print 'second reverse sort'
    a = [5, 2, 4, 6, 1, 9]
    print a
    insertionsortreverse2(a)
    print a
