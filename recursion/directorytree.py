'''
Created on Jul 11, 2016

@author: Sameer Adhikari
'''

import os

def get_dir_list(dir_path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """    
    if not os.path.isdir(dir_path):
        raise TypeError('Argument is not a directory')
    dir_list = os.listdir(dir_path)
    dir_list.sort()
    return dir_list

def print_dir_tree(dir_path, prefix=''):
    """ Recursively print a directory tree.
    """
    if not os.path.isdir(dir_path):
        raise TypeError('Argument is not a directory')
    if prefix == '':
        print "Tree for: ", dir_path
        prefix = '|-'
    dir_list = get_dir_list(dir_path)
    for entry in dir_list:
        print prefix + entry
        full_name = os.path.join(dir_path, entry)
        if os.path.isdir(full_name):
            print_dir_tree(full_name, prefix + '|-')
    

if __name__ == '__main__':
    print_dir_tree('/Users/sadhik1/Documents/wspython/PyFp')