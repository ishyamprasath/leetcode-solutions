from typing import List
from collections import Counter
import heapq

# LeetCode 3882 - Problem of the Day for 2026-10-28 (solved late)
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # reach[j]: XOR values achievable by paths ending at column j of the current row
        reach = [set() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    reach[0] = {grid[0][0]}
                    continue
                values = set()
                if i > 0:
                    values |= reach[j]      # came from above
                if j > 0:
                    values |= reach[j - 1]  # came from the left
                reach[j] = {x ^ grid[i][j] for x in values}
        return min(reach[n - 1])
