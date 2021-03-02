# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
'''
    Algorithm: 2D DP 
    dp(day, i) = minimum total job difficulty after doinog i jobs in day days
    dp(day, i) = min(dp(day-1, k) + max(k+1,j) for day-2<=k<j)
    Time: O(n^2*d)
    Space: O(n*d)
'''
from math import inf
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        colSize = len(jobDifficulty)
        # edgecase
        if d > colSize: return -1
        
        # create 2d DP array, row = day | col = difficult of job[i]
        # dp rows 1-based indexing
        dp = [[inf for col in range(colSize)] for row in range(d + 1)]
        
        # intialize first row
        dp[1][0] = jobDifficulty[0]
        for col in range(1, colSize):
            dp[1][col] = max(jobDifficulty[col], dp[1][col-1])
        
        for day in range(2, d+1):
            for col in range(day-1, colSize):
                k = col - 1
                maxSeen = -inf
                while k >= day-2:
                    # max container from [k+1,col] inclusive
                    maxSeen = max(maxSeen, jobDifficulty[k+1])
                    dp[day][col] = min(dp[day][col], dp[day-1][k] + maxSeen)
                    k -= 1
        return dp[d][colSize-1]
