'''
Created on May 11, 2016

@author: Sameer Adhikari
'''

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.leaf = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        n = len(word)
        i = 0
        
        # Go as far as a prefix already exists
        while i < n:
            if word[i] in node.child:
                node = node.child[word[i]]
                i += 1
            else:
                break
        
        while i < n:
            node.child[word[i]] = TrieNode()
            node = node.child[word[i]]
            i += 1
        
        node.leaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.child:
                return False
            else:
                node = node.child[word[i]] 
        
        return node.leaf
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in node.child:
                return False
            else:
                node = node.child[prefix[i]] 
        return True   
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
