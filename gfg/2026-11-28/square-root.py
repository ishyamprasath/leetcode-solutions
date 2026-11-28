class Solution:
    def floorSqrt(self, n):
        lo, hi = 1, n
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= n:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
