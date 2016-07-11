'''
Created on Jul 11, 2016

@author: Sameer Adhikari
'''

import pytest

from recursion.nestednumberlist import NestedNumberList

@pytest.fixture(scope='module')
def nstd_num_list():
    return NestedNumberList()

def test_recursive_sum(nstd_num_list):
    assert(nstd_num_list.recursive_sum([2, 9, [1, 13], 8, 6]) == 39)
    assert(nstd_num_list.recursive_sum([2, [[100, 7], 90], [1, 13], 8, 6]) == 227)
    # Check if a call with incompatible type raises exception
    with pytest.raises(TypeError):
        nstd_num_list.recursive_sum([2, 9, [1, 13], 'a', 6])

def test_recursive_max(nstd_num_list):
    assert(nstd_num_list.recursive_max([2, 9, [1, 13], 8, 6]) == 13)
    assert(nstd_num_list.recursive_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
    assert(nstd_num_list.recursive_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)    
    # Check if a call with incompatible type raises exception
    with pytest.raises(TypeError):
        nstd_num_list.recursive_sum([2, 9, [1, 13], 'a', 6])
    