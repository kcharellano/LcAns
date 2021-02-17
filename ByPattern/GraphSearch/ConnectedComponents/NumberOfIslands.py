'''
    Algorithm: DFS to find connected components
    - Peform a DFS search at every land cell
    - Count the number of times an initial DFS is triggered
    - Space Optomization: Instead of using a separate data structure to keep track 
    of visited cells, we can instead mark visited cells with a '0' to avoid visiting them again.
    Time: O(N)
    Space: O(1)
'''
class Solution:
    def dfs(self, row, col, grid, rowSize, colSize, directions):
        # mark cell as visited
        grid[row][col] = '0'
        # explore adjacent cells
        for d in directions:
            nextRow = row + d[0]
            nextCol = col + d[1]
            # check next cell is within bounds
            if 0 <= nextRow and nextRow < rowSize and 0 <= nextCol and nextCol < colSize:
                # check next cell is land
                if grid[nextRow][nextCol] == '1':
                    self.dfs(nextRow, nextCol, grid, rowSize, colSize, directions)
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        rowSize, colSize = len(grid), len(grid[0])
        islandCount = 0
        # up down left right
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        for row in range(rowSize):
            for col in range(colSize):
                if grid[row][col] == '0':
                    continue
                islandCount += 1
                self.dfs(row, col, grid, rowSize, colSize, directions)
        return islandCount