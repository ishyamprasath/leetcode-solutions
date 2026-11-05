# LeetCode 1385. Find the Distance Value Between Two Arrays (POD 2026-11-05)
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Count elements of arr1 that are farther than d from every element of arr2.
        return sum(all(abs(a - b) > d for b in arr2) for a in arr1)
