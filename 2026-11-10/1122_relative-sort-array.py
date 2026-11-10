# Relative Sort Array — Easy — https://leetcode.com/problems/relative-sort-array/
from collections import Counter
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        result = []
        for value in arr2:
            result.extend([value] * counts.pop(value, 0))

        remaining = []
        for value, count in counts.items():
            remaining.extend([value] * count)
        result.extend(sorted(remaining))
        return result
