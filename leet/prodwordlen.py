'''
Created on Apr 10, 2016

@author: Sameer Adhikari
'''

from string import ascii_lowercase
from operator import or_  # logical or

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        if not words:
            return 0
            
        # Generate the list of letters and map them to powers-of-two integers 
        ltoi = dict(zip(ascii_lowercase, (2 ** i for i in range(26))))
        
        # For each word generate a bitmap to track the letters present.
        # For each word also store the length of the word along with it.
        bmap = {}
        for word in words:
            bmap[word] = reduce(or_, (ltoi[c] for c in word), 0), len(word)
        
        # Compare the words against each other 
        max_product = 0
        num_words = len(words)
        for i in range (num_words - 1):
            imap, ilen = bmap[words[i]] 
            for j in range (i, num_words):
                jmap, jlen = bmap[words[j]]
                if not (imap & jmap):
                    # There is no overlap
                    curr_product = ilen * jlen
                    if curr_product > max_product:
                        max_product = curr_product
        return max_product
    
