# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count nums1, then consume matching counts while scanning nums2.
        counts = Counter(nums1)
        result = []
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        return result
