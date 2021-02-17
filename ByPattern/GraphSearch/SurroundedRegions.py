# https://leetcode.com/problems/surrounded-regions

'''
    Algorithm: DFS
    - Do one pass over cells and..
    - Begin a DFS search at every edge 'O'
    - Any other O that is reachable by and edge O cannot be
    captured.
    - Mark these cells in place using an 'F'
    - Do another pass over each cell and
    convert existing Os to Xs and Fs to Os
    Time: O(N)
    Space: O(1)
'''
class Solution:
    # Marks visited cells as 'F' for free
    def dfs(self, row, col, board):
        # Mark cell as free -- avoids cycles
        board[row][col] = 'F'
        
        # explore adjacent 'O's
        for d in self.directions:
            nxRow = row + d[0]
            nxCol = col + d[1]
            if 0 <= nxRow and nxRow < self.rowSize \
            and 0 <= nxCol and nxCol < self.colSize \
            and board[nxRow][nxCol] == 'O':
                self.dfs(nxRow, nxCol, board)
        return

    def solve(self, board: List[List[str]]) -> None:
        if board == []: return
        self.rowSize, self.colSize = len(board), len(board[0])
        # up down left right
        self.directions = [(1,0), (-1,0), (0,-1), (0,1)]
        # mark all free cells as 'F'
        for row in range(self.rowSize):
            for col in range(self.colSize):
                # Only trigger dfs on edge O cells
                if board[row][col] == 'O' and (row == 0 or col == 0 or \
                 row == self.rowSize-1 or col == self.colSize-1):
                    if board[row][col] == 'O':
                        self.dfs(row, col, board)
        # Convert 'O' to 'X' and 'F' to 'O'
        for row in range(self.rowSize):
            for col in range(self.colSize):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'F':
                    board[row][col] = 'O'
        return
      
        