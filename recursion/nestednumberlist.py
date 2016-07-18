'''
Created on Jul 11, 2016

@author: Sameer Adhikari
'''

import numbers

class NestedNumberList(object):
    def recursive_sum(self, nstd_num_list=[]):
        total = 0
        for item in nstd_num_list:
            if isinstance(item, numbers.Number):
                total += item
            elif isinstance(item, list):
                total += self.recursive_sum(item)
            else:
                raise TypeError('Wrong type in the input')
        return total
    
    def recursive_max(self, nstd_num_list=[]):
        current_max = float("-inf")
        for item in nstd_num_list:
            if isinstance(item, numbers.Number):
                if item > current_max:
                    current_max = item
            elif isinstance(item, list):
                child_max = self.recursive_max(item)
                if child_max > current_max:
                    current_max = child_max
            else:
                raise TypeError('Wrong type in the input')
        return current_max       
    
    def recursive_min(self, nstd_num_list=[]):
        current_min = float("inf")
        for item in nstd_num_list:
            if isinstance(item, numbers.Number):
                if item < current_min:
                    current_min = item
            elif isinstance(item, list):
                child_min = self.recursive_min(item)
                if child_min < current_min:
                    current_min = child_min
            else:
                raise TypeError('Wrong type in the input')
        return current_min       
        