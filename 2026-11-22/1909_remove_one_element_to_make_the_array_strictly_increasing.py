from typing import List
from collections import Counter


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def increasing(arr):
            return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                # Try removing either element of the first bad pair.
                return increasing(nums[:i] + nums[i + 1:]) or increasing(nums[:i + 1] + nums[i + 2:])
        return True
