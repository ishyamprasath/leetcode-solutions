# LeetCode 2916. Subarrays Distinct Element Sum of Squares II (POD 2026-10-16)
# Sum of (distinct count)^2 over all subarrays, mod 10^9+7. n <= 1e5.
# Maintain distinct counts for subarrays ending at i (indexed by start) in a
# segment tree with range-add; when +1 is applied, sq += 2*sum + len.
from typing import List


MOD = 10**9 + 7


class SegTree:
    """Range-add (+1) segment tree tracking sum of counts and sum of squares."""

    def __init__(self, n: int):
        self.n = n
        size = 4 * n
        self.sum_c = [0] * size
        self.sum_sq = [0] * size
        self.lazy = [0] * size

    def _apply(self, node: int, length: int, add: int) -> None:
        # (c+v)^2 = c^2 + 2*v*c + v^2  =>  sq += 2*v*sum + v^2*len
        self.sum_sq[node] = (
            self.sum_sq[node] + 2 * add * self.sum_c[node] + add * add * length
        ) % MOD
        self.sum_c[node] = (self.sum_c[node] + add * length) % MOD
        self.lazy[node] += add

    def _push(self, node: int, l: int, r: int) -> None:
        if self.lazy[node] and l != r:
            mid = (l + r) // 2
            self._apply(node * 2, mid - l + 1, self.lazy[node])
            self._apply(node * 2 + 1, r - mid, self.lazy[node])
            self.lazy[node] = 0

    def range_add(self, ql: int, qr: int, add: int = 1) -> None:
        if ql > qr:
            return
        self._range_add(1, 0, self.n - 1, ql, qr, add)

    def _range_add(self, node: int, l: int, r: int, ql: int, qr: int, add: int) -> None:
        if ql <= l and r <= qr:
            self._apply(node, r - l + 1, add)
            return
        self._push(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self._range_add(node * 2, l, mid, ql, qr, add)
        if qr > mid:
            self._range_add(node * 2 + 1, mid + 1, r, ql, qr, add)
        self.sum_c[node] = (self.sum_c[node * 2] + self.sum_c[node * 2 + 1]) % MOD
        self.sum_sq[node] = (self.sum_sq[node * 2] + self.sum_sq[node * 2 + 1]) % MOD

    def query_sq(self, ql: int, qr: int) -> int:
        if ql > qr:
            return 0
        return self._query_sq(1, 0, self.n - 1, ql, qr)

    def _query_sq(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.sum_sq[node]
        self._push(node, l, r)
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res += self._query_sq(node * 2, l, mid, ql, qr)
        if qr > mid:
            res += self._query_sq(node * 2 + 1, mid + 1, r, ql, qr)
        return res % MOD


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        tree = SegTree(n)
        last = {}
        ans = 0
        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            # Distinct count grows by 1 for every start in (prev, i]
            tree.range_add(prev + 1, i, 1)
            ans = (ans + tree.query_sq(0, i)) % MOD
            last[x] = i
        return ans
