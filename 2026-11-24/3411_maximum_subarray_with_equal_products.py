from typing import List
from collections import Counter
from math import gcd


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        best = 0
        n = len(nums)
        for i in range(n):
            prod, g, l = 1, 0, 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if prod == l * g:
                    best = max(best, j - i + 1)
        return best
