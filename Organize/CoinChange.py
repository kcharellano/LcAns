'''
Iterative DP solution. 
Time: O(number of coins * amount)
Space: O(amount)
'''
from math import inf
class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        for target in range(1, amount+1):
            minCoins = inf
            for coin in coins:
                if target - coin >= 0:
                    minCoins = min(minCoins, dp[target-coin] + 1)
            dp[target] = minCoins
        return dp[amount]
    '''
    Alternate problem: Find the number of solutions(permutations of solutions)
    '''
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = {0: 1}
        for target in range(1, amount+1):
            minWays = 0 
            for coin in coins:
                if target - coin >= 0:
                    minWays += dp[target-coin]
            dp[target] = minWays
        return dp[amount]

denom = [1, 2, 5]