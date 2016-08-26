'''
Created on Aug 25, 2016

@author: Sameer Adhikari
'''

class RomanNumerals(object):
    
    # Map unique Roman Numbers to their Decimal counterparts.
    lookup_map = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
       }
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        i = 0
        while i < n:
            s1 = s[i]
            s2 = None
            if i + 1 < n:
                s2 = s[i:i+2]
            v1 = RomanNumerals.lookup_map.get(s1)
            v2 = None
            if s2:
                v2 = RomanNumerals.lookup_map.get(s2)
            if v1 > v2:
                res += v1
                i += 1
            elif v2 > v1:
                res += v2
                i += 2
        return res
    
if __name__ == '__main__':
    rn = RomanNumerals()
    print 'XXXVI = ', rn.romanToInt('XXXVI'), ' Expected 36'
    print 'DCXXI = ', rn.romanToInt('DCXXI'), ' Expected 621'
    print 'MMXII = ', rn.romanToInt('MMXII'), ' Expected 2012'
    print 'MCMXCVI = ', rn.romanToInt('MCMXCVI'), ' Expected 1996'
    print 'MMMXLV = ', rn.romanToInt('MMMXLV'), ' Expected 3045'
