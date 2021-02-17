# https://leetcode.com/problems/coin-change/
'''
    Algorithm: Naive Knapsack DP
    - Build a 2d table and follow the piecewise function
                        { inf                                          if row < 0 or col < 0
        dp[row][col] =  { 0                                            if col == 0
                        { min(dp[row-1][col], dp[row][col-coinVal])    otherwise
    Time: O(N^2), N = # of coins
    Space: O(N^2)
    NOTE: Items do not need sorting
''' 
from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        rowSize, colSize = len(coins), amount+1
        dp = [[inf for i in range(colSize)] for j in range(rowSize)]
        for row in range(rowSize):
            for col in range(colSize):
                # column buffer
                if col == 0:
                    dp[row][col] = 0
                # first row edgecase
                if row == 0:
                    # value is divisible by coin
                    if col >= coins[row] and col % coins[row] == 0:
                        dp[row][col] = int(col / coins[row])
                    # otherwise leave cell at inf
                elif col >= coins[row]:
                    # dont use coins vs use coin
                    dp[row][col] = min(dp[row-1][col], dp[row][col-coins[row]]+1)
                else:
                    # dont use coin
                    dp[row][col] = dp[row-1][col]
        return dp[rowSize-1][colSize-1] if dp[rowSize-1][colSize-1] != inf else -1

'''
    Algorithm: Better Knapsack DP
    - Follows a modified version of the algorithm above where
    each dp[cell] = minimum # of coins needed to fulfill amount
    - For each cell iterate through all valid coins
    and keep the one that results in the minimum amount of coins after using that coin
    Time: O(N * C), N = amount, C = # of coins
    Space: O(N)
    NOTE: This approach does not require sorted items and instead only considers valid items but goes
    through each item for every cell.
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
    Algorithm: Better Knapsack DP
    - Follows a modified version of the algorithm above where
    each dp[cell] = minimum # of coins needed to fulfill amount
    - For each cell iterate through all valid coins(in ascending order)
    and keep the one that results in the minimum amount of coins after using that coin
    Time: O(N * C), N = amount, C = # of coins
    Space: O(N)
    NOTE: This approach requires items for be sorted so that the 2 loop can stop for invalid coins
'''
from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [inf for i in range(amount+1)]
        dp[0] = 0
        for col in range(1, amount+1):
            for coin in coins:
                if coin > col:
                    break
                dp[col] = min(dp[col], dp[col - coin] + 1)
        return dp[-1] if dp[-1] != inf else -1