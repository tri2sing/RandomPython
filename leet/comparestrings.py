'''
Created on Apr 20, 2016

@author: Sameer Adhikari
'''

from collections import defaultdict
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        tracker = defaultdict(int)
        for c in secret:
            tracker[c] += 1
        bulls = 0
        cows = 0
        for i in range(len(guess)):
            s = secret[i]
            g = guess[i]
            if s == g:
                bulls += 1
                tracker[g] = tracker[g] - 1
            else:
                if g in tracker:
                    cows += 1
                    tracker[g] = tracker[g] - 1
        
        print tracker
        for c in tracker:
            if tracker[c] < 0:
                # there were more guesses than digits
                cows += tracker[c] # Adding negative value
        return '{}A{}B'.format(bulls, cows)   
    
if __name__ == '__main__':
    s = Solution()
    secret = '1122'
    guess = '1222'
    result = s.getHint(secret, guess)
    print 'secret = {}, guess = {}, result = {}'.format(secret, guess, result)
