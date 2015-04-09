from random import randrange

def quicksort(lst):
    if lst == []:
        return []
    else:
        pivot = lst.pop(randrange(len(lst)))
        lesser = quicksort([x for x in lst if x < pivot])
        greater = quicksort([x for x in lst if x >= pivot])
        return lesser + [pivot] + greater
   
if __name__ == '__main__':
    
    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
    print 'Input = ', str(lst)
    lst = quicksort (lst)
    print 'Output = ',  str(lst)
