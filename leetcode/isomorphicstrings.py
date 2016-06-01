'''
Created on Apr 10, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def isIsomorphic1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and t:
            return False
        if s and not t:
            return False
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        
        # Build a histogram of the first string.
        # Store locations of a character too.
        smap = {}
        for i in range(len(s)):
            c = s[i]
            if c in smap:
                count, positions = smap[c]
                count += 1
                positions.add(i)
                smap[c] = count, positions
            else:
                smap[c] = 1, {i}
        
        tmap = {}        
        for i in range(len(t)):
            c = t[i]
            if c in tmap:
                count, positions = tmap[c]
                count += 1
                positions.add(i)
                tmap[c] = count, positions
            else:
                tmap[c] = 1, {i}
        
        # Go through both string to see if they are isomorphic
        for i in range(len(s)):
            cs = s[i]
            ct = t[i]
            ccount, clocs = smap[cs]
            tcount, tlocs = tmap[ct]
            if ccount != tcount:
                return False
            if clocs != tlocs:
                return False
        
        return True

    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and t:
            return False
        if s and not t:
            return False
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        
        # Keep track for each string what the
        # replacement from other string will be
        ds = {}
        dt = {}
        for cs, ct in zip(s, t):
            if cs not in ds and ct not in dt:
                ds[cs] = ct
                dt[ct] = cs
            else:
                if ds.get(cs) != ct and dt.get(ct) != cs:
                    return False
        return True
                
if __name__ == '__main__':
    s = Solution()
    print s.isIsomorphic1('a', 'a')
    print s.isIsomorphic2('ab', 'aa')
        
