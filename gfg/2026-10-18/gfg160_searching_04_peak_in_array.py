# GFG 160 - Searching #4: Peak in Array


class Solution:
    def peakElement(self, arr):
        # Binary search: move towards the larger neighbour, a peak must exist there.
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
