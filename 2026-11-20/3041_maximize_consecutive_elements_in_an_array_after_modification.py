class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # dp[v] = longest consecutive run that ends at value v.
        # After sorting, each number can be used as itself or as itself + 1.
        dp = {}
        best = 0
        for x in sorted(nums):
            # Use x as x + 1 first, so it extends the run ending at x
            # before dp[x] is updated by this same element.
            dp[x + 1] = dp.get(x, 0) + 1
            dp[x] = dp.get(x - 1, 0) + 1
            best = max(best, dp[x], dp[x + 1])
        return best
