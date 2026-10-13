# GFG 160 Arrays 10: Kadane's Algorithm
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/kadanes-algorithm-1587115620


class Solution:
    def maxSubarraySum(self, arr):
        best = arr[0]
        cur = arr[0]
        for x in arr[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best
