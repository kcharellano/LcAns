# https://leetcode.com/problems/unique-paths
'''
    Algorithm: DP distinct ways
    - Create a dp table where the value of each cell is the number of ways
    to arrive at that cell from the top left corner
    Time: O(m*n)
    Space: O(m*n)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for col in range(n):
                # add to right cell
                if col+1 < n:
                    dp[row][col+1] += dp[row][col]
                # add to bottom cell
                if row+1 < m:
                    dp[row+1][col] += dp[row][col]
        return dp[m-1][n-1]
        