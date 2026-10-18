# GFG 160 - Searching #2: Sorted and Rotated Minimum


class Solution:
    def findMin(self, arr):
        # Binary search for the rotation point (array has distinct elements).
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo]
