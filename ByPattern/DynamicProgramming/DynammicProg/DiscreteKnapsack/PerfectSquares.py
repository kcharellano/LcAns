'''
    Algorithm: Single row Discrete Knapsack
    - get a list of all squares below n (in ascending order)
    - dp[cell] = min(currentVal vs the minimum amount of numbers needed to sum to amount)
    - Note: Solution is almost identical to coin change problem
    Time: O(n * sqrt(n))
    Space: O(n)
'''
from math import inf
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**(0.5))+1)]
        dp = [inf] * (n + 1)
        dp[0] = 0
        for amount in range(1, n+1):
            for square in squares:
                if square > amount:
                    break
                dp[amount] = min(dp[amount], dp[amount - square] + 1)
        return dp[-1]