# Height Checker — Easy — https://leetcode.com/problems/height-checker/
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(actual != target for actual, target in zip(heights, expected))
