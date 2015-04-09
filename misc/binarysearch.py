'''
Created on Apr 9, 2015

@author: Sameer Adhikari
'''

# Input: Sorted array, value to find, starting and ending points of search in array
# Output: Index in array if element exists or -1 if it does not

def binarysearch (inArray, target, low, high):

    if low > high: return -1
    mid = (low + high)//2
    
    if inArray[mid] < target: return binarysearch (inArray, target, mid+1, high)
    elif inArray[mid] > target: return binarysearch (inArray, target, low, mid-1)
    else: return mid
 
    
print binarysearch([1, 2, 3, 4, 5], 3, 0, 4)
print binarysearch([1, 2, 3, 4, 5, 6, 7, 8], 9, 0, 7)    
print binarysearch([1, 2, 3, 4, 5, 6, 7, 8], 1, 0, 7)    
    