'''
    https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
    
    Algorithm: Backtracking with cache
        - Perform constrained DFS search on each cell in matrix
        - Use cache to store longest path from a processsed cell
    Time: O(M*N) --> process every cell once
    Space: O(M*N) --> cache stores paths for all cells
'''
class Solution:
    def dfs(self, row, col, matrix, cache):
        if cache[row][col] != 0:
            return cache[row][col]+1
        
        for d in self.directions:
            vStep = row+d[0]
            hStep = col+d[1]
            # check if new direction within bounds
            if vStep < self.rowSize and vStep > -1:
                if hStep < self.colSize and hStep > -1:
                    # check that new step is increasing
                    if matrix[vStep][hStep] > matrix[row][col]:
                            cache[row][col] = max(cache[row][col], self.dfs(vStep,hStep,matrix,cache))
        return cache[row][col]+1
                        
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # edgecase
        if matrix == []:
            return 0
        self.rowSize = len(matrix)
        self.colSize = len(matrix[0])
        
        # initialize cache
        cache = [[0 for i in range(self.colSize)] for j in range(self.rowSize)]

        # up, down, left, right
        self.directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
        longestPath = 1
        for row in range(self.rowSize):
            for col in range(self.colSize):
                longestPath = max(longestPath, self.dfs(row, col, matrix, cache))
        for row in cache:
            print(row)
        return longestPath