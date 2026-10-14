# 3194. Minimum Average of Smallest and Largest Elements (Easy)
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        n = len(nums)
        return min((nums[i] + nums[n - 1 - i]) / 2 for i in range(n // 2))
