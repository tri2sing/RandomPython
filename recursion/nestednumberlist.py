'''
Created on Jul 11, 2016

@author: Sameer Adhikari
'''

import numbers

class NestedNumberList(object):
    def recursive_sum(self, nested_num_list = []):
        ''' '''
        total = 0
        for item in nested_num_list:
            if isinstance(item, numbers.Number):
                total += item
            elif isinstance(item, list):
                total += self.recursive_sum(item)
            else:
                raise TypeError('Wrong type in the input')
        return total
    
