# GFG 160 - Searching 7: Allocate Minimum Pages


class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:
            return -1
        lo, hi = max(arr), sum(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            students = 1
            cur = 0
            for p in arr:
                if cur + p > mid:
                    students += 1
                    cur = p
                else:
                    cur += p
            if students <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
