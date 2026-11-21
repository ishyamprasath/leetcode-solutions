from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bits = 0
        for x in nums:
            bits |= x
        return bits << (len(nums) - 1)
