# Title: N-Queen Problem
# URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/recursion-and-backtracking-gfg-160/problem/n-queen-problem0315
# Difficulty: Hard
# Approach: Backtracking row by row with column/diagonal sets; 1-based columns; O(n!).
class Solution:
    def nQueen(self, n: int) -> list[list[int]]:
        res = []
        cols = set()
        d1 = set()
        d2 = set()
        cur = []
        def dfs(r):
            if r == n:
                res.append(cur[:])
                return
            for c in range(n):
                if c in cols or (r - c) in d1 or (r + c) in d2:
                    continue
                cols.add(c); d1.add(r - c); d2.add(r + c)
                cur.append(c + 1)
                dfs(r + 1)
                cur.pop()
                cols.remove(c); d1.remove(r - c); d2.remove(r + c)
        dfs(0)
        return res
