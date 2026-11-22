from typing import List
from collections import Counter


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return all(any(a <= x <= b for a, b in ranges) for x in range(left, right + 1))
