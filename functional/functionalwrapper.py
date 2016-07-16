'''
Created on Jul 15, 2016
@author: Sameer Adhikari
'''

# What intrigued me was the use of append method for an instance of this class without directly defining it.
# The __getattr__ function delegates the responsibility of any undefined attribute for this class 
# to the to the class of self.data attribute created in the __init__ method of this class.
# This causes this class to behave like self.data class for any method not defined in this class.
# There will be an error if you call a method for the class, which is undefined for it and selfd.data.

class FunctionalWrapper(object):
    def __init__(self, data):
        self.data = data
    def map(self, function):
        """Call `map` on the items in `data` using the provided `function`"""
        return FunctionalWrapper(map(function, self.data))
    def reduce(self, function):
        """Call `reduce` on the items in `data` using the provided `function`"""
        return reduce(function, self.data)
    def filter(self, function):
        """Call `filter` on the items in `data` using the provided `function`"""
        return FunctionalWrapper(filter(function, self.data))
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)
    def __getattr__(self, name):  return getattr(self.data, name)
    def __getitem__(self, k):  return self.data.__getitem__(k)
    def __repr__(self):  return 'FunctionalWrapper({0})'.format(repr(self.data))
    def __str__(self):  return 'FunctionalWrapper({0})'.format(str(self.data))
    
    
if __name__ == '__main__':
    # Create some data
    mapData = FunctionalWrapper(range(5, 10))
    print 'Type of mapData = {}'.format(type(mapData))
    
    # Define a function to be applied to each element
    f = lambda x: x + 3
    
    # Imperative programming: loop through and create a new object by applying f
    mapResult = FunctionalWrapper([])  # Initialize the result
    print 'Type of mapResult = {}'.format(type(mapResult))

    for element in mapData:
        mapResult.append(f(element))  # Apply f and save the new value
    print 'Result after for loop: {0}'.format(mapResult)
    
    # Functional programming: use map rather than a for loop
    print 'Result from map call: {0}'.format(mapData.map(f))
        
