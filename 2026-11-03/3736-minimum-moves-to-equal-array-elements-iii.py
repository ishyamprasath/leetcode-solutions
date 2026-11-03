# LeetCode 3736. Minimum Moves to Equal Array Elements III (POD 2026-11-03)
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Raise every element to the maximum; total moves = n * max - sum.
        return len(nums) * max(nums) - sum(nums)
