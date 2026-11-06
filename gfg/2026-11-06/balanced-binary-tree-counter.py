# GFG POTD 2026-11-06: Balanced Binary Tree Counter
# https://www.geeksforgeeks.org/problems/bbt-counter4914/1

MOD = 10**9 + 7


class Solution:
    def countBT(self, h: int) -> int:
        # Number of height-balanced binary trees of exact height h.
        # Recurrence: left/right heights (h-1,h-1), (h-1,h-2), (h-2,h-1).
        # Empty tree has height 0 -> 1 way; single node has height 1 -> 1 way.
        if h <= 1:
            return 1
        prev2, prev1 = 1, 1  # dp[0], dp[1]
        for _ in range(2, h + 1):
            cur = (prev1 * prev1 + 2 * prev1 * prev2) % MOD
            prev2, prev1 = prev1, cur
        return prev1
