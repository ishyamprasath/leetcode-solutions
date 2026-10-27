# 3963. Create Grid With Exactly One Path (POD 2026-10-27)
# https://leetcode.com/problems/create-grid-with-exactly-one-path/
# Difficulty: Easy
# Approach: free top row, then only the last column free below -> single path right then down.
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = ['.' * n]
        for _ in range(m - 1):
            grid.append('#' * (n - 1) + '.')
        return grid
