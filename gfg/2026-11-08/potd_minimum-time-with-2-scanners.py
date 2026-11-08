# GFG POTD 2026-11-08: Minimum Time with 2 Scanners
class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        k = n * s2 // (s1 + s2)
        a = max(k * s1, (n - k) * s2)
        b = max((k + 1) * s1, (n - k - 1) * s2)
        return min(a, b)
