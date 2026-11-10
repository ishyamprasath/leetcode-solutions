# Climbing Stairs II — Medium — https://leetcode.com/problems/climbing-stairs-ii/
from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[j] is the minimum cost to reach step j.
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for j in range(1, n + 1):
            step_cost = costs[j - 1]
            dp[j] = min(
                dp[i] + step_cost + (j - i) ** 2
                for i in range(max(0, j - 3), j)
            )

        return dp[n]
