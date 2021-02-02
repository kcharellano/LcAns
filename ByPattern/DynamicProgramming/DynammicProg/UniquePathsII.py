# https://leetcode.com/problems/unique-paths-ii
'''
    Algorithm: DP Distince ways
    - Same strategy as unique paths 1 except with extra checks because
    not the grid can contain obstacles
    Time: O(m*n)
    Space: O(m*n)
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rowLen, colLen = len(obstacleGrid), len(obstacleGrid[0])
        # edgecase: starting point is invalid
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for i in range(colLen)] for j in range(rowLen)]
        dp[0][0] = 1
        for row in range(rowLen):
            for col in range(colLen):
                # skip obstacle cells
                if obstacleGrid[row][col] == 1:
                    continue
                # add to right cell
                if col+1 < colLen and obstacleGrid[row][col+1] != 1:
                    dp[row][col+1] += dp[row][col]
                # add to bottom cell
                if row+1 < rowLen and obstacleGrid[row+1][col] != 1:
                    dp[row+1][col] += dp[row][col]
        return dp[rowLen-1][colLen-1]
        