from typing import List
from collections import Counter
from math import gcd


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    s = nums[a] + nums[b] + nums[c]
                    for d in range(c + 1, n):
                        if nums[d] == s:
                            count += 1
        return count
