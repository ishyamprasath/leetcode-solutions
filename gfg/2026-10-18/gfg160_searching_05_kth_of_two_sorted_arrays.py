# GFG 160 - Searching #5: K-th of Two Sorted Arrays


class Solution:
    def kthElement(self, a, b, k):
        # Binary search on the partition: take i elements from a and k - i from b.
        if len(a) > len(b):
            a, b = b, a
        n, m = len(a), len(b)
        lo, hi = max(0, k - m), min(k, n)
        inf = float('inf')
        while lo <= hi:
            i = (lo + hi) // 2
            j = k - i
            a_left = a[i - 1] if i > 0 else -inf
            a_right = a[i] if i < n else inf
            b_left = b[j - 1] if j > 0 else -inf
            b_right = b[j] if j < m else inf
            if a_left > b_right:
                hi = i - 1
            elif b_left > a_right:
                lo = i + 1
            else:
                return max(a_left, b_left)
