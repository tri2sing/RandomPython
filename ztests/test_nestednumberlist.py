'''
Created on Jul 11, 2016

@author: Sameer Adhikari
'''

from pytest import raises
from recursion.nestednumberlist import NestedNumberList

def test_recursive_sum():
    nlist = NestedNumberList()
    assert(nlist.recursive_sum([2, 9, [1, 13], 8, 6]) == 39)
    assert(nlist.recursive_sum([2, [[100, 7], 90], [1, 13], 8, 6]) == 227)
    # Check if a call with incompatible type raises execption
    with raises(TypeError):
        nlist.recursive_sum([2, 9, [1, 13], 'a', 6])