'''
Created on Apr 22, 2016

@author: Sameer Adhikari
'''

# Does not yet handle the case where coin change is not possible.

class Solution(object):
    def coinChangeInternal(self, coins, amount, minCoins):
        """
        minCoins[i] will contain the min num coins
        used to get to i where 0 <= i <= amount.
        usedCoin[i] will contain the last  
        used coin to get to the amount i.
        """
        minCoins[0] = 0
        for currAmt in range(1, amount + 1):
            coinCount = currAmt
            print 'current amount = ', currAmt
            for coin in [c for c in coins if c <= currAmt]:
                print 'checking coin = ', coin
                if minCoins[currAmt - coin] + 1 < coinCount:
                    coinCount = minCoins[currAmt - coin] + 1
            minCoins[currAmt] = coinCount
            
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        minCoins = [0] * (amount + 1)
        self.coinChangeInternal(coins, amount, minCoins)
        print [i for i in range(amount + 1)]
        print minCoins
        return minCoins[amount]
        

if __name__ == '__main__':
    s = Solution()
#     coins = [1, 2, 5]
#     amount = 11
#     print s.coinChange(coins, amount)
#     coins = [2]
#     amount = 4
#     print s.coinChange(coins, amount)
    coins = [2]
    amount = 3
    print s.coinChange(coins, amount)