# https://leetcode.com/problems/walls-and-gates/

'''
    Algorithm: Multisource BFS
    - Find all gates in the grid and add them to queue
    - "simultaneously" perform BFS on all gate locations
    guranteeing that every spot will contain the closest path to A gate
'''
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        # room constants
        EMPTY, GATE, WALL = 2147483647, 0, -1
        # grid dimensions
        rowSize, colSize = len(rooms), len(rooms[0])
        queue = deque()
        # find gates
        for row in range(rowSize):
            for col in range(colSize):
                if rooms[row][col] == GATE:
                    queue.append((row, col))
        # bfs
        # down up left right
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            row, col = queue.popleft()
            for d in directions:
                nRow = row + d[0]
                nCol = col + d[1]
                # bounds check
                if nRow >= 0 and nRow < rowSize and nCol >= 0 and nCol < colSize:
                    # room check 
                    if rooms[nRow][nCol] == EMPTY:
                        rooms[nRow][nCol] = rooms[row][col] + 1
                        queue.append((nRow, nCol))
        return
