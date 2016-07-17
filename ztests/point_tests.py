'''
Created on Jul 16, 2016

@author: Sameer Adhikari
'''

from recursion.point import Point

def test_eq():
    p1 = Point(1, 1)
    p2 = Point(1, 1)
    p3 = Point(2, 2)
    assert(p1 == p2)
    assert(p1 != p3)
    
def test_mid_point():
    p1 = Point()
    p2 = Point(1, 1)
    p3 = Point(2, 2)
    assert(p2 == p1.mid_point(p3))