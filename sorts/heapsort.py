import heapq

def heapsort (lst):
    result = []
    heapq.heapify(lst)
    print 'After heapify: ' + str(lst)
    while lst:
        result.append(heapq.heappop(lst))
    return result

def myheapifylargest (lst, index):
    left = 2*index + 1
    right = 2*index + 2
    last = len(lst) - 1
    if left <= last and lst[index] < lst [left]:
        largest = left
    else:
        largest = index
    if right <= last and lst[right] > lst[largest]:
        largest = right 
    if largest != index and largest <= last:
        temp = lst[largest]
        lst[largest] = lst[index]
        lst[index] = temp
        myheapifylargest (lst, largest)   

def mybuildheaplargest (lst):
    for i in range(len(lst)//2, -1, -1):
        myheapifylargest (lst, i)

def myheapsortdescending (lst):
    result = []
    mybuildheaplargest(lst)
    length = len(lst)
    while length > 0:
        result.append(lst.pop(0))
        myheapifylargest (lst, 0)
        length -= 1
    return result
    
def myheapifysmallest (lst, index):
    left = 2*index + 1
    right = 2*index + 2
    last = len(lst) - 1
    if left <= last and lst[index] < lst [left]:
        smallest = index
    else:
        smallest = left
    if right <= last and lst[right] < lst[smallest]:
        smallest = right 
    if smallest != index and smallest <= last:
        temp = lst[smallest]
        lst[smallest] = lst[index]
        lst[index] = temp
        myheapifysmallest (lst, smallest)   

def mybuildheapsmallest (lst):
    for i in range(len(lst)//2, -1, -1):
        myheapifysmallest (lst, i)

    

if __name__ == "__main__":
    lst = [10, 9, 8, 7, 1, 5, 6, 3, 2, 4]
    print 'Initial list: ' + str(lst)
    lst = heapsort (lst)
    print 'After sort' + str(lst)

    print('\n')
    lst = [10, 9, 8, 7, 1, 5, 6, 3, 2, 4]
    print 'Initial list: ' + str(lst)
    mybuildheaplargest(lst)
    print 'After my heapify largest: ' + str(lst)
    lst = [10, 9, 8, 7, 1, 5, 6, 3, 2, 4]
    lst = myheapsortdescending (lst)
    print 'after descending sort ' + str(lst)
    
    print('\n')
    lst = [10, 9, 8, 7, 1, 5, 6, 3, 2, 4]
    print 'Initial list: ' + str(lst)
    mybuildheapsmallest(lst)
    print 'After my heapify smallest: ' + str(lst)
