# 1512. Number of Good Pairs (Easy)
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        pairs = 0
        for x in nums:
            pairs += seen.get(x, 0)
            seen[x] = seen.get(x, 0) + 1
        return pairs
