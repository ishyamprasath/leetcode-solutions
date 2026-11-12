class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[""] * 3 for _ in range(3)]
        for i, (r, c) in enumerate(moves):
            board[r][c] = "A" if i % 2 == 0 else "B"
        lines = [row[:] for row in board]
        lines += [[board[r][c] for r in range(3)] for c in range(3)]
        lines.append([board[i][i] for i in range(3)])
        lines.append([board[i][2 - i] for i in range(3)])
        for line in lines:
            if line[0] and line[0] == line[1] == line[2]:
                return line[0]
        return "Draw" if len(moves) == 9 else "Pending"
