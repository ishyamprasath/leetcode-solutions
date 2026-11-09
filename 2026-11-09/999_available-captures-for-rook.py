# Problem: Available Captures for Rook
# URL: https://leetcode.com/problems/available-captures-for-rook/
# Difficulty: Easy
class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        r, c = next((i, j) for i in range(8) for j in range(8) if board[i][j] == 'R')
        captures = 0
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            row, col = r + dr, c + dc
            while 0 <= row < 8 and 0 <= col < 8 and board[row][col] != 'B':
                if board[row][col] == 'p':
                    captures += 1
                    break
                row += dr
                col += dc
        return captures
