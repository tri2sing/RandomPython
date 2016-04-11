'''
Created on Apr 10, 2016

@author: Sameer Adhikari
'''

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.reg_stack = []
        self.reg_num = 0
        self.min_stack = []
        self.min_num = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.reg_stack.append(x)
        self.reg_num += 1
        if not self.min_stack or x <= self.min_stack[self.min_num - 1]:
            self.min_stack.append(x)
            self.min_num += 1
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.reg_stack:
            return
        val = self.reg_stack.pop()
        self.reg_num -= 1
        if self.min_stack and val == self.min_stack[self.min_num - 1]:
            min_val = self.min_stack.pop()
            self.min_num -= 1
        
        
    def top(self):
        """
        :rtype: int
        """
        if not self.reg_stack:
            return None
        return self.reg_stack[self.reg_num - 1]


    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            return None
        return self.min_stack[self.min_num - 1]
        
                
if __name__ == '__main__':
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-1)
    ms.print_stack()
    min_val = ms.getMin()
    print min_val
    ms.print_stack()
    top_val = ms.top()
    print top_val
    ms.print_stack()
    ms.pop()
    ms.print_stack()
    min_val = ms.getMin()
    print min_val
    ms.print_stack()
    
    
    
    

