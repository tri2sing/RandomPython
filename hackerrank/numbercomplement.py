'''
Created on Jul 18, 2016

@author: Sameer Adhikari
'''


def getIntegerComplement(n):
    bits = []
    while n:
        r = n % 2
        n /= 2
        bits.append(r)
    bits.reverse()
    inverts = [1 - i for i in bits]
    ans = 0
    for i in inverts:
        ans = ans * 2 + i
    return ans
    

if __name__ == '__main__':
    print getIntegerComplement(0)
    print getIntegerComplement(50)
    print getIntegerComplement(100)
