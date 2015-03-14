'''
Created on Mar 13, 2015

@author: Sameer Adhikari
'''

class LListNode(object):
    '''
    A class to store the contents in a linked list
    '''
    
    def __init__(self, data):
        self.data = data
        self.follow = None


class LListIterator(object):
    
    def __init__(self, head):
        self.current = head
        
    def __iter__(self):
        return self.current.data

    def next(self):
        if self.current is None:
            raise StopIteration()
        else:
            result = self.current.data
            self.current = self.current.follow
            return result

    
class LList(object):
    '''
    A  linked list class
    '''

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        return LListIterator(self.head)
        
    def insert(self, data):
        node = LListNode(data)
        if not self.head:
            self.head = node
            self.tail = node
            
        else:
            temp = self.tail
            self.tail = node
            temp.follow = node

def main():            
    print 'List of integers'
    iList = LList()
    iList.insert(1)
    iList.insert(2)
    iList.insert(3)
    iList.insert(4)
    for data in iList:
        print data, 
    print ''

    print 'List of strings'
    sList = LList()
    sList.insert('abc')
    sList.insert('yz')
    sList.insert('lmn')
    for data in sList:
        print data, 
    print ''
    
main()
