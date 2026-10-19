# GFG 160 - Searching 8: Kth Missing Positive Number in a Sorted Array


class Solution:
    def kthMissing(self, arr, k):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] - (mid + 1) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo + k
