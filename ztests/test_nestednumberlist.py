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
        nstd_num_list.recursive_max([2, 9, [1, 13], 'a', 6])
    
def test_recursive_min(nstd_num_list):
    assert(nstd_num_list.recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    assert(nstd_num_list.recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    assert(nstd_num_list.recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    assert(nstd_num_list.recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)
    with pytest.raises(TypeError):
        nstd_num_list.recursive_min([2, 9, [1, 13], 'a', 6])
            
def test_recursive_target_count(nstd_num_list):
    assert(nstd_num_list.recursive_target_count(2, []) == 0)
    assert(nstd_num_list.recursive_target_count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    assert(nstd_num_list.recursive_target_count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    assert(nstd_num_list.recursive_target_count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    assert(nstd_num_list.recursive_target_count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    assert(nstd_num_list.recursive_target_count("a",
         [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)

def test_recursive_flatten(nstd_num_list):    
    assert(nstd_num_list.recursive_flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
    assert(nstd_num_list.recursive_flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
    assert(nstd_num_list.recursive_flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
    assert(nstd_num_list.recursive_flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) == ["this","a","thing","a","is","a","easy"])
    assert(nstd_num_list.recursive_flatten([]) == [])
    
    