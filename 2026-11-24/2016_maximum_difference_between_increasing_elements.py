from typing import List
from collections import Counter
from math import gcd


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        best = -1
        low = nums[0]
        for x in nums[1:]:
            if x > low:
                best = max(best, x - low)
            low = min(low, x)
        return best
