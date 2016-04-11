'''
Created on Apr 11, 2016

@author: Sameer Adhikari
'''

# This one revereses words with excess space characters
def reverseWords1(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return s

    return ' '.join(reversed(s.strip().split()))

# This one assumes that there aren't excess spaces
# so that we can focus on the core algorithm
def reversWords2(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return s
    
    # Reverse the characters of the whole string
    # As string is immutable we need a bytearray
    n = len(s)
    b = bytearray(s)
    for i in range(n):
        b[i] = s[n - i -1]
        
    # Reverse each individual word
    i = 0 
    j = 0 
    while j < n:
        while j < n and b[j] != ord(' '):
            j += 1   
        begin = i  # Start of the word
        end = j - 1 # end of the word
        while begin < end:
            temp = b[begin]
            b[begin] = b[end]
            b[end] = temp
            begin += 1
            end -= 1
        j +=1
        i = j
        
    return str(b.decode())

if __name__ == '__main__':
    s1 = 'hello i am sameer'
    print s1
    print reversWords2(s1)