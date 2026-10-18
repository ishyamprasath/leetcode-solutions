from typing import List

# 1569. Number of Ways to Reorder Array to Get Same BST (Hard) - Problem of the Day 2026-10-18


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        # Pascal's triangle for binomial coefficients
        comb = [[1] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % mod

        def count(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            ways = comb[len(arr) - 1][len(left)]
            return ways * count(left) % mod * count(right) % mod

        return (count(nums) - 1) % mod
