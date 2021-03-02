'''
    Algorithm: BFS from every cell
    - for every cell in the matrix, start a BFS search to find the nearest 0 cell
    Time: O(BFS^2)
    Space: O(r * c)
    NOTE: Its faster to do a multisource BFS starting at every 1 on the board if the grid
    has mostly 0s
'''
from collections import deque
class Solution:
    def bfs(self, startRow, startCol, rowSize, colSize, matrix):
        queue = deque([(startRow, startCol, 0)])
        visited = set()
        # up, down, left, right
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            row, col, steps = queue.popleft()
            
            # cell is out of range
            if row < 0 or row >= rowSize or col < 0 or col >= colSize:
                continue
            
            # goal condition
            if matrix[row][col] == 0:
                return steps
            
            visited.add((row,col))
            
            # continue bfs to next level
            for d in directions:
                nextRow = row + d[0]
                nextCol = col + d[1]
                if (nextRow, nextCol) not in visited:
                    queue.append((nextRow, nextCol, steps+1))
        
        return -1

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rowSize, colSize = len(matrix), len(matrix[0])
        ans = [[0 for j in range(colSize)] for i in range(rowSize)]
        for row in range(rowSize):
            for col in range(colSize):
                ans[row][col] = self.bfs(row, col, rowSize, colSize, matrix)
        return ans


'''
    Algorithm: 2 Pass DP
    - Create new matrix ans to store result
    - loop over matrix from top-bottom, left to right 
        if cell == 0: dp[row][col] = 0
        else: dp[row][col] = min(currentVal, min(aboveDPCell, leftDPCell) + 1)
    - do a second pass but this time from bottom-top, right to left
        dp[row][col] = min(currentVal, min(bottomDPCell, rightDpCell) + 1)
    Time: O(r * c)
    Space: O(r * c)
'''
from math import inf
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rowSize, colSize = len(matrix), len(matrix[0])
        ans = [[inf for i in range(colSize)] for j in range(rowSize)]
        # top-bottom, left-right pass
        for row in range(rowSize):
            for col in range(colSize):
                if matrix[row][col] == 0:
                    ans[row][col] = 0
                else:
                    if row > 0:
                        ans[row][col] = min(ans[row][col], ans[row-1][col] + 1)
                    if col > 0:
                        ans[row][col] = min(ans[row][col], ans[row][col-1] + 1)
        
        # bottom-top, right to left pass
        for row in reversed(range(rowSize)):
            for col in reversed(range(colSize)):
                if row < rowSize - 1:
                    ans[row][col] = min(ans[row][col], ans[row+1][col] + 1)
                if col < colSize - 1:
                    ans[row][col] = min(ans[row][col], ans[row][col+1] + 1)
        return ans
                
                