from typing import List
from collections import Counter
from math import gcd


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = Counter()
        count = 0
        for x in nums:
            count += seen[x - k] + seen[x + k]
            seen[x] += 1
        return count
