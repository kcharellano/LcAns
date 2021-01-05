'''
    https://leetcode.com/problems/number-of-islands/
'''

'''
    Algorithm: DFS
        - For every cell perform dfs to find all connected land cells and record visited cells
        - skip cells that have been visited
    Time: O(m x n) --> DFS visits every node once
    Space: O(m x n) --> store all visited nodes, also consider stack space 
'''
class Solution:
    def dfs(self, grid, visited, row, col, rowSize, colSize):
        visited.add((row, col))
        
        # visit up
        if row-1 >= 0:
            if not (row-1, col) in visited and grid[row-1][col] == '1':
                self.dfs(grid, visited, row-1, col, rowSize, colSize)
        # visit down
        if row+1 < rowSize:
            if not (row+1, col) in visited and grid[row+1][col] == '1':
                self.dfs(grid, visited, row+1, col, rowSize, colSize)
        # visit right
        if col+1 < colSize:
            if not (row, col+1) in visited and grid[row][col+1] == '1':
                self.dfs(grid, visited, row, col+1, rowSize, colSize)
        # visit left
        if col-1 >= 0:
            if not (row, col-1) in visited and grid[row][col-1] == '1':
                self.dfs(grid, visited, row, col-1, rowSize, colSize)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        # set of cells ---> (row, col)
        islandCount = 0
        visited = set()
        rowSize = len(grid)
        colSize = len(grid[0])
        for row in range(rowSize):
            for col in range(colSize):
                if not (row, col) in visited and grid[row][col] == '1':
                    # cell is unvisited and is land
                    islandCount += 1
                    self.dfs(grid, visited, row, col, rowSize, colSize)
                # else skip cell
        return islandCount
