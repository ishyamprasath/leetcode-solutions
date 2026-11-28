class Solution:
    def medianOf2(self, a, b):
        if len(a) > len(b):
            a, b = b, a
        m, n = len(a), len(b)
        half = (m + n + 1) // 2
        lo, hi = 0, m
        INF = float("inf")
        while lo <= hi:
            i = (lo + hi) // 2  # elements taken from a
            j = half - i        # elements taken from b
            a_left = a[i - 1] if i > 0 else -INF
            a_right = a[i] if i < m else INF
            b_left = b[j - 1] if j > 0 else -INF
            b_right = b[j] if j < n else INF
            if a_left <= b_right and b_left <= a_right:
                left_max = max(a_left, b_left)
                if (m + n) % 2:
                    return left_max
                total = left_max + min(a_right, b_right)
                return total // 2 if total % 2 == 0 else total / 2
            if a_left > b_right:
                hi = i - 1
            else:
                lo = i + 1
