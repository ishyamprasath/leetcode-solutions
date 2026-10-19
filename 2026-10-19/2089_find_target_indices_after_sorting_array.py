# LeetCode 2089. Find Target Indices After Sorting Array (Easy) - Problem of the Day 2026-10-19
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = sum(1 for x in nums if x < target)
        cnt = sum(1 for x in nums if x == target)
        return list(range(less, less + cnt))
