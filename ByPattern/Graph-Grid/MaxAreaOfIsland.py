# https://leetcode.com/problems/max-area-of-island/submissions/

'''
    Algorithm: DFS to explore connected cells
    - Use DFS on every cell to check for connected component size
    Time: O(m*n), m = rowSize, n = colSize
    Space: O(1) -- changed grid instead of using a visited tracker
'''
class Solution:
    # returns the size of an island
    def dfs(self, grid, row, col):
        areaSum = 0
        grid[row][col] = 0
        for d in self.directions:
            nxtRow = row + d[0]
            nxtCol = col + d[1]
            # bounds check
            if nxtRow < 0 or nxtRow >= self.rowSize or nxtCol < 0 or nxtCol >= self.colSize:
                continue
            # water and visited check
            if grid[nxtRow][nxtCol] == 0:
                continue
            areaSum += self.dfs(grid, nxtRow, nxtCol)
        return areaSum + 1
        
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rowSize, self.colSize = len(grid), len(grid[0])
        # down, up, left, right
        self.directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        maxArea = 0
        for row in range(self.rowSize):
            for col in range(self.colSize):
                cell = grid[row][col]
                # invalid cell
                if cell == 0:
                    continue
                maxArea = max(maxArea, self.dfs(grid, row, col))
        return maxArea    