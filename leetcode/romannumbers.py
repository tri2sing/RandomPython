'''
Created on Aug 25, 2016

@author: Sameer Adhikari
'''

class RomanNumbers(object):
    """
    Class with functions to covert Roman numbers to Integers and vice-versa.
    The functions assume that the input is within the range from 1 to 3999.
    """
    # Map unique Roman Numbers to their Decimal counterparts
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
    
    @classmethod
    def _largest_let_target(cls, target):
        # Return the largest number less than or equal to target
        l = 0
        if target < RomanNumbers._int_list[l]:
            return None

        r = len(RomanNumbers._int_list) - 1
        if target > RomanNumbers._int_list[r]:
            return RomanNumbers._int_list[r]

        while l <= r:
            m = (l + r) // 2
            curr = RomanNumbers._int_list[m]
            if curr == target:
                return curr
            elif curr > target:
                r = m - 1
            else:
                l = m + 1
        return RomanNumbers._int_list[r]
    
    @classmethod    
    def _smallest_get_target(cls, target):
        # Return the smallest number greater than or equal to target
        l = 0
        if target < RomanNumbers._int_list[l]:
            return RomanNumbers._int_list[0]

        r = len(RomanNumbers._int_list) - 1
        if target > RomanNumbers._int_list[r]:
            return None

        while l <= r:
            m = (l + r) // 2
            curr = RomanNumbers._int_list[m]
            if curr == target:
                return curr
            elif curr > target:
                r = m - 1
            else:
                l = m + 1
        return RomanNumbers._int_list[l]
        
    def roman_to_int(self, s):
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
            v1 = RomanNumbers._rtoi_map.get(s1)
            v2 = None
            if s2:
                v2 = RomanNumbers._rtoi_map.get(s2)
            if v1 > v2:
                res += v1
                i += 1
            elif v2 > v1:
                res += v2
                i += 2
        return res

    def int_to_roman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        while num > 0:
            val = RomanNumbers._largest_let_target(num)
            res.append(RomanNumbers._itor_map[val])
            num -= val
        return ''.join(res)
                
        
if __name__ == '__main__':
    print '_largest_let_target 16 = ', RomanNumbers._largest_let_target(16)
    print '_largest_let_target 50 = ', RomanNumbers._largest_let_target(50)
    print '_largest_let_target 300 = ', RomanNumbers._largest_let_target(300)
    print '_largest_let_target 2000 = ', RomanNumbers._largest_let_target(990)
    print
     
    print '_smallest_get_target 16 = ', RomanNumbers._smallest_get_target(16)
    print '_smallest_get_target 50 = ', RomanNumbers._smallest_get_target(50)
    print '_smallest_get_target 300 = ', RomanNumbers._smallest_get_target(300)
    print '_smallest_get_target 990 = ', RomanNumbers._smallest_get_target(990)
    print

    rn = RomanNumbers()
    print 'XXXVI = ', rn.roman_to_int('XXXVI'), ' Expected 36'
    print 'DCXXI = ', rn.roman_to_int('DCXXI'), ' Expected 621'
    print 'MMXII = ', rn.roman_to_int('MMXII'), ' Expected 2012'
    print 'MCMXCVI = ', rn.roman_to_int('MCMXCVI'), ' Expected 1996'
    print 'MMMXLV = ', rn.roman_to_int('MMMXLV'), ' Expected 3045'
    print

    print '36 = ', rn.int_to_roman(36), 'Expected = XXXVI'
    print '621 = ', rn.int_to_roman(621), 'Expected = DCXXI'
    print '2012 = ', rn.int_to_roman(2012), 'Expected = MMXII'
    print '1996 = ', rn.int_to_roman(1996), 'Expected = MCMXCVI'
    print '3045 = ', rn.int_to_roman(3045), 'Expected = MMMXLV'
    print
    
    
    
    
    
