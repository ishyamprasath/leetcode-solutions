# 3942. Minimum Operations to Sort a Permutation
# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/
from collections import deque
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def sorted_shift(arr):
            # Return the left-rotation count that sorts arr, or -1 if impossible.
            k = arr.index(0)
            for i in range(n):
                if arr[(k + i) % n] != i:
                    return -1
            return k

        targets = set()
        s0 = sorted_shift(nums)
        if s0 != -1:
            targets.add((0, s0))
        s1 = sorted_shift(nums[::-1])
        if s1 != -1:
            targets.add((1, s1))
        if not targets:
            return -1

        # State = (family, shift): family 0 is nums, family 1 is reversed nums.
        dist = {(0, 0): 0}
        queue = deque([(0, 0)])
        while queue:
            t, s = queue.popleft()
            d = dist[(t, s)]
            if (t, s) in targets:
                return d
            for nxt in ((t, (s + 1) % n), (1 - t, (n - s) % n)):
                if nxt not in dist:
                    dist[nxt] = d + 1
                    queue.append(nxt)
        return -1
