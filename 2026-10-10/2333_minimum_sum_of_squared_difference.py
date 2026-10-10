from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        if sum(diffs) <= k:
            return 0
        # Smallest cap t such that lowering every diff above t down to t costs <= k
        lo, hi = 0, max(diffs)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(d - mid for d in diffs if d > mid) <= k:
                hi = mid
            else:
                lo = mid + 1
        t = lo
        k -= sum(d - t for d in diffs if d > t)
        capped = [min(d, t) for d in diffs]
        # Leftover k (< number of diffs at t) lowers k of those values from t to t-1
        return sum(c * c for c in capped) - k * (t * t - (t - 1) * (t - 1))
