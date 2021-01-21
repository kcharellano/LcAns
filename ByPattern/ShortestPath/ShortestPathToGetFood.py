# https://leetcode.com/problems/shortest-path-to-get-food
from collections import deque

'''
    Algorithm: BFS to find shortest path
        - queue stores cells
        - append queue at tail and pop queue at head
        - each queue node stores the # of steps it has
'''
class Solution:
    def findStart(self, grid, rowSize, colSize):
        for row in range(rowSize):
            for col in range(colSize):
                if grid[row][col] == "*":
                    return (row, col)
        return (-1, -1)
    
    def getFood(self, grid: List[List[str]]) -> int:
        rowSize = len(grid)
        colSize = len(grid[0])
        # find starting point
        sRow, sCol = self.findStart(grid, rowSize, colSize)
        # initialize directions
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = deque([(sRow, sCol, 0)])
        visited = set()
        while queue:
            row, col, steps = queue.popleft()
            
            # cell not in range 
            if row < 0 or row >= rowSize or col < 0 or col >= colSize:
                continue
            
            # cell already visited
            if (row,col) in visited:
                continue
            
            # cell is a wall
            if grid[row][col] == "X":
                continue
            
            # cell is food cell
            if grid[row][col] == "#":
                return steps

            # add cell to visited to avoid duplicate searches
            visited.add((row,col))

            # add all valid neighboring cells
            for v,h in directions:
                nextRow = row + v
                nextCol = col + h
                queue.append((nextRow, nextCol, steps+1))
        return -1
