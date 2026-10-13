# GFG POTD 2026-10-13: Adding Ones
# https://www.geeksforgeeks.org/problems/adding-ones3628/1


class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        d = [0] * (n + 2)
        for j in updates:
            d[j] += 1
        res = []
        s = 0
        for i in range(1, n + 1):
            s += d[i]
            res.append(s)
        return res
