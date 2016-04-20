'''
Created on Apr 18, 2016

@author: Sameer Adhikari
'''

class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        symbols = list(pattern)
        num_syms = len(symbols)
        words = [word for word in string.split()]
        num_wrds = len(words)
        if num_syms != num_wrds:
            return False
        # To track if there is a bijection
        wtos = {} # word to symbol
        stow = {} # symbols to word
        for i in range(num_syms):
            print wtos,
            print stow
            word = words[i]
            symbol = symbols[i]
            s = wtos.get(word)
            w = stow.get(symbol)
            print 'word = {}, symbol = {}, w = {}, s = {}'.format(word, symbol, w, s)
            if not s and not w: # mappings do not exist, so insert
                wtos[word] = symbol
                stow[symbol] = word
            elif s and w: #mappings exist so should be a bijection
                if s != symbol or w != word:
                    return False
            else:
                return False
        return True
        
        
if __name__ == '__main__':
    s = Solution()
#     pattern = 'abba'
#     string = 'dog cat cat dog'
#     print 'pattern = {}, string = {}, matches = {}'.format(pattern, string, s.wordPattern(pattern, string))
    pattern = 'abba'
    string = 'dog cat cat fish'
    print 'pattern = {}, string = {}, matches = {}'.format(pattern, string, s.wordPattern(pattern, string))

