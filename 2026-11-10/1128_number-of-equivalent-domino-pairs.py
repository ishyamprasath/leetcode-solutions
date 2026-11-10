# Number of Equivalent Domino Pairs — Easy — https://leetcode.com/problems/number-of-equivalent-domino-pairs/
from collections import defaultdict
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        frequency = defaultdict(int)
        pairs = 0
        for first, second in dominoes:
            key = (min(first, second), max(first, second))
            pairs += frequency[key]
            frequency[key] += 1
        return pairs
