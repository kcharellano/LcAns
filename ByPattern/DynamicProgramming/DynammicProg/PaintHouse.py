'''
    Algorithm: Dynamic Programming
    - The color a house can be does not depend on the color of all previous houses. 
    It only depends on the color the house previous to it. Knowing this,
    we can construct an optimal ordering of colors and paint each cell as if 
    only optimal color choice colors were made.
    - At the end, the cheapest path will be the last row in our dp table
    Time: O(N)
    Space: O(N)
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        rowLen = len(costs)
        # edgecase: no houses
        if rowLen == 0:
            return 0
        # create dp table
        dp = [[0 for i in range(3)] for j in range(rowLen)]
        print(dp)
        # initialize first row
        for i in range(3):
            dp[0][i] = costs[0][i]
        # fill table
        for row in range(1, rowLen):
            leftCell = dp[row-1][0]
            midCell = dp[row-1][1]
            rightCell = dp[row-1][2]
            dp[row][0] = min(midCell+costs[row][0], rightCell+costs[row][0])
            dp[row][1] = min(leftCell+costs[row][1], rightCell+costs[row][1])
            dp[row][2] = min(leftCell+costs[row][2], midCell+costs[row][2])
        print(dp)
        return min(dp[rowLen-1])