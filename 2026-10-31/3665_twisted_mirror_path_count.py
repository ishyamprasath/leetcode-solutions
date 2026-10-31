from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        # land[d][i][j]: final cell when entering (i, j) moving right (d=0) or down (d=1)
        land = [[[None] * (n + 1) for _ in range(m + 1)] for _ in range(2)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    land[0][i][j] = (i, j)
                    land[1][i][j] = (i, j)
                else:
                    land[0][i][j] = land[1][i + 1][j] if i + 1 < m else None
                    land[1][i][j] = land[0][i][j + 1] if j + 1 < n else None
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                ways = dp[i][j]
                if ways == 0:
                    continue
                if j + 1 < n:
                    t = land[0][i][j + 1]
                    if t:
                        dp[t[0]][t[1]] = (dp[t[0]][t[1]] + ways) % MOD
                if i + 1 < m:
                    t = land[1][i + 1][j]
                    if t:
                        dp[t[0]][t[1]] = (dp[t[0]][t[1]] + ways) % MOD
        return dp[m - 1][n - 1]
