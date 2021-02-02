# https://leetcode.com/problems/minimum-path-sum
'''
    DP min/max path cost sum
    DP solution. Create a mxn table where each cell contains the
    minimum path cost to get from (0,0) to that cell.
    Time:O(m*n)
    Space:O(m*n)
'''
from math import inf
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # create zeroed mxn grid
        table = [[inf for col in range(n)] for row in range(m)]

        # initialize top left index of table
        table[0][0] = grid[0][0]

        # fill in table where each cell= minimumPathSum from top left
        for row in range(m):
            for col in range(n):
                # check that right cell is valid
                if col+1 < n:
                    table[row][col+1] = min(table[row][col+1], table[row][col] + grid[row][col+1])
                # check that downward cell is valid
                if row+1 < m:
                    table[row+1][col] = min(table[row+1][col], table[row][col] + grid[row+1][col])

        # return bottom right cell from table
        return table[m-1][n-1]

from math import inf
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowLen, colLen = len(grid), len(grid[0])
        dp = [[inf for i in range(colLen)] for j in range(rowLen)]
        for row in range(rowLen):
            for col in range(colLen):
                leftPath = dp[row][col-1] if col-1 >= 0 else inf
                upPath = dp[row-1][col] if row-1 >= 0 else inf
                if leftPath == inf and upPath == inf:
                    dp[row][col] = grid[row][col]
                else:
                    dp[row][col] = min(leftPath, upPath) + grid[row][col]
        return dp[rowLen-1][colLen-1]