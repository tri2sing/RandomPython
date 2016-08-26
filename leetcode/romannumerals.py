'''
Created on Aug 25, 2016

@author: Sameer Adhikari
'''

class RomanNumerals(object):
    
    # Map unique Roman Numbers to their Decimal counterparts.
    _rtoi_map = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
        }
    
    _itor_map = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
        }
    
    _int_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    
    def _largest_let_target(self, target):
        # Finds the largest number less than or equal to target
        l = 0
        r = len(RomanNumerals._int_list) - 1
        while l <= r:
            m = (l + r) // 2
            curr = RomanNumerals._int_list[m]
            if curr == target:
                return curr
            elif curr > target:
                r = m - 1
            else:
                l = m + 1
        return RomanNumerals._int_list[r]
        
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
            v1 = RomanNumerals._rtoi_map.get(s1)
            v2 = None
            if s2:
                v2 = RomanNumerals._rtoi_map.get(s2)
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

    print '_largest_let_target 16 = ', rn._largest_let_target(16)
    print '_largest_let_target 50 = ', rn._largest_let_target(50)
    print '_largest_let_target 300 = ', rn._largest_let_target(300)
    print '_largest_let_target 2000 = ', rn._largest_let_target(2000)
