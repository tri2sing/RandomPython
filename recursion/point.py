'''
Created on Jul 16, 2016

@author: Sameer Adhikari
'''

class Point(object):
    """
    Class that represents a two dimensional point.
    """
    def __init__(self, x=0.0, y=0.0):
        """
        Create a point, with a default at origin.
        Args:
            x (float): x-axis coordinate for the point.
            y (float): y-axis coordinate for the point.
        """
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            raise TypeError('Argument is not of type Point')
        return self.x == other.x and self.y == other.y
        
    def mid_point(self, other):
        if not isinstance(other, Point):
            raise TypeError('Argument is not of type Point')
        return Point((self.x + other.x)/2, (self.y + other.y)/2)
            