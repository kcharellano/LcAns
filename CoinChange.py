'''
Iterative DP solution. 
Time: O(number of coins * amount)
Space: O(amount)
'''
from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        for target in range(1, amount+1):
            minCoins = inf
            for coin in coins:
                if target - coin >= 0:
                    minCoins = min(minCoins, dp[target-coin] + 1)
            dp[target] = minCoins
        return dp[amount]