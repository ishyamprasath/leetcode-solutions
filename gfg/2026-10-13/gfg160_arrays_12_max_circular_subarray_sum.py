# GFG 160 Arrays 12: Max Circular Subarray Sum
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/max-circular-subarray-sum-1587115620


class Solution:
    def maxCircularSum(self, arr):
        if not arr:
            return 0
        total = 0
        cmax = cmin = 0
        best = arr[0]
        worst = arr[0]
        for x in arr:
            total += x
            cmax = max(x, cmax + x)
            best = max(best, cmax)
            cmin = min(x, cmin + x)
            worst = min(worst, cmin)
        if best < 0:
            return best
        return max(best, total - worst)
