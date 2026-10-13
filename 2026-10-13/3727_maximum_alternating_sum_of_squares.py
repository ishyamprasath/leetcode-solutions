# 3727. Maximum Alternating Sum of Squares (POD 2026-10-13)
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted(x * x for x in nums)
        k = len(a) // 2
        return sum(a[k:]) - sum(a[:k])
