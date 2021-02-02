
# https://leetcode.com/problems/triangle/
'''
    Algorithm: DP min/max path cost sum
    - Create dp table with same dimensions as triangle
    - Each cell in table is the min-cost path from root to that cell
    - The minimum cost path from top to bottom is the minimum val in the bottom
    of the dp table
'''
from math import inf
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangleLen = len(triangle)
        # create dp table
        dp = [[inf] * i for i in range(1, triangleLen + 1)]
        # initialize first cell
        dp[0][0] = triangle[0][0]
        # fill table top-down
        for row in range(triangleLen-1):
            for col in range(row+1):
                parent = dp[row][col]
                dp[row+1][col] = min(dp[row+1][col], parent+triangle[row+1][col])
                dp[row+1][col+1] = min(dp[row+1][col+1], parent+triangle[row+1][col+1])
        return min(dp[triangleLen-1])
                