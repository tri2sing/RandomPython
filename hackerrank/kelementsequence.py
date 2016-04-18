'''
Created on Apr 15, 2016

@author: Sameer Adhikari
'''

class KElementSequence(object):
    
    def __init__(self):
        # Using memoization
        self.cache = {}
        self.cache[0, 0] = 1
    
    def get_sequence_count(self, target_sum, sequence_len):
        
        if (target_sum, sequence_len) in self.cache:
            return self.cache[target_sum, sequence_len]
        
        if sequence_len == 0 and target_sum != 0:
            if (target_sum, sequence_len) not in self.cache:
                self.cache[target_sum, sequence_len] = 0
            return 0

        if target_sum == 0 and sequence_len == 0:
            # This value is initialized in the cache already
            return 1
        
        seq_count = 0
        for i in range(1, target_sum + 1):
            seq_count += self.get_sequence_count(target_sum - i, sequence_len - 1)
        
        self.cache[target_sum, sequence_len] = seq_count
        
        return seq_count 
        
if __name__ == '__main__':
    target_sum = 4
    sequence_len = 3
    kes = KElementSequence()
    print kes.get_sequence_count(target_sum, sequence_len) % (10**9 + 7)
