import operator
import functools


def iterativedivide (inarray):
    '''
    Returns: array where each element i is the product of all the terms except i in the input array.
    '''
    prod = 1
    outarray = []

    # The variable prod contains the product of elements to the left of element i 
    # We insert the partial product into position i in the output   
    for i in range (len(inarray)):
        outarray.append(prod)
        prod *= inarray[i]
        
    prod = 1
    # The variable prod contains the product of elements to the right of element i
    # We multiply prod with the existing partial sum    
    for i in range (len(inarray) - 1, -1, -1):
        outarray[i] *= prod
        prod *= inarray[i]
    
    return outarray

def functionaldivide(inarray):
    '''
    '''
    prodall = functools.reduce(operator.mul, inarray, 1)
    outarray = [prodall/x for x in inarray]
    return outarray
    
    
if __name__ == '__main__':
    
    inarr = [1, 2, 3, 4, 5]
    print 'Input = ', inarr
    print 'Output iterative = ', iterativedivide (inarr)
    print 'Output functional = ', functionaldivide (inarr)
    
