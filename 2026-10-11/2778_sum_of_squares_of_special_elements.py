# 2778. Sum of Squares of Special Elements (Easy) - POD 2026-10-11
from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(nums[i - 1] ** 2 for i in range(1, n + 1) if n % i == 0)
