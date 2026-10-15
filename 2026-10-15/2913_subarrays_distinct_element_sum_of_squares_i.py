# LeetCode 2913. Subarrays Distinct Element Sum of Squares I (POD 2026-10-15)
# For every subarray, add (distinct count)^2. n <= 100 so O(n^2) with a set is fine.
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                ans += len(seen) * len(seen)
        return ans
