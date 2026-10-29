# 697. Degree of an Array
# https://leetcode.com/problems/degree-of-an-array/
# Difficulty: Easy
# Approach: track count, first and last index per value.
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, cnt = {}, {}
        deg, best = 0, 0
        for i, x in enumerate(nums):
            first.setdefault(x, i)
            cnt[x] = cnt.get(x, 0) + 1
            length = i - first[x] + 1
            if cnt[x] > deg or (cnt[x] == deg and length < best):
                deg, best = cnt[x], length
        return best
