# 
'''
    Algorithm: Dynammic Programming
    - create a table where each cell is the bottom right corner of the 
    enclosing maximal square
    - The answer is the largest cell val^2
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rowLen, colLen = len(matrix), len(matrix[0])
        dp = [[0 for i in range(colLen)] for j in range(rowLen)]
        maxSquare = 0
        for row in range(rowLen):
            for col in range(colLen):
                if matrix[row][col] == '1':
                    dp[row][col] = 1
                    if col-1 >= 0 and row-1 >= 0:
                        dp[row][col] = min(dp[row][col-1], dp[row-1][col-1], dp[row-1][col]) + 1
                    maxSquare = max(maxSquare, dp[row][col])
        return maxSquare * maxSquare
        