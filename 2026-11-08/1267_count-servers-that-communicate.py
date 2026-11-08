# 1267. Count Servers that Communicate (Medium) - Problem of the Day 2026-11-08
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_count = [sum(row) for row in grid]
        col_count = [sum(grid[r][c] for r in range(rows)) for c in range(cols)]
        return sum(grid[r][c] == 1 and (row_count[r] > 1 or col_count[c] > 1) for r in range(rows) for c in range(cols))
