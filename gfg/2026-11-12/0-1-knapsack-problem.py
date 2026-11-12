class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        dp = [0] * (W + 1)
        for v, w in zip(val, wt):
            for cap in range(W, w - 1, -1):
                dp[cap] = max(dp[cap], dp[cap - w] + v)
        return dp[W]
