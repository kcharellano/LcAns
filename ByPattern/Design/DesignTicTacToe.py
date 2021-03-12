# https://leetcode.com/problems/design-tic-tac-toe/

'''
    Use row, col, and diag trackers to check win conditions
    move(): Time O(1)
'''
from collections import defaultdict
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.vertical = defaultdict(lambda: [0,0])
        self.horizontal = defaultdict(lambda: [0,0])
        self.upDiag = [0,0]
        self.lowDiag = [0,0]
    
    def winningMove(self, row, col, playerIdx):
        if self.horizontal[row][playerIdx] == self.n:
            return True
        if self.vertical[col][playerIdx] == self.n:
            return True
        if self.upDiag[playerIdx] == self.n:
            return True
        if self.lowDiag[playerIdx] == self.n:
            return True
        return False

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        playerIdx = player - 1
        self.horizontal[row][playerIdx] += 1
        self.vertical[col][playerIdx] += 1
        if row == col:
            self.lowDiag[playerIdx] += 1
        if row + col == self.n - 1:
            self.upDiag[playerIdx] += 1
        if self.winningMove(row, col, playerIdx):
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)