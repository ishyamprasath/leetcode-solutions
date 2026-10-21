# Minimum Sum Subarray
# https://www.geeksforgeeks.org/problems/smallest-sum-contiguous-subarray/1
class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        best = cur = arr[0]
        for x in arr[1:]:
            cur = min(x, cur + x)
            best = min(best, cur)
        return best
