# 441. Arranging Coins
# https://leetcode.com/problems/arranging-coins/
from math import isqrt


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Largest k with k * (k + 1) / 2 <= n, solved exactly with integer sqrt.
        return (isqrt(8 * n + 1) - 1) // 2
